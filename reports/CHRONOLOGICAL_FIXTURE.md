# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-b8e6d4a1cd48492e9dfb3ec75278d18b` · model `offline-chronological-fixture` · status **completed**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-b8e6d4a1cd48492e9dfb3ec75278d18b",
  "mode": "chronological_replay",
  "query": "Discover implicit routines and expectations",
  "model": "offline-chronological-fixture",
  "created_at": "2026-09-09T22:18:09.527651+00:00",
  "status": "completed",
  "phase": "revise",
  "config": {
    "batch_size": 4,
    "max_windows": 3,
    "turns_per_window": 2,
    "documents_per_window": 4,
    "retrieval_per_peer": 1,
    "max_output_tokens": 1800,
    "synthetic": true,
    "seed": 7
  },
  "windows": [
    {
      "window": 1,
      "virtual_time": "2001-02-07T16:00:00+00:00",
      "arrival_sequence": 4,
      "admitted": 4,
      "selected": 3,
      "duplicate_gated": 0,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 2,
      "virtual_time": "2001-03-14T22:00:00+00:00",
      "arrival_sequence": 8,
      "admitted": 4,
      "selected": 3,
      "duplicate_gated": 0,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 3,
      "virtual_time": "2001-04-12T20:00:00+00:00",
      "arrival_sequence": 12,
      "admitted": 4,
      "selected": 3,
      "duplicate_gated": 0,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    }
  ],
  "peers": [
    "routines",
    "expectations",
    "expertise",
    "contrasts"
  ],
  "agent_errors": [],
  "quote_checks": {
    "accepted": 9,
    "rejected": 0
  },
  "replay": {
    "virtual_time": "2001-04-12T20:00:00+00:00",
    "arrived": 12,
    "initial_arrived": 0,
    "selected": 9,
    "skipped": 3,
    "model_calls": 0,
    "windows": 3,
    "eligible": 12,
    "coverage_complete": true,
    "gate_reason": "novel_selected",
    "retrieval_queries": 0,
    "prompt_exposed_documents": 9
  },
  "coverage_limitations": [
    "All eligible arrivals can be admitted; only sampled novel documents are shown to models.",
    "Unselected or duplicate-gated messages are not established irrelevant.",
    "Outer-header chronology and inline attribution are not authenticated human knowledge times.",
    "Quoted support and later-arrival prediction checks do not validate tacit knowledge transfer."
  ],
  "runtime_usage": {
    "calls": 24,
    "tokens": 0,
    "cost": 0.0
  },
  "finished_at": "2026-09-09T22:18:09.574422+00:00"
}
```

## Observation timeline

### 2001-02-07T16:00:00+00:00 — review window 1

**routines / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e`; evidence `mail-60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e:0:273:5645c8b95027ba95`; origin `enron-authored:8f91282a56b805717e1b565502c1278c7179b963a233543ea890829c227ea525`.

Attribution and exact offsets: `{"segment_id": "mail-60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e:segment:0:273", "segment_kind": "authored", "claimed_sender": "mira@example.invalid", "claimed_date": "Wed, 07 Feb 2001 10:00:00 -0600", "segment_source_family": "enron-segment:6a1eec50acfa9b32686755f1ea8fefe2c1297324d5031ff77dbdd89ff6aeab3e", "segment_fingerprint": "6a1eec50acfa9b32686755f1ea8fefe2c1297324d5031ff77dbdd89ff6aeab3e", "attribution_status": "unverified_header_claim", "document_id": "mail-60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e", "span_id": "mail-60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e:0:273", "start": 0, "end": 273, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nPlease retain the delegation and the Monday authorization with the Harbor job. Retrospective filing alone should not be confused with missing authorization. This closes the documentation question.\n", "quote_fingerprint": "6a1eec50acfa9b32686755f1ea8fefe2c1297324d5031ff77dbdd89ff6aeab3e", "independence_status": "not_established", "raw_sha256": "60db3def0ed5415cd98d98941b03db9c3f4db0674f4809312d1608fe1d7f2f6e", "body_sha256": "1045f99bff541b576da4a69f5b0b8f21e92e77466d38d4a8f12e02bf61c65085", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/harbor-04.eml", "source_family": "enron-authored:8f91282a56b805717e1b565502c1278c7179b963a233543ea890829c227ea525", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> Please retain the delegation and the Monday authorization with the Harbor job. Retrospective filing alone should not be confused with missing authorization. This closes the documentation question.
> 

**expectations / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308`; evidence `mail-2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308:0:255:950d529a62237b03`; origin `enron-authored:2c948aaf2c88e1d41348e374336ed2bbd7bacd616b7c52d4fd20511fc3e3d082`.

