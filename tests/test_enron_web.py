"""Real loopback requests exercise data routes and the monitor's write boundary."""

import http.client
import json
import threading

import pytest

from swarmkit.enron.web import create_server


@pytest.fixture
def monitor():
    changes = []

    def document_snapshot(identifier):
        snapshot = {"id": identifier, "body": "<script>untrusted</script>"}
        if identifier == "segmented":
            snapshot.update(sender="outer@example.test", date="2001-01-01", raw_date="Mon, 1 Jan 2001", segments=[
                {"segment_id": "s0", "document_id": identifier, "kind": "authored", "depth": 0,
                 "start": 0, "end": 10, "text": "Outer author's reply", "confidence": 0.9},
                {"segment_id": "s1", "document_id": identifier, "kind": "header", "depth": 1,
                 "text": "From: claimed@example.test", "claimed_sender": "claimed@example.test"},
                {"segment_id": "s2", "document_id": identifier, "kind": "forwarded", "depth": 1,
                 "text": "Forwarded passage", "claimed_sender": "claimed@example.test",
                 "claimed_date": "2000-12-31", "claimed_subject": "Earlier topic",
                 "ambiguities": ["No closing delimiter"], "content_fingerprint": "abc123"},
                {"segment_id": "s3", "document_id": identifier, "kind": "quoted", "depth": 2,
                 "text": "<img src=x onerror=alert(1)>", "confidence": 0.5},
            ])
            return {"document": snapshot}
        return snapshot

    callbacks = dict(
        status=lambda: {"paused": changes[-1] if changes else False, "run_id": "r1",
                        "budget": {"tokens": 25, "limits": {"max_tokens": 100}}},
        runs=lambda: [{"id": "r1"}],
        run=lambda identifier: {"id": identifier, "posts": [{
            "agent_id": "reader", "text": "Reading evidence", "phase": "assess",
            "evidence": [{"document_id": "d1", "quote": "<img src=x onerror=alert(1)>", "valid": True}],
        }], "wiki": [{"title": "Working hypothesis", "text": "An explanation", "kind": "knowledge",
                      "alternative": "Ordinary delegation", "missing_evidence": "Held-out documents",
                      "next_test": "Compare a separate thread", "transfer_tested": False,
                      "independence_status": "not_established"}]} if identifier == "r1" else None,
        document=document_snapshot,
        search=lambda query: [{"id": "d1", "subject": query}],
        set_paused=lambda paused: changes.append(paused) or {"paused": paused},
    )
    server = create_server(port=0, **callbacks)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield server, changes
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)


def request(monitor, path, method="GET", body=None, headers=None):
    server, _ = monitor
    connection = http.client.HTTPConnection(*server.server_address, timeout=3)
    connection.request(method, path, body=body, headers=headers or {})
    response = connection.getresponse()
    result = response.status, dict(response.getheaders()), response.read()
    connection.close()
    return result


def origin(monitor):
    host, port = monitor[0].server_address
    return f"http://{host}:{port}"


def test_read_routes_and_static_security(monitor):
    status, headers, body = request(monitor, "/")
    assert status == 200 and b"Peer forum" in body
    assert "frame-ancestors 'none'" in headers["Content-Security-Policy"]
    assert headers["X-Content-Type-Options"] == "nosniff"
    assert "Access-Control-Allow-Origin" not in headers
    for path in ("/style.css", "/app.js", "/api/status", "/api/runs", "/api/runs/r1"):
        assert request(monitor, path)[0] == 200
    status, _, body = request(monitor, "/api/document?id=folder%2Fmessage")
    assert status == 200
    assert json.loads(body)["id"] == "folder/message"
    assert json.loads(body)["body"] == "<script>untrusted</script>"
    assert json.loads(request(monitor, "/api/search?q=hello%20world")[2])[0]["subject"] == "hello world"
    script = request(monitor, "/app.js")[2]
    assert b"innerHTML" not in script
    assert b"textContent" in script


