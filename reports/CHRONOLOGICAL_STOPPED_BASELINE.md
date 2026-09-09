# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-8eed65987d1a4b7d93ef2e0581471394` · model `deepseek-v4-flash` · status **interrupted**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-8eed65987d1a4b7d93ef2e0581471394",
  "mode": "chronological_replay",
  "prompt_version": "chronological-tacit-v5",
  "prompt_sha256": "a152641f0742a910122db398adbe9241297426bcde4a5e081da242a131588930",
  "sampling_version": "body-novel-reservoir-subject-cap-v1",
  "query": "Discover implicit routines and expectations",
  "model": "deepseek-v4-flash",
  "created_at": "2026-09-09T22:39:24.320927+00:00",
  "status": "interrupted",
  "phase": "admit",
  "config": {
    "batch_size": 22000,
    "max_windows": 24,
    "turns_per_window": 2,
    "documents_per_window": 32,
    "retrieval_per_peer": 1,
    "max_output_tokens": 3000,
    "synthetic": false,
    "seed": 7
  },
  "windows": [
    {
      "window": 1,
      "virtual_time": "2000-02-18T10:05:00+00:00",
      "arrival_sequence": 22000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 13417,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 2,
      "virtual_time": "2000-05-05T17:42:00+00:00",
      "arrival_sequence": 44000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14381,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 3,
      "virtual_time": "2000-06-30T20:55:00+00:00",
      "arrival_sequence": 66000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14210,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 4,
      "virtual_time": "2000-08-16T14:45:00+00:00",
      "arrival_sequence": 88000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14828,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 5,
      "virtual_time": "2000-09-19T15:13:00+00:00",
      "arrival_sequence": 110000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14562,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 6,
      "virtual_time": "2000-10-18T12:22:00+00:00",
      "arrival_sequence": 132000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14592,
      "agent_invocations": 8,
      "gate_reason": "reasoning_error_remaining_arrivals_only"
    },
    {
      "window": 7,
      "virtual_time": "2000-11-10T15:33:00+00:00",
      "arrival_sequence": 154000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14577,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 8,
      "virtual_time": "2000-12-01T08:21:00+00:00",
      "arrival_sequence": 176000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14969,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 9,
      "virtual_time": "2000-12-14T08:53:00+00:00",
      "arrival_sequence": 198000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 15216,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 10,
      "virtual_time": "2001-01-18T15:33:00+00:00",
      "arrival_sequence": 220000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14655,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 11,
      "virtual_time": "2001-02-14T09:13:00+00:00",
      "arrival_sequence": 242000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14251,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 12,
      "virtual_time": "2001-03-12T13:36:00+00:00",
      "arrival_sequence": 264000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14097,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 13,
      "virtual_time": "2001-04-04T08:26:00+00:00",
      "arrival_sequence": 286000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 13687,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 14,
      "virtual_time": "2001-04-23T13:51:00+00:00",
      "arrival_sequence": 308000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 13877,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 15,
      "virtual_time": "2001-05-10T10:31:00+00:00",
      "arrival_sequence": 330000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 12961,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    }
  ],
  "peers": [
    "routines",
    "expectations",
    "expertise",
    "contrasts"
  ],
  "agent_errors": [
    {
      "window": 6,
      "phase": "revise",
      "agent": "routines",
      "error_type": "GateDenied"
    },
    {
      "window": 6,
      "phase": "revise",
      "agent": "expectations",
      "error_type": "GateDenied"
    },
    {
      "window": 6,
      "phase": "revise",
      "agent": "expertise",
      "error_type": "GateDenied"
    },
    {
      "window": 6,
      "phase": "revise",
      "agent": "contrasts",
      "error_type": "GateDenied"
    }
  ],
  "reasoning_rejections": 0,
  "quote_checks": {
    "accepted": 100,
    "rejected": 1
  },
  "replay": {
    "virtual_time": "2001-05-10T10:31:00+00:00",
    "arrived": 330000,
    "initial_arrived": 0,
    "selected": 480,
    "skipped": 329520,
    "model_calls": 44,
    "windows": 15,
    "eligible": 516182,
    "coverage_complete": false,
    "gate_reason": "reasoning_disabled_after_error",
    "retrieval_queries": 21,
    "prompt_exposed_documents": 195
  },
  "coverage_limitations": [
    "All eligible arrivals can be admitted; only sampled novel documents are shown to models.",
    "Unselected or duplicate-gated messages are not established irrelevant.",
    "Outer-header chronology and inline attribution are not authenticated human knowledge times.",
    "Quoted support and later-arrival prediction checks do not validate tacit knowledge transfer."
  ],
  "validation_rejections": {
    "citations": 1,
    "hypotheses": 2,
    "predictions": 20
  },
  "predictions": [
    {
      "prediction_id": "prediction-248c36f486ce44eb8f571650227345c3",
      "hypothesis_id": "hypothesis-777b76851e4c4d8fa37f08ffe4444d4a",
      "prediction": "Future software requests will also be routed via personal contacts rather than formal channels.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-83d95d8bea834bf19025f3a3bf4ea7cb",
      "hypothesis_id": "hypothesis-195878fb36fb4be2bb49d26e106fb5e5",
      "prediction": "In similar future requests, the legal contact will be the one to communicate with the external preparer, not the original requester.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-b920e68e230d449585a5546110ca79db",
      "hypothesis_id": "hypothesis-f12d44845a134f238b370d6b63cf8e8b",
      "prediction": "If a new OMLX product is cleared, Enron will use Paribas or Carr, not Merrill Lynch, unless Houston explicitly overrides.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-8f2b8fe7b7f24e27ad1e452c5dab8a26",
      "hypothesis_id": "hypothesis-b3a7fd9748f74a66bc50dca47aefd715",
      "prediction": "In future clearing house discussions, Paribas will be recommended over Carr unless specific constraints arise.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-191d61ee3be74da49dd39bb7818326ba",
      "hypothesis_id": "hypothesis-c597d57bf70545ff820e4d3c5fda3063",
      "prediction": "Future incomplete meter events will also be handled by overriding with estimates unless MIPS escalates priority.",
      "window": 2,
      "arrival_sequence": 44000
    },
    {
      "prediction_id": "prediction-54de3db5f31e4048b3afd4a19b8870c2",
      "hypothesis_id": "hypothesis-97f0c03e05004e00bb8bb7dc7e0a1fd5",
      "prediction": "In similar future absences, colleagues will be asked to cover routine tasks informally.",
      "window": 2,
      "arrival_sequence": 44000
    },
    {
      "prediction_id": "prediction-cf5631b7235e40a69b852dda244ee0fb",
      "hypothesis_id": "hypothesis-c2554531fd984b2581be381c98d7df30",
      "prediction": "Future external visit requests will be rescheduled if they conflict with internal travel plans.",
      "window": 3,
      "arrival_sequence": 66000
    },
    {
      "prediction_id": "prediction-c601f97fbc0e45238555f1159cda1c32",
      "hypothesis_id": "hypothesis-7abe00e983664568afe66333e18b2a99",
      "prediction": "In future system crashes, the responsible analyst will informally promise recovery without immediate escalation.",
      "window": 4,
      "arrival_sequence": 88000
    },
    {
      "prediction_id": "prediction-ba52391a6a6047388909d8beb952d219",
      "hypothesis_id": "hypothesis-79e070680e8649139efde6728a066eb5",
      "prediction": "In future drafting tasks, attorneys will reference prior oral agreements to determine contract terms without seeking written confirmation.",
      "window": 5,
      "arrival_sequence": 110000
    },
    {
      "prediction_id": "prediction-b5bf7cdd2c42444a9ef2c1508c28ca69",
      "hypothesis_id": "hypothesis-e509e9deb20d4aeba215795e8b1651cb",
      "prediction": "In future drafting tasks, attorneys will reference prior oral agreements to determine contract terms without seeking written confirmation.",
      "window": 5,
      "arrival_sequence": 110000
    },
    {
      "prediction_id": "prediction-ffd20425dafa4836980abe54aa09bd23",
      "hypothesis_id": "hypothesis-5e925d22dfad46aea5ec60531edfa201",
      "prediction": "In similar future drafting tasks, staff will circulate rough drafts informally for peer review before finalizing.",
      "window": 6,
      "arrival_sequence": 132000
    },
    {
      "prediction_id": "prediction-787956848c074ed993712de57778a5cc",
      "hypothesis_id": "hypothesis-ceaa329b17614a7d95e286c6ddee83b0",
      "prediction": "In similar future disputes, the dispute owner's restriction will be followed unless a senior manager explicitly overrides it.",
      "window": 6,
      "arrival_sequence": 132000
    }
  ],
  "runtime_usage": {
    "calls": 48,
    "tokens": 604518,
    "cost": 0.28206024
  },
  "finished_at": "2026-09-09T22:42:38.243154+00:00",
  "ledger_delta": {
    "calls": 44,
    "tokens": 604518,
    "cost_usd": 0.2820602400000001
  },
  "ledger_delta_scope": "Shared ledger activity during run; includes concurrent users if any.",
  "interruption_corpus_state": {
    "total": 517401,
    "eligible": 516182,
    "quarantined": 1219,
    "unknown_dates": 0,
    "documents": 340000,
    "arrived": 340000,
    "remaining": 176182,
    "cursor": [
      "2001-05-17T16:15:00+00:00",
      "mail-7656c0d546077f4ebb5f7ec10de17936e9580f9d754381bcbc1a27a02fcd11a0"
    ],
    "bounds": {
      "corpus_path": "/Users/henneberger/swarm/var/enron/corpus.sqlite",
      "start": "1999-01-01T00:00:00+00:00",
      "end": "2002-12-31T23:59:59+00:00",
      "ranking": "arrived_only_fts_v1"
    },
    "observation_basis": "outer_header_UTC_date_then_ID",
    "complete": false,
    "exhausted": false,
    "virtual_time": "2001-05-17T16:15:00+00:00",
    "session_retrieval": {
      "search_calls": 0,
      "get_calls": 0,
      "raw_reads": 0
    }
  },
  "stop_reason": "User requested fundamental reassessment of swarm discovery objective and pipeline. Shared API gate paused; active calls drained before interruption."
}
```

## Observation timeline

### 2000-02-18T10:05:00+00:00 — review window 1

**routines / observe**

Email traffic shows scheduling around holidays, document preparation, and out-of-office notices. No clear tacit rule emerges from these disparate items.

**expectations / observe**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that Enron London uses only Bank Paribas and Carr as clearing houses, with Paribas preferred for back office. This exchange reveals an implicit preference for established clearers and a need for swift confirmation before finalizing legal documents.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:9e03438d0532b536`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:0:611", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 05:19:00 -0700", "segment_source_family": "enron-segment:89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "segment_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611", "start": 0, "end": 611, "quote": "Maria,\n\nThe Clearing docs we got in from the Exchange showed Merrill Lynch in London \nas Houston's clearer.  This is not to say this is fixed, but for some reason \nthe OMLX were under the impression that it would be Merrills.  By the way, we \ncan have as many clearers as we like (provided, of course, that they are \nGeneral Clearing Members at the OMLX).\n\nIf you could let me now quite swiftly on this issue I would be very grateful \nas we finalised the legal points on Clearing docs a couple of weeks ago and I \nhave already couriered the final  versions for signature to Houston. \n\nKind regards\n\nMark   \n\n\n\n\n", "quote_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Maria,
> 
> The Clearing docs we got in from the Exchange showed Merrill Lynch in London 
> as Houston's clearer.  This is not to say this is fixed, but for some reason 
> the OMLX were under the impression that it would be Merrills.  By the way, we 
> can have as many clearers as we like (provided, of course, that they are 
> General Clearing Members at the OMLX).
> 
> If you could let me now quite swiftly on this issue I would be very grateful 
> as we finalised the legal points on Clearing docs a couple of weeks ago and I 
> have already couriered the final  versions for signature to Houston. 
> 
> Kind regards
> 
> Mark   
> 
> 
> 
> 
> 

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:9719d4f7c545293d`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

**expertise / observe**

Tana Jones routes OMLX software request to Susan Gill via Mark Elliott, showing informal referral chain. Kevin Moore's truncated Saturday email hints at office move coordination. Shirley Crenshaw announces supervisor-discretion personal days. Mark Taylor discusses paper product description wording with Bob Crane's input.

**Observation — revision 1**

When handling external software requests, Enron staff route through known internal contacts who have direct experience with the vendor, rather than using formal channels.

Inference gap: The email does not state that this is a standard practice; it only shows one instance. The contrast between Tana's referral and the absence of formal process suggests an informal norm.

Evidence basis: Single episode from Tana Jones's email, referencing Mark Elliott and Susan Gill; no other software requests in current data.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee receives a request about external software and needs to identify the appropriate contact.

Exceptions: Unknown; no counterexample in current data.

Alternative: Staff might use a centralized directory or vendor's main line instead of personal referrals.

Uncertainty: Single episode; no evidence of repeated pattern across other software requests.

Next query: Search for other software-related requests to see if similar referral chains occur.

Prediction: Future software requests will also be routed via personal contacts rather than formal channels.

Hypothesis `hypothesis-777b76851e4c4d8fa37f08ffe4444d4a`; transfer tested: false.

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:d85bd0056d80070c`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:7b98d7d9c70eea5b`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

Attribution and exact offsets: `{"segment_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:segment:0:1206", "segment_kind": "authored", "claimed_sender": "shirley.crenshaw@enron.com", "claimed_date": "Tue, 01 Feb 2000 23:29:00 -0800", "segment_source_family": "enron-segment:5c0f35373fe2db148d5e361554c0e6420f5d2979497967fa5b11dd761be607b0", "segment_fingerprint": "5c0f35373fe2db148d5e361554c0e6420f5d2979497967fa5b11dd761be607b0", "attribution_status": "unverified_header_claim", "document_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2", "span_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700", "start": 0, "end": 700, "quote": "Good morning all:\n\nThe question has arisen as to whether Enron has \"personal days\", that, \nyou can take in case of repair problems at home; car problems; sick spouse, \nsick child, etc.\n\nI checked with HR and the Policy Manual and the answer is \"no\", but they\ncan be designated at the discretion of the supervisor.  I talked this over\nwith Vince and he has decided that the Research Group will be allowed\ntwo (2) personal days per year to take care of personal business and\nnot have to take a vacation day, discretionary day, or leave of absence.\n\nIf you have advance notice (such as an air conditioner repair scheduled),\nplease let me know when you are going to take these days.  If an \nemergency ari", "quote_fingerprint": "d85ce778aaa009ef33549979c6f8aea3018dbacccff37c839984ccde2d6f531b", "independence_status": "not_established", "raw_sha256": "582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2", "body_sha256": "01c74cf778d7b9c426bf1818d1a1508bf38df22e44d5e2301033df64b1c8ea3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/all_documents/10590.", "source_family": "enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2 700"}`

> Good morning all:
> 
> The question has arisen as to whether Enron has "personal days", that, 
> you can take in case of repair problems at home; car problems; sick spouse, 
> sick child, etc.
> 
> I checked with HR and the Policy Manual and the answer is "no", but they
> can be designated at the discretion of the supervisor.  I talked this over
> with Vince and he has decided that the Research Group will be allowed
> two (2) personal days per year to take care of personal business and
> not have to take a vacation day, discretionary day, or leave of absence.
> 
> If you have advance notice (such as an air conditioner repair scheduled),
> please let me know when you are going to take these days.  If an 
> emergency ari

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:be2366fe138f7988`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:0:363", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 19 Oct 1999 06:54:00 -0700", "segment_source_family": "enron-segment:98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "segment_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363", "start": 0, "end": 363, "quote": "I fully agree with the \"fade\" effect.  But this looks right to me.  As I \nremember it, we were not totally happy with the Notional Quantity language \nbut this was the best we could do.  We were going to make sure that whether \nthe submitted volume was per day or per month was clearly reflected elsewhere \nin the long description.  Not elegant, but adequate.\n\n\n\n\n", "quote_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I fully agree with the "fade" effect.  But this looks right to me.  As I 
> remember it, we were not totally happy with the Notional Quantity language 
> but this was the best we could do.  We were going to make sure that whether 
> the submitted volume was per day or per month was clearly reflected elsewhere 
> in the long description.  Not elegant, but adequate.
> 
> 
> 
> 
> 

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:836d309747b519d8`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

**contrasts / observe**

Legal review of HPL letters is routed to Gerald Nemec, who confirms handling. Mark Taylor notes an executed Engage Energy Canada master agreement. Ben Rogers requests Con Ed annual report. Credit EOL responses are circulated. Richard Sanders finds an email unclear. Mark Taylor explains bcc delivery issues. Vince Kaminski schedules lunch meetings.

**Candidate tacit rule — revision 1**

When legal documents require approval, they are routed to the legal contact (e.g., Gerald Nemec) who then coordinates directly with the preparer, rather than the original requester.

Inference gap: Sources show Shari forwarding to Gerald because he does legal work for HPL, but do not state a general policy for all legal document approvals.

Evidence basis: Single episode: Shari Stack forwards to Gerald Nemec, who agrees to review and contact Cheryl King. No other legal routing examples in this batch.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A non-legal employee receives letters or contracts needing legal sign-off from an external party.

Exceptions: Unknown; may differ if the legal contact is unavailable or the document is routine.

Alternative: The original requester might follow up directly if no response is received.

Uncertainty: Only one episode observed; no evidence of how other legal approvals are handled.

Next query: Search for other instances where legal review is requested to see if routing to a specific legal contact is consistent.

Prediction: In similar future requests, the legal contact will be the one to communicate with the external preparer, not the original requester.

Hypothesis `hypothesis-195878fb36fb4be2bb49d26e106fb5e5`; transfer tested: false.

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:42bd648d159491c4`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

Source `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7`; evidence `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124:8f3093923a9dd018`; origin `enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca`.