Attribution and exact offsets: `{"segment_id": "mail-2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308:segment:0:255", "segment_kind": "authored", "claimed_sender": "jon@example.invalid", "claimed_date": "Mon, 05 Feb 2001 11:00:00 -0600", "segment_source_family": "enron-segment:4fadd09d654d6b26962cfcc71e178d3ca6fcfd50ba9fd4cffb891281f1391527", "segment_fingerprint": "4fadd09d654d6b26962cfcc71e178d3ca6fcfd50ba9fd4cffb891281f1391527", "attribution_status": "unverified_header_claim", "document_id": "mail-2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308", "span_id": "mail-2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308:0:255", "start": 0, "end": 255, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nI approved the replacement under the standing emergency maintenance delegation. The signed form will follow tomorrow. This authority covers safety repairs below the stated limit.\n", "quote_fingerprint": "4fadd09d654d6b26962cfcc71e178d3ca6fcfd50ba9fd4cffb891281f1391527", "independence_status": "not_established", "raw_sha256": "2c2e6439b9ed4806f38653170f9a278eba6d50af99c9a0c4f3b02c7c9316f308", "body_sha256": "f81a59efcb535a5035eddf7c163e77e2a09749b54dfae4fe0b2c3be5c8228b27", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/harbor-02.eml", "source_family": "enron-authored:2c948aaf2c88e1d41348e374336ed2bbd7bacd616b7c52d4fd20511fc3e3d082", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> I approved the replacement under the standing emergency maintenance delegation. The signed form will follow tomorrow. This authority covers safety repairs below the stated limit.
> 

**expertise / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef`; evidence `mail-5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef:0:247:2ce75d9cfe1dcdc9`; origin `enron-authored:8b85e11cde15db76850e4bb12a1183888daa6b45cdf1736fad83cb05f0ed7250`.

Attribution and exact offsets: `{"segment_id": "mail-5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef:segment:0:247", "segment_kind": "authored", "claimed_sender": "mira@example.invalid", "claimed_date": "Mon, 05 Feb 2001 09:00:00 -0600", "segment_source_family": "enron-segment:4c348281c9e88dc2960c5683818c361044fc4cdf5eea367cbbb46a6b02d18ca4", "segment_fingerprint": "4c348281c9e88dc2960c5683818c361044fc4cdf5eea367cbbb46a6b02d18ca4", "attribution_status": "unverified_header_claim", "document_id": "mail-5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef", "span_id": "mail-5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef:0:247", "start": 0, "end": 247, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThe Harbor valve replacement must start Tuesday morning. The written approval is not yet in the job folder. Please confirm who can authorize work before the form arrives.\n", "quote_fingerprint": "4c348281c9e88dc2960c5683818c361044fc4cdf5eea367cbbb46a6b02d18ca4", "independence_status": "not_established", "raw_sha256": "5d47c487445c124e841e099ce4fc1e74bc972a37b3446f06d7b3ae2c781a24ef", "body_sha256": "ffaf92b919b88bd04b89bf1cfcf1146424752fe9b8f67b05ec388e3816c2321e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/harbor-01.eml", "source_family": "enron-authored:8b85e11cde15db76850e4bb12a1183888daa6b45cdf1736fad83cb05f0ed7250", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> The Harbor valve replacement must start Tuesday morning. The written approval is not yet in the job folder. Please confirm who can authorize work before the form arrives.
> 

**contrasts / observe**

Synthetic chronological plumbing check; no learned practice claimed.

**routines / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expectations / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expertise / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**contrasts / revise**

Synthetic chronological plumbing check; no learned practice claimed.

### 2001-03-14T22:00:00+00:00 — review window 2

**routines / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d`; evidence `mail-4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d:0:257:5645c8b95027ba95`; origin `enron-authored:34c9b7f1a28368d3b54c8824a92e4817145e493bf8e81f2edbfce5732cf1dc4f`.