@pytest.mark.parametrize("path,code", [
    ("/api/runs/missing", 404), ("/api/runs/", 400), ("/api/runs/a%2Fb", 400),
    ("/api/document", 400), ("/api/search?q=%20", 400), ("/../web.py", 404),
    ("/api/search?q=" + "x" * 513, 400), ("https://evil.example/api/status", 403),
])
def test_invalid_routes(monitor, path, code):
    assert request(monitor, path)[0] == code


def test_pause_and_resume_require_same_origin_and_exact_boolean(monitor):
    headers = {"Content-Type": "application/json", "Origin": origin(monitor)}
    for value in (True, False):
        response = request(monitor, "/api/pause", "POST", json.dumps({"paused": value}), headers)
        assert response[0] == 200 and json.loads(response[2])["paused"] is value
    assert monitor[1] == [True, False]
    for payload in ({"paused": "false"}, {"paused": 1}, {"paused": None}, {}, {"paused": True, "other": 1}, []):
        assert request(monitor, "/api/pause", "POST", json.dumps(payload), headers)[0] == 400
    assert monitor[1] == [True, False]


@pytest.mark.parametrize("extra", [
    {}, {"Origin": "https://evil.example"}, {"Origin": "null"},
    {"Origin": "SAME", "Sec-Fetch-Site": "cross-site"},
])
def test_csrf_rejected(monitor, extra):
    headers = {"Content-Type": "application/json", **extra}
    if headers.get("Origin") == "SAME":
        headers["Origin"] = origin(monitor)
    assert request(monitor, "/api/pause", "POST", '{"paused":true}', headers)[0] == 403
    assert monitor[1] == []


def test_rebinding_and_body_limits(monitor):
    assert request(monitor, "/api/status", headers={"Host": "attacker.example"})[0] == 403
    headers = {"Origin": origin(monitor), "Content-Type": "application/json"}
    assert request(monitor, "/api/pause", "POST", " " * 4097, headers)[0] == 400
    assert request(monitor, "/api/pause", "POST", "bad json", headers)[0] == 400
    assert request(monitor, "/api/other", "POST", "{}", headers)[0] == 404
    headers["Content-Type"] = "text/plain"
    assert request(monitor, "/api/pause", "POST", '{"paused":true}', headers)[0] == 415
    assert monitor[1] == []


@pytest.mark.parametrize("host", ["0.0.0.0", "192.168.1.1", "example.com", "::1"])
def test_nonloopback_or_unsupported_bind_rejected(host):
    with pytest.raises(ValueError, match="loopback"):
        create_server(host=host, status=None, runs=None, run=None, document=None, search=None, set_paused=None)


