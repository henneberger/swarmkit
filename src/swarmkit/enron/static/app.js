"use strict";

const $ = (id) => document.getElementById(id);
const list = (value) => Array.isArray(value) ? value : [];
const string = (value, fallback = "") => value == null ? fallback : String(value);
const actionName = (post) => typeof post.action === "object" && post.action ? post.action.kind : post.action || post.phase;
const quantity = (count, noun) => `${count} ${noun}${count === 1 ? "" : "s"}`;
let currentStatus = {};
let selectedRun = "";
let followActive = true;
let pollBusy = false;
let lastRunJSON = "";
let documentRequest = 0;
let displayedRun = null;

function node(tag, text, className) {
  const element = document.createElement(tag);
  if (text != null) element.textContent = String(text);
  if (className) element.className = className;
  return element;
}
async function api(path, options = {}) {
  const response = await fetch(path, {...options, cache: "no-store", signal: AbortSignal.timeout(10000)});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `Request failed (${response.status})`);
  return data;
}
function notice(message) {
  $("notice").textContent = message;
  $("notice").hidden = !message;
}
function formatNumber(value) {
  return typeof value === "number" && Number.isFinite(value) ? value.toLocaleString(undefined, {maximumFractionDigits: 4}) : string(value, "—");
}
function dateLabel(value) {
  if (!value) return "";
  const date = new Date(typeof value === "number" ? value * 1000 : value);
  return Number.isNaN(date.getTime()) ? String(value) : date.toLocaleString();
}
function renderStatus(status) {
  currentStatus = status;
  $("run-name").textContent = string(status.run_id || status.active_run_id, "No active run");
  $("run-state").textContent = string(status.status || status.state, "Waiting for a research run");
  const paused = status.paused === true;
  const disabled = status.enabled === false;
  $("pause").textContent = disabled ? "Dispatch disabled" : paused ? "Resume new work" : "Pause new work";
  $("pause").disabled = disabled || status.pause_enabled === false;
  $("pause-detail").textContent = disabled ? "Live dispatch is disabled in this workspace" : status.pause_enabled === false ? "Execution gate unavailable" : paused ? "Paused · in-flight work may still finish" : "In-flight work may finish after pausing";
  const budget = status.budget || status.ledger || {};
  const used = budget.used ?? budget.total_tokens ?? budget.tokens;
  const limit = budget.limit ?? budget.max_tokens ?? budget.limits?.max_tokens;
  $("budget-value").textContent = used != null ? `${formatNumber(used)}${limit != null ? " / " + formatNumber(limit) : ""}` : "Usage ledger";
  const ratio = typeof used === "number" && typeof limit === "number" && limit > 0 ? used / limit : 0;
  $("budget-bar").value = Math.max(0, Math.min(1, ratio));
  // Flexible ledger: show actual callback fields without assuming token/currency units.
  const details = [];
  Object.entries(budget).filter(([key]) => !["used", "limit", "enabled", "paused"].includes(key)).forEach(([key, value]) => {
    if (value && typeof value === "object" && !Array.isArray(value)) {
      Object.entries(value).forEach(([nestedKey, nestedValue]) => details.push(`${nestedKey.replaceAll("_", " ")}: ${formatNumber(nestedValue)}`));
    } else {
      details.push(`${key.replaceAll("_", " ")}: ${formatNumber(value)}`);
    }
  });
  $("budget-detail").textContent = details.join(" · ") || "Usage appears when available";
  const peers = list(status.peers);
  const peerNodes = peers.length ? peers : Array.from({length: 4}, (_, index) => ({id: `peer-${index + 1}`, name: `Peer ${index + 1}`, status: "Awaiting a run"}));
  $("peers").replaceChildren(...peerNodes.map((peer, index) => {
    const card = node("div", null, "peer");
    card.append(node("span", String(index + 1).padStart(2, "0"), "avatar"));
    const description = node("div");
    description.append(node("strong", peer.name || peer.id || `Peer ${index + 1}`), node("small", peer.status || "No status reported"));
    card.append(description);
    return card;
  }));
}
function evidenceNodes(items) {
  return list(items).map((item) => {
    const block = node("blockquote", item.quote || item.text || "No quote supplied", "evidence");
    if (item.document_id != null) {
      const link = node("button", `Open source · ${item.document_id}`);
      link.type = "button";
      link.addEventListener("click", () => openDocument(String(item.document_id)));
      block.append(link);
    }
    const checked = item.valid ?? item.quote_valid;
    const mechanical = checked === true ? "Quote text matches source" : checked === false ? "Quote text failed source check" : "Quote text not checked";
    const review = item.human_reviewed === true ? "Human review recorded" : "Not human reviewed";
    block.append(node("span", `${mechanical} · ${review}`, "evidence-status"));
    return block;
  });
}
function renderRun(run) {
  const snapshot = JSON.stringify(run);
  if (snapshot === lastRunJSON) return;
  lastRunJSON = snapshot;
  displayedRun = run;
  renderQuality(run);
  renderReplay(run);
  renderInquiries(run);
  const posts = list(run?.posts);
  renderTimeline(run);
  if (run?.mode === "inquiry_swarm") return;
  const replay = run?.mode === "chronological_replay";
  const revisions = list(run?.wiki || run?.cases);
  const latest = new Map();
  if (replay) revisions.forEach((item, index) => latest.set(item.hypothesis_id || item.id || index, item));
  const wiki = replay ? [...latest.values()] : revisions;
  const assessments = posts.filter((post) => post.phase === "assess");
  const candidates = replay ? wiki.filter((item) => item.knowledge_type === "tacit_hypothesis").length : 0;
  $("wiki-count").textContent = replay ? `${quantity(wiki.length - candidates, "observation")} · ${quantity(candidates, "candidate")} · ${quantity(revisions.length, "revision")}` : `${wiki.length} proposals · ${assessments.length} assessments`;
  $("wiki-items").replaceChildren(...wiki.map((item) => {
    const article = node("article", null, "wiki-item");
    const tags = node("div", null, "wiki-tags");
    if (replay) tags.append(node("span", item.knowledge_type === "tacit_hypothesis" ? "Candidate tacit hypothesis" : "Observation", "knowledge-type phase-tag"));
    tags.append(node("span", replay ? `Revision ${item.revision ?? "—"}` : item.kind || "working note", "phase-tag"));
    tags.append(node("span", item.transfer_tested === true ? "Transfer test recorded" : "Transfer not tested", "phase-tag"));
    article.append(tags, node("h3", item.title || "Untitled working note"), node("p", item.text || item.explanation || item.content || "", "wiki-text"));
    if (replay) article.append(node("p", `As of ${string(item.virtual_time, "unreported replay time")} · ${string(item.agent_id, "peer")} · ${string(item.hypothesis_id, "hypothesis")}`, "virtual-time"));
    const ruleLabel = item.knowledge_type === "tacit_hypothesis" ? "Candidate unwritten rule" : "Observed practice or open question";
    const fields = replay ? [[ruleLabel, item.unwritten_rule], ["Inference beyond explicit text", item.inference_gap], ["Applies when", item.applies_when], ["Exceptions", item.exceptions], ["Alternative explanation", item.alternative], ["Uncertainty", item.uncertainty], ["Prediction", item.prediction], ["Next inquiry", item.next_query]] : [["Alternative explanation", item.alternative], ["Missing evidence", item.missing_evidence], ["Next test", item.next_test]];
    const details = node("dl", null, "case-details");
    fields.forEach(([label, value]) => {
      details.append(node("dt", label), node("dd", value || "Not specified"));
    });
    article.append(details);
    if (item.independence_status) article.append(node("p", `Evidence independence: ${String(item.independence_status).replaceAll("_", " ")}`, "muted"));
    if (item.status) article.append(node("p", `Status: ${item.status}`, "muted"));
    article.append(...evidenceNodes(item.evidence));
    if (replay && list(item.counterevidence).length) {
      article.append(node("h4", "Counterevidence", "counterevidence-label"), ...evidenceNodes(item.counterevidence));
    }
    return article;
  }));
  if (!wiki.length) $("wiki-items").append(node("p", replay ? "No observations or candidate hypotheses yet. Revisions will follow the arriving evidence." : "No formal case or knowledge proposals in this run.", "empty"));
  if (assessments.length) {
    const section = node("section", null, "peer-assessments");
    section.setAttribute("aria-label", "Peer assessments");
    section.append(node("h3", "Peer assessments", "assessment-title"));
    section.append(node("p", "Final-phase interpretations are shown separately from formal proposals. They may disagree and have not established a case or a transferable rule.", "assessment-intro"));
    assessments.forEach((post) => {
      const article = node("article", null, "peer-assessment");
      article.append(node("strong", post.agent_name || post.agent_id || post.author || "Peer"));
      article.append(node("p", "Peer assessment — not a proposed case or validated rule", "assessment-label"));
      article.append(node("p", post.text || post.content || "", "wiki-text"));
      article.append(...evidenceNodes(post.evidence));
      section.append(article);
    });
    $("wiki-items").append(section);
  }
}
function renderReplay(run) {
  const replay = run?.mode === "chronological_replay";
  $("replay-summary").hidden = !replay;
  $("replay-controls").hidden = !replay;
  $("corpus-scope").hidden = !replay && run?.mode !== "inquiry_swarm";
  $("forum-title").textContent = replay ? "Chronological observations" : "Peer forum";
  $("wiki-title").textContent = replay ? "Evolving knowledge" : "Shared knowledge";
  $("wiki-note").textContent = replay ? "Observations are distinct from candidate tacit hypotheses. Candidate status requires multiple source families in this experiment, which does not establish independent episodes or a validated rule. Latest revisions are shown; transfer remains untested unless reported." : "Working interpretations require review. A matching quote checks the text, not the truth of an inferred routine or expectation.";
  if (!replay) return;
  const state = run.replay || {};
  $("replay-clock").textContent = `Virtual time: ${string(state.virtual_time, "awaiting first arrival")} · Window ${formatNumber(state.windows)}. Replay follows stored outer-message dates; delivery time is unverified.`;
  const metrics = [["Arrived", state.arrived], ["Selected", state.selected], ["Skipped", state.skipped], ["Model calls", state.model_calls]];
  $("replay-counts").replaceChildren(...metrics.map(([label, value]) => {
    const metric = node("div");
    metric.append(node("strong", formatNumber(value)), node("span", label));
    return metric;
  }));
  const coverage = state.coverage_complete === true ? "Arrival coverage complete" : state.coverage_complete === false ? "Arrival coverage incomplete" : "Arrival coverage not reported";
  $("replay-gate").textContent = `Gate: ${string(state.gate_reason, "not reported")} · Eligible: ${formatNumber(state.eligible)} · ${coverage}. Selection is not a relevance judgment; skipped messages have not received the same model review.`;
}
function readable(value, fallback = "Not reported") {
  if (value == null || value === "") return fallback;
  if (typeof value === "object") return JSON.stringify(value, null, 2);
  return String(value);
}
function updateOptions(id, entries) {
  const previous = $(id).value;
  $(id).replaceChildren(...entries.map(([value, label]) => {
    const option = node("option", label);
    option.value = value;
    return option;
  }));
  $(id).value = entries.some(([value]) => value === previous) ? previous : "all";
}
function renderInquiries(run) {
  const active = run?.mode === "inquiry_swarm";
  $("inquiry-portfolio").hidden = !active;
  $("inquiry-controls").hidden = !active;
  $("wiki").hidden = active;
  $("peers").hidden = active;
  $("research-grid").classList.toggle("inquiry-grid", active);
  $("baseline-mode").hidden = active || !run;
  $("baseline-mode").textContent = run?.mode === "chronological_replay" ? "Archived baseline: chronological rule extraction. These cards are not inquiry-driven investigations." : "Archived baseline: retrospective peer forum and proposed case notes.";
  $("workspace-eyebrow").textContent = active ? "UNFOLDING INVESTIGATIONS / ENRON" : "BASELINE WORKSPACE / ENRON";
  $("workspace-title").textContent = active ? "Follow what doesn’t add up." : "Review the earlier experiment.";
  $("workspace-subtitle").textContent = active ? "Open questions, competing explanations, and evidence that changes the account." : "Historical results remain visible for comparison with inquiry-driven discovery.";
  $("knowledge-nav").textContent = active ? "▤  Investigations" : "▤  Shared knowledge";
  $("knowledge-nav").href = active ? "#inquiry-portfolio" : "#wiki";
  if (!active) return;
  $("forum-title").textContent = "Investigation activity";
  const inquiries = list(run.inquiries);
  const state = run.metrics || run.replay || {};
  $("inquiry-count").textContent = quantity(run.monitor_truncation?.inquiries?.total ?? inquiries.length, "investigation");
  $("inquiry-clock").textContent = `Evidence available through ${string(state.virtual_time || run.virtual_time, "unreported virtual time")}. Arrival time follows the replay cursor; it does not establish when people knew something.`;
  const arrived = state.arrived ?? run.arrived;
  const eligible = state.eligible ?? run.replay?.eligible ?? run.population?.eligible ?? run.replay_bounds?.eligible;
  const hasTotal = Number.isFinite(eligible) && eligible > 0 && Number.isFinite(arrived);
  $("arrival-progress").hidden = !hasTotal;
  if (hasTotal) $("arrival-progress").value = Math.max(0, Math.min(1, arrived / eligible));
  $("inquiry-progress").textContent = `${formatNumber(arrived)}${hasTotal ? " / " + formatNumber(eligible) : ""} messages admitted${hasTotal ? " (" + (100 * arrived / eligible).toFixed(1) + "%)" : ""}. Admission is chronological availability, not evidence that every message was read by a model.`;
  const clipped = Object.entries(run.monitor_truncation || {}).filter(([, count]) => count.total > count.shown);
  $("monitor-window").hidden = !clipped.length;
  $("monitor-window").textContent = "Recent monitor window: " + clipped.map(([key, count]) => `${count.shown} of ${formatNumber(count.total)} ${key}`).join(" · ") + ". Filters apply to these displayed records. Complete audit history remains in the run store and exports.";
  const metrics = [["Arrived messages", arrived], ["Scheduled model calls", state.scheduled_calls ?? run.scheduled_calls], ["Active investigations", run.active_inquiry_count ?? inquiries.filter((item) => !["resolved", "abandoned", "closed", "retired"].includes(item.status)).length]];
  for (const [label, key] of [["Model calls", "model_calls"], ["Documents exposed to prompts", "exposed"], ["Allocated messages", "allocated"], ["Tokens", "tokens"], ["Run cost (USD)", "cost"]]) {
    if (state[key] != null) metrics.push([label, state[key]]);
  }
  const pending = run.pending ?? run.agenda?.pending;
  const running = run.running ?? run.agenda?.running;
  if (run.pending_count != null || Array.isArray(pending)) metrics.push(["Queued assignments", run.pending_count ?? pending.length]);
  if (run.running_count != null || Array.isArray(running)) metrics.push(["Running assignments", run.running_count ?? running.length]);
  $("inquiry-metrics").replaceChildren(...metrics.map(([label, value]) => {
    const metric = node("div");
    metric.append(node("strong", formatNumber(value)), node("span", label));
    return metric;
  }));
  updateOptions("inquiry-filter", [["all", "All investigations"], ...inquiries.map((item) => [String(item.inquiry_id || item.id), item.question || item.title || item.inquiry_id || item.id])]);
  const actions = [...new Set(list(run.posts).map(actionName).filter(Boolean))];
  updateOptions("action-filter", [["all", "All actions"], ...actions.map((action) => [String(action), String(action).replaceAll("_", " ")])]);
  $("inquiry-cards").replaceChildren(...inquiries.map((item) => {
    const article = node("article", null, "inquiry-card");
    const id = String(item.inquiry_id || item.id || "unidentified");
    const head = node("div", null, "inquiry-heading");
    head.append(node("h3", item.question || item.title || "Unspecified investigation question"), node("span", item.status || "Status unreported", "phase-tag"));
    article.append(head, node("p", readable(item.why_matters || item.why_interesting), "inquiry-interest"));
    const rivals = node("section", null, "inquiry-rivals");
    rivals.append(node("h4", "Competing explanations"));
    const alternatives = list(item.rivals);
    alternatives.forEach((rival, index) => {
      const text = typeof rival === "object" ? rival.explanation || rival.theory || rival.text || readable(rival) : rival;
      rivals.append(node("p", `${index + 1}. ${text}`));
    });
    if (!alternatives.length) rivals.append(node("p", "No competing explanations recorded yet."));
    article.append(rivals);
    const changes = node("dl", null, "inquiry-next");
    const next = item.next_action || list(item.next_actions).map((action) => readable(action)).join("\n");
    changes.append(node("dt", "Latest change"), node("dd", readable(item.latest_change)));
    if (item.unresolved_premise) changes.append(node("dt", "Still unresolved"), node("dd", readable(item.unresolved_premise)));
    changes.append(node("dt", "Next useful action"), node("dd", readable(next)));
    article.append(changes);
    const people = list(item.participants).map((person) => typeof person === "object" ? person.agent_id || person.id || readable(person) : person);
    article.append(node("p", `Owner: ${string(item.owner, "not recorded")} · Temporary team: ${people.length ? people.join(", ") : "No participants recorded"}`, "inquiry-team"));
    const history = Array.isArray(item.history) ? item.history : list(run.history).filter((entry) => entry.inquiry_id === id);
    const events = list(run.events).filter((event) => event.inquiry_id === id && /recruit|team|join|leave|request_peer|peer_message/.test(`${event.kind || ""} ${event.action || ""}`));
    const requests = list(run.posts).filter((post) => post.inquiry_id === id && actionName(post) === "request_peer");
    const trail = node("details", null, "inquiry-history");
    const teamHistory = events.length ? events : requests;
    trail.append(node("summary", `Theory and team history · ${history.length + teamHistory.length} entries`));
    [...history, ...teamHistory].sort((left, right) => (Date.parse(left.virtual_time || left.created_at) || 0) - (Date.parse(right.virtual_time || right.created_at) || 0) || (left.event_sequence ?? 0) - (right.event_sequence ?? 0)).forEach((entry) => {
      const row = node("div", null, "inquiry-history-entry");
      row.append(node("p", `${string(entry.virtual_time || entry.created_at, "Time unreported")} · ${string(entry.agent_id || entry.actor || entry.owner, "peer")} · ${string(actionName(entry) || entry.kind, entry.version != null ? "Version " + entry.version : "update")}`, "muted"));
      row.append(node("p", readable(entry.change || entry.latest_change || entry.text || entry.reason || entry.summary || entry.question)), ...evidenceNodes(entry.evidence));
      trail.append(row);
    });
    if (!history.length && !teamHistory.length) trail.append(node("p", "No changes or team events recorded yet."));
    article.append(trail);
    if (list(item.evidence).length) {
      const sources = node("details", null, "inquiry-history");
      sources.append(node("summary", "Current supporting evidence"), ...evidenceNodes(item.evidence));
      article.append(sources);
    }
    const follow = node("button", "Follow this investigation in the timeline", "follow-inquiry");
    follow.addEventListener("click", () => {
      $("inquiry-filter").value = id;
      $("action-filter").value = "all";
      renderTimeline(displayedRun);
      $("forum").scrollIntoView({behavior: "smooth", block: "start"});
    });
    article.append(follow);
    return article;
  }));
  if (!inquiries.length) $("inquiry-cards").append(node("p", "No investigations opened yet. Arrivals alone do not constitute a discovery.", "empty"));
}
function renderTimeline(run) {
  const inquiry = run?.mode === "inquiry_swarm";
  const replay = run?.mode === "chronological_replay" || inquiry;
  let posts = list(run?.posts);
  const total = run?.monitor_truncation?.posts?.total ?? posts.length;
  if (replay) {
    posts = [...posts].sort((left, right) => {
      const a = Date.parse(left.virtual_time);
      const b = Date.parse(right.virtual_time);
      return (Number.isNaN(a) ? Infinity : a) - (Number.isNaN(b) ? Infinity : b) || (left.arrival_sequence ?? 0) - (right.arrival_sequence ?? 0) || (left.event_sequence ?? 0) - (right.event_sequence ?? 0) || (left.window ?? 0) - (right.window ?? 0);
    });
    if (!inquiry && $("timeline-filter").value === "observations") posts = posts.filter((post) => post.phase === "observe");
    if (!inquiry && $("timeline-filter").value === "revisions") posts = posts.filter((post) => post.phase === "revise");
  }
  if (inquiry && $("inquiry-filter").value !== "all") posts = posts.filter((post) => String(post.inquiry_id) === $("inquiry-filter").value);
  if (inquiry && $("action-filter").value !== "all") posts = posts.filter((post) => String(actionName(post)) === $("action-filter").value);
  $("post-count").textContent = posts.length === total ? `${total} posts` : `${posts.length} / ${total} posts`;
  const scroll = $("posts").scrollTop;
  $("posts").replaceChildren(...posts.map((post) => {
    const article = node("article", null, "post");
    const head = node("div", null, "post-head");
    const agent = string(post.agent_name || post.agent_id || post.author, "Peer");
    head.append(node("span", agent.slice(0, 2).toUpperCase(), "avatar"), node("strong", agent));
    if (post.action || post.phase) head.append(node("span", inquiry ? actionName(post) : post.phase, "phase-tag"));
    head.append(node("time", `${replay && post.created_at ? "Recorded " : ""}${dateLabel(post.created_at)}`));
    article.append(head);
    if (inquiry && post.inquiry_id) article.append(node("p", `Investigation: ${post.inquiry_id}`, "virtual-time"));
    if (replay) article.append(node("p", `Virtual time: ${string(post.virtual_time, "not reported")} · Window ${formatNumber(post.window)} · Arrival cutoff ${formatNumber(post.arrival_sequence)}`, "virtual-time"));
    if (post.reasoning_rejection || post.reasoning_rejected) article.append(node("p", `Reasoning or action rejected: ${post.reasoning_rejection || "see the recorded update and audit event"}`, "reasoning-rejection"));
    article.append(node("p", post.text || post.content || "", "post-text"), ...evidenceNodes(post.evidence));
    return article;
  }));
  if (!posts.length) $("posts").append(node("p", replay ? "No chronological posts match this view yet." : "No posts yet. The conversation appears here as peers work.", "empty"));
  $("posts").scrollTop = scroll;
}
$("timeline-filter").addEventListener("change", () => renderTimeline(displayedRun));
$("inquiry-filter").addEventListener("change", () => renderTimeline(displayedRun));
$("action-filter").addEventListener("change", () => renderTimeline(displayedRun));
function renderQuality(run) {
  $("run-quality").hidden = !run;
  if (!run) return;
  const checks = run.quote_checks || {};
  const rejected = Number(checks.rejected || 0);
  const errors = run.agent_errors ?? run.errors;
  const errorCount = Array.isArray(errors) ? (run.monitor_truncation?.[run.agent_errors != null ? "agent_errors" : "errors"]?.total ?? errors.length) : Number(errors || 0);
  const rejectedTurns = run.reasoning_rejections ?? run.metrics?.reasoning_rejections;
  const reasoningRejections = Number(rejectedTurns || 0);
  const actionRejections = Number(run.metrics?.action_rejections || 0);
  const validation = run.validation_rejections || {};
  const validationCount = Object.values(validation).reduce((sum, value) => sum + (typeof value === "number" ? value : 0), 0);
  const rejectionStatus = run.status === "completed_with_rejections";
  const needsReview = rejected > 0 || errorCount > 0 || reasoningRejections > 0 || validationCount > 0 || actionRejections > 0 || rejectionStatus;
  $("run-quality").classList.toggle("quality-warning", needsReview);
  $("quality-title").textContent = rejected > 0 ? "Citation review needed" : errorCount > 0 ? "Agent errors need review" : reasoningRejections > 0 || rejectionStatus ? "Reasoning output rejections" : validationCount > 0 || actionRejections > 0 ? "Some proposed content failed validation" : "Evidence review status";
  const synthetic = run.synthetic === true || run.config?.synthetic === true;
  const explicitlyReal = run.synthetic === false || run.config?.synthetic === false;
  $("quality-mode").textContent = synthetic ? "Synthetic demonstration" : explicitlyReal ? "Corpus investigation" : "Data mode not reported";
  $("quality-context").textContent = `Viewing ${string(run.id, "run")} · Model: ${string(run.model, "not reported")} · Execution: ${string(run.status, "not reported")}`;
  if (typeof run.config?.peer_exchange === "boolean") $("quality-context").textContent += run.config.peer_exchange ? " · Peer exchange enabled" : " · Independent control: peer exchange disabled";
  if (run.config?.query) $("quality-context").textContent += ` · Query: ${run.config.query}`;
  if (typeof run.config?.independent === "boolean") $("quality-context").textContent += run.config.independent ? " · Independent control (peer exchange disabled)" : " · Swarm (peer exchange enabled)";
  const counts = [["Quote matches", checks.accepted], ["Rejected citations", checks.rejected], ["Completed invocations", run.completed_invocations], ["Agent errors", errors == null ? null : errorCount]];
  if (rejectedTurns != null || rejectionStatus) counts.push(["Rejected reasoning turns", rejectedTurns]);
  if (run.metrics?.action_rejections != null) counts.push(["Rejected actions", actionRejections]);
  if (run.validation_rejections != null) counts.push(["Content validation rejections", validationCount]);
  $("quality-counts").replaceChildren(...counts.map(([label, value]) => {
    const metric = node("div");
    metric.append(node("strong", formatNumber(value)), node("span", label));
    return metric;
  }));
  $("quality-explanation").textContent = `${synthetic ? "Fictional fixture data; this is not an Enron finding. " : ""}${rejected > 0 ? "Some supplied citations failed validation and were rejected. " : ""}Execution completion does not establish the truth of a finding. Quote matching is a mechanical check; claims require independent review.`;
  if (reasoningRejections > 0 || rejectionStatus) $("quality-explanation").textContent += " Malformed or truncated reasoning turns were rejected; continuing later windows does not recover those missing interpretations.";
  if (run.validation_rejections != null) $("quality-explanation").textContent += ` Content validation rejections: citations ${formatNumber(validation.citations)}, hypotheses ${formatNumber(validation.hypotheses)}, predictions ${formatNumber(validation.predictions)}. These are separate from whole-turn failures.`;
}
async function poll() {
  if (pollBusy) return;
  pollBusy = true;
  try {
    const [status, history] = await Promise.all([api("/api/status"), api("/api/runs")]);
    const entries = list(history.runs || history);
    const active = entries.find((entry) => String(entry.id) === string(status.run_id || status.active_run_id));
    renderStatus({...status, status: status.status || status.state || active?.status});
    if (followActive) selectedRun = string(status.run_id || status.active_run_id || entries[0]?.id);
    if (selectedRun && !entries.some((entry) => String(entry.id) === selectedRun)) entries.unshift({id: selectedRun});
    $("run-select").replaceChildren(...entries.map((entry) => {
      const option = node("option", `${entry.id}${entry.status ? " · " + entry.status : ""}`);
      option.value = String(entry.id);
      return option;
    }));
    if (!entries.length) $("run-select").append(node("option", "No runs yet"));
    $("run-select").value = selectedRun;
    const requestedRun = selectedRun;
    const run = requestedRun ? await api(`/api/runs/${encodeURIComponent(requestedRun)}`) : null;
    if (requestedRun === selectedRun) renderRun(run);
    $("connection").textContent = "Live · local";
    $("connection-dot").classList.remove("offline");
    notice("");
  } catch (error) {
    $("connection").textContent = "Connection interrupted";
    $("connection-dot").classList.add("offline");
    notice(`Unable to refresh: ${error.message}. Retrying automatically.`);
  } finally {
    pollBusy = false;
  }
}
$("run-select").addEventListener("change", () => {
  selectedRun = $("run-select").value;
  followActive = selectedRun === string(currentStatus.run_id || currentStatus.active_run_id);
  lastRunJSON = "";
  poll();
});
$("pause").addEventListener("click", async () => {
  $("pause").disabled = true;
  try {
    await api("/api/pause", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({paused: currentStatus.paused !== true})});
    await poll();
  } catch (error) {
    notice(`Unable to change execution gate: ${error.message}`);
  } finally {
    $("pause").disabled = currentStatus.enabled === false || currentStatus.pause_enabled === false;
  }
});
$("search-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const query = $("query").value.trim();
  if (!query) return;
  const button = event.currentTarget.querySelector("button");
  button.disabled = true;
  $("search-results").replaceChildren(node("p", "Searching local correspondence…", "empty"));
  try {
    const response = await api(`/api/search?q=${encodeURIComponent(query)}`);
    const results = list(response.results || response);
    $("search-results").replaceChildren(...results.map((result) => {
      const card = node("div", null, "result");
      const id = result.id ?? result.document_id;
      const link = node("button", result.subject || result.title || id || "Untitled document");
      link.disabled = id == null;
      link.addEventListener("click", () => openDocument(String(id)));
      card.append(link, node("p", result.snippet || result.preview || ""));
      return card;
    }));
    if (!results.length) $("search-results").append(node("p", "No matching documents.", "empty"));
  } catch (error) {
    $("search-results").replaceChildren(node("p", `Search unavailable: ${error.message}`, "empty"));
  } finally {
    button.disabled = false;
  }
});
async function openDocument(id) {
  const request = ++documentRequest;
  $("document-title").textContent = "Loading source…";
  $("document-meta").textContent = id;
  $("document-body").textContent = "";
  $("document-segments").replaceChildren();
  $("document-raw").open = true;
  if (!$("document-dialog").open) $("document-dialog").showModal();
  try {
    const response = await api(`/api/document?id=${encodeURIComponent(id)}`);
    if (request !== documentRequest) return;
    renderDocument(response.document || response, id);
  } catch (error) {
    if (request === documentRequest) $("document-body").textContent = `Source unavailable: ${error.message}`;
  }
}
function renderDocument(document, id) {
  $("document-title").textContent = document.subject || document.title || id;
  const metadata = [
    `Document occurrence: ${string(document.id || document.document_id, id)}`,
    `Outer-message sender (stored header): ${string(document.sender || document.from, "not available")}`,
    `Outer-message date (stored header): ${string(document.raw_date || document.date || document.date_utc, "not available")}`,
  ];
  $("document-meta").textContent = metadata.join("\n");
  if (["chronological_replay", "inquiry_swarm"].includes(displayedRun?.mode)) $("document-meta").textContent += "\nHuman archive inspection: this document may be outside the replay peers' admitted history.";
  $("document-body").textContent = document.body || document.text || "No body available.";
  const segments = list(document.segments).filter((segment) => segment && typeof segment === "object");
  $("document-raw").open = !segments.length;
  $("document-segments").replaceChildren();
  if (!segments.length) return;
  $("document-segments").append(node("p", "Parsed message segments. Embedded sender, date, and subject fields are claims in the text, not verified attribution. Boundaries may be ambiguous; inspect the original body when needed.", "segment-explainer"));
  const labels = {authored: "Authored text", quoted: "Quoted text", forwarded: "Forwarded text", header: "Embedded header"};
  segments.forEach((segment) => {
    const kind = Object.hasOwn(labels, segment.kind) ? segment.kind : "unknown";
    const depth = Number.isInteger(segment.depth) && segment.depth >= 0 ? segment.depth : 0;
    const section = node(kind === "header" ? "details" : "section", null, `email-segment segment-${kind} segment-depth-${Math.min(depth, 3)}`);
    const heading = node(kind === "header" ? "summary" : "div", null, "segment-heading");
    heading.append(node("strong", labels[kind] || "Unclassified text"), node("span", `Depth ${depth}`, "muted"));
    section.append(heading);
    const claims = [["Claimed sender", segment.claimed_sender], ["Claimed date", segment.claimed_date], ["Claimed subject", segment.claimed_subject]].filter(([, value]) => value);
    if (claims.length) section.append(node("p", claims.map(([label, value]) => `${label}: ${value}`).join("\n"), "segment-claims"));
    section.append(node("pre", segment.text || "", "segment-text"));
    const provenance = node("details", null, "segment-provenance");
    provenance.append(node("summary", "Segment occurrence and parser details"));
    const fields = [`Segment occurrence: ${string(segment.segment_id, "not available")}`, `Document: ${string(segment.document_id, document.id || id)}`];
    if (segment.start != null && segment.end != null) fields.push(`Body character offsets: [${segment.start}, ${segment.end})`);
    if (segment.confidence != null) fields.push(`Parser confidence: ${segment.confidence} (not claim confidence)`);
    if (segment.content_fingerprint) fields.push(`Content fingerprint: ${segment.content_fingerprint}`);
    provenance.append(node("p", fields.join("\n")));
    section.append(provenance);
    const ambiguities = Array.isArray(segment.ambiguities) ? segment.ambiguities : segment.ambiguities ? [segment.ambiguities] : [];
    if (ambiguities.length) section.append(node("p", `Parsing ambiguities: ${ambiguities.join("; ")}`, "segment-ambiguities"));
    $("document-segments").append(section);
  });
}
$("close-document").addEventListener("click", () => $("document-dialog").close());
poll();
setInterval(poll, 3000);