Attribution and exact offsets: `{"segment_id": "mail-4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d:segment:0:257", "segment_kind": "authored", "claimed_sender": "tessa@example.invalid", "claimed_date": "Mon, 12 Mar 2001 10:30:00 -0600", "segment_source_family": "enron-segment:51adafe1714a1531ec569d6da86251099dc31eb3689a1177554be5adc82ac8e6", "segment_fingerprint": "51adafe1714a1531ec569d6da86251099dc31eb3689a1177554be5adc82ac8e6", "attribution_status": "unverified_header_claim", "document_id": "mail-4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d", "span_id": "mail-4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d:0:257", "start": 0, "end": 257, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThere may be a change from gross units to net units, or a corrected input. I do not have the supporting worksheet attachment. Please keep both explanations open until we obtain it.\n", "quote_fingerprint": "51adafe1714a1531ec569d6da86251099dc31eb3689a1177554be5adc82ac8e6", "independence_status": "not_established", "raw_sha256": "4f5e2ac326b97924e3839b7f7c68f989dc5344f8cd15cfece8793a3eee9a476d", "body_sha256": "e8bcfd4e27c06b2f63976e8ad0320fb37f78b598280fadc7a8577ca1f6d9e6b9", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/beacon-02.eml", "source_family": "enron-authored:34c9b7f1a28368d3b54c8824a92e4817145e493bf8e81f2edbfce5732cf1dc4f", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> There may be a change from gross units to net units, or a corrected input. I do not have the supporting worksheet attachment. Please keep both explanations open until we obtain it.
> 

**expectations / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99`; evidence `mail-7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99:0:256:950d529a62237b03`; origin `enron-authored:db4bc7ca988e6299b670c23f529bf53efd6f99a41ed9075d4fe403013b7a19f5`.

Attribution and exact offsets: `{"segment_id": "mail-7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99:segment:0:256", "segment_kind": "authored", "claimed_sender": "jon@example.invalid", "claimed_date": "Tue, 13 Mar 2001 09:00:00 -0600", "segment_source_family": "enron-segment:c5588246a1f465b7b2804d3d8fa7bebefd23ea06f37c89302f83dc1bc0eb2d78", "segment_fingerprint": "c5588246a1f465b7b2804d3d8fa7bebefd23ea06f37c89302f83dc1bc0eb2d78", "attribution_status": "unverified_header_claim", "document_id": "mail-7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99", "span_id": "mail-7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99:0:256", "start": 0, "end": 256, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThe draft was revised after a call. I did not attend that call and cannot say which basis was agreed. The email archive alone does not establish who authorized the revised amount.\n", "quote_fingerprint": "c5588246a1f465b7b2804d3d8fa7bebefd23ea06f37c89302f83dc1bc0eb2d78", "independence_status": "not_established", "raw_sha256": "7887171521609a7d3ac2aa76a31ab6f9556fed85f810ace031f3da6390065d99", "body_sha256": "e8044918941b7b450fcdd30988f3e9b9edea19f7c0b2cd539dc963d14e05661f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/beacon-03.eml", "source_family": "enron-authored:db4bc7ca988e6299b670c23f529bf53efd6f99a41ed9075d4fe403013b7a19f5", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> The draft was revised after a call. I did not attend that call and cannot say which basis was agreed. The email archive alone does not establish who authorized the revised amount.
> 

**expertise / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c`; evidence `mail-dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c:0:240:2ce75d9cfe1dcdc9`; origin `enron-authored:1098af6673759520100329dc6204fc33ee1d54836ebdfd1073c2eddf049d5e3c`.