def test_browser_renders_caveats_sources_budget_and_gate(monitor):
    """Optional real-browser smoke; Playwright remains a local development tool."""
    sync_api = pytest.importorskip("playwright.sync_api")
    with sync_api.sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=True)
        except sync_api.Error as exc:
            pytest.skip(f"Playwright Chromium not installed: {exc}")
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(origin(monitor))
            page.wait_for_function("() => document.getElementById('connection').textContent === 'Live · local'")
            assert page.locator("#budget-value").inner_text() == "25 / 100"
            assert page.locator("#budget-bar").evaluate("element => element.value") == 0.25
            assert page.locator(".post .phase-tag").text_content() == "assess"
            assert "Ordinary delegation" in page.locator("#wiki").text_content()
            assert "Held-out documents" in page.locator("#wiki").text_content()
            assert "Compare a separate thread" in page.locator("#wiki").text_content()
            assert "Transfer not tested" in page.locator("#wiki").text_content()
            assert "not established" in page.locator("#wiki").text_content()
            assert page.locator("#wiki-count").inner_text() == "1 proposals · 1 assessments"
            assert page.locator(".peer-assessment").count() == 1
            assert "not a proposed case or validated rule" in page.locator(".peer-assessment").inner_text()
            assert page.locator(".evidence img").count() == 0
            assert "Not human reviewed" in page.locator(".post .evidence").inner_text()
            page.get_by_role("button", name="Open source · d1").first.click()
            page.wait_for_function("() => document.getElementById('document-body').textContent.includes('untrusted')")
            assert page.locator("#document-body script").count() == 0
            assert page.locator("#document-raw").evaluate("element => element.open")
            assert page.locator(".email-segment").count() == 0
            page.get_by_role("button", name="Close document").click()
            page.evaluate("() => openDocument('segmented')")
            page.wait_for_selector(".segment-authored")
            assert page.locator(".email-segment").count() == 4
            assert not page.locator("#document-raw").evaluate("element => element.open")
            assert not page.locator(".segment-header").evaluate("element => element.open")
            assert "Outer-message sender (stored header): outer@example.test" in page.locator("#document-meta").inner_text()
            assert "Outer-message date (stored header): Mon, 1 Jan 2001" in page.locator("#document-meta").inner_text()
            assert "Claimed sender: claimed@example.test" in page.locator(".segment-forwarded").inner_text()
            assert "Claimed date: 2000-12-31" in page.locator(".segment-forwarded").inner_text()
            assert "No closing delimiter" in page.locator(".segment-forwarded").inner_text()
            assert "segment-depth-2" in page.locator(".segment-quoted").get_attribute("class")
            assert page.locator(".segment-quoted img").count() == 0
            page.locator(".segment-authored .segment-provenance summary").click()
            assert "Segment occurrence: s0" in page.locator(".segment-authored").inner_text()
            assert "Body character offsets: [0, 10)" in page.locator(".segment-authored").inner_text()
            assert "not claim confidence" in page.locator(".segment-authored").inner_text()
            page.locator("#document-raw > summary").click()
            assert page.locator("#document-body").is_visible()
            page.get_by_role("button", name="Close document").click()
            page.locator("#query").fill("<b>literal query</b>")
            page.get_by_role("button", name="Search corpus", exact=True).click()
            page.wait_for_selector("#search-results .result")
            assert page.locator("#search-results button").inner_text() == "<b>literal query</b>"
            assert page.locator("#search-results b").count() == 0
            page.get_by_role("button", name="Pause new work", exact=True).click()
            page.wait_for_function("() => document.getElementById('pause').textContent === 'Resume new work'")
            assert monitor[1] == [True]
            page.evaluate("renderStatus({enabled: false, paused: false})")
            assert page.locator("#pause").is_disabled()
            assert page.locator("#pause").inner_text() == "Dispatch disabled"
            page.evaluate("""() => renderQuality({id:'pilot', status:'completed', model:'<b>test-model</b>',
                config:{synthetic:false}, quote_checks:{accepted:0,rejected:36},
                completed_invocations:24, agent_errors:[]})""")
            assert page.locator("#quality-title").inner_text() == "Citation review needed"
            assert "quality-warning" in page.locator("#run-quality").get_attribute("class")
            assert page.locator("#quality-mode").text_content() == "Corpus investigation"
            assert page.locator("#quality-counts strong").all_text_contents() == ["0", "36", "24", "0"]
            assert "Execution: completed" in page.locator("#quality-context").inner_text()
            assert "<b>test-model</b>" in page.locator("#quality-context").inner_text()
            assert page.locator("#quality-context b").count() == 0
            assert "does not establish the truth" in page.locator("#quality-explanation").inner_text()
            page.evaluate("""() => renderQuality({id:'fixture', model:'offline-fixture',
                config:{synthetic:true}, quote_checks:{accepted:24,rejected:0},
                completed_invocations:24, agent_errors:[{error:'failure'}]})""")
            assert page.locator("#quality-title").inner_text() == "Agent errors need review"
            assert page.locator("#quality-mode").text_content() == "Synthetic demonstration"
            assert "Fictional fixture data" in page.locator("#quality-explanation").inner_text()
            page.evaluate("() => renderQuality({id:'empty'})")
            assert page.locator("#quality-counts strong").all_text_contents() == ["—", "—", "—", "—"]
            assert page.locator("#quality-mode").text_content() == "Data mode not reported"
            page.evaluate("""() => renderQuality({id:'rejected-output',status:'completed_with_rejections',
                reasoning_rejections:2,validation_rejections:{citations:0,hypotheses:3,predictions:1},
                quote_checks:{accepted:10,rejected:0},completed_invocations:8,agent_errors:[]})""")
            assert page.locator("#quality-title").inner_text() == "Reasoning output rejections"
            assert page.locator("#quality-counts strong").all_text_contents() == ["10", "0", "8", "0", "2", "4"]
            assert "hypotheses 3" in page.locator("#quality-explanation").inner_text()
            assert "does not recover those missing interpretations" in page.locator("#quality-explanation").inner_text()
            page.evaluate("() => renderQuality({id:'reset'})")
            assert "quality-warning" not in page.locator("#run-quality").get_attribute("class")
            page.evaluate("""() => renderRun({id:'no-proposals', wiki:[], posts:[
                {agent_id:'reader',phase:'scout',text:'Early observation'},
                ...['chronology','practice','bridge','skeptic'].map(agent_id => ({
                    agent_id,phase:'assess',text:'Final interpretation',evidence:[]
                }))]})""")
            assert page.locator("#wiki-count").inner_text() == "0 proposals · 4 assessments"
            assert page.locator(".wiki-item").count() == 0
            assert page.locator(".peer-assessment").count() == 4
            assert "No formal case or knowledge proposals" in page.locator("#wiki").inner_text()
            assert "Early observation" not in page.locator("#wiki").inner_text()
            assert errors == []
        finally:
            browser.close()