Attribution and exact offsets: `{"segment_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:segment:0:124", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 30 Nov 1999 02:16:00 -0800", "segment_source_family": "enron-segment:58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "segment_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "attribution_status": "unverified_header_claim", "document_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "span_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124", "start": 0, "end": 124, "quote": "We have an executed master agreement with Engage Energy Canada L.P. which we \nreceived signed around the end of August 1999.", "quote_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "independence_status": "not_established", "raw_sha256": "570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "body_sha256": "43ee90e776923d1c8241793276d4e6af45e0b2feb58fc0e776f03f6abd632470", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/906.", "source_family": "enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> We have an executed master agreement with Engage Energy Canada L.P. which we 
> received signed around the end of August 1999.

Source `mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e`; evidence `mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:0:215:6da2710b4923d293`; origin `enron-authored:28defc3b74a4ed0b7b03b0199def6f57dccfd06f682a059705453011c0fab339`.

Attribution and exact offsets: `{"segment_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:segment:0:215", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Mon, 23 Aug 1999 13:32:00 -0700", "segment_source_family": "enron-segment:d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "segment_fingerprint": "d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "attribution_status": "unverified_header_claim", "document_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e", "span_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:0:215", "start": 0, "end": 215, "quote": "I see what you mean, and I can't explain the bcc - unfortunately, unless they \nuse \"mtaylo1@ect.enron.com\" it doesn't get here.  It must just disappear into \ncyberspace.  Thanks for continuing to send them on.\n\nMark", "quote_fingerprint": "d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "independence_status": "not_established", "raw_sha256": "156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e", "body_sha256": "f9ddcf113f4c34e335ed0bf11b830d26007edd566acdd3656fd7132e0644ee4e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/574.", "source_family": "enron-authored:28defc3b74a4ed0b7b03b0199def6f57dccfd06f682a059705453011c0fab339", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I see what you mean, and I can't explain the bcc - unfortunately, unless they 
> use "mtaylo1@ect.enron.com" it doesn't get here.  It must just disappear into 
> cyberspace.  Thanks for continuing to send them on.
> 
> Mark

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> 
> Attached are some letters that Cheryl King from HPL has prepared. I think it 
> would be more appropriate for you ( or someone from your group) to OK these 
> as from reading the email, I gather that you do the legal work for HPL. 
> 
> Can I leave it with you to get with Cheryl King? 
> 
> Many thanks, 
> 
> Shari  
> 
> 

**routines / revise**

Email traffic shows informal routing of legal and software requests through known contacts, with discretion exercised by supervisors. No strong tacit rule emerges beyond observed coordination.

**Candidate tacit rule — revision 2**

When legal documents require approval, they are routed to the legal contact (e.g., Gerald Nemec) who then coordinates directly with the preparer, rather than the original requester.

Inference gap: Sources show Shari forwarding to Gerald because he does legal work for HPL, but do not state a general policy for all legal document approvals.

Evidence basis: Two segments from the same email chain: Shari Stack forwards HPL letters to Gerald Nemec, who agrees to review and coordinate with Cheryl King. Single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A non-legal employee receives letters or contracts needing legal sign-off from an external party.

Exceptions: Unknown; may differ if the legal contact is unavailable or the document is routine.

Alternative: The original requester might follow up directly if no response is received.

Uncertainty: Only one episode observed; no evidence of how other legal approvals are handled.

Next query: Find another instance where legal documents are approved to see if routing to a legal contact is consistent.

Prediction: In similar future requests, the legal contact will be the one to communicate with the external preparer, not the original requester.

Hypothesis `hypothesis-195878fb36fb4be2bb49d26e106fb5e5`; transfer tested: false.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:05cbda84e4c9e0f7`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:0:611", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 05:19:00 -0700", "segment_source_family": "enron-segment:89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "segment_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611", "start": 0, "end": 611, "quote": "Maria,\n\nThe Clearing docs we got in from the Exchange showed Merrill Lynch in London \nas Houston's clearer.  This is not to say this is fixed, but for some reason \nthe OMLX were under the impression that it would be Merrills.  By the way, we \ncan have as many clearers as we like (provided, of course, that they are \nGeneral Clearing Members at the OMLX).\n\nIf you could let me now quite swiftly on this issue I would be very grateful \nas we finalised the legal points on Clearing docs a couple of weeks ago and I \nhave already couriered the final  versions for signature to Houston. \n\nKind regards\n\nMark   \n\n\n\n\n", "quote_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Maria,
> 
> The Clearing docs we got in from the Exchange showed Merrill Lynch in London 
> as Houston's clearer.  This is not to say this is fixed, but for some reason 
> the OMLX were under the impression that it would be Merrills.  By the way, we 
> can have as many clearers as we like (provided, of course, that they are 
> General Clearing Members at the OMLX).
> 
> If you could let me now quite swiftly on this issue I would be very grateful 
> as we finalised the legal points on Clearing docs a couple of weeks ago and I 
> have already couriered the final  versions for signature to Houston. 
> 
> Kind regards
> 
> Mark   
> 
> 
> 
> 
> 

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:87418ced7760870e`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:bc406811fe934df6`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

Attribution and exact offsets: `{"segment_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:segment:0:1206", "segment_kind": "authored", "claimed_sender": "shirley.crenshaw@enron.com", "claimed_date": "Tue, 01 Feb 2000 23:29:00 -0800", "segment_source_family": "enron-segment:5c0f35373fe2db148d5e361554c0e6420f5d2979497967fa5b11dd761be607b0", "segment_fingerprint": "5c0f35373fe2db148d5e361554c0e6420f5d2979497967fa5b11dd761be607b0", "attribution_status": "unverified_header_claim", "document_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2", "span_id": "mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700", "start": 0, "end": 700, "quote": "Good morning all:\n\nThe question has arisen as to whether Enron has \"personal days\", that, \nyou can take in case of repair problems at home; car problems; sick spouse, \nsick child, etc.\n\nI checked with HR and the Policy Manual and the answer is \"no\", but they\ncan be designated at the discretion of the supervisor.  I talked this over\nwith Vince and he has decided that the Research Group will be allowed\ntwo (2) personal days per year to take care of personal business and\nnot have to take a vacation day, discretionary day, or leave of absence.\n\nIf you have advance notice (such as an air conditioner repair scheduled),\nplease let me know when you are going to take these days.  If an \nemergency ari", "quote_fingerprint": "d85ce778aaa009ef33549979c6f8aea3018dbacccff37c839984ccde2d6f531b", "independence_status": "not_established", "raw_sha256": "582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2", "body_sha256": "01c74cf778d7b9c426bf1818d1a1508bf38df22e44d5e2301033df64b1c8ea3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/all_documents/10590.", "source_family": "enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2 700"}`

> Good morning all:
> 
> The question has arisen as to whether Enron has "personal days", that, 
> you can take in case of repair problems at home; car problems; sick spouse, 
> sick child, etc.
> 
> I checked with HR and the Policy Manual and the answer is "no", but they
> can be designated at the discretion of the supervisor.  I talked this over
> with Vince and he has decided that the Research Group will be allowed
> two (2) personal days per year to take care of personal business and
> not have to take a vacation day, discretionary day, or leave of absence.
> 
> If you have advance notice (such as an air conditioner repair scheduled),
> please let me know when you are going to take these days.  If an 
> emergency ari

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> 
> Attached are some letters that Cheryl King from HPL has prepared. I think it 
> would be more appropriate for you ( or someone from your group) to OK these 
> as from reading the email, I gather that you do the legal work for HPL. 
> 
> Can I leave it with you to get with Cheryl King? 
> 
> Many thanks, 
> 
> Shari  
> 
> 

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

**expectations / revise**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that Enron London uses only Bank Paribas and Carr as clearing houses, with Paribas preferred for back office. This exchange reveals an implicit preference for established clearers and a need for swift confirmation before finalizing legal documents.

**Candidate tacit rule — revision 1**

When Enron London selects clearing houses for new exchange-traded products, staff defer to the two established London clearers (Paribas, Carr) rather than the clearer named in exchange documentation.

Inference gap: Sources show London's stated preference for Paribas/Carr but do not state that this preference overrides exchange suggestions or Houston's needs. The contrast between Mark's mention of Merrill Lynch and Maria's list of only two clearers suggests an implicit norm, but the outcome is unknown.

Evidence basis: Two segments from the same email chain: Mark Elliott's authored message and Maria Nartey's forwarded reply. Single episode, no independent corroboration.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A new product requires clearing at OMLX and exchange documents suggest a specific clearer.

Exceptions: Unknown; may differ if the suggested clearer is already a General Clearing Member and preferred by Houston.

Alternative: Houston might insist on Merrill Lynch if they have a pre-existing relationship, overriding London's preference.

Uncertainty: Single episode; no evidence of how final decision was made or whether other clearers were considered.

Next query: Search for later emails about OMLX clearing finalization or Merrill Lynch involvement.

Prediction: If a new OMLX product is cleared, Enron will use Paribas or Carr, not Merrill Lynch, unless Houston explicitly overrides.

Hypothesis `hypothesis-f12d44845a134f238b370d6b63cf8e8b`; transfer tested: false.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:9e03438d0532b536`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:0:611", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 05:19:00 -0700", "segment_source_family": "enron-segment:89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "segment_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611", "start": 0, "end": 611, "quote": "Maria,\n\nThe Clearing docs we got in from the Exchange showed Merrill Lynch in London \nas Houston's clearer.  This is not to say this is fixed, but for some reason \nthe OMLX were under the impression that it would be Merrills.  By the way, we \ncan have as many clearers as we like (provided, of course, that they are \nGeneral Clearing Members at the OMLX).\n\nIf you could let me now quite swiftly on this issue I would be very grateful \nas we finalised the legal points on Clearing docs a couple of weeks ago and I \nhave already couriered the final  versions for signature to Houston. \n\nKind regards\n\nMark   \n\n\n\n\n", "quote_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Maria,
> 
> The Clearing docs we got in from the Exchange showed Merrill Lynch in London 
> as Houston's clearer.  This is not to say this is fixed, but for some reason 
> the OMLX were under the impression that it would be Merrills.  By the way, we 
> can have as many clearers as we like (provided, of course, that they are 
> General Clearing Members at the OMLX).
> 
> If you could let me now quite swiftly on this issue I would be very grateful 
> as we finalised the legal points on Clearing docs a couple of weeks ago and I 
> have already couriered the final  versions for signature to Houston. 
> 
> Kind regards
> 
> Mark   
> 
> 
> 
> 
> 

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:9719d4f7c545293d`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

**expertise / revise**

Mark Elliott's clearing-house preference for Paribas over Carr, despite Carr's improved back office, suggests an unwritten reliability hierarchy. This contrasts with Maria Nartey's statement that both are used, indicating a tacit preference not formally documented.

**Candidate tacit rule — revision 1**

When selecting clearing houses for London operations, Enron staff prefer Bank Paribas over Carr due to historical back-office reliability, despite Carr's recent improvements.

Inference gap: Sources state both are used and Paribas was better historically, but do not explicitly state a current preference or selection rule. The contrast between Maria's historical note and Mark's request for swift confirmation suggests an implicit preference.

Evidence basis: Two separate episodes: Maria's reply to Jeff Harbert about clearing houses, and Mark Elliott's email to Maria about OMLX clearers. Both involve London clearing arrangements but different actors and contexts.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Enron London staff choose clearing houses for new transactions or roles.

Exceptions: Unknown; may use Carr if Paribas unavailable or for specific counterparty requirements.

Alternative: Staff might choose based on current performance metrics or client mandates, not historical preference.

Uncertainty: Single episode; no evidence of repeated selection decisions or formal policy.

Next query: Look for emails discussing clearing house selection criteria or comparisons beyond this exchange.

Prediction: In future clearing house discussions, Paribas will be recommended over Carr unless specific constraints arise.

Hypothesis `hypothesis-b3a7fd9748f74a66bc50dca47aefd715`; transfer tested: false.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:17dba8b0a07c7852`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:d65c0fe358ef7e7a`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:0:611", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 05:19:00 -0700", "segment_source_family": "enron-segment:89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "segment_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611", "start": 0, "end": 611, "quote": "Maria,\n\nThe Clearing docs we got in from the Exchange showed Merrill Lynch in London \nas Houston's clearer.  This is not to say this is fixed, but for some reason \nthe OMLX were under the impression that it would be Merrills.  By the way, we \ncan have as many clearers as we like (provided, of course, that they are \nGeneral Clearing Members at the OMLX).\n\nIf you could let me now quite swiftly on this issue I would be very grateful \nas we finalised the legal points on Clearing docs a couple of weeks ago and I \nhave already couriered the final  versions for signature to Houston. \n\nKind regards\n\nMark   \n\n\n\n\n", "quote_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Maria,
> 
> The Clearing docs we got in from the Exchange showed Merrill Lynch in London 
> as Houston's clearer.  This is not to say this is fixed, but for some reason 
> the OMLX were under the impression that it would be Merrills.  By the way, we 
> can have as many clearers as we like (provided, of course, that they are 
> General Clearing Members at the OMLX).
> 
> If you could let me now quite swiftly on this issue I would be very grateful 
> as we finalised the legal points on Clearing docs a couple of weeks ago and I 
> have already couriered the final  versions for signature to Houston. 
> 
> Kind regards
> 
> Mark   
> 
> 
> 
> 
> 

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:9719d4f7c545293d`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:9e03438d0532b536`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:0:611", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 05:19:00 -0700", "segment_source_family": "enron-segment:89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "segment_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611", "start": 0, "end": 611, "quote": "Maria,\n\nThe Clearing docs we got in from the Exchange showed Merrill Lynch in London \nas Houston's clearer.  This is not to say this is fixed, but for some reason \nthe OMLX were under the impression that it would be Merrills.  By the way, we \ncan have as many clearers as we like (provided, of course, that they are \nGeneral Clearing Members at the OMLX).\n\nIf you could let me now quite swiftly on this issue I would be very grateful \nas we finalised the legal points on Clearing docs a couple of weeks ago and I \nhave already couriered the final  versions for signature to Houston. \n\nKind regards\n\nMark   \n\n\n\n\n", "quote_fingerprint": "89501815ac2440cfc938b3517153f89a1b5a6053566fad639c97a76a52b1051e", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Maria,
> 
> The Clearing docs we got in from the Exchange showed Merrill Lynch in London 
> as Houston's clearer.  This is not to say this is fixed, but for some reason 
> the OMLX were under the impression that it would be Merrills.  By the way, we 
> can have as many clearers as we like (provided, of course, that they are 
> General Clearing Members at the OMLX).
> 
> If you could let me now quite swiftly on this issue I would be very grateful 
> as we finalised the legal points on Clearing docs a couple of weeks ago and I 
> have already couriered the final  versions for signature to Houston. 
> 
> Kind regards
> 
> Mark   
> 
> 
> 
> 
> 

**contrasts / revise**

Gerald Nemec agrees to review HPL letters and coordinate with Cheryl King, confirming legal review routing. Mark Taylor notes an executed Engage Energy Canada master agreement. Mark Elliott and Maria Nartey discuss OMLX clearing arrangements, revealing preference for established clearers. Tana Jones routes OMLX software request via informal referral chain.

**Candidate tacit rule — revision 3**

When legal documents require approval, they are routed to the legal contact (e.g., Gerald Nemec) who then coordinates directly with the preparer, rather than the original requester.

Inference gap: Sources show Shari forwarding to Gerald because he does legal work for HPL, but do not state a general policy for all legal document approvals.

Evidence basis: Single episode with two segments from same email chain: Shari Stack forwards to Gerald Nemec, who agrees to review and coordinate with Cheryl King.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A non-legal employee receives letters or contracts needing legal sign-off from an external party.

Exceptions: Unknown; may differ if the legal contact is unavailable or the document is routine.

Alternative: The original requester might follow up directly if no response is received.

Uncertainty: Only one episode observed; no evidence of how other legal approvals are handled.

Next query: Find another instance where legal documents are approved to see if the legal contact always coordinates directly.

Prediction: In similar future requests, the legal contact will be the one to communicate with the external preparer, not the original requester.

Hypothesis `hypothesis-195878fb36fb4be2bb49d26e106fb5e5`; transfer tested: false.

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:42bd648d159491c4`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

Source `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7`; evidence `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124:8f3093923a9dd018`; origin `enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca`.

Attribution and exact offsets: `{"segment_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:segment:0:124", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 30 Nov 1999 02:16:00 -0800", "segment_source_family": "enron-segment:58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "segment_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "attribution_status": "unverified_header_claim", "document_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "span_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124", "start": 0, "end": 124, "quote": "We have an executed master agreement with Engage Energy Canada L.P. which we \nreceived signed around the end of August 1999.", "quote_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "independence_status": "not_established", "raw_sha256": "570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "body_sha256": "43ee90e776923d1c8241793276d4e6af45e0b2feb58fc0e776f03f6abd632470", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/906.", "source_family": "enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> We have an executed master agreement with Engage Energy Canada L.P. which we 
> received signed around the end of August 1999.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:cb7e93c364085a1c`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

Attribution and exact offsets: `{"segment_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:segment:973:3175", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "span_id": "mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673", "start": 973, "end": 1673, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315", "body_sha256": "62ae096a080156d007908332be311cdad1e1f29c81f90b2e8be10bcfd16b5257", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/10.", "source_family": "enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315 1673"}`

> 
> Jeff,
> 
> We only use two London clearing houses, Bank Paribas and Carr.  The back 
> office at Carr was not very good when I used to deal with them but I've been 
> told that they are much better now.  Paribas was definitely the better of the 
> two from a back office point of view.
> 
> Let me know if you need anything else.
> Regards,
> Maria.
> 
> 
>    
> 	Enron Capital & Trade Resources Corp.
> 	
> 	From:  Jeff Harbert                           29/04/99 18:45
> 	
> 
> To: Barry Pearce/LON/ECT@ECT
> cc: Maria Nartey/LON/ECT@ECT 
> Subject: Re: Documentation from OM  
> 
> Hi Barry,
> 
> Regarding our upcoming Pulpex "market maker" role, we're running into a few 
> problems with the clearing function.  I mentioned to Bob that it may m

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> 
> Attached are some letters that Cheryl King from HPL has prepared. I think it 
> would be more appropriate for you ( or someone from your group) to OK these 
> as from reading the email, I gather that you do the legal work for HPL. 
> 
> Can I leave it with you to get with Cheryl King? 
> 
> Many thanks, 
> 
> Shari  
> 
> 

### 2000-05-05T17:42:00+00:00 — review window 2

**routines / observe**

Recent emails show informal routing of legal and software requests through known contacts, with discretion exercised by supervisors. No strong tacit rule emerges beyond observed coordination.

Source `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b`; evidence `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592:8af3a27520e41d8e`; origin `enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8`.

Attribution and exact offsets: `{"segment_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:segment:0:592", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 23 Mar 2000 10:46:00 -0800", "segment_source_family": "enron-segment:f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "segment_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "attribution_status": "unverified_header_claim", "document_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "span_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592", "start": 0, "end": 592, "quote": "We have to respond to comments on the Credit Support Annex and a few items in \nthe Schedule..  We are waiting for copies of standing  PUC orders from PG&E \n(addressing derivatives issues) as well as a blackline of the Schedule since \nPG&E controls the drafting.  Sara\n\n\n   \n\t\n\t\n\tFrom:  Jennifer Fraser                           03/23/2000 06:32 PM\n\t\n\nTo: Sara Shackleton/HOU/ECT@ECT\ncc: Craig Breslau/HOU/ECT@ECT \nSubject: PG&E ISDA\n\nSara:\nIt appears the ball is our court. What are the outstanding issues regarding \nthe PG&E ISDA?\nOur client says he gave everything to you.\nThanks\nJennifer\n\n", "quote_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "independence_status": "not_established", "raw_sha256": "671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "body_sha256": "0287570ad7babdd0d8b1ffe1929fbed23e62dfdd8558130d97c4addd4a2bf15a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/1529.", "source_family": "enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> We have to respond to comments on the Credit Support Annex and a few items in 
> the Schedule..  We are waiting for copies of standing  PUC orders from PG&E 
> (addressing derivatives issues) as well as a blackline of the Schedule since 
> PG&E controls the drafting.  Sara
> 
> 
>    
> 	
> 	
> 	From:  Jennifer Fraser                           03/23/2000 06:32 PM
> 	
> 
> To: Sara Shackleton/HOU/ECT@ECT
> cc: Craig Breslau/HOU/ECT@ECT 
> Subject: PG&E ISDA
> 
> Sara:
> It appears the ball is our court. What are the outstanding issues regarding 
> the PG&E ISDA?
> Our client says he gave everything to you.
> Thanks
> Jennifer
> 
> 

Source `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3`; evidence `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3:0:538:ca64f11760a968ee`; origin `enron-authored:5b0a9320e008dbd86bd3074751517dc2f862053e1e89abefa8e5ea57525aed73`.

Attribution and exact offsets: `{"segment_id": "mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3:segment:0:538", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Tue, 04 Apr 2000 05:38:00 -0700", "segment_source_family": "enron-segment:dc8f01f85ffb03df72d5bc16baa235d9dd56583f33549b852f0f424e1366341c", "segment_fingerprint": "dc8f01f85ffb03df72d5bc16baa235d9dd56583f33549b852f0f424e1366341c", "attribution_status": "unverified_header_claim", "document_id": "mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3", "span_id": "mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3:0:538", "start": 0, "end": 538, "quote": "Marie:\nI left Mary Gosnell a message making sure that she was of what we are doing \nand that she needed to provide you with any additional new counterparties \nthat we have done trades with since last weeks list was compiled.  Alos, \ncould you please give Bob Bowen a call later today or first thing tomorrow if \nwe haven't heard from him?  Finally, it's my understanding that the \ncomparison Annex A that we will attach to the letter will be the new Annex A \nthat has been compared to the old annex a with the name change.  Thanks.\nCarol ", "quote_fingerprint": "dc8f01f85ffb03df72d5bc16baa235d9dd56583f33549b852f0f424e1366341c", "independence_status": "not_established", "raw_sha256": "1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3", "body_sha256": "a891442175683a9b7b390d83d264d40a3f46f895418802f242b3bcf2efb9f18f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/stclair-c/all_documents/8.", "source_family": "enron-authored:5b0a9320e008dbd86bd3074751517dc2f862053e1e89abefa8e5ea57525aed73", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Marie:
> I left Mary Gosnell a message making sure that she was of what we are doing 
> and that she needed to provide you with any additional new counterparties 
> that we have done trades with since last weeks list was compiled.  Alos, 
> could you please give Bob Bowen a call later today or first thing tomorrow if 
> we haven't heard from him?  Finally, it's my understanding that the 
> comparison Annex A that we will attach to the letter will be the new Annex A 
> that has been compared to the old annex a with the name change.  Thanks.
> Carol 

Source `mail-a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1`; evidence `mail-a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1:0:162:22497cf012df1f27`; origin `enron-authored:92afbcc26c634d7bc7dfcdf2e7edd73aa1bdaf21ba98fe81baacd60225720994`.

Attribution and exact offsets: `{"segment_id": "mail-a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1:segment:0:162", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Thu, 13 Apr 2000 04:25:00 -0700", "segment_source_family": "enron-segment:58be14a11b368f61f5bafabed6a52831ef0b8b9b7276e4f6f5bba41730f2305a", "segment_fingerprint": "58be14a11b368f61f5bafabed6a52831ef0b8b9b7276e4f6f5bba41730f2305a", "attribution_status": "unverified_header_claim", "document_id": "mail-a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1", "span_id": "mail-a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1:0:162", "start": 0, "end": 162, "quote": "David:\nPer my voice mail I have bolded the sections of the CA that I want you to \nlook at.  One is a description of the info that they are providing to us.\nCarol\n", "quote_fingerprint": "58be14a11b368f61f5bafabed6a52831ef0b8b9b7276e4f6f5bba41730f2305a", "independence_status": "not_established", "raw_sha256": "a1c29c534777423556b7fbb287ae1542512983c04a3b0adcc21927852fbf3de1", "body_sha256": "1d54aef132140f13e2b4bb9eaee2cfa98f8c59470c68b33107aa994ea36490e6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/stclair-c/all_documents/74.", "source_family": "enron-authored:92afbcc26c634d7bc7dfcdf2e7edd73aa1bdaf21ba98fe81baacd60225720994", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> David:
> Per my voice mail I have bolded the sections of the CA that I want you to 
> look at.  One is a description of the info that they are providing to us.
> Carol
> 

**expectations / observe**

New emails show routine requests for research, pricing, and meeting scheduling. Ben Rogers sends product structures for review; Chris Germany asks for research on a capacity offer; Joe Casas asks about changing a DPL ticket. No new tacit knowledge emerges beyond explicit task assignments.

Source `mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460`; evidence `mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41:4057af7bb3499a43`; origin `enron-authored:d8dc1e3da5d62539c3cb0618bbe36a115c3e10b26fdc6ebcfe521436f8c8f295`.

Attribution and exact offsets: `{"segment_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:segment:0:41", "segment_kind": "authored", "claimed_sender": "chris.germany@enron.com", "claimed_date": "Wed, 15 Mar 2000 01:54:00 -0800", "segment_source_family": "enron-span:mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41", "segment_fingerprint": "f82d5dc4eaa7930716dc0107e1ee65d7b911a1c52878bc242b654ee2d6c52a2e", "attribution_status": "unverified_header_claim", "document_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460", "span_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41", "start": 0, "end": 41, "quote": "Would you research this please?\n\nThanks\n\n", "quote_fingerprint": "f82d5dc4eaa7930716dc0107e1ee65d7b911a1c52878bc242b654ee2d6c52a2e", "independence_status": "not_established", "raw_sha256": "439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460", "body_sha256": "a8d934c14d87c209cbce8ff56c5ec51fc564c23cf567b80b430c78fb49c575e4", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/all_documents/1907.", "source_family": "enron-authored:d8dc1e3da5d62539c3cb0618bbe36a115c3e10b26fdc6ebcfe521436f8c8f295", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Would you research this please?
> 
> Thanks
> 
> 

Source `mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62`; evidence `mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62:0:44:42fd5d7ca5e31459`; origin `enron-authored:8e51652c306e98abdfcc66b805f6968654ef7c428421c72e409c3cc6e93711b6`.

Attribution and exact offsets: `{"segment_id": "mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62:segment:0:44", "segment_kind": "authored", "claimed_sender": "joe.casas@enron.com", "claimed_date": "Tue, 21 Mar 2000 08:16:00 -0800", "segment_source_family": "enron-span:mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62:0:44", "segment_fingerprint": "72f962783df7683b1016759f4988ee8ce809aba1d65b344cebd199d810ac3993", "attribution_status": "unverified_header_claim", "document_id": "mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62", "span_id": "mail-4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62:0:44", "start": 0, "end": 44, "quote": "Chris, do u want me 2 change the dpl tkt?\n\n\n", "quote_fingerprint": "72f962783df7683b1016759f4988ee8ce809aba1d65b344cebd199d810ac3993", "independence_status": "not_established", "raw_sha256": "4f41a94bc00476da42cd9a51c29600fc2ef60f41320f52be264d8780efce7c62", "body_sha256": "a40ff4dd2540a7d7d72e91ab01aa95ac5f4d7f9792806a174a9e3187f35dbf12", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/discussion_threads/847.", "source_family": "enron-authored:8e51652c306e98abdfcc66b805f6968654ef7c428421c72e409c3cc6e93711b6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Chris, do u want me 2 change the dpl tkt?
> 
> 
> 

Source `mail-3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287`; evidence `mail-3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287:0:126:83d6bfb020c8d5a1`; origin `enron-authored:4a138d611a067be86e379c05d9e388ca0dd60ba1be7974f4f0cde3fb9361c5db`.

Attribution and exact offsets: `{"segment_id": "mail-3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287:segment:0:126", "segment_kind": "authored", "claimed_sender": "benjamin.rogers@enron.com", "claimed_date": "Mon, 01 May 2000 07:04:00 -0700", "segment_source_family": "enron-segment:5b2b5779ef40491e1cceed3c42780156c0446419e9c88524c7aca1fc0d7bfa19", "segment_fingerprint": "5b2b5779ef40491e1cceed3c42780156c0446419e9c88524c7aca1fc0d7bfa19", "attribution_status": "unverified_header_claim", "document_id": "mail-3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287", "span_id": "mail-3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287:0:126", "start": 0, "end": 126, "quote": "Here is the presentation with the different product structures.  Let me know \nof any changes or additions.  Thanks\nBen\n3-7998\n", "quote_fingerprint": "5b2b5779ef40491e1cceed3c42780156c0446419e9c88524c7aca1fc0d7bfa19", "independence_status": "not_established", "raw_sha256": "3c7827f0080b3224192bf441f160e1cebdd44c631121b300ad5a198e5384e287", "body_sha256": "6f6f0face1a675bf3954cd61053a35f5bf510e2a921636c5c66f2f37a593adb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/all_documents/1467.", "source_family": "enron-authored:4a138d611a067be86e379c05d9e388ca0dd60ba1be7974f4f0cde3fb9361c5db", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Here is the presentation with the different product structures.  Let me know 
> of any changes or additions.  Thanks
> Ben
> 3-7998
> 

**expertise / observe**

New emails show informal routing of requests through known contacts (e.g., Tana Jones referring OMLX software to Susan Gill) and supervisor discretion (Vince granting personal days). No new tacit rule emerges beyond observed coordination.

**Observation — revision 1**

When MIPS sends incomplete meter data, POPS team overrides with estimated volumes rather than waiting for fix, treating it as acceptable interim measure.

Inference gap: Charlotte states they are overriding volumes but does not state this is standard practice or approved. Contrast with Lauri's forwarded concern about P&L impact suggests tension between operational necessity and financial accuracy.

Evidence basis: Charlotte's email describes the override action; Lauri's forwarded email highlights the problem's magnitude. Both are from same episode (March 21, 2000) involving POPS team and MIPS.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A mirrored meter receives an 'incomplete' from parent meter causing zero volumes in POPS.

Exceptions: Unknown; may not apply if override causes significant P&L impact or if MIPS prioritizes fix.

Alternative: Staff might escalate to MIPS management or halt allocations until corrected.

Uncertainty: Single episode; no evidence of formal approval or frequency of such overrides.

Next query: Search for other instances of POPS overrides or MIPS incomplete handling to see if this is routine.

Prediction: Future incomplete meter events will also be handled by overriding with estimates unless MIPS escalates priority.

Hypothesis `hypothesis-c597d57bf70545ff820e4d3c5fda3063`; transfer tested: false.

Source `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46`; evidence `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700:c613da22918befcc`; origin `enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991`.

Attribution and exact offsets: `{"segment_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:segment:0:1342", "segment_kind": "authored", "claimed_sender": "greg.johnston@enron.com", "claimed_date": "Thu, 27 Apr 2000 00:55:00 -0700", "segment_source_family": "enron-segment:816e7d243f48c44f545c4e0a871ec6b34d42af39c38fda2a7f976c9060672347", "segment_fingerprint": "816e7d243f48c44f545c4e0a871ec6b34d42af39c38fda2a7f976c9060672347", "attribution_status": "unverified_header_claim", "document_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46", "span_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700", "start": 0, "end": 700, "quote": "Yes, all physical gas deals are defined as \"Transactions\" under our physical \nmaster.\n\nSo, what is it.  You guys planned to do all the fun stuff the two days before \nI get there?  Thanks, I appreciate that.  Hopefully, I'll be able to get from \nthe airport to my place without needing to call you, but I can't guarnatee it!\n\n\n   \n\tEnron North America Corp.\n\t\n\tFrom:  Tana Jones                           04/27/2000 07:11 AM\n\t\n\nTo: Greg Johnston/CAL/ECT@ECT\ncc:  \nSubject: Need your help\n\nI am preparing an assignment of two physical gas trades that were incorrectly \ndone online with Canadian Imperial Bank of Commerce and ENA and assigning \nthem to CIBC World Markets plc and ECC (ECC has a physical", "quote_fingerprint": "5d75993ecaa59f2a1b9c31728bf14c51b737e30d3b2f04c68763180493d26a59", "independence_status": "not_established", "raw_sha256": "230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46", "body_sha256": "0c5943fb49e8091baef207f2c097334c3ded4dfd22a4c5ffc1c8631d1f0bb5a6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/notes_inbox/220.", "source_family": "enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46 700"}`

> Yes, all physical gas deals are defined as "Transactions" under our physical 
> master.
> 
> So, what is it.  You guys planned to do all the fun stuff the two days before 
> I get there?  Thanks, I appreciate that.  Hopefully, I'll be able to get from 
> the airport to my place without needing to call you, but I can't guarnatee it!
> 
> 
>    
> 	Enron North America Corp.
> 	
> 	From:  Tana Jones                           04/27/2000 07:11 AM
> 	
> 
> To: Greg Johnston/CAL/ECT@ECT
> cc:  
> Subject: Need your help
> 
> I am preparing an assignment of two physical gas trades that were incorrectly 
> done online with Canadian Imperial Bank of Commerce and ENA and assigning 
> them to CIBC World Markets plc and ECC (ECC has a physical

Source `mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf`; evidence `mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:0:627:e6bbce98f533377c`; origin `enron-authored:a3d9b92b4083d5b1f64bab7a551858eed6d8d7d9c715a29182777defc40e06fd`.

Attribution and exact offsets: `{"segment_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:segment:0:627", "segment_kind": "authored", "claimed_sender": "charlotte.hawkins@enron.com", "claimed_date": "Tue, 21 Mar 2000 01:32:00 -0800", "segment_source_family": "enron-segment:bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "segment_fingerprint": "bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "attribution_status": "unverified_header_claim", "document_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf", "span_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:0:627", "start": 0, "end": 627, "quote": "Daren and Lauri:\n\nWe do have a problem with some of our mirrored meters.  When MIPS receives an \n\"incomplete\" from the parent meter it sends a -0- to POPS.  Yes, this is a \nbig problem.  Our POPS team (Romeo D'Souza) has identified this problem and \nnotified MIPS.  However, he was told this was not a priority item.   In the \nmean time we are overriding the volumes in POPS with the estimated volumes.\n\nThis particular meter was correct last night, the 14th rolled last night from \nMIPS and overrode the BAV with a -0- from day 14 forward.\n\nThis was corrected this morning and the meter re-allocated.\n\nThanks,\n\nCharlotte\n\n\n\n\n\n", "quote_fingerprint": "bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "independence_status": "not_established", "raw_sha256": "5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf", "body_sha256": "48eb3e1b672ca60faa34c8f47fdc0689128a82b9d24a5f79756c12577479af46", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/all_documents/2289.", "source_family": "enron-authored:a3d9b92b4083d5b1f64bab7a551858eed6d8d7d9c715a29182777defc40e06fd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Daren and Lauri:
> 
> We do have a problem with some of our mirrored meters.  When MIPS receives an 
> "incomplete" from the parent meter it sends a -0- to POPS.  Yes, this is a 
> big problem.  Our POPS team (Romeo D'Souza) has identified this problem and 
> notified MIPS.  However, he was told this was not a priority item.   In the 
> mean time we are overriding the volumes in POPS with the estimated volumes.
> 
> This particular meter was correct last night, the 14th rolled last night from 
> MIPS and overrode the BAV with a -0- from day 14 forward.
> 
> This was corrected this morning and the meter re-allocated.
> 
> Thanks,
> 
> Charlotte
> 
> 
> 
> 
> 
> 

Source `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796`; evidence `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796:0:342:c72c02d3fec4ddf0`; origin `enron-authored:789d0befb0e09d1a6294f9a12825bb472e340c2f137c576bf8d4d70910bbc492`.

Attribution and exact offsets: `{"segment_id": "mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796:segment:0:342", "segment_kind": "authored", "claimed_sender": "jinsung.myung@enron.com", "claimed_date": "Tue, 07 Mar 2000 09:29:00 -0800", "segment_source_family": "enron-segment:a52f4dd28b4634d178fc6cbd499358d5904058ea36de7c608343209c23295a77", "segment_fingerprint": "a52f4dd28b4634d178fc6cbd499358d5904058ea36de7c608343209c23295a77", "attribution_status": "unverified_header_claim", "document_id": "mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796", "span_id": "mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796:0:342", "start": 0, "end": 342, "quote": "Edith,\n\nI talked to Tom Swank today on the Synthetic Combined Cycle. Tom wants to \nhave the capacity payment numbers based off of mid and bid curve as well as \noffer curve for indicative proposal to Aquila. Carl told me that you already \nran the model one month ago. Is it relevant idea? Let me know your thought. \nThank you.\n\nJinsung (37330)", "quote_fingerprint": "a52f4dd28b4634d178fc6cbd499358d5904058ea36de7c608343209c23295a77", "independence_status": "not_established", "raw_sha256": "2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796", "body_sha256": "9bc27dfe063088d0890d03e61a8a154987e3addb1e0bb6a16942e899e4c3ddf8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/ctg_deals/101.", "source_family": "enron-authored:789d0befb0e09d1a6294f9a12825bb472e340c2f137c576bf8d4d70910bbc492", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Edith,
> 
> I talked to Tom Swank today on the Synthetic Combined Cycle. Tom wants to 
> have the capacity payment numbers based off of mid and bid curve as well as 
> offer curve for indicative proposal to Aquila. Carl told me that you already 
> ran the model one month ago. Is it relevant idea? Let me know your thought. 
> Thank you.
> 
> Jinsung (37330)

Source `mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf`; evidence `mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:0:627:836d309747b519d8`; origin `enron-authored:a3d9b92b4083d5b1f64bab7a551858eed6d8d7d9c715a29182777defc40e06fd`.

Attribution and exact offsets: `{"segment_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:segment:0:627", "segment_kind": "authored", "claimed_sender": "charlotte.hawkins@enron.com", "claimed_date": "Tue, 21 Mar 2000 01:32:00 -0800", "segment_source_family": "enron-segment:bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "segment_fingerprint": "bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "attribution_status": "unverified_header_claim", "document_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf", "span_id": "mail-5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf:0:627", "start": 0, "end": 627, "quote": "Daren and Lauri:\n\nWe do have a problem with some of our mirrored meters.  When MIPS receives an \n\"incomplete\" from the parent meter it sends a -0- to POPS.  Yes, this is a \nbig problem.  Our POPS team (Romeo D'Souza) has identified this problem and \nnotified MIPS.  However, he was told this was not a priority item.   In the \nmean time we are overriding the volumes in POPS with the estimated volumes.\n\nThis particular meter was correct last night, the 14th rolled last night from \nMIPS and overrode the BAV with a -0- from day 14 forward.\n\nThis was corrected this morning and the meter re-allocated.\n\nThanks,\n\nCharlotte\n\n\n\n\n\n", "quote_fingerprint": "bcc64c08820d724acde9809fdaa4b777ceacd8531daef14c104ecae95c27f39a", "independence_status": "not_established", "raw_sha256": "5c3d30a8e011320e3f9916811a9e012816720cb1ae993ac939d74998f1813caf", "body_sha256": "48eb3e1b672ca60faa34c8f47fdc0689128a82b9d24a5f79756c12577479af46", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/all_documents/2289.", "source_family": "enron-authored:a3d9b92b4083d5b1f64bab7a551858eed6d8d7d9c715a29182777defc40e06fd", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Daren and Lauri:
> 
> We do have a problem with some of our mirrored meters.  When MIPS receives an 
> "incomplete" from the parent meter it sends a -0- to POPS.  Yes, this is a 
> big problem.  Our POPS team (Romeo D'Souza) has identified this problem and 
> notified MIPS.  However, he was told this was not a priority item.   In the 
> mean time we are overriding the volumes in POPS with the estimated volumes.
> 
> This particular meter was correct last night, the 14th rolled last night from 
> MIPS and overrode the BAV with a -0- from day 14 forward.
> 
> This was corrected this morning and the meter re-allocated.
> 
> Thanks,
> 
> Charlotte
> 
> 
> 
> 
> 
> 

**contrasts / observe**

Ben Thomason delegates deal list maintenance to Ben during his honeymoon, indicating informal backup coverage. Sara Shackleton clarifies she did not verify guaranty form before sending, showing reliance on prior distribution. Ben Rogers delays B-school to improve grades, suggesting career planning flexibility.

**Observation — revision 1**

When a colleague is absent, another with access to shared drives is expected to maintain their routine tasks without formal reassignment.

Inference gap: The email does not state that this is a standard practice; it only shows one instance. The contrast between the informal request and the absence of formal reassignment suggests an implicit norm.

Evidence basis: Single authored email from Ben Thomason to Ben, one episode, no complementary traces.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee goes on leave and has a shared file repository accessible to a colleague.

Exceptions: Unknown; may not apply if the task requires specific expertise or if no colleague has access.

Alternative: Tasks might be reassigned formally by a manager or left until the employee returns.

Uncertainty: Single episode; no evidence of a broader pattern across other absences.

Next query: read: mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf 447

Prediction: In similar future absences, colleagues will be asked to cover routine tasks informally.

Hypothesis `hypothesis-97f0c03e05004e00bb8bb7dc7e0a1fd5`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-777b76851e4c4d8fa37f08ffe4444d4a",
    "prediction_id": "prediction-248c36f486ce44eb8f571650227345c3",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test the software routing prediction.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  },
  {
    "hypothesis_id": "hypothesis-195878fb36fb4be2bb49d26e106fb5e5",
    "prediction_id": "prediction-83d95d8bea834bf19025f3a3bf4ea7cb",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test the legal routing prediction.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  }
]
```

Source `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf`; evidence `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447:6a0751eb154f33de`; origin `enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e`.

Attribution and exact offsets: `{"segment_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:segment:0:447", "segment_kind": "authored", "claimed_sender": "benjamin.thomason@enron.com", "claimed_date": "Tue, 29 Feb 2000 09:55:00 -0800", "segment_source_family": "enron-segment:8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "segment_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "attribution_status": "unverified_header_claim", "document_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "span_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447", "start": 0, "end": 447, "quote": "Ben,\n\nI will be out of the office for the next couple of weeks on a honeymoon.  I \nwill be out until March 20th, so could you keep the deal list updated until \nthen?  Tina told me that you should already have access to the O:drive where \nit is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I \ncreated a new format so it will look little different.  Please let me know if \nyou have any questions.\n\nThank you,\n\nBen Thomason\nx-58802", "quote_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "independence_status": "not_established", "raw_sha256": "253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "body_sha256": "825f78c7f345a69b1fc7464e72c98c5fe8f7ad26223c6bf17c97921bd1c7a06a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/discussion_threads/286.", "source_family": "enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Ben,
> 
> I will be out of the office for the next couple of weeks on a honeymoon.  I 
> will be out until March 20th, so could you keep the deal list updated until 
> then?  Tina told me that you should already have access to the O:drive where 
> it is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I 
> created a new format so it will look little different.  Please let me know if 
> you have any questions.
> 
> Thank you,
> 
> Ben Thomason
> x-58802

Source `mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8`; evidence `mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8:0:700:efe7b3901f4220fb`; origin `enron-authored:2202cfac35a023ff97b1260e1c38d9a653bbf63b7488be8723216b8ed3b82a20`.

Attribution and exact offsets: `{"segment_id": "mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8:segment:0:902", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Wed, 12 Apr 2000 05:42:00 -0700", "segment_source_family": "enron-segment:9980cba7caa1cd170ab59e37609bb96cbb1a2e810348a3f0ec45491c1d051fbc", "segment_fingerprint": "9980cba7caa1cd170ab59e37609bb96cbb1a2e810348a3f0ec45491c1d051fbc", "attribution_status": "unverified_header_claim", "document_id": "mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8", "span_id": "mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8:0:700", "start": 0, "end": 700, "quote": "Bob:  I haven't commented on preferred guaranty formats, I only asked Kris to \nfax the form of guaranty which Ed Wood had sent originally.  I thought that \nthe e-mailed guaranty was the same as Ed Wood had distributed but I hadn't \nverified that item prior to sending.  I have not had a chance to review \nKris's fax   If you have your own form, please send and we can review.  Sara\n\n\n\n\nRobert.Aicher@kmz.com on 04/12/2000 11:54:27 AM\nTo: \"Sara Shackleton\" <Sara.Shackleton@enron.com>\ncc: kris.grosshans@abnamro.com \nSubject: Re: ABN AMRO margin line agreement\n\n\n\nSara, I received your e-mail yesterday and was unsure whether the form of\nguaranty you attached was the correct form. I understand you ta", "quote_fingerprint": "c2932a95ba0bb23ddea122f581acdd5cb03be04e687fb48c86a7dffd05ad5e49", "independence_status": "not_established", "raw_sha256": "17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8", "body_sha256": "31c531b292a31b35bbba1ed42c6a062162033498116f746cdb907cde9af98f8a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/1182.", "source_family": "enron-authored:2202cfac35a023ff97b1260e1c38d9a653bbf63b7488be8723216b8ed3b82a20", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-17ae9e1b3b86c1223728dff0999826890b615ed12dab5583041656ce0a8bd4e8 700"}`

> Bob:  I haven't commented on preferred guaranty formats, I only asked Kris to 
> fax the form of guaranty which Ed Wood had sent originally.  I thought that 
> the e-mailed guaranty was the same as Ed Wood had distributed but I hadn't 
> verified that item prior to sending.  I have not had a chance to review 
> Kris's fax   If you have your own form, please send and we can review.  Sara
> 
> 
> 
> 
> Robert.Aicher@kmz.com on 04/12/2000 11:54:27 AM
> To: "Sara Shackleton" <Sara.Shackleton@enron.com>
> cc: kris.grosshans@abnamro.com 
> Subject: Re: ABN AMRO margin line agreement
> 
> 
> 
> Sara, I received your e-mail yesterday and was unsure whether the form of
> guaranty you attached was the correct form. I understand you ta

Source `mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302`; evidence `mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302:0:632:c54d5488eae53f7d`; origin `enron-authored:837079e1e4cff149ece31ecd3c90d739b2270466435c86841539a085173ca4f0`.

Attribution and exact offsets: `{"segment_id": "mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302:segment:0:632", "segment_kind": "authored", "claimed_sender": "benjamin.rogers@enron.com", "claimed_date": "Fri, 05 May 2000 09:11:00 -0700", "segment_source_family": "enron-segment:b9abc0cf858886227a40e5298da2dcf5d91c025a45484072931b9b05608afe76", "segment_fingerprint": "b9abc0cf858886227a40e5298da2dcf5d91c025a45484072931b9b05608afe76", "attribution_status": "unverified_header_claim", "document_id": "mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302", "span_id": "mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302:0:632", "start": 0, "end": 632, "quote": "Hey, sorry its been a little while but I've been traveling and keeping some \nlate hours on these generation projects.  With regards to UT, I am going to \nstay at Enron for another year.  I feel that the thing that hurt me from \ngetting in the schools I wanted to get into were my undergraduate grades.  So \nI have decided to take a couple of graduate level finance courses this summer \nand re-apply next year.  Actually, I'll apply to Columbia this Sept to get \ninto their January program, which goes for a year and half.  \n\nSo lets get together for lunch before you head off for B-school this summer.  \nTalk to you soon.\nBen\n3-7998", "quote_fingerprint": "b9abc0cf858886227a40e5298da2dcf5d91c025a45484072931b9b05608afe76", "independence_status": "not_established", "raw_sha256": "2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302", "body_sha256": "e06a6d27d2b5a64846e4effd2d8e91076d15b33261427dc5d4786e958acb706a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/_sent_mail/564.", "source_family": "enron-authored:837079e1e4cff149ece31ecd3c90d739b2270466435c86841539a085173ca4f0", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Hey, sorry its been a little while but I've been traveling and keeping some 
> late hours on these generation projects.  With regards to UT, I am going to 
> stay at Enron for another year.  I feel that the thing that hurt me from 
> getting in the schools I wanted to get into were my undergraduate grades.  So 
> I have decided to take a couple of graduate level finance courses this summer 
> and re-apply next year.  Actually, I'll apply to Columbia this Sept to get 
> into their January program, which goes for a year and half.  
> 
> So lets get together for lunch before you head off for B-school this summer.  
> Talk to you soon.
> Ben
> 3-7998

Source `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf`; evidence `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447:836d309747b519d8`; origin `enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e`.

Attribution and exact offsets: `{"segment_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:segment:0:447", "segment_kind": "authored", "claimed_sender": "benjamin.thomason@enron.com", "claimed_date": "Tue, 29 Feb 2000 09:55:00 -0800", "segment_source_family": "enron-segment:8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "segment_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "attribution_status": "unverified_header_claim", "document_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "span_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447", "start": 0, "end": 447, "quote": "Ben,\n\nI will be out of the office for the next couple of weeks on a honeymoon.  I \nwill be out until March 20th, so could you keep the deal list updated until \nthen?  Tina told me that you should already have access to the O:drive where \nit is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I \ncreated a new format so it will look little different.  Please let me know if \nyou have any questions.\n\nThank you,\n\nBen Thomason\nx-58802", "quote_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "independence_status": "not_established", "raw_sha256": "253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "body_sha256": "825f78c7f345a69b1fc7464e72c98c5fe8f7ad26223c6bf17c97921bd1c7a06a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/discussion_threads/286.", "source_family": "enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Ben,
> 
> I will be out of the office for the next couple of weeks on a honeymoon.  I 
> will be out until March 20th, so could you keep the deal list updated until 
> then?  Tina told me that you should already have access to the O:drive where 
> it is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I 
> created a new format so it will look little different.  Please let me know if 
> you have any questions.
> 
> Thank you,
> 
> Ben Thomason
> x-58802

**routines / revise**

New email shows Executive Compensation procedures requiring signed request forms before distributing drafts, with specific exceptions needing justification. This is an explicit instruction, not tacit knowledge.

Source `mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264`; evidence `mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264:3187:3887:79012d7031f7ab21`; origin `enron-authored:bf94c1221bc6f37f91849e8c50877d4a094f0a4d75f7c6b2edbef30319b1f0e8`.

Attribution and exact offsets: `{"segment_id": "mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264:segment:2487:4053", "segment_kind": "forwarded", "claimed_sender": "Mary Joyce@ENRON", "claimed_date": "05/03/00 01:19 PM", "segment_source_family": "enron-segment:8c8847e5b6affa3a49d6f84dd939523ee2f9f14f221a8bf3f38e0a7734c5be12", "segment_fingerprint": "8c8847e5b6affa3a49d6f84dd939523ee2f9f14f221a8bf3f38e0a7734c5be12", "attribution_status": "unverified_header_claim", "document_id": "mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264", "span_id": "mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264:3187:3887", "start": 3187, "end": 3887, "quote": "nerating drafts.  Please do not distribute a draft to \nanyone without a signed and initialed request form.\n\nAlso, as discussed, requests for signing bonuses, retention bonuses, up-front \ngrants by number of options rather than value, and guaranteed LTI awards are \nexceptions to the rules that the business units will need to justify before \nthey will be approved.  Please do not make changes to these items or add any \nprovisions to the standard short form without contacting Executive \nCompensation.\n\nThese procedures have been implemented at the request of the Office of the \nChairman.  Consistent application of compensation standards and attention to \nthe One Enron goal are key to our success.\n", "quote_fingerprint": "52a00a9d9df61eb93d2f75fb54bab8d7ea335b98eb341f6b852dd9894a97fa49", "independence_status": "not_established", "raw_sha256": "61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264", "body_sha256": "91430bd2d7f36adbd72706962ab6b49c040915940238e61fba7412befcc285b4", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/cash-m/all_documents/739.", "source_family": "enron-authored:bf94c1221bc6f37f91849e8c50877d4a094f0a4d75f7c6b2edbef30319b1f0e8", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-61f9b39225e557b87bde6c89268f176158861f59b5553964fef6ff22b68d0264 3887"}`

> nerating drafts.  Please do not distribute a draft to 
> anyone without a signed and initialed request form.
> 
> Also, as discussed, requests for signing bonuses, retention bonuses, up-front 
> grants by number of options rather than value, and guaranteed LTI awards are 
> exceptions to the rules that the business units will need to justify before 
> they will be approved.  Please do not make changes to these items or add any 
> provisions to the standard short form without contacting Executive 
> Compensation.
> 
> These procedures have been implemented at the request of the Office of the 
> Chairman.  Consistent application of compensation standards and attention to 
> the One Enron goal are key to our success.
> 

**expectations / revise**

Capacity offer forwarded through multiple Enron contacts to Chris Germany, who asks for research. No new tacit rule emerges; explicit task delegation only.

Source `mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460`; evidence `mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41:4057af7bb3499a43`; origin `enron-authored:d8dc1e3da5d62539c3cb0618bbe36a115c3e10b26fdc6ebcfe521436f8c8f295`.

Attribution and exact offsets: `{"segment_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:segment:0:41", "segment_kind": "authored", "claimed_sender": "chris.germany@enron.com", "claimed_date": "Wed, 15 Mar 2000 01:54:00 -0800", "segment_source_family": "enron-span:mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41", "segment_fingerprint": "f82d5dc4eaa7930716dc0107e1ee65d7b911a1c52878bc242b654ee2d6c52a2e", "attribution_status": "unverified_header_claim", "document_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460", "span_id": "mail-439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460:0:41", "start": 0, "end": 41, "quote": "Would you research this please?\n\nThanks\n\n", "quote_fingerprint": "f82d5dc4eaa7930716dc0107e1ee65d7b911a1c52878bc242b654ee2d6c52a2e", "independence_status": "not_established", "raw_sha256": "439d9ac968d079ad807fff45246d68c4c27a03f33a9ceeba787b1eaa9865d460", "body_sha256": "a8d934c14d87c209cbce8ff56c5ec51fc564c23cf567b80b430c78fb49c575e4", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/all_documents/1907.", "source_family": "enron-authored:d8dc1e3da5d62539c3cb0618bbe36a115c3e10b26fdc6ebcfe521436f8c8f295", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Would you research this please?
> 
> Thanks
> 
> 

Source `mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8`; evidence `mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8:0:36:c080a904448b28d0`; origin `enron-authored:3e1427ce250628c413978b513985d8742fc6ee48884926282a95ab783584ee1c`.

Attribution and exact offsets: `{"segment_id": "mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8:segment:0:36", "segment_kind": "authored", "claimed_sender": "bperron@columbiaenergygroup.com", "claimed_date": "Wed, 15 Mar 2000 02:07:00 -0800", "segment_source_family": "enron-span:mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8:0:36", "segment_fingerprint": "bf66c8ed419ded2eb7115297ffaf60a0472d576d748249f6d9396078f6a94331", "attribution_status": "unverified_header_claim", "document_id": "mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8", "span_id": "mail-25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8:0:36", "start": 0, "end": 36, "quote": "I was asked to forward this to you.\n", "quote_fingerprint": "bf66c8ed419ded2eb7115297ffaf60a0472d576d748249f6d9396078f6a94331", "independence_status": "not_established", "raw_sha256": "25146d3b0d5529d24e0639e2e00c6e86af499f0be83ee66f10f11ba7928030c8", "body_sha256": "9cdeeb007e6244937409b4b368622b8ac9c98068e877b477d4ec597837102053", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/discussion_threads/772.", "source_family": "enron-authored:3e1427ce250628c413978b513985d8742fc6ee48884926282a95ab783584ee1c", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I was asked to forward this to you.
> 

**expertise / revise**

Greg Johnston confirms physical gas deals are 'Transactions' under ECC master, enabling assignment to CIBC. This explicit confirmation supports legal definitional consistency across entities.

Source `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46`; evidence `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700:5187a6881fab27b8`; origin `enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991`.

Attribution and exact offsets: `{"segment_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:segment:0:1342", "segment_kind": "authored", "claimed_sender": "greg.johnston@enron.com", "claimed_date": "Thu, 27 Apr 2000 00:55:00 -0700", "segment_source_family": "enron-segment:816e7d243f48c44f545c4e0a871ec6b34d42af39c38fda2a7f976c9060672347", "segment_fingerprint": "816e7d243f48c44f545c4e0a871ec6b34d42af39c38fda2a7f976c9060672347", "attribution_status": "unverified_header_claim", "document_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46", "span_id": "mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700", "start": 0, "end": 700, "quote": "Yes, all physical gas deals are defined as \"Transactions\" under our physical \nmaster.\n\nSo, what is it.  You guys planned to do all the fun stuff the two days before \nI get there?  Thanks, I appreciate that.  Hopefully, I'll be able to get from \nthe airport to my place without needing to call you, but I can't guarnatee it!\n\n\n   \n\tEnron North America Corp.\n\t\n\tFrom:  Tana Jones                           04/27/2000 07:11 AM\n\t\n\nTo: Greg Johnston/CAL/ECT@ECT\ncc:  \nSubject: Need your help\n\nI am preparing an assignment of two physical gas trades that were incorrectly \ndone online with Canadian Imperial Bank of Commerce and ENA and assigning \nthem to CIBC World Markets plc and ECC (ECC has a physical", "quote_fingerprint": "5d75993ecaa59f2a1b9c31728bf14c51b737e30d3b2f04c68763180493d26a59", "independence_status": "not_established", "raw_sha256": "230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46", "body_sha256": "0c5943fb49e8091baef207f2c097334c3ded4dfd22a4c5ffc1c8631d1f0bb5a6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/notes_inbox/220.", "source_family": "enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46 700"}`

> Yes, all physical gas deals are defined as "Transactions" under our physical 
> master.
> 
> So, what is it.  You guys planned to do all the fun stuff the two days before 
> I get there?  Thanks, I appreciate that.  Hopefully, I'll be able to get from 
> the airport to my place without needing to call you, but I can't guarnatee it!
> 
> 
>    
> 	Enron North America Corp.
> 	
> 	From:  Tana Jones                           04/27/2000 07:11 AM
> 	
> 
> To: Greg Johnston/CAL/ECT@ECT
> cc:  
> Subject: Need your help
> 
> I am preparing an assignment of two physical gas trades that were incorrectly 
> done online with Canadian Imperial Bank of Commerce and ENA and assigning 
> them to CIBC World Markets plc and ECC (ECC has a physical

**contrasts / revise**

Ben Thomason delegates deal list maintenance to Ben during his honeymoon, indicating informal backup coverage. Sara Shackleton clarifies she did not verify guaranty form before sending, showing reliance on prior distribution. Ben Rogers delays B-school to improve grades, suggesting career planning flexibility.

Source `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf`; evidence `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447:6a0751eb154f33de`; origin `enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e`.

Attribution and exact offsets: `{"segment_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:segment:0:447", "segment_kind": "authored", "claimed_sender": "benjamin.thomason@enron.com", "claimed_date": "Tue, 29 Feb 2000 09:55:00 -0800", "segment_source_family": "enron-segment:8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "segment_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "attribution_status": "unverified_header_claim", "document_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "span_id": "mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447", "start": 0, "end": 447, "quote": "Ben,\n\nI will be out of the office for the next couple of weeks on a honeymoon.  I \nwill be out until March 20th, so could you keep the deal list updated until \nthen?  Tina told me that you should already have access to the O:drive where \nit is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I \ncreated a new format so it will look little different.  Please let me know if \nyou have any questions.\n\nThank you,\n\nBen Thomason\nx-58802", "quote_fingerprint": "8c233a004a5fbfc4cc5db644228a911767e1464546b5f51b640f1540f635fcfc", "independence_status": "not_established", "raw_sha256": "253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf", "body_sha256": "825f78c7f345a69b1fc7464e72c98c5fe8f7ad26223c6bf17c97921bd1c7a06a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/discussion_threads/286.", "source_family": "enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Ben,
> 
> I will be out of the office for the next couple of weeks on a honeymoon.  I 
> will be out until March 20th, so could you keep the deal list updated until 
> then?  Tina told me that you should already have access to the O:drive where 
> it is now listed.  You can access it at O:Corpdev/Gtg/Deals/Newlist.  I 
> created a new format so it will look little different.  Please let me know if 
> you have any questions.
> 
> Thank you,
> 
> Ben Thomason
> x-58802

### 2000-06-30T20:55:00+00:00 — review window 3

**routines / observe**

New emails show routine access requests, file transfers, and informal task delegation. No new tacit rules emerge; explicit instructions dominate. Existing hypotheses remain unsupported by new evidence.

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:188a22f12da2216a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177`; evidence `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266:d4a3f7c3f4ab2623`; origin `enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e`.

Attribution and exact offsets: `{"segment_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:segment:0:266", "segment_kind": "authored", "claimed_sender": "clement.lau@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:22:00 -0700", "segment_source_family": "enron-segment:3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "segment_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "attribution_status": "unverified_header_claim", "document_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "span_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266", "start": 0, "end": 266, "quote": "I have saved the first info memo (generic version, w/o mentioned of Orion) \nunder \"EGC12-Generic-051100\" and various site pictures and maps under \n\"Pictures\" folder, both in o:/_dropbox.\n\nI will continue transfering file to the o:_dropbox over the next few days.\n\n  ", "quote_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "independence_status": "not_established", "raw_sha256": "27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "body_sha256": "21a1b7ec9a36c79908e6474294f323c67e3aae49b1e218fdaf244a9816cb2b3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/genco_jv_ipo/437.", "source_family": "enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I have saved the first info memo (generic version, w/o mentioned of Orion) 
> under "EGC12-Generic-051100" and various site pictures and maps under 
> "Pictures" folder, both in o:/_dropbox.
> 
> I will continue transfering file to the o:_dropbox over the next few days.
> 
>   

Source `mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35`; evidence `mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35:0:700:ae284dfa0cc4c8ee`; origin `enron-authored:65e7e9472635370bc4ea7e4f151503152a5f1d199728dd32d836f64e1c1f44b5`.

Attribution and exact offsets: `{"segment_id": "mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35:segment:0:958", "segment_kind": "authored", "claimed_sender": "michael.eiben@enron.com", "claimed_date": "Thu, 22 Jun 2000 06:09:00 -0700", "segment_source_family": "enron-segment:dd97fdc65577a79ddd04362d6259e230ce062ca5d05f193355b4a0338c5b4794", "segment_fingerprint": "dd97fdc65577a79ddd04362d6259e230ce062ca5d05f193355b4a0338c5b4794", "attribution_status": "unverified_header_claim", "document_id": "mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35", "span_id": "mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35:0:700", "start": 0, "end": 700, "quote": "We need to discuss further.  My concern would be that how do we know what % \nHPL should be retaining at a compressor or zone to make sure we recoup our \nfuel cost ?  Also, could allocated fuel cause a contract imbalance?  I think \nthat Pipeline Operations can handle the scheduling of third party fuel \nretainage.  But, if we retain fuel on ENA transports, then we need to come up \nwith a plan to nominate this in Marketing Operations to Houston Pipeline.  \nCurrently, this process is not in place.\n\n\n   \n\tEnron North America Corp.\n\t\n\tFrom:  Brenda F Herod                           06/22/2000 12:35 PM\n\t\n\nTo: Lisa Csikos/HOU/ECT@ECT, Daren J Farmer/HOU/ECT@ECT, Mary M \nSmith/HOU/ECT@ECT, Rita Wynne", "quote_fingerprint": "a678628508a0485875527febae996a576cd7f0734cd8692158d712efd92cdc6e", "independence_status": "not_established", "raw_sha256": "2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35", "body_sha256": "fc18bb0cb97a323675cafa831737b677b38821980917df5cacab2cffbcde2ee8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/all_documents/1489.", "source_family": "enron-authored:65e7e9472635370bc4ea7e4f151503152a5f1d199728dd32d836f64e1c1f44b5", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35 700"}`

> We need to discuss further.  My concern would be that how do we know what % 
> HPL should be retaining at a compressor or zone to make sure we recoup our 
> fuel cost ?  Also, could allocated fuel cause a contract imbalance?  I think 
> that Pipeline Operations can handle the scheduling of third party fuel 
> retainage.  But, if we retain fuel on ENA transports, then we need to come up 
> with a plan to nominate this in Marketing Operations to Houston Pipeline.  
> Currently, this process is not in place.
> 
> 
>    
> 	Enron North America Corp.
> 	
> 	From:  Brenda F Herod                           06/22/2000 12:35 PM
> 	
> 
> To: Lisa Csikos/HOU/ECT@ECT, Daren J Farmer/HOU/ECT@ECT, Mary M 
> Smith/HOU/ECT@ECT, Rita Wynne

**expectations / observe**

New arrivals show scheduling flexibility (Vince reschedules Ehud's visit), legal document routing (Shari defers to Gerald for HPL), and explicit policy (personal days granted by supervisor). No new tacit rule emerges; these are explicit instructions or single-episode observations.

**Observation — revision 1**

When external parties propose visits, senior Enron staff reschedule to fit their own travel constraints rather than accommodating the proposer's preferred date.

Inference gap: Vince's reply does not state a general policy; it only shows one instance of rescheduling. Contrast with Ehud's request suggests implicit priority on internal schedules.

Evidence basis: Single episode from Vince's email to Ehud; no other scheduling examples in current data.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An external academic or partner requests a Houston visit for a presentation.

Exceptions: Unknown; may differ if the visitor is a key client or regulator.

Alternative: Staff might accept the proposed date if no conflicts exist.

Uncertainty: Single episode; no evidence of repeated scheduling behavior.

Next query: read: mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920 700

Prediction: Future external visit requests will be rescheduled if they conflict with internal travel plans.

Hypothesis `hypothesis-c2554531fd984b2581be381c98d7df30`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-777b76851e4c4d8fa37f08ffe4444d4a",
    "prediction_id": "prediction-248c36f486ce44eb8f571650227345c3",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test software request routing.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-195878fb36fb4be2bb49d26e106fb5e5",
    "prediction_id": "prediction-83d95d8bea834bf19025f3a3bf4ea7cb",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test legal document routing.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:737d2638b94d4ab3`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

Attribution and exact offsets: `{"segment_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:segment:0:1088", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Mon, 22 May 2000 02:32:00 -0700", "segment_source_family": "enron-segment:0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "segment_fingerprint": "0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "attribution_status": "unverified_header_claim", "document_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "span_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700", "start": 0, "end": 700, "quote": "Ehud,\n\nThanks fro your message. \nWhat about June 22?  I have several trips in between May 25 and June 22.\n\nVince\n\n\n\n\n\n\n\"Ehud I. Ronn\" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM\nTo: Vince.J.Kaminski@enron.com\ncc:  \nSubject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit\n\n\nVince,\n\nGreetings.\n\n1.  Thanks again for hosting the dinner at Power 2000.  Congratulations\nalso on a thoughtful keynote address, a copy of which I picked up on the\nway out of the Conference.\n\n2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I\nwould like to reschedule my proposed Houston visit, and presentation of the\n\"Enterprise-Wide Risk Management\" model to Enron's Research Dept., to the\nnex", "quote_fingerprint": "64549c895b7b5ef849495a3371ffe7d6091c204c36def5d4ef1c6085eabbb02a", "independence_status": "not_established", "raw_sha256": "2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "body_sha256": "66e007804d8cf760b5f1058f1b6efa26f6f4129b86434b294b204afa4053d48c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/3977.", "source_family": "enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920 700"}`

> Ehud,
> 
> Thanks fro your message. 
> What about June 22?  I have several trips in between May 25 and June 22.
> 
> Vince
> 
> 
> 
> 
> 
> 
> "Ehud I. Ronn" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM
> To: Vince.J.Kaminski@enron.com
> cc:  
> Subject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit
> 
> 
> Vince,
> 
> Greetings.
> 
> 1.  Thanks again for hosting the dinner at Power 2000.  Congratulations
> also on a thoughtful keynote address, a copy of which I picked up on the
> way out of the Conference.
> 
> 2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I
> would like to reschedule my proposed Houston visit, and presentation of the
> "Enterprise-Wide Risk Management" model to Enron's Research Dept., to the
> nex

Source `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69`; evidence `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100:10122d0c16c1ded3`; origin `enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10`.

Attribution and exact offsets: `{"segment_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:segment:0:100", "segment_kind": "authored", "claimed_sender": "david.delainey@enron.com", "claimed_date": "Thu, 29 Jun 2000 03:04:00 -0700", "segment_source_family": "enron-segment:3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "segment_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "attribution_status": "unverified_header_claim", "document_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "span_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100", "start": 0, "end": 100, "quote": "Nella, sorry to see you go; however, best of luck in all your future \nendeavours.\n\nRegards\nDelainey\n", "quote_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "independence_status": "not_established", "raw_sha256": "47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "body_sha256": "b32d061cee56a113ba341f453b605ca474cc052559df0ac2cd74a5d98f3b60c1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/delainey-d/sent/544.", "source_family": "enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Nella, sorry to see you go; however, best of luck in all your future 
> endeavours.
> 
> Regards
> Delainey
> 

Source `mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd`; evidence `mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34:441fa35f81e43b1b`; origin `enron-authored:0c6e00823bed3980c9cf5751e38ffc3cf0bdd88ad913f32c3921c8d7d7976e91`.

Attribution and exact offsets: `{"segment_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:segment:0:34", "segment_kind": "authored", "claimed_sender": "richard.sanders@enron.com", "claimed_date": "Wed, 14 Jun 2000 04:26:00 -0700", "segment_source_family": "enron-span:mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34", "segment_fingerprint": "01c3d4bad923312343526298157055ca71a2ca680bf43a4c748e892d5518f45e", "attribution_status": "unverified_header_claim", "document_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd", "span_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34", "start": 0, "end": 34, "quote": "Call Steve Howard with info. Thx.\n", "quote_fingerprint": "01c3d4bad923312343526298157055ca71a2ca680bf43a4c748e892d5518f45e", "independence_status": "not_established", "raw_sha256": "6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd", "body_sha256": "72751c00d32b4a0912c1c16aaf8698e71431ab5cf92dddf0c07ef18eb3306df6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/sanders-r/sent/130.", "source_family": "enron-authored:0c6e00823bed3980c9cf5751e38ffc3cf0bdd88ad913f32c3921c8d7d7976e91", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Call Steve Howard with info. Thx.
> 

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:836d309747b519d8`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

Attribution and exact offsets: `{"segment_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:segment:0:1088", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Mon, 22 May 2000 02:32:00 -0700", "segment_source_family": "enron-segment:0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "segment_fingerprint": "0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "attribution_status": "unverified_header_claim", "document_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "span_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700", "start": 0, "end": 700, "quote": "Ehud,\n\nThanks fro your message. \nWhat about June 22?  I have several trips in between May 25 and June 22.\n\nVince\n\n\n\n\n\n\n\"Ehud I. Ronn\" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM\nTo: Vince.J.Kaminski@enron.com\ncc:  \nSubject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit\n\n\nVince,\n\nGreetings.\n\n1.  Thanks again for hosting the dinner at Power 2000.  Congratulations\nalso on a thoughtful keynote address, a copy of which I picked up on the\nway out of the Conference.\n\n2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I\nwould like to reschedule my proposed Houston visit, and presentation of the\n\"Enterprise-Wide Risk Management\" model to Enron's Research Dept., to the\nnex", "quote_fingerprint": "64549c895b7b5ef849495a3371ffe7d6091c204c36def5d4ef1c6085eabbb02a", "independence_status": "not_established", "raw_sha256": "2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "body_sha256": "66e007804d8cf760b5f1058f1b6efa26f6f4129b86434b294b204afa4053d48c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/3977.", "source_family": "enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920 700"}`

> Ehud,
> 
> Thanks fro your message. 
> What about June 22?  I have several trips in between May 25 and June 22.
> 
> Vince
> 
> 
> 
> 
> 
> 
> "Ehud I. Ronn" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM
> To: Vince.J.Kaminski@enron.com
> cc:  
> Subject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit
> 
> 
> Vince,
> 
> Greetings.
> 
> 1.  Thanks again for hosting the dinner at Power 2000.  Congratulations
> also on a thoughtful keynote address, a copy of which I picked up on the
> way out of the Conference.
> 
> 2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I
> would like to reschedule my proposed Houston visit, and presentation of the
> "Enterprise-Wide Risk Management" model to Enron's Research Dept., to the
> nex

**expertise / observe**

Carol Clair requests comments on a draft confirmation reply letter, an explicit instruction. No new tacit knowledge emerges from this single request.

Source `mail-54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23`; evidence `mail-54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23:0:386:2279a57708b36a6e`; origin `enron-authored:e93aa6816d6fb5ef548d6d9eb7d4ea4515502b83fa7d6e7a80dd03a1c740612f`.

Attribution and exact offsets: `{"segment_id": "mail-54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23:segment:0:386", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Fri, 16 Jun 2000 02:25:00 -0700", "segment_source_family": "enron-segment:1db1f7c55eea5bd72455e1204ca97b7db83ae00939bb6b2942d5d55c044b92a3", "segment_fingerprint": "1db1f7c55eea5bd72455e1204ca97b7db83ae00939bb6b2942d5d55c044b92a3", "attribution_status": "unverified_header_claim", "document_id": "mail-54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23", "span_id": "mail-54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23:0:386", "start": 0, "end": 386, "quote": "Joe Hunter has asked me to draft a form of confirmation reply letter that we \ncould send to our counterparties in lieu of signing their confirmations.  \nThis form of letter with the appropriate chnages could also be used by those \ncounterparties that we confirm.  Please let me know if you have any comments \non this form or any concerns about implementing this process.  Thanks.\nCarol\n", "quote_fingerprint": "1db1f7c55eea5bd72455e1204ca97b7db83ae00939bb6b2942d5d55c044b92a3", "independence_status": "not_established", "raw_sha256": "54a23227519f5a0842e9e2e05fbd649030b7d366bbb6b142d2616cc63595df23", "body_sha256": "d9b4edb272fd521c9dbc9d1c4511b5e21c11513afafe61fbbdbc2c0981e575d1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/notes_inbox/801.", "source_family": "enron-authored:e93aa6816d6fb5ef548d6d9eb7d4ea4515502b83fa7d6e7a80dd03a1c740612f", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Joe Hunter has asked me to draft a form of confirmation reply letter that we 
> could send to our counterparties in lieu of signing their confirmations.  
> This form of letter with the appropriate chnages could also be used by those 
> counterparties that we confirm.  Please let me know if you have any comments 
> on this form or any concerns about implementing this process.  Thanks.
> Carol
> 

**contrasts / observe**

Carol Clair asks Jeff about tax issues for online Mexican trades, noting ENA as counterparty. Mark McCoy reports Conoco supply cuts entered in MOPS. Jeff Fawcett questions EPNG rebuttal testimony. These are explicit requests/observations, not tacit rules.

Source `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc`; evidence `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:0:397:d1b804742cd0b167`; origin `enron-authored:6f580c4f40f2a03c7ee044f389b2140f633e0c5a7367aca49b24de6eadaacfd1`.

Attribution and exact offsets: `{"segment_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:segment:0:397", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:15:00 -0700", "segment_source_family": "enron-segment:8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "segment_fingerprint": "8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "attribution_status": "unverified_header_claim", "document_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc", "span_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:0:397", "start": 0, "end": 397, "quote": "Jeff:\nAs I think you are aware, the Meixco and online group want to implement \nonline trading for Mexican counterparties.  Are there any tax issues taht we \nshould be aware of?  If we conduct online trades using ENA and telephone \ntrades with an Enron Mexican entity, will the exercise of setoff rights \ncreate any tax issues?   My understanding is that the Enron counterparty will \nbe ENA.\nCarol\n", "quote_fingerprint": "8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "independence_status": "not_established", "raw_sha256": "3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc", "body_sha256": "fa01715a530856d93dcb9a3e96330ec339b09ccbc7062edda995052e8d3ec66e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/stclair-c/sent/771.", "source_family": "enron-authored:6f580c4f40f2a03c7ee044f389b2140f633e0c5a7367aca49b24de6eadaacfd1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Jeff:
> As I think you are aware, the Meixco and online group want to implement 
> online trading for Mexican counterparties.  Are there any tax issues taht we 
> should be aware of?  If we conduct online trades using ENA and telephone 
> trades with an Enron Mexican entity, will the exercise of setoff rights 
> create any tax issues?   My understanding is that the Enron counterparty will 
> be ENA.
> Carol
> 

Source `mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940`; evidence `mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:0:320:d9da230e56d764b8`; origin `enron-authored:23cd2ce6760bd2c3ddcc869344e3ff83f941a468bebbdf84ac3f5914adbed03d`.

Attribution and exact offsets: `{"segment_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:segment:0:320", "segment_kind": "authored", "claimed_sender": "mark.mccoy@enron.com", "claimed_date": "Tue, 23 May 2000 02:36:00 -0700", "segment_source_family": "enron-segment:9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "segment_fingerprint": "9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "attribution_status": "unverified_header_claim", "document_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940", "span_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:0:320", "start": 0, "end": 320, "quote": "Conoco supply from El Paso #9DWE was cut into Oasis:\n\n5/21 nom 10,000 cut to 9,399  (cut of 601)\n5/22 nom 10,000 cut to 8,312 (cut of 1,688)\n\nDelivery into HPL from Oasis Katy kept whole.\n\nI entered these cuts in the estimate column in MOPS for both Oasis/HPL & \nOasis/ENA....please verify that is correct.\n\nThanks,\nMark", "quote_fingerprint": "9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "independence_status": "not_established", "raw_sha256": "536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940", "body_sha256": "19e78f1de452b23d0a41e3d6960ac9bbfa8bdc08e98b5f6c1fee623496dcff63", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/all_documents/1819.", "source_family": "enron-authored:23cd2ce6760bd2c3ddcc869344e3ff83f941a468bebbdf84ac3f5914adbed03d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Conoco supply from El Paso #9DWE was cut into Oasis:
> 
> 5/21 nom 10,000 cut to 9,399  (cut of 601)
> 5/22 nom 10,000 cut to 8,312 (cut of 1,688)
> 
> Delivery into HPL from Oasis Katy kept whole.
> 
> I entered these cuts in the estimate column in MOPS for both Oasis/HPL & 
> Oasis/ENA....please verify that is correct.
> 
> Thanks,
> Mark

Source `mail-15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d`; evidence `mail-15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d:0:400:da8cdf44aadfdfc4`; origin `enron-authored:8065a4e0d03f359d57093cbb6ffb67b1cdbdb88045521c2622f7c9d26c95ddb8`.

Attribution and exact offsets: `{"segment_id": "mail-15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d:segment:0:400", "segment_kind": "authored", "claimed_sender": "jeffery.fawcett@enron.com", "claimed_date": "Mon, 22 May 2000 08:31:00 -0700", "segment_source_family": "enron-segment:507a0b52cb7eb75cb9952221a46c15faf2726226a8e9c411169f92eb95c075e1", "segment_fingerprint": "507a0b52cb7eb75cb9952221a46c15faf2726226a8e9c411169f92eb95c075e1", "attribution_status": "unverified_header_claim", "document_id": "mail-15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d", "span_id": "mail-15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d:0:400", "start": 0, "end": 400, "quote": "Mark,\nI don't see any problem with Kathy's testimony here.  She's repeating a theme \nwe've heard many times from EPNG.  However, I'm wondering if the testimony \nsponsored by John Weaver might not be problematic in that it may give rise to \na discussion of the Wheeler Ridge - Hector Road relationship -- particularly \nif EPNG aggressively attacks PG&E's proposal.\nThoughts?  Let's talk tomorrow.\n\n\n\n\n", "quote_fingerprint": "507a0b52cb7eb75cb9952221a46c15faf2726226a8e9c411169f92eb95c075e1", "independence_status": "not_established", "raw_sha256": "15c4a5b44c21137678e5df0084f14698d512f8e955d69e66dc208ab458309a2d", "body_sha256": "126969ca1e803001ac3bfc21976aa64c018ff0b49d9b399938f1aed0e933acd4", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/scott-s/all_documents/293.", "source_family": "enron-authored:8065a4e0d03f359d57093cbb6ffb67b1cdbdb88045521c2622f7c9d26c95ddb8", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark,
> I don't see any problem with Kathy's testimony here.  She's repeating a theme 
> we've heard many times from EPNG.  However, I'm wondering if the testimony 
> sponsored by John Weaver might not be problematic in that it may give rise to 
> a discussion of the Wheeler Ridge - Hector Road relationship -- particularly 
> if EPNG aggressively attacks PG&E's proposal.
> Thoughts?  Let's talk tomorrow.
> 
> 
> 
> 
> 

**routines / revise**

New emails show explicit instructions and single-episode observations, not tacit rules. No new evidence supports existing hypotheses. Predictions remain unresolved.

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:188a22f12da2216a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177`; evidence `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266:d4a3f7c3f4ab2623`; origin `enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e`.

Attribution and exact offsets: `{"segment_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:segment:0:266", "segment_kind": "authored", "claimed_sender": "clement.lau@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:22:00 -0700", "segment_source_family": "enron-segment:3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "segment_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "attribution_status": "unverified_header_claim", "document_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "span_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266", "start": 0, "end": 266, "quote": "I have saved the first info memo (generic version, w/o mentioned of Orion) \nunder \"EGC12-Generic-051100\" and various site pictures and maps under \n\"Pictures\" folder, both in o:/_dropbox.\n\nI will continue transfering file to the o:_dropbox over the next few days.\n\n  ", "quote_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "independence_status": "not_established", "raw_sha256": "27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "body_sha256": "21a1b7ec9a36c79908e6474294f323c67e3aae49b1e218fdaf244a9816cb2b3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/genco_jv_ipo/437.", "source_family": "enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I have saved the first info memo (generic version, w/o mentioned of Orion) 
> under "EGC12-Generic-051100" and various site pictures and maps under 
> "Pictures" folder, both in o:/_dropbox.
> 
> I will continue transfering file to the o:_dropbox over the next few days.
> 
>   

Source `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69`; evidence `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100:fc542450d48e0af2`; origin `enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10`.

Attribution and exact offsets: `{"segment_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:segment:0:100", "segment_kind": "authored", "claimed_sender": "david.delainey@enron.com", "claimed_date": "Thu, 29 Jun 2000 03:04:00 -0700", "segment_source_family": "enron-segment:3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "segment_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "attribution_status": "unverified_header_claim", "document_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "span_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100", "start": 0, "end": 100, "quote": "Nella, sorry to see you go; however, best of luck in all your future \nendeavours.\n\nRegards\nDelainey\n", "quote_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "independence_status": "not_established", "raw_sha256": "47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "body_sha256": "b32d061cee56a113ba341f453b605ca474cc052559df0ac2cd74a5d98f3b60c1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/delainey-d/sent/544.", "source_family": "enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Nella, sorry to see you go; however, best of luck in all your future 
> endeavours.
> 
> Regards
> Delainey
> 

**expectations / revise**

New emails show explicit instructions and routine updates, but no new tacit rules emerge. Existing hypotheses remain unsupported by new evidence.

**expertise / revise**

New emails show explicit instructions and single-episode observations, not tacit rules. Existing hypotheses remain unsupported by new evidence.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-777b76851e4c4d8fa37f08ffe4444d4a",
    "prediction_id": "prediction-248c36f486ce44eb8f571650227345c3",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test software request routing.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-195878fb36fb4be2bb49d26e106fb5e5",
    "prediction_id": "prediction-83d95d8bea834bf19025f3a3bf4ea7cb",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test legal document routing.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:ecbdf36dab6f438b`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc`; evidence `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:0:397:70933d646ca9fe6b`; origin `enron-authored:6f580c4f40f2a03c7ee044f389b2140f633e0c5a7367aca49b24de6eadaacfd1`.

Attribution and exact offsets: `{"segment_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:segment:0:397", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:15:00 -0700", "segment_source_family": "enron-segment:8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "segment_fingerprint": "8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "attribution_status": "unverified_header_claim", "document_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc", "span_id": "mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:0:397", "start": 0, "end": 397, "quote": "Jeff:\nAs I think you are aware, the Meixco and online group want to implement \nonline trading for Mexican counterparties.  Are there any tax issues taht we \nshould be aware of?  If we conduct online trades using ENA and telephone \ntrades with an Enron Mexican entity, will the exercise of setoff rights \ncreate any tax issues?   My understanding is that the Enron counterparty will \nbe ENA.\nCarol\n", "quote_fingerprint": "8b5126bb386db044197615a60dfe780fe9621de910c951d43323944c86ebce4d", "independence_status": "not_established", "raw_sha256": "3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc", "body_sha256": "fa01715a530856d93dcb9a3e96330ec339b09ccbc7062edda995052e8d3ec66e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/stclair-c/sent/771.", "source_family": "enron-authored:6f580c4f40f2a03c7ee044f389b2140f633e0c5a7367aca49b24de6eadaacfd1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Jeff:
> As I think you are aware, the Meixco and online group want to implement 
> online trading for Mexican counterparties.  Are there any tax issues taht we 
> should be aware of?  If we conduct online trades using ENA and telephone 
> trades with an Enron Mexican entity, will the exercise of setoff rights 
> create any tax issues?   My understanding is that the Enron counterparty will 
> be ENA.
> Carol
> 

Source `mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940`; evidence `mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:0:320:5e011b093bc8ed3a`; origin `enron-authored:23cd2ce6760bd2c3ddcc869344e3ff83f941a468bebbdf84ac3f5914adbed03d`.

Attribution and exact offsets: `{"segment_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:segment:0:320", "segment_kind": "authored", "claimed_sender": "mark.mccoy@enron.com", "claimed_date": "Tue, 23 May 2000 02:36:00 -0700", "segment_source_family": "enron-segment:9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "segment_fingerprint": "9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "attribution_status": "unverified_header_claim", "document_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940", "span_id": "mail-536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940:0:320", "start": 0, "end": 320, "quote": "Conoco supply from El Paso #9DWE was cut into Oasis:\n\n5/21 nom 10,000 cut to 9,399  (cut of 601)\n5/22 nom 10,000 cut to 8,312 (cut of 1,688)\n\nDelivery into HPL from Oasis Katy kept whole.\n\nI entered these cuts in the estimate column in MOPS for both Oasis/HPL & \nOasis/ENA....please verify that is correct.\n\nThanks,\nMark", "quote_fingerprint": "9527e3d34610bd7f5620f44f299957e6a4adb1044bcbd1936e2651bc51f26711", "independence_status": "not_established", "raw_sha256": "536411c6384f8c4ca29586aff5d197165f35162abc1b37e50f42954b7dca5940", "body_sha256": "19e78f1de452b23d0a41e3d6960ac9bbfa8bdc08e98b5f6c1fee623496dcff63", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/all_documents/1819.", "source_family": "enron-authored:23cd2ce6760bd2c3ddcc869344e3ff83f941a468bebbdf84ac3f5914adbed03d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Conoco supply from El Paso #9DWE was cut into Oasis:
> 
> 5/21 nom 10,000 cut to 9,399  (cut of 601)
> 5/22 nom 10,000 cut to 8,312 (cut of 1,688)
> 
> Delivery into HPL from Oasis Katy kept whole.
> 
> I entered these cuts in the estimate column in MOPS for both Oasis/HPL & 
> Oasis/ENA....please verify that is correct.
> 
> Thanks,
> Mark

**contrasts / revise**

Ben Rogers' closing line is a routine courtesy, not new evidence. Existing hypotheses remain unsupported by new arrivals; no material correction or new insight emerges.

### 2000-08-16T14:45:00+00:00 — review window 4

**routines / observe**

New emails show explicit instructions and routine updates, but no new tacit rules emerge. Existing hypotheses remain unsupported by new evidence.

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011:3b21b60985b1216a`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

Attribution and exact offsets: `{"segment_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:segment:311:1292", "segment_kind": "forwarded", "claimed_sender": "Chris Long@ENRON", "claimed_date": "07/27/2000 04:34 PM", "segment_source_family": "enron-segment:e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "segment_fingerprint": "e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "attribution_status": "unverified_header_claim", "document_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "span_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011", "start": 311, "end": 1011, "quote": "\nToday we were successful in killing an amendment that was offered by Rep. \nCarolyn Maloney (D-NY) in the House Banking Committee during its markup of \nthe Commodities Future Modernization Act of 2000.  This amendment would have \nstricken language that provided an exclusion from CFTC jurisdiction for all \nnon-agriculture transactions (energy, metals, broadband).  The amendment \nfailed, largely due to pressure from Enron, by a vote of 20-12.  Rep. Ken \nBensten (D-TX) joined Chairman Leach in speaking against the amendment.  \n\nIn more positive movement, yesterday the House Commerce Committee passed its \nversion on the bill including a provision that exempts metal trading \nmultilateral trading ", "quote_fingerprint": "50ec5b3990dc5cb012f395bfd8fabc4cbe17263989602b341cb498e038c3cf09", "independence_status": "not_established", "raw_sha256": "206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "body_sha256": "81ecded4e8994257d04936b5a051dc7d261f4472a37e72d02e70a817b2ecd834", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/archiving/untitled/1497.", "source_family": "enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb 1011"}`

> 
> Today we were successful in killing an amendment that was offered by Rep. 
> Carolyn Maloney (D-NY) in the House Banking Committee during its markup of 
> the Commodities Future Modernization Act of 2000.  This amendment would have 
> stricken language that provided an exclusion from CFTC jurisdiction for all 
> non-agriculture transactions (energy, metals, broadband).  The amendment 
> failed, largely due to pressure from Enron, by a vote of 20-12.  Rep. Ken 
> Bensten (D-TX) joined Chairman Leach in speaking against the amendment.  
> 
> In more positive movement, yesterday the House Commerce Committee passed its 
> version on the bill including a provision that exempts metal trading 
> multilateral trading 

Source `mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e`; evidence `mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e:0:700:8204d3f651688cc3`; origin `enron-authored:d69e95096f83afe3e94c26b62d7374c17ac836169083b2c684abb08fba0f5c3b`.

Attribution and exact offsets: `{"segment_id": "mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e:segment:0:1816", "segment_kind": "authored", "claimed_sender": "brant.reves@enron.com", "claimed_date": "Mon, 24 Jul 2000 02:09:00 -0700", "segment_source_family": "enron-segment:debef946b94d5584c0cf91774fa9eca1a04bc1fd3f189fc0cae9dd4c6519d148", "segment_fingerprint": "debef946b94d5584c0cf91774fa9eca1a04bc1fd3f189fc0cae9dd4c6519d148", "attribution_status": "unverified_header_claim", "document_id": "mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e", "span_id": "mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e:0:700", "start": 0, "end": 700, "quote": "Hello everyone,\n\nWe recently approved a nov-feb'01 10,000/d physcial sale.  This sale was \nbroken down into three parts.\n\nNR7689 5,000/d @ index - .10, with a floor of 2.95\nNR7727 2,000/d @ index - .12, with a floor of 2.88\nNR7730 3,000/d @ index - .17, with a floor of 3.09\n\nThe parent company of this entity provides a $800M gty that we utilize within \nthe credit managment of this relationship.  We will need special language to \nbe included within each of the confirms associated with legs 1 and 2 of this \nthese trades.\n\nFinancial Legal:\n\nPlease see the attached credit worksheet to be used in the preparation of \nlanguage to be included with the above referenced trades and then provide \nsuch l", "quote_fingerprint": "00ff5fc7dbd7bf65a5290ace4e431341a1c9ce3fefb4da5764b5c91e1f6b95d2", "independence_status": "not_established", "raw_sha256": "3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e", "body_sha256": "937886ab72a5d7cc168d36c3a6f6d8635083bee5e4ff3529ecfa5126abf0f7f1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2771.", "source_family": "enron-authored:d69e95096f83afe3e94c26b62d7374c17ac836169083b2c684abb08fba0f5c3b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e 700"}`

> Hello everyone,
> 
> We recently approved a nov-feb'01 10,000/d physcial sale.  This sale was 
> broken down into three parts.
> 
> NR7689 5,000/d @ index - .10, with a floor of 2.95
> NR7727 2,000/d @ index - .12, with a floor of 2.88
> NR7730 3,000/d @ index - .17, with a floor of 3.09
> 
> The parent company of this entity provides a $800M gty that we utilize within 
> the credit managment of this relationship.  We will need special language to 
> be included within each of the confirms associated with legs 1 and 2 of this 
> these trades.
> 
> Financial Legal:
> 
> Please see the attached credit worksheet to be used in the preparation of 
> language to be included with the above referenced trades and then provide 
> such l

Source `mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f`; evidence `mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f:0:51:9f4cf72907588dcb`; origin `enron-authored:b9b4da066102430a5f7da98af04bb7d569b3e5972ce5606b1db6d7648cd8bb35`.

Attribution and exact offsets: `{"segment_id": "mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f:segment:0:51", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Mon, 10 Jul 2000 10:22:00 -0700", "segment_source_family": "enron-span:mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f:0:51", "segment_fingerprint": "58ad26d71b0f73e77ff4acd9fd652b61fc5ac86fd293d48fe8cdf78628734cf1", "attribution_status": "unverified_header_claim", "document_id": "mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f", "span_id": "mail-13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f:0:51", "start": 0, "end": 51, "quote": "My fax number is (713) 646-3490.  Thanks.  Sara\n\n\n\n", "quote_fingerprint": "58ad26d71b0f73e77ff4acd9fd652b61fc5ac86fd293d48fe8cdf78628734cf1", "independence_status": "not_established", "raw_sha256": "13970658b10045724595446f95185d301fb961950bf083efc05a45b70377c28f", "body_sha256": "ff18a446ac7b17519b388b6272a204a7d9477f302cf3468ed82700e041e87007", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/1666.", "source_family": "enron-authored:b9b4da066102430a5f7da98af04bb7d569b3e5972ce5606b1db6d7648cd8bb35", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> My fax number is (713) 646-3490.  Thanks.  Sara
> 
> 
> 
> 

**expectations / observe**

Robin's apology for system crash reveals informal position-tracking duties across multiple books, but no new tacit rule emerges. Other emails are routine updates or explicit instructions. Existing hypotheses remain unsupported.

**Observation — revision 1**

When a trader's position book system crashes, colleagues informally expect the responsible analyst to recover and provide positions without formal escalation, as Robin promises to deliver shortly.

Inference gap: Robin's email shows she handles multiple books and promises recovery, but does not state a general rule for crash handling. Contrast with absence of escalation suggests informal norm, but scope is unclear.

Evidence basis: Single authored email from Robin to an unnamed recipient, one episode. No other crash-related emails in current data.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A system crash affects position book availability and a colleague requests their position.

Exceptions: Unknown; may differ if crash is prolonged or affects critical trading decisions.

Alternative: Colleagues might escalate to IT or management if recovery is delayed.

Uncertainty: Single episode; no evidence of repeated crash handling or formal procedures.

Next query: all: system crash position book recovery

Prediction: In future system crashes, the responsible analyst will informally promise recovery without immediate escalation.

Hypothesis `hypothesis-7abe00e983664568afe66333e18b2a99`; transfer tested: false.

Source `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6`; evidence `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254:9ea804ae78554e5b`; origin `enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e`.

Attribution and exact offsets: `{"segment_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:segment:0:254", "segment_kind": "authored", "claimed_sender": "robin.rodrigue@enron.com", "claimed_date": "Thu, 03 Aug 2000 12:22:00 -0700", "segment_source_family": "enron-segment:c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "segment_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "attribution_status": "unverified_header_claim", "document_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "span_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254", "start": 0, "end": 254, "quote": "No I promise I didn't....your post-id crashed my system.  I had your book and \nthe power book and the Nymex book all coming in at the same time and the \nsystem just stopped.  We're going again though, so I should have your \nposition in a few minutes.\n\nRR", "quote_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "independence_status": "not_established", "raw_sha256": "84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "body_sha256": "99c87bca3237b1b67a94e3e40044d20fc00d12e3dccffdcdee293593a1605e24", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rodrique-r/all_documents/640.", "source_family": "enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> No I promise I didn't....your post-id crashed my system.  I had your book and 
> the power book and the Nymex book all coming in at the same time and the 
> system just stopped.  We're going again though, so I should have your 
> position in a few minutes.
> 
> RR

Source `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6`; evidence `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254:836d309747b519d8`; origin `enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e`.

Attribution and exact offsets: `{"segment_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:segment:0:254", "segment_kind": "authored", "claimed_sender": "robin.rodrigue@enron.com", "claimed_date": "Thu, 03 Aug 2000 12:22:00 -0700", "segment_source_family": "enron-segment:c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "segment_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "attribution_status": "unverified_header_claim", "document_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "span_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254", "start": 0, "end": 254, "quote": "No I promise I didn't....your post-id crashed my system.  I had your book and \nthe power book and the Nymex book all coming in at the same time and the \nsystem just stopped.  We're going again though, so I should have your \nposition in a few minutes.\n\nRR", "quote_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "independence_status": "not_established", "raw_sha256": "84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "body_sha256": "99c87bca3237b1b67a94e3e40044d20fc00d12e3dccffdcdee293593a1605e24", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rodrique-r/all_documents/640.", "source_family": "enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No I promise I didn't....your post-id crashed my system.  I had your book and 
> the power book and the Nymex book all coming in at the same time and the 
> system just stopped.  We're going again though, so I should have your 
> position in a few minutes.
> 
> RR

**expertise / observe**

New emails show explicit instructions and single-episode observations, not tacit rules. Existing hypotheses remain unsupported by new evidence.

Source `mail-7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd`; evidence `mail-7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd:0:126:97a8d8ab1fa17c96`; origin `enron-authored:c40c4e9e9aa7f9895d14a306612e3474941a774f95d839fa636dd9289b990089`.

Attribution and exact offsets: `{"segment_id": "mail-7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd:segment:0:126", "segment_kind": "authored", "claimed_sender": "matthew.lenhart@enron.com", "claimed_date": "Tue, 11 Jul 2000 00:30:00 -0700", "segment_source_family": "enron-segment:cbfc2a948e3cae8b33c92185ed391ae967cc077a12b898eee808501e82a28924", "segment_fingerprint": "cbfc2a948e3cae8b33c92185ed391ae967cc077a12b898eee808501e82a28924", "attribution_status": "unverified_header_claim", "document_id": "mail-7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd", "span_id": "mail-7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd:0:126", "start": 0, "end": 126, "quote": "lets go to new orleans.  that sounds good to me.  i don't know how i got such \na good deal but i am psyched up.  i can't wait.", "quote_fingerprint": "cbfc2a948e3cae8b33c92185ed391ae967cc077a12b898eee808501e82a28924", "independence_status": "not_established", "raw_sha256": "7d90b4cec94e755918bc59617a501ae034c20c91d0bef07ee0ca2906d0c4f6fd", "body_sha256": "d4fa4490543bd3be9921d0d035f2921410589a753a5e1ed289356d0a686502fd", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/lenhart-m/sent/1225.", "source_family": "enron-authored:c40c4e9e9aa7f9895d14a306612e3474941a774f95d839fa636dd9289b990089", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> lets go to new orleans.  that sounds good to me.  i don't know how i got such 
> a good deal but i am psyched up.  i can't wait.

Source `mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806`; evidence `mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806:609:1309:74d0ae6d86021da7`; origin `enron-authored:aa356627fae30d839e4dc8617a23fc43860939db602bbf40a40896ca9359b1bf`.

Attribution and exact offsets: `{"segment_id": "mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806:segment:609:5761", "segment_kind": "forwarded", "claimed_sender": null, "claimed_date": "Gagliardi/Hou-ComOps/EnergyTrading/PEC on 07/31/2000 07:31 AM", "segment_source_family": "enron-segment:270317d5f6448fc7671862bc03beefa615ca33f8691b5320836036138e2d7100", "segment_fingerprint": "270317d5f6448fc7671862bc03beefa615ca33f8691b5320836036138e2d7100", "attribution_status": "unverified_header_claim", "document_id": "mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806", "span_id": "mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806:609:1309", "start": 609, "end": 1309, "quote": "\n\n\n\nI am repeating this because I don't think everybody got it the first time.\nIf\nyou get two copies, I'm sorry, but I wanted to be sure everybody who is\nsupposed to get it gets at least one copy.\n\nTrue Orange Fax/E-Mail Service\nVolume 8, Fax/E-Mail #65, Sunday, July 30, 2000\nJerry Scarbrough's True Orange, P. O. Box 26530, Austin, Texas 78755 -\nPhone\n512-795-8536\n\nLonghorns Get Huge Longview Offensive Lineman as 12th Commitment\nTerrance Young, 6-6, 340, 5.5, of Longview, another star in the outstanding\nclass of offensive line recruits in the state this year, came to Texas\nSaturday with his parents and committed to the Longhorns. He is Texas' 12th\ncommitment, and that group includes seven of", "quote_fingerprint": "4dca26f58670bf06bdc652983a1be606e8f2dd1e93731111291dac46a18df164", "independence_status": "not_established", "raw_sha256": "39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806", "body_sha256": "50ce50db56d0be0009c5afd48130b602881f921928619fe8612161ae1490c059", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/dean-c/discussion_threads/79.", "source_family": "enron-authored:aa356627fae30d839e4dc8617a23fc43860939db602bbf40a40896ca9359b1bf", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-39dc2fda53692a5b3ef0f5ff523983123660fbffb9c8ae3d0d6771ce7efc5806 1309"}`

> 
> 
> 
> 
> I am repeating this because I don't think everybody got it the first time.
> If
> you get two copies, I'm sorry, but I wanted to be sure everybody who is
> supposed to get it gets at least one copy.
> 
> True Orange Fax/E-Mail Service
> Volume 8, Fax/E-Mail #65, Sunday, July 30, 2000
> Jerry Scarbrough's True Orange, P. O. Box 26530, Austin, Texas 78755 -
> Phone
> 512-795-8536
> 
> Longhorns Get Huge Longview Offensive Lineman as 12th Commitment
> Terrance Young, 6-6, 340, 5.5, of Longview, another star in the outstanding
> class of offensive line recruits in the state this year, came to Texas
> Saturday with his parents and committed to the Longhorns. He is Texas' 12th
> commitment, and that group includes seven of

Source `mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47`; evidence `mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47:0:700:691031efc7a02559`; origin `enron-authored:a1fccf41f411e588eced7b9063f84fba9c496574ef1e233a308f9208981004d1`.

Attribution and exact offsets: `{"segment_id": "mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47:segment:0:1306", "segment_kind": "authored", "claimed_sender": "rosalee.fleming@enron.com", "claimed_date": "Wed, 09 Aug 2000 06:24:00 -0700", "segment_source_family": "enron-segment:659b50afafa821a8c2772270643a387094ef024cf3a2904c4a8816cff449d3aa", "segment_fingerprint": "659b50afafa821a8c2772270643a387094ef024cf3a2904c4a8816cff449d3aa", "attribution_status": "unverified_header_claim", "document_id": "mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47", "span_id": "mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47:0:700", "start": 0, "end": 700, "quote": "Michael, in case you need Ken's bio, I am attaching it for your use.\n\nRosalee\n\n\n\n\n\tEnron Energy Services\n\t\n\tFrom:  Michael Mann @ EES                           08/08/2000 09:12 PM\n\tPhone No: 609.252.0907\n\t\n\n\n\nTo: Thomas E White/HOU/EES@EES, Kenneth Lay/Corp/Enron\ncc: Harold G Buchanan/HOU/EES, Lou Pai, Jeremy Blachman, Mark Peterson, Julie \nDavidson/HOU/EES, Judy G Smith/HOU/EES@EES \nSubject: Owens-Illinois Meeting\n\nWe have confirmed a meeting to introduce you to Tom Young, EVP (and member, \nO-I Board of Directors) and members of his management team at O-I \nHeadquarters next Tuesday, 8/15 at 11:30 am.  We have 90 minutes, Mr. Young \nwill be hosting us to lunch during our meeting.  Joe Lemieu", "quote_fingerprint": "777db68262a9a23c13c5a8bc71ab36b24bfd2c71abfb9e3c50cb3c3d3c157f79", "independence_status": "not_established", "raw_sha256": "0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47", "body_sha256": "68ecc39f2ba436d1aa89795be63fc11fb366f7184ad244f61ae3ec85d8a8090b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/lay-k/sent/70.", "source_family": "enron-authored:a1fccf41f411e588eced7b9063f84fba9c496574ef1e233a308f9208981004d1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-0cd67a36d661e73cd379508e014e5b47cdc54363ef79ed72de2e90fd2b727f47 700"}`

> Michael, in case you need Ken's bio, I am attaching it for your use.
> 
> Rosalee
> 
> 
> 
> 
> 	Enron Energy Services
> 	
> 	From:  Michael Mann @ EES                           08/08/2000 09:12 PM
> 	Phone No: 609.252.0907
> 	
> 
> 
> 
> To: Thomas E White/HOU/EES@EES, Kenneth Lay/Corp/Enron
> cc: Harold G Buchanan/HOU/EES, Lou Pai, Jeremy Blachman, Mark Peterson, Julie 
> Davidson/HOU/EES, Judy G Smith/HOU/EES@EES 
> Subject: Owens-Illinois Meeting
> 
> We have confirmed a meeting to introduce you to Tom Young, EVP (and member, 
> O-I Board of Directors) and members of his management team at O-I 
> Headquarters next Tuesday, 8/15 at 11:30 am.  We have 90 minutes, Mr. Young 
> will be hosting us to lunch during our meeting.  Joe Lemieu

**contrasts / observe**

New emails show explicit instructions and routine updates, but no new tacit rules emerge. Existing hypotheses remain unsupported by new evidence.

**routines / revise**

New email shows Enron lobbyists celebrating defeat of Maloney amendment and planning next steps, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011:bcd704423ee3e88e`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

Attribution and exact offsets: `{"segment_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:segment:311:1292", "segment_kind": "forwarded", "claimed_sender": "Chris Long@ENRON", "claimed_date": "07/27/2000 04:34 PM", "segment_source_family": "enron-segment:e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "segment_fingerprint": "e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "attribution_status": "unverified_header_claim", "document_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "span_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011", "start": 311, "end": 1011, "quote": "\nToday we were successful in killing an amendment that was offered by Rep. \nCarolyn Maloney (D-NY) in the House Banking Committee during its markup of \nthe Commodities Future Modernization Act of 2000.  This amendment would have \nstricken language that provided an exclusion from CFTC jurisdiction for all \nnon-agriculture transactions (energy, metals, broadband).  The amendment \nfailed, largely due to pressure from Enron, by a vote of 20-12.  Rep. Ken \nBensten (D-TX) joined Chairman Leach in speaking against the amendment.  \n\nIn more positive movement, yesterday the House Commerce Committee passed its \nversion on the bill including a provision that exempts metal trading \nmultilateral trading ", "quote_fingerprint": "50ec5b3990dc5cb012f395bfd8fabc4cbe17263989602b341cb498e038c3cf09", "independence_status": "not_established", "raw_sha256": "206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "body_sha256": "81ecded4e8994257d04936b5a051dc7d261f4472a37e72d02e70a817b2ecd834", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/archiving/untitled/1497.", "source_family": "enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb 1011"}`

> 
> Today we were successful in killing an amendment that was offered by Rep. 
> Carolyn Maloney (D-NY) in the House Banking Committee during its markup of 
> the Commodities Future Modernization Act of 2000.  This amendment would have 
> stricken language that provided an exclusion from CFTC jurisdiction for all 
> non-agriculture transactions (energy, metals, broadband).  The amendment 
> failed, largely due to pressure from Enron, by a vote of 20-12.  Rep. Ken 
> Bensten (D-TX) joined Chairman Leach in speaking against the amendment.  
> 
> In more positive movement, yesterday the House Commerce Committee passed its 
> version on the bill including a provision that exempts metal trading 
> multilateral trading 

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:1011:1292:4005cd196a516971`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

Attribution and exact offsets: `{"segment_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:segment:311:1292", "segment_kind": "forwarded", "claimed_sender": "Chris Long@ENRON", "claimed_date": "07/27/2000 04:34 PM", "segment_source_family": "enron-segment:e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "segment_fingerprint": "e1f7cbe8929a63cda0618164c7af72b05f22cd4712bbbfe983dc18340ab5aa76", "attribution_status": "unverified_header_claim", "document_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "span_id": "mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:1011:1292", "start": 1011, "end": 1292, "quote": "facilities from CFTC jurisdiction.\n\nCongress goes into recess tomorrow and we will have a better sense on how the \nRules Committee plans to reconcile differences between the versions of the \nbill later this week.  The Senate is still the unknown.\n\nCall me at any question - Chris\n\n", "quote_fingerprint": "0411f405a3e4d372a172c92e73dad743d849073699245d49730b3326a5d99d81", "independence_status": "not_established", "raw_sha256": "206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb", "body_sha256": "81ecded4e8994257d04936b5a051dc7d261f4472a37e72d02e70a817b2ecd834", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/archiving/untitled/1497.", "source_family": "enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> facilities from CFTC jurisdiction.
> 
> Congress goes into recess tomorrow and we will have a better sense on how the 
> Rules Committee plans to reconcile differences between the versions of the 
> bill later this week.  The Senate is still the unknown.
> 
> Call me at any question - Chris
> 
> 

**expectations / revise**

New emails show explicit instructions and routine updates, but no new tacit rules emerge. Existing hypotheses remain unsupported by new evidence.

**expertise / revise**

New email shows a forwarded newsletter about a Texas football recruit, unrelated to Enron business. No new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

**contrasts / revise**

New emails show explicit instructions and routine updates, but no new tacit rules emerge. Existing hypotheses remain unsupported by new evidence.

### 2000-09-19T15:13:00+00:00 — review window 5

**routines / observe**

Sara Shackleton requests four ISDA Notebook sets, showing routine internal ordering. Vince Kaminski confirms GARP speaking engagement, indicating external commitment. Jeff Dasovich forwards California governor's electricity meeting news. Hunter Shively schedules training. No new tacit knowledge emerges.

Source `mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a`; evidence `mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a:0:34:5075909aafc29737`; origin `enron-authored:dceeac4f38d31ffc5d4c1d7e5d72590e5c4de37681e86de3a059265348a8dbcd`.

Attribution and exact offsets: `{"segment_id": "mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a:segment:0:34", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 07 Sep 2000 04:27:00 -0700", "segment_source_family": "enron-span:mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a:0:34", "segment_fingerprint": "6a14ac9998843f38812d560a262c793096c1911e977c7111d845591b4fad5de1", "attribution_status": "unverified_header_claim", "document_id": "mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a", "span_id": "mail-5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a:0:34", "start": 0, "end": 34, "quote": "I would like 4.  Thanks.  Sara\n\n\n\n", "quote_fingerprint": "6a14ac9998843f38812d560a262c793096c1911e977c7111d845591b4fad5de1", "independence_status": "not_established", "raw_sha256": "5c306afb2dbe4fad215b0b543049cfac9019ef617087c77e04d39577760a973a", "body_sha256": "c5f1b9aa04fe5e3575ec29f2baea340f033890d94c6c385aa410837e6f4e0938", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/1963.", "source_family": "enron-authored:dceeac4f38d31ffc5d4c1d7e5d72590e5c4de37681e86de3a059265348a8dbcd", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I would like 4.  Thanks.  Sara
> 
> 
> 
> 

Source `mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1`; evidence `mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1:2328:3028:2e9dd8a072228514`; origin `enron-authored:0c3d0fa00d88248871d2c61d8a2d30c338af550a234925e987b7b6c5adf78d0e`.

Attribution and exact offsets: `{"segment_id": "mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1:segment:2328:3588", "segment_kind": "forwarded", "claimed_sender": "Julee Malinowski-Ball [mailto:jmball@ns.net]", "claimed_date": "Thursday, September 07, 2000 10:45 AM", "segment_source_family": "enron-segment:43acb023606f233c7ac1941e823cb5d45d17666b8c1d528ca6910561c765279d", "segment_fingerprint": "43acb023606f233c7ac1941e823cb5d45d17666b8c1d528ca6910561c765279d", "attribution_status": "unverified_header_claim", "document_id": "mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1", "span_id": "mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1:2328:3028", "start": 2328, "end": 3028, "quote": "\n\nAn excerpt from a SD Union Tribune article this morning, and I quote:\n\n\nThe governor will spend most of this month signing and vetoing hundreds of\nbills passed by the Legislature before adjournment last week. He said he\nwill meet with power generators and \"immerse\" himself in the electricity\nissue next month before proposing reforms in November.\n\n\"If people don't act responsibly I am going to name names and publish a list\nout in my reception area,\" Davis said. \"We have to do this together.\"\n\nThe governor said that ratepayers, utilities and power generators will all\nhave to \"accept their fair share of pain.\" He called on all Californians,\nincluding businesses and environmentalists, to act r", "quote_fingerprint": "ab73518bf7eae9247dd5d355955133c20339cc91d508441e731d68cb495bb43a", "independence_status": "not_established", "raw_sha256": "0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1", "body_sha256": "969a24d0e7b73771bbca0954ac86d3c9123b84d0c37555b9ed3f48f86c14bf23", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/dasovich-j/sent/198.", "source_family": "enron-authored:0c3d0fa00d88248871d2c61d8a2d30c338af550a234925e987b7b6c5adf78d0e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-0e01a3860b4090bdd32366054b67fa7fece24aa3519fe3712480b647c7df78e1 3028"}`

> 
> 
> An excerpt from a SD Union Tribune article this morning, and I quote:
> 
> 
> The governor will spend most of this month signing and vetoing hundreds of
> bills passed by the Legislature before adjournment last week. He said he
> will meet with power generators and "immerse" himself in the electricity
> issue next month before proposing reforms in November.
> 
> "If people don't act responsibly I am going to name names and publish a list
> out in my reception area," Davis said. "We have to do this together."
> 
> The governor said that ratepayers, utilities and power generators will all
> have to "accept their fair share of pain." He called on all Californians,
> including businesses and environmentalists, to act r

**expectations / observe**

New emails show routine approvals, scheduling, and forwarded updates. No new tacit knowledge emerges; existing hypotheses remain unsupported by new evidence.

**expertise / observe**

Mary Cook's draft on Juniper partnership interests references Andrea's agreement on termination rights, suggesting legal drafting relies on prior oral agreements. Sara Shackleton forwards McGarret closing documents, indicating her role in transaction coordination. No new tacit rules emerge.

**Observation — revision 1**

When drafting legal documents for structured transactions, Enron attorneys rely on prior oral agreements with colleagues (e.g., Andrea) to determine scope of terms, rather than seeking explicit written instructions.

Inference gap: The email states Andrea agreed on termination rights but does not state that this is a standard practice. The contrast between Mary's reliance on Andrea's agreement and the absence of written confirmation suggests an implicit norm, but scope is unclear.

Evidence basis: Single episode from Mary Cook's email to Sara Shackleton, showing one attorney referencing an oral agreement with Andrea. No other episodes show similar reliance.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An attorney drafts a new agreement based on a prior template and needs to decide whether to include partial termination rights.

Exceptions: Unknown; may differ if the agreement is for a new counterparty or if the prior agreement is not directly applicable.

Alternative: Attorneys might include partial termination rights by default unless explicitly told otherwise.

Uncertainty: Single episode; no evidence of how often such oral agreements guide drafting.

Next query: read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700

Prediction: In future drafting tasks, attorneys will reference prior oral agreements to determine contract terms without seeking written confirmation.

Hypothesis `hypothesis-79e070680e8649139efde6728a066eb5`; transfer tested: false.

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:011e947bec342f4a`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

Source `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692`; evidence `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:1193:1893:e567be0d98774a8d`; origin `enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c`.

Attribution and exact offsets: `{"segment_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:segment:1193:3509", "segment_kind": "forwarded", "claimed_sender": "\"CHRIS KRECEK\" <KRECC@andrews-kurth.com>", "claimed_date": "08/23/00 02:47 PM", "segment_source_family": "enron-segment:7c7d63859b0fd91d1f3b435e80b697448661d755c02e2f7a4c0568dfd6baa043", "segment_fingerprint": "7c7d63859b0fd91d1f3b435e80b697448661d755c02e2f7a4c0568dfd6baa043", "attribution_status": "unverified_header_claim", "document_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "span_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:1193:1893", "start": 1193, "end": 1893, "quote": "\n\nIn connection with the Hawaii 125-0 McGarret C transaction scheduled to close \nAugust 31, 2000, attached in WordPerfect format are the following closing \ndocuments marked against the McGarret B Series:\n\nClosing Checklist (254308);\nAsset Notice (254309);\nSeries Certificate of Beneficial Ownership (254316);\nSeries Supplement (254319);\nDrawdown Request (254322);\nTotal Return Swap Confirmation (254324);\nPut Option Agreement (254334);\nPut Option Assignment (254341);\nNotice of Put Option Assignment (254345);\nPromissory Note (Big Island III) (254347);\nB Interest Assignment Agreement (254349);\nWarrant Assignment (254351);\nAmended and Restated LLC Agreement (McGarret III) (254352);\nAmended and Rest", "quote_fingerprint": "3679ab7440898cb7db3d780d4fa72f8e7eb1dd8293721981d3a18a6c03fb34b2", "independence_status": "not_established", "raw_sha256": "57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "body_sha256": "392a48d2e75d5616da3a338a125149bc944ba3d319f16519ea5fa1aadb4db9a1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/notes_inbox/1278.", "source_family": "enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692 1893"}`

> 
> 
> In connection with the Hawaii 125-0 McGarret C transaction scheduled to close 
> August 31, 2000, attached in WordPerfect format are the following closing 
> documents marked against the McGarret B Series:
> 
> Closing Checklist (254308);
> Asset Notice (254309);
> Series Certificate of Beneficial Ownership (254316);
> Series Supplement (254319);
> Drawdown Request (254322);
> Total Return Swap Confirmation (254324);
> Put Option Agreement (254334);
> Put Option Assignment (254341);
> Notice of Put Option Assignment (254345);
> Promissory Note (Big Island III) (254347);
> B Interest Assignment Agreement (254349);
> Warrant Assignment (254351);
> Amended and Restated LLC Agreement (McGarret III) (254352);
> Amended and Rest

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:836d309747b519d8`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

**contrasts / observe**

New emails show routine business updates and explicit instructions, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

Source `mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024`; evidence `mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:0:192:aaf79038bf3ad35c`; origin `enron-authored:1784c6113af7fad88f6dd1260062d49823fc555919b6e1e8897a87f638cf9659`.

Attribution and exact offsets: `{"segment_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:segment:0:192", "segment_kind": "authored", "claimed_sender": "brant.reves@enron.com", "claimed_date": "Fri, 08 Sep 2000 07:50:00 -0700", "segment_source_family": "enron-segment:57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "segment_fingerprint": "57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "attribution_status": "unverified_header_claim", "document_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024", "span_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:0:192", "start": 0, "end": 192, "quote": "After reviewing new information i am comforatable amending the existing \nMaster Agreement's credit line from $2.25MM to $3.00.\n\nLet me know if I can be of any futher assistance.\n\nthanks\nbrant\n", "quote_fingerprint": "57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "independence_status": "not_established", "raw_sha256": "561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024", "body_sha256": "eb9cd68df2d3da1085d6e2cd89f5c82c9bd2e6100e376d472a63b3829fa6d3e2", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/notes_inbox/1575.", "source_family": "enron-authored:1784c6113af7fad88f6dd1260062d49823fc555919b6e1e8897a87f638cf9659", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> After reviewing new information i am comforatable amending the existing 
> Master Agreement's credit line from $2.25MM to $3.00.
> 
> Let me know if I can be of any futher assistance.
> 
> thanks
> brant
> 

Source `mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b`; evidence `mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b:281:454:cb01a25624f2e495`; origin `enron-authored:981f4642ef9e1014847536a39507724e46ad80141c0190d0b6f95fa137aebfc4`.

Attribution and exact offsets: `{"segment_id": "mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b:segment:281:454", "segment_kind": "forwarded", "claimed_sender": "Kay Mann                           09/01/2000 10:30 AM", "claimed_date": null, "segment_source_family": "enron-segment:cae46dab9a40d9589f9eb3e51cf0e096e4c55fc0f27b20fcc473ccd35c9328bb", "segment_fingerprint": "cae46dab9a40d9589f9eb3e51cf0e096e4c55fc0f27b20fcc473ccd35c9328bb", "attribution_status": "unverified_header_claim", "document_id": "mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b", "span_id": "mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b:281:454", "start": 281, "end": 454, "quote": "\nLaura,\n\nHere's a draft for your review.  If you find it acceptable, it should be \nready to go to Peoples as a draft.\n\nPlease let  me know if you have any comments.\n\nKay\n\n\n\n", "quote_fingerprint": "cae46dab9a40d9589f9eb3e51cf0e096e4c55fc0f27b20fcc473ccd35c9328bb", "independence_status": "not_established", "raw_sha256": "540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b", "body_sha256": "27f92ac1be3e103d77d0c871952777fb865eab113cf961099823b63c82097afc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/discussion_threads/537.", "source_family": "enron-authored:981f4642ef9e1014847536a39507724e46ad80141c0190d0b6f95fa137aebfc4", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> 
> Laura,
> 
> Here's a draft for your review.  If you find it acceptable, it should be 
> ready to go to Peoples as a draft.
> 
> Please let  me know if you have any comments.
> 
> Kay
> 
> 
> 
> 

Source `mail-0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16`; evidence `mail-0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16:0:108:ad9e053a58dac79f`; origin `enron-authored:7f937a4745d9bf0d1e5526288003b6fafe9783df227991f8e1a197aa0ad1e0e6`.

Attribution and exact offsets: `{"segment_id": "mail-0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16:segment:0:108", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Tue, 29 Aug 2000 08:13:00 -0700", "segment_source_family": "enron-segment:f42eff4a06bc76021cba10a7c89ed7334198fcd653e4338bbddc7bbb7c04e8ba", "segment_fingerprint": "f42eff4a06bc76021cba10a7c89ed7334198fcd653e4338bbddc7bbb7c04e8ba", "attribution_status": "unverified_header_claim", "document_id": "mail-0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16", "span_id": "mail-0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16:0:108", "start": 0, "end": 108, "quote": "Barbara,\n\nWe are in touch with Ketra and John and we shall work with them when they are \nhere.\n\nVince\n\n\n\n\n\n\n", "quote_fingerprint": "f42eff4a06bc76021cba10a7c89ed7334198fcd653e4338bbddc7bbb7c04e8ba", "independence_status": "not_established", "raw_sha256": "0f5d762d64996391609a7e8c32900671589999ae4e580a6d299655e81cb36a16", "body_sha256": "7395ddf825d850d1c22c50186063083465a97f044c857f394821b437c830f076", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/c/technote/mail/projects/260.", "source_family": "enron-authored:7f937a4745d9bf0d1e5526288003b6fafe9783df227991f8e1a197aa0ad1e0e6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Barbara,
> 
> We are in touch with Ketra and John and we shall work with them when they are 
> here.
> 
> Vince
> 
> 
> 
> 
> 
> 
> 

**routines / revise**

Mary Cook's draft references Andrea's oral agreement on termination rights, suggesting legal drafting relies on prior verbal agreements. Sara Shackleton forwards McGarret closing documents, indicating her coordination role. No new tacit knowledge emerges.

**Observation — revision 1**

When drafting legal documents for structured transactions, Enron attorneys rely on prior oral agreements with colleagues to determine contract terms, rather than seeking written confirmation.

Inference gap: Mary Cook states Andrea agreed on termination rights but does not state this is standard practice. Contrast with absence of written confirmation suggests reliance on oral agreements, but scope is unclear.

Evidence basis: Mary Cook's email to Sara Shackleton (v563420df48e5188d) references Andrea's agreement on termination rights, indicating reliance on prior oral agreement. Single episode, no other drafting emails observed.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An attorney drafts a new agreement based on a prior template and needs to decide whether to include partial termination rights.

Exceptions: Unknown; may differ if the agreement is for a new counterparty or if the prior agreement is not directly applicable.

Alternative: Attorneys might include partial termination rights by default unless explicitly told otherwise.

Uncertainty: Single episode; no evidence of how often such oral agreements guide drafting.

Next query: Search for other drafting emails referencing oral agreements or template modifications to see if this pattern repeats.

Prediction: In future drafting tasks, attorneys will reference prior oral agreements to determine contract terms without seeking written confirmation.

Hypothesis `hypothesis-e509e9deb20d4aeba215795e8b1651cb`; transfer tested: false.

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:65ecea17bcf937b1`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

Source `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692`; evidence `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:1193:1893:8eb05945fdb678d6`; origin `enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c`.

Attribution and exact offsets: `{"segment_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:segment:1193:3509", "segment_kind": "forwarded", "claimed_sender": "\"CHRIS KRECEK\" <KRECC@andrews-kurth.com>", "claimed_date": "08/23/00 02:47 PM", "segment_source_family": "enron-segment:7c7d63859b0fd91d1f3b435e80b697448661d755c02e2f7a4c0568dfd6baa043", "segment_fingerprint": "7c7d63859b0fd91d1f3b435e80b697448661d755c02e2f7a4c0568dfd6baa043", "attribution_status": "unverified_header_claim", "document_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "span_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:1193:1893", "start": 1193, "end": 1893, "quote": "\n\nIn connection with the Hawaii 125-0 McGarret C transaction scheduled to close \nAugust 31, 2000, attached in WordPerfect format are the following closing \ndocuments marked against the McGarret B Series:\n\nClosing Checklist (254308);\nAsset Notice (254309);\nSeries Certificate of Beneficial Ownership (254316);\nSeries Supplement (254319);\nDrawdown Request (254322);\nTotal Return Swap Confirmation (254324);\nPut Option Agreement (254334);\nPut Option Assignment (254341);\nNotice of Put Option Assignment (254345);\nPromissory Note (Big Island III) (254347);\nB Interest Assignment Agreement (254349);\nWarrant Assignment (254351);\nAmended and Restated LLC Agreement (McGarret III) (254352);\nAmended and Rest", "quote_fingerprint": "3679ab7440898cb7db3d780d4fa72f8e7eb1dd8293721981d3a18a6c03fb34b2", "independence_status": "not_established", "raw_sha256": "57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "body_sha256": "392a48d2e75d5616da3a338a125149bc944ba3d319f16519ea5fa1aadb4db9a1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/notes_inbox/1278.", "source_family": "enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692 1893"}`

> 
> 
> In connection with the Hawaii 125-0 McGarret C transaction scheduled to close 
> August 31, 2000, attached in WordPerfect format are the following closing 
> documents marked against the McGarret B Series:
> 
> Closing Checklist (254308);
> Asset Notice (254309);
> Series Certificate of Beneficial Ownership (254316);
> Series Supplement (254319);
> Drawdown Request (254322);
> Total Return Swap Confirmation (254324);
> Put Option Agreement (254334);
> Put Option Assignment (254341);
> Notice of Put Option Assignment (254345);
> Promissory Note (Big Island III) (254347);
> B Interest Assignment Agreement (254349);
> Warrant Assignment (254351);
> Amended and Restated LLC Agreement (McGarret III) (254352);
> Amended and Rest

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:836d309747b519d8`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

**expectations / revise**

No new evidence supports existing hypotheses. The current email is a legal disclaimer, not relevant to tacit knowledge. Existing hypotheses remain unsupported.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-777b76851e4c4d8fa37f08ffe4444d4a",
    "prediction_id": "prediction-248c36f486ce44eb8f571650227345c3",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals relevant to software request routing.",
    "evidence": [],
    "virtual_time": "2000-09-19T15:13:00+00:00",
    "arrival_sequence": 110000
  },
  {
    "hypothesis_id": "hypothesis-195878fb36fb4be2bb49d26e106fb5e5",
    "prediction_id": "prediction-83d95d8bea834bf19025f3a3bf4ea7cb",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals relevant to legal document approval routing.",
    "evidence": [],
    "virtual_time": "2000-09-19T15:13:00+00:00",
    "arrival_sequence": 110000
  }
]
```

**expertise / revise**

Mary Cook's draft references Andrea's agreement on termination rights, suggesting legal drafting relies on prior oral agreements. Sara Shackleton forwards McGarret closing documents, indicating her role in transaction coordination. No new tacit rules emerge.

**Observation — revision 2**

When drafting legal documents for structured transactions, Enron attorneys rely on prior oral agreements with colleagues (e.g., Andrea) to determine scope of terms, rather than seeking explicit written instructions.

Inference gap: The email states Andrea agreed on termination rights but does not state that this is a standard practice. The contrast between Mary's reliance on Andrea's agreement and the absence of written confirmation suggests an implicit norm, but scope is unclear.

Evidence basis: Mary Cook's email to Sara Shackleton (vd4604852c6eb008b) and draft text (v563420df48e5188d) show one episode of drafting based on oral agreement with Andrea.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An attorney drafts a new agreement based on a prior template and needs to decide whether to include partial termination rights.

Exceptions: Unknown; may differ if the agreement is for a new counterparty or if the prior agreement is not directly applicable.

Alternative: Attorneys might include partial termination rights by default unless explicitly told otherwise.

Uncertainty: Single episode; no evidence of how often such oral agreements guide drafting.

Next query: read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 1132

Prediction: In future drafting tasks, attorneys will reference prior oral agreements to determine contract terms without seeking written confirmation.

Hypothesis `hypothesis-79e070680e8649139efde6728a066eb5`; transfer tested: false.

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:da440d7717ef25e4`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:700:1132:1b34b1446a30cc4a`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:700:1132", "start": 700, "end": 1132, "quote": "ince partnership interests could be sold, exchanged, \nrolled up to a master partnership etc.  It is not perfect, but it seems to \ncover those types of events adequately.  Give me a call Monday morning and we \ncan call Jean.  Again, thanks for your help on Friday.  Mary\n\n\n\n\n\nEnron North America Corp.\nMary Cook\n1400 Smith, 38th Floor, Legal\nHouston, Texas   77002-7361\n(713) 345-7732 (phone)\n(713) 646-3490 (fax)\nmary.cook@enron.com", "quote_fingerprint": "629977b39e925e89ac7f0e62c4d7818ca6b5fcc5adaf59f7248c77df5ca9c03a", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> ince partnership interests could be sold, exchanged, 
> rolled up to a master partnership etc.  It is not perfect, but it seems to 
> cover those types of events adequately.  Give me a call Monday morning and we 
> can call Jean.  Again, thanks for your help on Friday.  Mary
> 
> 
> 
> 
> 
> Enron North America Corp.
> Mary Cook
> 1400 Smith, 38th Floor, Legal
> Houston, Texas   77002-7361
> (713) 345-7732 (phone)
> (713) 646-3490 (fax)
> mary.cook@enron.com

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:836d309747b519d8`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

**contrasts / revise**

New emails show routine business updates and explicit instructions, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

**Observation — revision 2**

When external parties propose visits, senior Enron staff reschedule to fit their own travel constraints rather than accommodating the proposer's preferred date.

Inference gap: Vince's reply does not state a general policy; it only shows one instance of rescheduling. Contrast with Ehud's request suggests implicit priority on internal schedules.

Evidence basis: Single episode from one email exchange between Vince and Ehud, showing Vince's stated preference for June 22 over May 25.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An external academic or partner requests a Houston visit for a presentation.

Exceptions: Unknown; may differ if the visitor is a key client or regulator.

Alternative: Staff might accept the proposed date if no conflicts exist.

Uncertainty: Single episode; no evidence of repeated scheduling behavior.

Next query: Search for other visit scheduling emails to see if rescheduling is common.

Prediction: Future external visit requests will be rescheduled if they conflict with internal travel plans.

Hypothesis `hypothesis-c2554531fd984b2581be381c98d7df30`; transfer tested: false.

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:a025315179da15e5`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

Attribution and exact offsets: `{"segment_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:segment:0:1088", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Mon, 22 May 2000 02:32:00 -0700", "segment_source_family": "enron-segment:0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "segment_fingerprint": "0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "attribution_status": "unverified_header_claim", "document_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "span_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700", "start": 0, "end": 700, "quote": "Ehud,\n\nThanks fro your message. \nWhat about June 22?  I have several trips in between May 25 and June 22.\n\nVince\n\n\n\n\n\n\n\"Ehud I. Ronn\" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM\nTo: Vince.J.Kaminski@enron.com\ncc:  \nSubject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit\n\n\nVince,\n\nGreetings.\n\n1.  Thanks again for hosting the dinner at Power 2000.  Congratulations\nalso on a thoughtful keynote address, a copy of which I picked up on the\nway out of the Conference.\n\n2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I\nwould like to reschedule my proposed Houston visit, and presentation of the\n\"Enterprise-Wide Risk Management\" model to Enron's Research Dept., to the\nnex", "quote_fingerprint": "64549c895b7b5ef849495a3371ffe7d6091c204c36def5d4ef1c6085eabbb02a", "independence_status": "not_established", "raw_sha256": "2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "body_sha256": "66e007804d8cf760b5f1058f1b6efa26f6f4129b86434b294b204afa4053d48c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/3977.", "source_family": "enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920 700"}`

> Ehud,
> 
> Thanks fro your message. 
> What about June 22?  I have several trips in between May 25 and June 22.
> 
> Vince
> 
> 
> 
> 
> 
> 
> "Ehud I. Ronn" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM
> To: Vince.J.Kaminski@enron.com
> cc:  
> Subject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit
> 
> 
> Vince,
> 
> Greetings.
> 
> 1.  Thanks again for hosting the dinner at Power 2000.  Congratulations
> also on a thoughtful keynote address, a copy of which I picked up on the
> way out of the Conference.
> 
> 2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I
> would like to reschedule my proposed Houston visit, and presentation of the
> "Enterprise-Wide Risk Management" model to Enron's Research Dept., to the
> nex

Source `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6`; evidence `mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254:598d2536cc1e1ded`; origin `enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e`.

Attribution and exact offsets: `{"segment_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:segment:0:254", "segment_kind": "authored", "claimed_sender": "robin.rodrigue@enron.com", "claimed_date": "Thu, 03 Aug 2000 12:22:00 -0700", "segment_source_family": "enron-segment:c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "segment_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "attribution_status": "unverified_header_claim", "document_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "span_id": "mail-84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6:0:254", "start": 0, "end": 254, "quote": "No I promise I didn't....your post-id crashed my system.  I had your book and \nthe power book and the Nymex book all coming in at the same time and the \nsystem just stopped.  We're going again though, so I should have your \nposition in a few minutes.\n\nRR", "quote_fingerprint": "c0eb97c87ba066105d65932595d0166ae3d14480cf639c1ca2560283725dd558", "independence_status": "not_established", "raw_sha256": "84252243f116307571d19828a3fca2e9605c16ec9d192accb683ea421f2945a6", "body_sha256": "99c87bca3237b1b67a94e3e40044d20fc00d12e3dccffdcdee293593a1605e24", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rodrique-r/all_documents/640.", "source_family": "enron-authored:34daea8323a92069ad940c274d2e56da3d233859a428a3c3aada72f0f8e0044e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> No I promise I didn't....your post-id crashed my system.  I had your book and 
> the power book and the Nymex book all coming in at the same time and the 
> system just stopped.  We're going again though, so I should have your 
> position in a few minutes.
> 
> RR

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:27c346549c17f1aa`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

Attribution and exact offsets: `{"segment_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:segment:0:1132", "segment_kind": "authored", "claimed_sender": "mary.cook@enron.com", "claimed_date": "Sun, 17 Sep 2000 02:54:00 -0700", "segment_source_family": "enron-segment:f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "segment_fingerprint": "f38f1aec8373b0c9e728a6fb5c4f773a8eee25cb9829d0277f713c21af5e841d", "attribution_status": "unverified_header_claim", "document_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "span_id": "mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700", "start": 0, "end": 700, "quote": "Sara, attached is my draft for partnership interests based upon the Juniper \nLP.  Andrea has agreed that as to partnership interests, the mutual \ntermination right is only for the entire interest and we  do not need to \ndraft in partial termination rights so the Notice, if given, will always be \nfor the entire interest.  I have fixed Equity Notional Amount and this makes \nthe numbers work.  I modified Method of Adjustment to cover any event of \ndilution or conversion (but did not specifically say in sole discretion of \nCalc Agent)--this will cover primarily the effect of the addition of new \npartners to the partnership.  I also left in Extraordinary Events as we have \npreviously syled same s", "quote_fingerprint": "009b33516774759db856ee578a1ac6d6007a59951672ca801b75cff217aebc11", "independence_status": "not_established", "raw_sha256": "1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd", "body_sha256": "0255b24d1154c777df48a5a6330625b725c802ccda7c25b8a4395a6935becdb7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1035.", "source_family": "enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd 700"}`

> Sara, attached is my draft for partnership interests based upon the Juniper 
> LP.  Andrea has agreed that as to partnership interests, the mutual 
> termination right is only for the entire interest and we  do not need to 
> draft in partial termination rights so the Notice, if given, will always be 
> for the entire interest.  I have fixed Equity Notional Amount and this makes 
> the numbers work.  I modified Method of Adjustment to cover any event of 
> dilution or conversion (but did not specifically say in sole discretion of 
> Calc Agent)--this will cover primarily the effect of the addition of new 
> partners to the partnership.  I also left in Extraordinary Events as we have 
> previously syled same s

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:836d309747b519d8`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

Attribution and exact offsets: `{"segment_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:segment:0:1088", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Mon, 22 May 2000 02:32:00 -0700", "segment_source_family": "enron-segment:0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "segment_fingerprint": "0fb0b36953e7f48d7cbc95f87ec03b1187acc428cccf2a2985829bfd605fec2f", "attribution_status": "unverified_header_claim", "document_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "span_id": "mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700", "start": 0, "end": 700, "quote": "Ehud,\n\nThanks fro your message. \nWhat about June 22?  I have several trips in between May 25 and June 22.\n\nVince\n\n\n\n\n\n\n\"Ehud I. Ronn\" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM\nTo: Vince.J.Kaminski@enron.com\ncc:  \nSubject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit\n\n\nVince,\n\nGreetings.\n\n1.  Thanks again for hosting the dinner at Power 2000.  Congratulations\nalso on a thoughtful keynote address, a copy of which I picked up on the\nway out of the Conference.\n\n2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I\nwould like to reschedule my proposed Houston visit, and presentation of the\n\"Enterprise-Wide Risk Management\" model to Enron's Research Dept., to the\nnex", "quote_fingerprint": "64549c895b7b5ef849495a3371ffe7d6091c204c36def5d4ef1c6085eabbb02a", "independence_status": "not_established", "raw_sha256": "2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920", "body_sha256": "66e007804d8cf760b5f1058f1b6efa26f6f4129b86434b294b204afa4053d48c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/3977.", "source_family": "enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920 700"}`

> Ehud,
> 
> Thanks fro your message. 
> What about June 22?  I have several trips in between May 25 and June 22.
> 
> Vince
> 
> 
> 
> 
> 
> 
> "Ehud I. Ronn" <eronn@mail.utexas.edu> on 05/16/2000 02:47:49 PM
> To: Vince.J.Kaminski@enron.com
> cc:  
> Subject: 1. Power 2000; 2. My Proposed 5/25 Houston Visit
> 
> 
> Vince,
> 
> Greetings.
> 
> 1.  Thanks again for hosting the dinner at Power 2000.  Congratulations
> also on a thoughtful keynote address, a copy of which I picked up on the
> way out of the Conference.
> 
> 2.  My family and I are leaving on a family trip 5/25 thru 6/4.  Thus, I
> would like to reschedule my proposed Houston visit, and presentation of the
> "Enterprise-Wide Risk Management" model to Enron's Research Dept., to the
> nex

### 2000-10-18T12:22:00+00:00 — review window 6

**routines / observe**

New emails show routine business updates and explicit instructions, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

**expectations / observe**

New emails show routine business updates and explicit instructions, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

**expertise / observe**

Kay Mann sends a rough services agreement draft to Heather for review, noting it is based on a prior JV agreement and asking for Clement's corporate guaranty info. This shows informal legal drafting collaboration and reliance on prior templates.

**Candidate tacit rule — revision 1**

When drafting new agreements, Enron legal staff informally circulate rough drafts to colleagues for review before finalizing, relying on prior templates and peer input.

Inference gap: The email does not state that this is a standard practice; it only shows one instance. The contrast between Kay's informal sending and the absence of formal process suggests an implicit norm.

Evidence basis: Two segments from the same email by Kay Mann, showing her sending a draft to Heather and explaining its basis. Single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A new agreement is based on a prior template and requires internal review before external distribution.

Exceptions: Unknown; may not apply if the agreement is routine or time-sensitive.

Alternative: Staff might use formal document management systems or seek approval from managers before sharing drafts.

Uncertainty: Single episode; no evidence of repeated pattern across other drafting tasks.

Next query: Search for other instances where rough drafts are circulated for review before finalization.

Prediction: In similar future drafting tasks, staff will circulate rough drafts informally for peer review before finalizing.

Hypothesis `hypothesis-5e925d22dfad46aea5ec60531edfa201`; transfer tested: false.

Source `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e`; evidence `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:0:197:61c2a0d3ef51513e`; origin `enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0`.

Attribution and exact offsets: `{"segment_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:segment:0:197", "segment_kind": "authored", "claimed_sender": "kay.mann@enron.com", "claimed_date": "Wed, 27 Sep 2000 11:36:00 -0700", "segment_source_family": "enron-segment:dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "segment_fingerprint": "dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "attribution_status": "unverified_header_claim", "document_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "span_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:0:197", "start": 0, "end": 197, "quote": "Heather,\n\nThis is a rough cut of a services agreement.  Since the loan agreement, \nservices agreement and LLC agreement are all pieces of the same puzzle, I \nthought I would send it your way.\n\nKay\n", "quote_fingerprint": "dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "independence_status": "not_established", "raw_sha256": "0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "body_sha256": "b428cc9279c61fa05f423778c361903996e0f95da191c19724597d9a697e0310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/sent/913.", "source_family": "enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Heather,
> 
> This is a rough cut of a services agreement.  Since the loan agreement, 
> services agreement and LLC agreement are all pieces of the same puzzle, I 
> thought I would send it your way.
> 
> Kay
> 

Source `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e`; evidence `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:473:1083:6681cc7fa0715d1d`; origin `enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0`.

Attribution and exact offsets: `{"segment_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:segment:473:1083", "segment_kind": "forwarded", "claimed_sender": "Kay Mann                           09/19/2000 11:45 AM", "claimed_date": null, "segment_source_family": "enron-segment:346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "segment_fingerprint": "346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "attribution_status": "unverified_header_claim", "document_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "span_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:473:1083", "start": 473, "end": 1083, "quote": "\nThis is a very rough draft based on an agreement done previously with a jv \ncompany.  I'm sending it for Enron review only, since I haven't even read the \nentire thing yet.  I thought you might want to take a look at it to see what \nyou think, and to consider the scope of the services to be provided.\n\nAs for legal services, one alternative would be to have the services provided \nby an outside law firm, not associated with either principal.\n\nCould you forward me what you received from Clement regarding the corporate \nguaranty issue?  I would like to see what's the latest in that regard.\n\nThanks,\n\nKay\n\n\n", "quote_fingerprint": "346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "independence_status": "not_established", "raw_sha256": "0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "body_sha256": "b428cc9279c61fa05f423778c361903996e0f95da191c19724597d9a697e0310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/sent/913.", "source_family": "enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> 
> This is a very rough draft based on an agreement done previously with a jv 
> company.  I'm sending it for Enron review only, since I haven't even read the 
> entire thing yet.  I thought you might want to take a look at it to see what 
> you think, and to consider the scope of the services to be provided.
> 
> As for legal services, one alternative would be to have the services provided 
> by an outside law firm, not associated with either principal.
> 
> Could you forward me what you received from Clement regarding the corporate 
> guaranty issue?  I would like to see what's the latest in that regard.
> 
> Thanks,
> 
> Kay
> 
> 
> 

Source `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e`; evidence `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:0:197:836d309747b519d8`; origin `enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0`.

Attribution and exact offsets: `{"segment_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:segment:0:197", "segment_kind": "authored", "claimed_sender": "kay.mann@enron.com", "claimed_date": "Wed, 27 Sep 2000 11:36:00 -0700", "segment_source_family": "enron-segment:dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "segment_fingerprint": "dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "attribution_status": "unverified_header_claim", "document_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "span_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:0:197", "start": 0, "end": 197, "quote": "Heather,\n\nThis is a rough cut of a services agreement.  Since the loan agreement, \nservices agreement and LLC agreement are all pieces of the same puzzle, I \nthought I would send it your way.\n\nKay\n", "quote_fingerprint": "dc46b744289e8a8dd35408f9732703b2c876a91a0d78fcab6c28e728f66f81e0", "independence_status": "not_established", "raw_sha256": "0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "body_sha256": "b428cc9279c61fa05f423778c361903996e0f95da191c19724597d9a697e0310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/sent/913.", "source_family": "enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Heather,
> 
> This is a rough cut of a services agreement.  Since the loan agreement, 
> services agreement and LLC agreement are all pieces of the same puzzle, I 
> thought I would send it your way.
> 
> Kay
> 

Source `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e`; evidence `mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:473:1083:836d309747b519d8`; origin `enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0`.

Attribution and exact offsets: `{"segment_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:segment:473:1083", "segment_kind": "forwarded", "claimed_sender": "Kay Mann                           09/19/2000 11:45 AM", "claimed_date": null, "segment_source_family": "enron-segment:346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "segment_fingerprint": "346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "attribution_status": "unverified_header_claim", "document_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "span_id": "mail-0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e:473:1083", "start": 473, "end": 1083, "quote": "\nThis is a very rough draft based on an agreement done previously with a jv \ncompany.  I'm sending it for Enron review only, since I haven't even read the \nentire thing yet.  I thought you might want to take a look at it to see what \nyou think, and to consider the scope of the services to be provided.\n\nAs for legal services, one alternative would be to have the services provided \nby an outside law firm, not associated with either principal.\n\nCould you forward me what you received from Clement regarding the corporate \nguaranty issue?  I would like to see what's the latest in that regard.\n\nThanks,\n\nKay\n\n\n", "quote_fingerprint": "346b58c79dabda19ba77a6a82f065c8e03d2c877c0ab44444c9453f915a0b5dc", "independence_status": "not_established", "raw_sha256": "0a937b9ec4fa7adf56b74786ac134ff3b92a26d4c26f1cff9010292c12613d8e", "body_sha256": "b428cc9279c61fa05f423778c361903996e0f95da191c19724597d9a697e0310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/sent/913.", "source_family": "enron-authored:097ab8107e381560d0b28c5ed28a451c8aa7a46abe6b9bbc9983847efafab7d0", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> 
> This is a very rough draft based on an agreement done previously with a jv 
> company.  I'm sending it for Enron review only, since I haven't even read the 
> entire thing yet.  I thought you might want to take a look at it to see what 
> you think, and to consider the scope of the services to be provided.
> 
> As for legal services, one alternative would be to have the services provided 
> by an outside law firm, not associated with either principal.
> 
> Could you forward me what you received from Clement regarding the corporate 
> guaranty issue?  I would like to see what's the latest in that regard.
> 
> Thanks,
> 
> Kay
> 
> 
> 

**contrasts / observe**

New emails show routine business updates and explicit instructions, but no new tacit knowledge emerges. Existing hypotheses remain unsupported by new evidence.

**Candidate tacit rule — revision 1**

When a counterparty is in an unresolved dispute, Enron traders informally expect that the dispute owner's instruction to restrict trading takes precedence over standard credit approvals, unless a higher authority explicitly overrides.

Inference gap: The sources show Peter's restriction and Justin's conditional approval but do not state a general rule for resolving such conflicts. The contrast between Peter's directive and Justin's approval suggests an implicit hierarchy, but the outcome is unknown.

Evidence basis: Two separate emails from different actors (Peter Keohane and Justin Boyd) discussing the same counterparty, showing conflicting instructions without a stated resolution.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A counterparty is flagged as being in an unresolved dispute and a credit approval exists for that counterparty.

Exceptions: Unknown; may not apply if the dispute is resolved or if senior management explicitly approves trading despite the dispute.

Alternative: Credit approvals might be followed without regard to dispute status if the dispute is not widely known.

Uncertainty: Single episode; no evidence of how such conflicts are typically resolved across other disputes.

Next query: Search for other instances where a dispute owner's restriction conflicts with a credit approval to see if the restriction is consistently upheld.

Prediction: In similar future disputes, the dispute owner's restriction will be followed unless a senior manager explicitly overrides it.

Hypothesis `hypothesis-ceaa329b17614a7d95e286c6ddee83b0`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-f12d44845a134f238b370d6b63cf8e8b",
    "prediction_id": "prediction-b920e68e230d449585a5546110ca79db",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address OMLX clearing house selection.",
    "evidence": [],
    "virtual_time": "2000-10-18T12:22:00+00:00",
    "arrival_sequence": 132000
  },
  {
    "hypothesis_id": "hypothesis-b3a7fd9748f74a66bc50dca47aefd715",
    "prediction_id": "prediction-8f2b8fe7b7f24e27ad1e452c5dab8a26",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals discuss clearing house preferences.",
    "evidence": [],
    "virtual_time": "2000-10-18T12:22:00+00:00",
    "arrival_sequence": 132000
  }
]
```

Source `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56`; evidence `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:0:700:8b96d7a2f6714e57`; origin `enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34`.

Attribution and exact offsets: `{"segment_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:segment:0:812", "segment_kind": "authored", "claimed_sender": "peter.keohane@enron.com", "claimed_date": "Mon, 25 Sep 2000 10:17:00 -0700", "segment_source_family": "enron-segment:88dce4df96f7f25fcb2acbf64a2420c37697288fb65ded56775275e60b9d68e4", "segment_fingerprint": "88dce4df96f7f25fcb2acbf64a2420c37697288fb65ded56775275e60b9d68e4", "attribution_status": "unverified_header_claim", "document_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "span_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:0:700", "start": 0, "end": 700, "quote": "Justin, Enron Canada is currently in an unresolved dispute with Bank of Nova \nScotia where from our perspective Bank of Nova Scotia has essentially been \ntelling us to shove off.  The dispute involves BNS's purported requirement to \nconsent to collateral security given to Enron Canada for physical and \nfinancial trading positions with a counterparty known as Beau Canada.  \nNeither Bank of Nova Scotia nor any affiliate of Bank of Nova Scotia should \nbe traded OnLine and all trading ought to be monitored until such time as \nthis matter is resolved, and this should be expressly communicated to Bank of \nNova Scotia.  They can speak to me directly at 403.974.6923 or to our \nPresident and CEO, Rob", "quote_fingerprint": "438ff8cef7bf65f60affd328f1e1223511f7d81452b40a9f857a936a3d2bded6", "independence_status": "not_established", "raw_sha256": "11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "body_sha256": "c76783e5c854f98670fc3ab4acb02ab2f0cc6e8458779c90135b3e87c5651808", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/3321.", "source_family": "enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56 700"}`

> Justin, Enron Canada is currently in an unresolved dispute with Bank of Nova 
> Scotia where from our perspective Bank of Nova Scotia has essentially been 
> telling us to shove off.  The dispute involves BNS's purported requirement to 
> consent to collateral security given to Enron Canada for physical and 
> financial trading positions with a counterparty known as Beau Canada.  
> Neither Bank of Nova Scotia nor any affiliate of Bank of Nova Scotia should 
> be traded OnLine and all trading ought to be monitored until such time as 
> this matter is resolved, and this should be expressly communicated to Bank of 
> Nova Scotia.  They can speak to me directly at 403.974.6923 or to our 
> President and CEO, Rob

Source `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56`; evidence `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:948:1648:76a231e2cd87daa9`; origin `enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34`.

Attribution and exact offsets: `{"segment_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:segment:948:1791", "segment_kind": "forwarded", "claimed_sender": "Justin Boyd", "claimed_date": "09/25/2000 08:36 AM", "segment_source_family": "enron-segment:2879f754a0f735dd72e7fead5509ed8c10d3c9b62d7fbc7d4b9ca17b83e6906a", "segment_fingerprint": "2879f754a0f735dd72e7fead5509ed8c10d3c9b62d7fbc7d4b9ca17b83e6906a", "attribution_status": "unverified_header_claim", "document_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "span_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:948:1648", "start": 948, "end": 1648, "quote": "\nLara\n\nSubject to approval from Peter (the C/P is a Canadian corporate), I approve \nfor all products except for US power, weather and credit\n\nPeter - thanks!\n\nJustin\n\n\n\n\nTo: Edmund Cooper/LON/ECT@ECT, Justin Boyd/LON/ECT@ECT, Debbie \nNicholls/LON/ECT@ECT, Gail Hill/LON/ECT@ECT, Enron London - EOL Product \nControl Group/LON/ECT@ECT, Enron Europe Global CounterParty, Annette \nSchneider/LON/ECT@ECT, ECT London Credit, Enron Europe Global Contracts and \nFacilities, EOL Marketing Europe@ECT\ncc:  \n\nSubject: PA Review Bank of Nova Scotia\n\nHello all,\n\nThe Bank of Nova Scotia would like to trade with us online.  They are in GCP \nas #54087 and are existing customers of Enron Metals (Jimmy Gordon is th", "quote_fingerprint": "fc2cb52730f6c560930c6bccf5f91c6177575fcb9ce7675e06cb5af867b2ea27", "independence_status": "not_established", "raw_sha256": "11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "body_sha256": "c76783e5c854f98670fc3ab4acb02ab2f0cc6e8458779c90135b3e87c5651808", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/3321.", "source_family": "enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56 1648"}`

> 
> Lara
> 
> Subject to approval from Peter (the C/P is a Canadian corporate), I approve 
> for all products except for US power, weather and credit
> 
> Peter - thanks!
> 
> Justin
> 
> 
> 
> 
> To: Edmund Cooper/LON/ECT@ECT, Justin Boyd/LON/ECT@ECT, Debbie 
> Nicholls/LON/ECT@ECT, Gail Hill/LON/ECT@ECT, Enron London - EOL Product 
> Control Group/LON/ECT@ECT, Enron Europe Global CounterParty, Annette 
> Schneider/LON/ECT@ECT, ECT London Credit, Enron Europe Global Contracts and 
> Facilities, EOL Marketing Europe@ECT
> cc:  
> 
> Subject: PA Review Bank of Nova Scotia
> 
> Hello all,
> 
> The Bank of Nova Scotia would like to trade with us online.  They are in GCP 
> as #54087 and are existing customers of Enron Metals (Jimmy Gordon is th

Source `mail-77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12`; evidence `mail-77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12:0:131:051041b95e0aad19`; origin `enron-authored:09ac8187b613b015fa3b1e8505f079fa1b52305bea0056e83113d9843b381bd2`.

Attribution and exact offsets: `{"segment_id": "mail-77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12:segment:0:131", "segment_kind": "authored", "claimed_sender": "michelle.cash@enron.com", "claimed_date": "Fri, 29 Sep 2000 10:02:00 -0700", "segment_source_family": "enron-segment:f2e63c352bd25bea3b667aad526ac6916f56b1c83b66c409d4534193ae35346d", "segment_fingerprint": "f2e63c352bd25bea3b667aad526ac6916f56b1c83b66c409d4534193ae35346d", "attribution_status": "unverified_header_claim", "document_id": "mail-77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12", "span_id": "mail-77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12:0:131", "start": 0, "end": 131, "quote": "Amy, this looks fine, except I would delete the provision about exceptions, \nbecause there really are none!  Thanks.  Michelle\n\n\n\n\n", "quote_fingerprint": "f2e63c352bd25bea3b667aad526ac6916f56b1c83b66c409d4534193ae35346d", "independence_status": "not_established", "raw_sha256": "77de17ab60a2409afb464e7ee6c1d9dfcd8b7391cb37427f8d06954ee18dce12", "body_sha256": "b0433e41dfc83ab0db08d0037ad1767bcd839987f44cfe63e010c412925e167f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/cash-m/all_documents/446.", "source_family": "enron-authored:09ac8187b613b015fa3b1e8505f079fa1b52305bea0056e83113d9843b381bd2", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Amy, this looks fine, except I would delete the provision about exceptions, 
> because there really are none!  Thanks.  Michelle
> 
> 
> 
> 
> 

Source `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56`; evidence `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:0:700:836d309747b519d8`; origin `enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34`.

Attribution and exact offsets: `{"segment_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:segment:0:812", "segment_kind": "authored", "claimed_sender": "peter.keohane@enron.com", "claimed_date": "Mon, 25 Sep 2000 10:17:00 -0700", "segment_source_family": "enron-segment:88dce4df96f7f25fcb2acbf64a2420c37697288fb65ded56775275e60b9d68e4", "segment_fingerprint": "88dce4df96f7f25fcb2acbf64a2420c37697288fb65ded56775275e60b9d68e4", "attribution_status": "unverified_header_claim", "document_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "span_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:0:700", "start": 0, "end": 700, "quote": "Justin, Enron Canada is currently in an unresolved dispute with Bank of Nova \nScotia where from our perspective Bank of Nova Scotia has essentially been \ntelling us to shove off.  The dispute involves BNS's purported requirement to \nconsent to collateral security given to Enron Canada for physical and \nfinancial trading positions with a counterparty known as Beau Canada.  \nNeither Bank of Nova Scotia nor any affiliate of Bank of Nova Scotia should \nbe traded OnLine and all trading ought to be monitored until such time as \nthis matter is resolved, and this should be expressly communicated to Bank of \nNova Scotia.  They can speak to me directly at 403.974.6923 or to our \nPresident and CEO, Rob", "quote_fingerprint": "438ff8cef7bf65f60affd328f1e1223511f7d81452b40a9f857a936a3d2bded6", "independence_status": "not_established", "raw_sha256": "11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "body_sha256": "c76783e5c854f98670fc3ab4acb02ab2f0cc6e8458779c90135b3e87c5651808", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/3321.", "source_family": "enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56 700"}`

> Justin, Enron Canada is currently in an unresolved dispute with Bank of Nova 
> Scotia where from our perspective Bank of Nova Scotia has essentially been 
> telling us to shove off.  The dispute involves BNS's purported requirement to 
> consent to collateral security given to Enron Canada for physical and 
> financial trading positions with a counterparty known as Beau Canada.  
> Neither Bank of Nova Scotia nor any affiliate of Bank of Nova Scotia should 
> be traded OnLine and all trading ought to be monitored until such time as 
> this matter is resolved, and this should be expressly communicated to Bank of 
> Nova Scotia.  They can speak to me directly at 403.974.6923 or to our 
> President and CEO, Rob

Source `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56`; evidence `mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:948:1648:836d309747b519d8`; origin `enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34`.

Attribution and exact offsets: `{"segment_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:segment:948:1791", "segment_kind": "forwarded", "claimed_sender": "Justin Boyd", "claimed_date": "09/25/2000 08:36 AM", "segment_source_family": "enron-segment:2879f754a0f735dd72e7fead5509ed8c10d3c9b62d7fbc7d4b9ca17b83e6906a", "segment_fingerprint": "2879f754a0f735dd72e7fead5509ed8c10d3c9b62d7fbc7d4b9ca17b83e6906a", "attribution_status": "unverified_header_claim", "document_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "span_id": "mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56:948:1648", "start": 948, "end": 1648, "quote": "\nLara\n\nSubject to approval from Peter (the C/P is a Canadian corporate), I approve \nfor all products except for US power, weather and credit\n\nPeter - thanks!\n\nJustin\n\n\n\n\nTo: Edmund Cooper/LON/ECT@ECT, Justin Boyd/LON/ECT@ECT, Debbie \nNicholls/LON/ECT@ECT, Gail Hill/LON/ECT@ECT, Enron London - EOL Product \nControl Group/LON/ECT@ECT, Enron Europe Global CounterParty, Annette \nSchneider/LON/ECT@ECT, ECT London Credit, Enron Europe Global Contracts and \nFacilities, EOL Marketing Europe@ECT\ncc:  \n\nSubject: PA Review Bank of Nova Scotia\n\nHello all,\n\nThe Bank of Nova Scotia would like to trade with us online.  They are in GCP \nas #54087 and are existing customers of Enron Metals (Jimmy Gordon is th", "quote_fingerprint": "fc2cb52730f6c560930c6bccf5f91c6177575fcb9ce7675e06cb5af867b2ea27", "independence_status": "not_established", "raw_sha256": "11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56", "body_sha256": "c76783e5c854f98670fc3ab4acb02ab2f0cc6e8458779c90135b3e87c5651808", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/3321.", "source_family": "enron-authored:39389c4e4c45bb9ea9b667b8206b745c3392a53818c405fd35c15492dff3fb34", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-11e4b7c288b707c1bd0f0c0c03d1408f34c2efb6dd5ad82fac9a1370f11b7a56 1648"}`

> 
> Lara
> 
> Subject to approval from Peter (the C/P is a Canadian corporate), I approve 
> for all products except for US power, weather and credit
> 
> Peter - thanks!
> 
> Justin
> 
> 
> 
> 
> To: Edmund Cooper/LON/ECT@ECT, Justin Boyd/LON/ECT@ECT, Debbie 
> Nicholls/LON/ECT@ECT, Gail Hill/LON/ECT@ECT, Enron London - EOL Product 
> Control Group/LON/ECT@ECT, Enron Europe Global CounterParty, Annette 
> Schneider/LON/ECT@ECT, ECT London Credit, Enron Europe Global Contracts and 
> Facilities, EOL Marketing Europe@ECT
> cc:  
> 
> Subject: PA Review Bank of Nova Scotia
> 
> Hello all,
> 
> The Bank of Nova Scotia would like to trade with us online.  They are in GCP 
> as #54087 and are existing customers of Enron Metals (Jimmy Gordon is th

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:39:46.800121+00:00",
  "window": 1,
  "virtual_time": "2000-02-18T10:05:00+00:00",
  "arrival_sequence": 22000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 13417,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:40:06.793828+00:00",
  "window": 2,
  "virtual_time": "2000-05-05T17:42:00+00:00",
  "arrival_sequence": 44000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14381,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:40:29.184776+00:00",
  "window": 3,
  "virtual_time": "2000-06-30T20:55:00+00:00",
  "arrival_sequence": 66000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14210,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:40:46.903914+00:00",
  "window": 4,
  "virtual_time": "2000-08-16T14:45:00+00:00",
  "arrival_sequence": 88000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14828,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:09.110802+00:00",
  "window": 5,
  "virtual_time": "2000-09-19T15:13:00+00:00",
  "arrival_sequence": 110000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14562,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:26.836152+00:00",
  "window": 6,
  "virtual_time": "2000-10-18T12:22:00+00:00",
  "arrival_sequence": 132000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14592,
  "agent_invocations": 8,
  "gate_reason": "reasoning_error_remaining_arrivals_only"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:34.417948+00:00",
  "window": 7,
  "virtual_time": "2000-11-10T15:33:00+00:00",
  "arrival_sequence": 154000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14577,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:42.035311+00:00",
  "window": 8,
  "virtual_time": "2000-12-01T08:21:00+00:00",
  "arrival_sequence": 176000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14969,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:48.729186+00:00",
  "window": 9,
  "virtual_time": "2000-12-14T08:53:00+00:00",
  "arrival_sequence": 198000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 15216,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:41:56.905930+00:00",
  "window": 10,
  "virtual_time": "2001-01-18T15:33:00+00:00",
  "arrival_sequence": 220000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14655,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:42:04.967970+00:00",
  "window": 11,
  "virtual_time": "2001-02-14T09:13:00+00:00",
  "arrival_sequence": 242000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14251,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:42:13.050407+00:00",
  "window": 12,
  "virtual_time": "2001-03-12T13:36:00+00:00",
  "arrival_sequence": 264000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14097,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:42:21.300478+00:00",
  "window": 13,
  "virtual_time": "2001-04-04T08:26:00+00:00",
  "arrival_sequence": 286000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 13687,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:42:28.491739+00:00",
  "window": 14,
  "virtual_time": "2001-04-23T13:51:00+00:00",
  "arrival_sequence": 308000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 13877,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:42:34.879978+00:00",
  "window": 15,
  "virtual_time": "2001-05-10T10:31:00+00:00",
  "arrival_sequence": 330000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 12961,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

## Execution errors

```json
[
  {
    "window": 6,
    "phase": "revise",
    "agent": "routines",
    "error_type": "GateDenied"
  },
  {
    "window": 6,
    "phase": "revise",
    "agent": "expectations",
    "error_type": "GateDenied"
  },
  {
    "window": 6,
    "phase": "revise",
    "agent": "expertise",
    "error_type": "GateDenied"
  },
  {
    "window": 6,
    "phase": "revise",
    "agent": "contrasts",
    "error_type": "GateDenied"
  }
]
```