Attribution and exact offsets: `{"segment_id": "mail-dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c:segment:0:240", "segment_kind": "authored", "claimed_sender": "owen@example.invalid", "claimed_date": "Mon, 12 Mar 2001 08:30:00 -0600", "segment_source_family": "enron-segment:95f117b643a84c09829fe18cd92b95a3279a2a3b824b68a26b772d2eea60ff86", "segment_fingerprint": "95f117b643a84c09829fe18cd92b95a3279a2a3b824b68a26b772d2eea60ff86", "attribution_status": "unverified_header_claim", "document_id": "mail-dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c", "span_id": "mail-dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c:0:240", "start": 0, "end": 240, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThe Beacon worksheet shows a provisional amount of 480 units. The draft summary shows 640 units. I cannot reconcile the variance from the messages available to me.\n", "quote_fingerprint": "95f117b643a84c09829fe18cd92b95a3279a2a3b824b68a26b772d2eea60ff86", "independence_status": "not_established", "raw_sha256": "dbfa672b6e414b4bde9d2cef72341d258e5a7ab69ca61a4f1fcb553251e6ec2c", "body_sha256": "5b21e66099fe87852d38a4d7bdbc7a2a57b73e73ddfe2a77f448e23980f76dcc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/beacon-01.eml", "source_family": "enron-authored:1098af6673759520100329dc6204fc33ee1d54836ebdfd1073c2eddf049d5e3c", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> The Beacon worksheet shows a provisional amount of 480 units. The draft summary shows 640 units. I cannot reconcile the variance from the messages available to me.
> 

**contrasts / observe**

Synthetic chronological plumbing check; no learned practice claimed.

**routines / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expectations / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expertise / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**contrasts / revise**

Synthetic chronological plumbing check; no learned practice claimed.

### 2001-04-12T20:00:00+00:00 — review window 3

**routines / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8`; evidence `mail-d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8:0:264:5645c8b95027ba95`; origin `enron-authored:8c8f379a8ebf2058aa70a50096a6233189467e38ec7ba4909b5e1e9f3ad2e7de`.

Attribution and exact offsets: `{"segment_id": "mail-d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8:segment:0:264", "segment_kind": "authored", "claimed_sender": "owen@example.invalid", "claimed_date": "Tue, 10 Apr 2001 13:00:00 -0500", "segment_source_family": "enron-segment:65b240ca8243b9cb79ee955f97115cf36c9a2292acc718bf38d00beb2d647dba", "segment_fingerprint": "65b240ca8243b9cb79ee955f97115cf36c9a2292acc718bf38d00beb2d647dba", "attribution_status": "unverified_header_claim", "document_id": "mail-d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8", "span_id": "mail-d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8:0:264", "start": 0, "end": 264, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThe afternoon desk returned a capacity note for Cedar before any supervisor message appeared. I waited for the supervisor response rather than treating the capacity note as authorization.\n", "quote_fingerprint": "65b240ca8243b9cb79ee955f97115cf36c9a2292acc718bf38d00beb2d647dba", "independence_status": "not_established", "raw_sha256": "d2bef0e43bf7be2a473cd06b76fea9065b477c5e0d774b9609278d4e4fd248c8", "body_sha256": "864584c51a578924d6e8bef5223a27945e30b865580d7b70cd5d2cf06365e269", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/cedar-02.eml", "source_family": "enron-authored:8c8f379a8ebf2058aa70a50096a6233189467e38ec7ba4909b5e1e9f3ad2e7de", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> The afternoon desk returned a capacity note for Cedar before any supervisor message appeared. I waited for the supervisor response rather than treating the capacity note as authorization.
> 

**expectations / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da`; evidence `mail-94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da:0:254:950d529a62237b03`; origin `enron-authored:9888df41e28c838b70cab64228e6cdf8fae55933c005db7a617f127381f718b8`.