def test_browser_chronological_replay_and_hypothesis_revisions(monitor):
    sync_api = pytest.importorskip("playwright.sync_api")
    with sync_api.sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=True)
        except sync_api.Error as exc:
            pytest.skip(f"Playwright Chromium not installed: {exc}")
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 1100})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(origin(monitor))
            page.wait_for_function("() => document.getElementById('connection').textContent === 'Live · local'")
            page.evaluate("""() => {
                window.replayFixture = {
                  id:'replay-fixture', mode:'chronological_replay', config:{synthetic:true},
                  replay:{virtual_time:'2000-01-02T00:00:00Z',arrived:100,selected:8,skipped:92,
                    model_calls:4,gate_reason:'Local novelty threshold',windows:2,eligible:1000,
                    coverage_complete:false},
                  posts:[
                    {phase:'revise',text:'Revise the routine',virtual_time:'2000-01-02T00:00:00Z',
                     window:2,arrival_sequence:100,created_at:'2026-01-01',evidence:[]},
                    {phase:'observe',text:'Initial observation',virtual_time:'2000-01-01T00:00:00Z',
                     window:1,arrival_sequence:50,created_at:'2026-01-02',evidence:[]},
                    {phase:'observe',text:'Later same-time observation',virtual_time:'2000-01-01T00:00:00Z',
                     window:1,arrival_sequence:51,evidence:[]}],
                  wiki:[
                    {id:'r1',hypothesis_id:'h1',revision:1,title:'Old routine',text:'Old explanation'},
                    {id:'r2',hypothesis_id:'h1',revision:2,title:'Revised routine',text:'Revised explanation',
                     unwritten_rule:'Ask the desk first',inference_gap:'The reply assumes an unstated gate',applies_when:'Before external sharing',
                     exceptions:'Urgent escalation',alternative:'Ordinary scheduling',
                     uncertainty:'Only one thread',prediction:'Another approval request',
                     next_query:'Find a second thread',virtual_time:'2000-01-02T00:00:00Z',
                     counterevidence:[{document_id:'d1',quote:'<b>A conflicting case</b>',valid:true}]}]
                };
                renderRun(window.replayFixture);
            }""")
            assert page.locator("#replay-summary").is_visible()
            assert "Human inspection searches the full archive" in page.locator("#corpus-scope").inner_text()
            assert page.locator("#replay-counts strong").all_text_contents() == ["100", "8", "92", "4"]
            assert "2000-01-02T00:00:00Z" in page.locator("#replay-clock").inner_text()
            assert "Local novelty threshold" in page.locator("#replay-gate").inner_text()
            assert "coverage incomplete" in page.locator("#replay-gate").inner_text()
            assert page.locator(".post-text").all_text_contents() == [
                "Initial observation", "Later same-time observation", "Revise the routine"]
            assert "Arrival cutoff 50" in page.locator(".post .virtual-time").first.inner_text()
            assert page.locator("#wiki-count").inner_text() == "1 observation · 0 candidates · 2 revisions"
            assert page.locator(".wiki-item").count() == 1
            assert page.locator(".knowledge-type").text_content() == "Observation"
            assert page.locator("#wiki-title").inner_text() == "Evolving knowledge"
            assert "Old explanation" not in page.locator("#wiki-items").inner_text()
            for text in ("Ask the desk first", "The reply assumes an unstated gate", "Before external sharing", "Urgent escalation",
                         "Only one thread", "Another approval request", "Find a second thread",
                         "Counterevidence", "<b>A conflicting case</b>"):
                assert text in page.locator("#wiki-items").inner_text()
            assert page.locator("#wiki-items .evidence b").count() == 0
            page.locator("#timeline-filter").select_option("revisions")
            assert page.locator(".post-text").all_text_contents() == ["Revise the routine"]
            assert page.locator("#post-count").inner_text() == "1 / 3 posts"
            page.locator("#timeline-filter").select_option("observations")
            assert page.locator(".post").count() == 2
            page.evaluate("""() => {
                window.replayFixture.wiki.push({id:'r3',hypothesis_id:'h2',revision:1,
                    knowledge_type:'tacit_hypothesis',title:'A bounded candidate',text:'Provisional'});
                renderRun(window.replayFixture);
            }""")
            assert page.locator("#wiki-count").inner_text() == "1 observation · 1 candidate · 3 revisions"
            assert page.locator(".knowledge-type").all_text_contents() == ["Observation", "Candidate tacit hypothesis"]
            assert "does not establish independent episodes" in page.locator("#wiki-note").inner_text()
            page.evaluate("""() => {
                window.replayFixture.posts.push({phase:'revise',text:'Abstained',
                    reasoning_rejection:'Malformed hypotheses list',virtual_time:'2000-01-03T00:00:00Z'});
                renderRun(window.replayFixture);
            }""")
            page.locator("#timeline-filter").select_option("revisions")
            assert "Malformed hypotheses list" in page.locator(".reasoning-rejection").inner_text()
            page.evaluate("() => renderRun({id:'retrospective',posts:[],wiki:[]})")
            assert page.locator("#replay-summary").is_hidden()
            assert page.locator("#replay-controls").is_hidden()
            assert page.locator("#corpus-scope").is_hidden()
            assert page.locator("#forum-title").inner_text() == "Peer forum"
            assert page.locator("#wiki-title").inner_text() == "Shared knowledge"
            assert errors == []
        finally:
            browser.close()