Attribution and exact offsets: `{"segment_id": "mail-94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da:segment:0:254", "segment_kind": "authored", "claimed_sender": "mira@example.invalid", "claimed_date": "Mon, 09 Apr 2001 08:00:00 -0500", "segment_source_family": "enron-segment:ef065ee0abcfbdec5d244eaf3c3bb7011c085d501176e8661c0b7b599dd79653", "segment_fingerprint": "ef065ee0abcfbdec5d244eaf3c3bb7011c085d501176e8661c0b7b599dd79653", "attribution_status": "unverified_header_claim", "document_id": "mail-94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da", "span_id": "mail-94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da:0:254", "start": 0, "end": 254, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nFor Cedar requests, send the draft to the afternoon desk before asking the supervisor. The desk checks capacity informally. We usually enter the final approval after that check.\n", "quote_fingerprint": "ef065ee0abcfbdec5d244eaf3c3bb7011c085d501176e8661c0b7b599dd79653", "independence_status": "not_established", "raw_sha256": "94dbbab4731082c80f8cfedf1c3c0fa0ec4b802180fe0b6c575ba177b9f900da", "body_sha256": "805ab0d6c8030e05d43e0e2beb1ea4307fc8de8c43dba3c0b7fbb172054abd12", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/cedar-01.eml", "source_family": "enron-authored:9888df41e28c838b70cab64228e6cdf8fae55933c005db7a617f127381f718b8", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> For Cedar requests, send the draft to the afternoon desk before asking the supervisor. The desk checks capacity informally. We usually enter the final approval after that check.
> 

**expertise / observe**

Synthetic chronological plumbing check; no learned practice claimed.

Source `mail-d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f`; evidence `mail-d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f:0:275:2ce75d9cfe1dcdc9`; origin `enron-authored:8a2b1d67721743748d34bd3aafaa1fd98226047ea75fd962f7566838ee4ca182`.

Attribution and exact offsets: `{"segment_id": "mail-d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f:segment:0:275", "segment_kind": "authored", "claimed_sender": "tessa@example.invalid", "claimed_date": "Thu, 12 Apr 2001 15:00:00 -0500", "segment_source_family": "enron-segment:bcee89f4dd7ee654101c132d6eb7404687e440ffaf3e212eaa6c6c5c2b7ffe6d", "segment_fingerprint": "bcee89f4dd7ee654101c132d6eb7404687e440ffaf3e212eaa6c6c5c2b7ffe6d", "attribution_status": "unverified_header_claim", "document_id": "mail-d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f", "span_id": "mail-d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f:0:275", "start": 0, "end": 275, "quote": "SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.\n\nThe written checklist omits the afternoon desk review. The messages suggest an unwritten sequencing practice, not a substitute approver. Test other periods and rejected requests before generalizing.\n", "quote_fingerprint": "bcee89f4dd7ee654101c132d6eb7404687e440ffaf3e212eaa6c6c5c2b7ffe6d", "independence_status": "not_established", "raw_sha256": "d7932e73d946b6713951cfaa022148dec79868099e60d6a6f9326432721d1d5f", "body_sha256": "d0e87d5fc42449d4b82cae1240fe7e4a6bdb8e6839a7b3fa8f5ce51470229dd0", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/tests/fixtures/enron_demo/cedar-04.eml", "source_family": "enron-authored:8a2b1d67721743748d34bd3aafaa1fd98226047ea75fd962f7566838ee4ca182", "synthetic": true, "claim_status": "interpretation"}`

> SYNTHETIC TEST FIXTURE: fictional people and events; not an Enron finding.
> 
> The written checklist omits the afternoon desk review. The messages suggest an unwritten sequencing practice, not a substitute approver. Test other periods and rejected requests before generalizing.
> 

**contrasts / observe**

Synthetic chronological plumbing check; no learned practice claimed.

**routines / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expectations / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**expertise / revise**

Synthetic chronological plumbing check; no learned practice claimed.

**contrasts / revise**

Synthetic chronological plumbing check; no learned practice claimed.

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:18:09.540670+00:00",
  "window": 1,
  "virtual_time": "2001-02-07T16:00:00+00:00",
  "arrival_sequence": 4,
  "admitted": 4,
  "selected": 3,
  "duplicate_gated": 0,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:18:09.555233+00:00",
  "window": 2,
  "virtual_time": "2001-03-14T22:00:00+00:00",
  "arrival_sequence": 8,
  "admitted": 4,
  "selected": 3,
  "duplicate_gated": 0,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:18:09.572837+00:00",
  "window": 3,
  "virtual_time": "2001-04-12T20:00:00+00:00",
  "arrival_sequence": 12,
  "admitted": 4,
  "selected": 3,
  "duplicate_gated": 0,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```