def test_browser_inquiry_portfolio_and_temporary_team_history(monitor):
    sync_api = pytest.importorskip("playwright.sync_api")
    with sync_api.sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=True)
        except sync_api.Error as exc:
            pytest.skip(f"Playwright Chromium not installed: {exc}")
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 1100})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(origin(monitor))
            page.wait_for_function("() => document.getElementById('connection').textContent === 'Live · local'")
            page.evaluate("""() => renderRun({id:'inquiry-run',mode:'inquiry_swarm',
                metrics:{virtual_time:'2000-01-03T00:00:00Z',arrived:120,scheduled_calls:3,reasoning_rejections:0,action_rejections:1},
                errors:[],config:{peer_exchange:false},agenda:{pending:[{inquiry_id:'q1',action:'retrieve'}],running:[]},
                inquiries:[{inquiry_id:'q1',question:'Why did the correction disappear?',
                  why_matters:'A downstream fix may be overwritten.',rivals:['Upstream refresh','Manual reversal'],
                  latest_change:'Refresh timing explains the recurrence.',unresolved_premise:'Which value is authoritative?',
                  next_actions:['Inspect the next refresh'],owner:'observer',participants:['observer','challenger'],
                  status:'open',evidence:[{document_id:'d1',quote:'<img src=x onerror=alert(1)>',valid:true}]},
                  {inquiry_id:'q2',question:'Does the dependency persist?',why_matters:'Check another episode.',
                   rivals:[],next_actions:[],owner:'reader',participants:['reader'],status:'watching'}],
                history:[{inquiry_id:'q1',version:1,virtual_time:'2000-01-01T00:00:00Z',latest_change:'Two accounts disagree.'},
                         {inquiry_id:'q1',version:2,virtual_time:'2000-01-03T00:00:00Z',latest_change:'Refresh timing explains the recurrence.'}],
                posts:[{inquiry_id:'q1',action:{kind:'request_peer',target:'challenger'},agent_id:'observer',virtual_time:'2000-01-02T00:00:00Z',text:'Recruit challenger to test reversal.'},
                       {inquiry_id:'q1',action:'inspect',agent_id:'observer',virtual_time:'2000-01-01T00:00:00Z',text:'Read the first correction.'},
                       {inquiry_id:'q2',action:'wait',agent_id:'reader',virtual_time:'2000-01-03T00:00:00Z',text:'Wait for another episode.'}]
            })""")
            assert page.locator("#inquiry-portfolio").is_visible()
            assert page.locator("#wiki").is_hidden()
            assert page.locator("#peers").is_hidden()
            assert page.locator("#baseline-mode").is_hidden()
            assert page.locator("#inquiry-count").inner_text() == "2 investigations"
            assert "Independent control: peer exchange disabled" in page.locator("#quality-context").inner_text()
            assert page.locator("#quality-title").inner_text() == "Some proposed content failed validation"
            assert "Rejected actions" in page.locator("#quality-counts").inner_text()
            assert page.locator("#inquiry-metrics strong").all_text_contents() == ["120", "3", "2", "1", "0"]
            assert "Scheduled model calls" in page.locator("#inquiry-metrics").inner_text()
            assert "Completed" not in page.locator("#inquiry-metrics").inner_text()
            assert page.locator(".inquiry-card").count() == 2
            card = page.locator(".inquiry-card").first
            for text in ("Why did the correction disappear?", "A downstream fix may be overwritten.",
                         "Upstream refresh", "Manual reversal", "Which value is authoritative?",
                         "Inspect the next refresh", "observer, challenger"):
                assert text in card.inner_text()
            card.locator(".inquiry-history summary").first.click()
            assert "Two accounts disagree" in card.inner_text()
            assert "Recruit challenger to test reversal" in card.inner_text()
            assert "2000-01-02T00:00:00Z" in card.inner_text()
            card.get_by_text("Current supporting evidence", exact=True).click()
            assert card.locator(".evidence img").count() == 0
            card.get_by_role("button", name="Follow this investigation in the timeline").click()
            assert page.locator(".post-text").all_text_contents() == [
                "Read the first correction.", "Recruit challenger to test reversal."]
            page.locator("#action-filter").select_option("request_peer")
            assert page.locator(".post").count() == 1
            assert "Recruit challenger" in page.locator(".post-text").inner_text()
            page.evaluate("() => renderRun({id:'empty-inquiry',mode:'inquiry_swarm',inquiries:[],posts:[]})")
            assert "No investigations opened yet" in page.locator("#inquiry-cards").inner_text()
            assert page.locator("#inquiry-metrics strong").all_text_contents()[:2] == ["—", "—"]
            page.evaluate("() => renderRun({id:'old',mode:'chronological_replay',wiki:[],posts:[]})")
            assert page.locator("#inquiry-portfolio").is_hidden()
            assert page.locator("#wiki").is_visible()
            assert "Archived baseline: chronological rule extraction" in page.locator("#baseline-mode").inner_text()
            assert errors == []
        finally:
            browser.close()
