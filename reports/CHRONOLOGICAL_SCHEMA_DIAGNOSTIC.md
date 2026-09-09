# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-74182b3044644ba4ac7f741822056a57` · model `deepseek-v4-flash` · status **incomplete**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-74182b3044644ba4ac7f741822056a57",
  "mode": "chronological_replay",
  "prompt_version": "chronological-tacit-v4",
  "prompt_sha256": "232a45ae242a55d137fa6ddc831bcdf4bcded4518527d470e7426af416cf1919",
  "sampling_version": "body-novel-reservoir-subject-cap-v1",
  "query": "Discover implicit routines and expectations",
  "model": "deepseek-v4-flash",
  "created_at": "2026-09-09T22:32:17.088923+00:00",
  "status": "incomplete",
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
      "agent_invocations": 4,
      "gate_reason": "reasoning_error_remaining_arrivals_only"
    },
    {
      "window": 6,
      "virtual_time": "2000-10-18T12:22:00+00:00",
      "arrival_sequence": 132000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 14592,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
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
    },
    {
      "window": 16,
      "virtual_time": "2001-05-30T16:14:00+00:00",
      "arrival_sequence": 352000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 11884,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 17,
      "virtual_time": "2001-07-05T06:39:00+00:00",
      "arrival_sequence": 374000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 8770,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 18,
      "virtual_time": "2001-09-14T18:31:32+00:00",
      "arrival_sequence": 396000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 4442,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 19,
      "virtual_time": "2001-10-18T16:44:49+00:00",
      "arrival_sequence": 418000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 4618,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 20,
      "virtual_time": "2001-10-31T20:55:41+00:00",
      "arrival_sequence": 440000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 6585,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 21,
      "virtual_time": "2001-11-26T10:02:03+00:00",
      "arrival_sequence": 462000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 5250,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 22,
      "virtual_time": "2002-01-09T02:37:18+00:00",
      "arrival_sequence": 484000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 4394,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 23,
      "virtual_time": "2002-02-07T05:16:01+00:00",
      "arrival_sequence": 506000,
      "admitted": 22000,
      "selected": 32,
      "duplicate_gated": 5708,
      "agent_invocations": 0,
      "gate_reason": "reasoning_disabled_after_error"
    },
    {
      "window": 24,
      "virtual_time": "2002-12-21T08:24:45+00:00",
      "arrival_sequence": 516182,
      "admitted": 10182,
      "selected": 32,
      "duplicate_gated": 1771,
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
      "window": 5,
      "phase": "observe",
      "agent": "routines",
      "error_type": "ValueError"
    }
  ],
  "quote_checks": {
    "accepted": 120,
    "rejected": 0
  },
  "replay": {
    "virtual_time": "2002-12-21T08:24:45+00:00",
    "arrived": 516182,
    "initial_arrived": 0,
    "selected": 768,
    "skipped": 515414,
    "model_calls": 36,
    "windows": 24,
    "eligible": 516182,
    "coverage_complete": true,
    "gate_reason": "reasoning_disabled_after_error",
    "retrieval_queries": 16,
    "prompt_exposed_documents": 163
  },
  "coverage_limitations": [
    "All eligible arrivals can be admitted; only sampled novel documents are shown to models.",
    "Unselected or duplicate-gated messages are not established irrelevant.",
    "Outer-header chronology and inline attribution are not authenticated human knowledge times.",
    "Quoted support and later-arrival prediction checks do not validate tacit knowledge transfer."
  ],
  "validation_rejections": {
    "citations": 0,
    "hypotheses": 4,
    "predictions": 10
  },
  "predictions": [
    {
      "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
      "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
      "prediction": "Future product description changes will involve trader input and legal will recall past compromises.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
      "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
      "prediction": "Future clearing house decisions will involve consultation with Maria or similar back-office staff.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-aa865e798bb0414e951b7e40b0f4077e",
      "hypothesis_id": "hypothesis-4e62cc9b4e4d4cad91d4d40a2cbe13e9",
      "prediction": "In future ISDA negotiations with counterparties controlling drafting, Enron will wait for counterparty drafts rather than initiate.",
      "window": 2,
      "arrival_sequence": 44000
    },
    {
      "prediction_id": "prediction-76ddcdacf948425f87ab59241c451baa",
      "hypothesis_id": "hypothesis-f75a3006cec843048b7e462282df2071",
      "prediction": "Future product description changes will involve trader input and legal will recall past compromises.",
      "window": 2,
      "arrival_sequence": 44000
    },
    {
      "prediction_id": "prediction-73f17bf7f7ca497287172fc2ee8e8681",
      "hypothesis_id": "hypothesis-463629c358b2483d9dd6d1af5ae68d78",
      "prediction": "Future access requests for new attorneys will be granted promptly without additional approval steps.",
      "window": 3,
      "arrival_sequence": 66000
    },
    {
      "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
      "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
      "prediction": "Future requests for personal days will be made to supervisors with advance notice when possible.",
      "window": 3,
      "arrival_sequence": 66000
    },
    {
      "prediction_id": "prediction-6c446f4612094b5e8529f9661cc40607",
      "hypothesis_id": "hypothesis-6b58c0603ca14670b25041fd041221a6",
      "prediction": "Future interview scheduling will involve informal suggestions of alternative interviewers from managers.",
      "window": 4,
      "arrival_sequence": 88000
    },
    {
      "prediction_id": "prediction-43d439ed1e334b41ace7213e0c0a49ba",
      "hypothesis_id": "hypothesis-9a8f2ef42f69424d9dbb9b3187bffcbb",
      "prediction": "Future process improvement ideas will be forwarded informally to managers for consideration.",
      "window": 5,
      "arrival_sequence": 110000
    },
    {
      "prediction_id": "prediction-cb611915bee84a39b2f79061786a2382",
      "hypothesis_id": "hypothesis-ef8f9e2a091841bb80d5e82a8aa14342",
      "prediction": "Future access requests for new attorneys will be granted promptly without additional approval steps.",
      "window": 5,
      "arrival_sequence": 110000
    }
  ],
  "runtime_usage": {
    "calls": 36,
    "tokens": 445790,
    "cost": 0.21455191999999998
  },
  "finished_at": "2026-09-09T22:36:30.393673+00:00",
  "ledger_delta": {
    "calls": 36,
    "tokens": 462445,
    "cost_usd": 0.2222532399999999
  },
  "ledger_delta_scope": "Shared ledger activity during run; includes concurrent users if any."
}
```

## Observation timeline

### 2000-02-18T10:05:00+00:00 — review window 1

**routines / observe**

Renato's auto-reply indicates he is out for September, delaying Brazil trading meetings. Marianne's revised Tennessee volumes show coordination with sales reps and GMS. Columbia Energy's holiday scheduling highlights early nominations and intraday adjustments. UI deal closing books and CIBC termination signing require coordination with offsite officers.

Source `mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410`; evidence `mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410:0:700:38b9c6859bdf689c`; origin `enron-authored:c235a368a02a913a39c38cb26a1ff50a8136cd34659665f20020ca123417f856`.

Attribution and exact offsets: `{"segment_id": "mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410:segment:0:726", "segment_kind": "authored", "claimed_sender": "berg@tfts.tozzini.com.br", "claimed_date": "Wed, 01 Sep 1999 15:43:00 -0700", "segment_source_family": "enron-segment:200bba917743a99eed3db610d36af4586af4543084d4a541838ce11b1820b696", "segment_fingerprint": "200bba917743a99eed3db610d36af4586af4543084d4a541838ce11b1820b696", "attribution_status": "unverified_header_claim", "document_id": "mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410", "span_id": "mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410:0:700", "start": 0, "end": 700, "quote": "Resposta autom?tica.\nEstarei fora do escrit?rio durante o ms de setembro.?Renato.??Automatic Reply:?I will be out of the office during the month of September.?Renato.???>>> \"sshackl@ect.enron.com\" 09/01/99 19:41 >>>????Although I am still waiting for another Brazilian visa, I would like to pose?several potential dates to meet with you regarding Enron North America Corp.?trading issues.  I am presently considering several time periods:??     September 9,10, 12-17,19-24??Obviously, I can be available at any time during the month of Septermber as ?well?as future months.  But I would like to get started as soon as possible.??If you could kindly e-mail or call me (713/853-5620), I can elaborate f", "quote_fingerprint": "dbdfa4983babff2a6cc96d0325092d4001d74db7a7be0fa76a8ec294630084f4", "independence_status": "not_established", "raw_sha256": "cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410", "body_sha256": "af250d7e020b6c8480031f94b45efe1fca6bb33fbb401f30bc0ab70cf3ea2fa9", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/brazil_trips/4.", "source_family": "enron-authored:c235a368a02a913a39c38cb26a1ff50a8136cd34659665f20020ca123417f856", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-cc4cc75763d9507d0335d0ea91cf8a2ba43f565802ea1e91ac9a7eaf6472b410 700"}`

> Resposta autom?tica.
> Estarei fora do escrit?rio durante o ms de setembro.?Renato.??Automatic Reply:?I will be out of the office during the month of September.?Renato.???>>> "sshackl@ect.enron.com" 09/01/99 19:41 >>>????Although I am still waiting for another Brazilian visa, I would like to pose?several potential dates to meet with you regarding Enron North America Corp.?trading issues.  I am presently considering several time periods:??     September 9,10, 12-17,19-24??Obviously, I can be available at any time during the month of Septermber as ?well?as future months.  But I would like to get started as soon as possible.??If you could kindly e-mail or call me (713/853-5620), I can elaborate f

Source `mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3`; evidence `mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3:1244:1478:22792620957c13b0`; origin `enron-authored:76b1fc3f4d89e07d9a7b4dc649d562db49fdbabdfe3816ebbd3cfcc4adac3f4d`.

Attribution and exact offsets: `{"segment_id": "mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3:segment:1244:1478", "segment_kind": "forwarded", "claimed_sender": "Marianne Stiles", "claimed_date": "12/23/99", "segment_source_family": "enron-segment:f721a0eae0b80feffef2d5c493227c67a71c3e09ce8fa82efc44e02a3c399707", "segment_fingerprint": "f721a0eae0b80feffef2d5c493227c67a71c3e09ce8fa82efc44e02a3c399707", "attribution_status": "unverified_header_claim", "document_id": "mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3", "span_id": "mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3:1244:1478", "start": 1244, "end": 1478, "quote": "\nPer the sales reps and GMS I will need the following:\n\n\n100 dth per day to meter # 020030\n596 dth per day to meter # 020028\n\nI will receive a final number for these next week but this is an estimate.\n(should not be that far off).\n\n\n\n", "quote_fingerprint": "f721a0eae0b80feffef2d5c493227c67a71c3e09ce8fa82efc44e02a3c399707", "independence_status": "not_established", "raw_sha256": "5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3", "body_sha256": "7a1e93054aa9ef7846b0b6f126fdd6f3d3194421ee20f4fcf4a939a91568ad74", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/all_documents/2606.", "source_family": "enron-authored:76b1fc3f4d89e07d9a7b4dc649d562db49fdbabdfe3816ebbd3cfcc4adac3f4d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> 
> Per the sales reps and GMS I will need the following:
> 
> 
> 100 dth per day to meter # 020030
> 596 dth per day to meter # 020028
> 
> I will receive a final number for these next week but this is an estimate.
> (should not be that far off).
> 
> 
> 
> 

Source `mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c`; evidence `mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c:0:546:4eb2d152aef2811f`; origin `enron-authored:dac3baa1b4a64e03c09d3da38f6c8454087b5c6fb63c4f2d40c30e0adb7c431d`.

Attribution and exact offsets: `{"segment_id": "mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c:segment:0:546", "segment_kind": "authored", "claimed_sender": "sgilles@columbiaenergygroup.com", "claimed_date": "Thu, 30 Dec 1999 05:52:00 -0800", "segment_source_family": "enron-segment:5c7edcf68d5fbf9c776e93303a3285fbe5eb75b98f2527d020124eb93f2c4b47", "segment_fingerprint": "5c7edcf68d5fbf9c776e93303a3285fbe5eb75b98f2527d020124eb93f2c4b47", "attribution_status": "unverified_header_claim", "document_id": "mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c", "span_id": "mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c:0:546", "start": 0, "end": 546, "quote": "Dayton Power is away from the office on Friday and Monday for the new year\nholiday.  They have requested nominations for the 1st to the 4th by 2:00 \ntoday.\n\nThe first day of January is the most critical.  I will have the ability to\nadjust any of the days from my home over the weekend on an intraday basis.\n\nI will need to work with Joann and Joni (Tco schedulers) to get the \nnominations\nin place.\n\nI'll call you, Chris, after morning trading to devise a game plan for the 1st.\n\nIf Joann works here today, I'm going to need to stay close by.\n\nsg", "quote_fingerprint": "5c7edcf68d5fbf9c776e93303a3285fbe5eb75b98f2527d020124eb93f2c4b47", "independence_status": "not_established", "raw_sha256": "3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c", "body_sha256": "b7db048cdfb72b55db99d153c269976e6d3a02d43b0ef4c7595e9d0ae31e7a93", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/germany-c/ces/358.", "source_family": "enron-authored:dac3baa1b4a64e03c09d3da38f6c8454087b5c6fb63c4f2d40c30e0adb7c431d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Dayton Power is away from the office on Friday and Monday for the new year
> holiday.  They have requested nominations for the 1st to the 4th by 2:00 
> today.
> 
> The first day of January is the most critical.  I will have the ability to
> adjust any of the days from my home over the weekend on an intraday basis.
> 
> I will need to work with Joann and Joni (Tco schedulers) to get the 
> nominations
> in place.
> 
> I'll call you, Chris, after morning trading to devise a game plan for the 1st.
> 
> If Joann works here today, I'm going to need to stay close by.
> 
> sg

**expectations / observe**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that they use only two London clearing houses, Bank Paribas and Carr, and comments on their back office quality. This exchange reveals an implicit preference for established clearers and a need for swift confirmation.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:372088e15f787ebf`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:123800b29a7b3f1e`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Tana Jones routes OMLX software request via Mark Elliott to Susan Gill, showing informal expertise referral. Mark Taylor comments on paper product descriptions, recalling past dissatisfaction with Notional Quantity language. Shirley Crenshaw announces supervisor-discretionary personal days for Research Group, an explicit policy decision.

**Candidate tacit rule — revision 1**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two forwarded segments in one email from Mark Taylor, referencing David Forster and Jennifer deBoisblanc Denny, all in one episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: Search for other product description discussions involving Bob Crane or paper/pulp to see if this is recurring.

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:11735fe3d545d11a`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:26e5522923fd9f34`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:aa5a9d63ab8a2894`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:0:363", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 19 Oct 1999 06:54:00 -0700", "segment_source_family": "enron-segment:98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "segment_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363", "start": 0, "end": 363, "quote": "I fully agree with the \"fade\" effect.  But this looks right to me.  As I \nremember it, we were not totally happy with the Notional Quantity language \nbut this was the best we could do.  We were going to make sure that whether \nthe submitted volume was per day or per month was clearly reflected elsewhere \nin the long description.  Not elegant, but adequate.\n\n\n\n\n", "quote_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**contrasts / observe**

Emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

Source `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7`; evidence `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124:1fae199b587a1fda`; origin `enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca`.

Attribution and exact offsets: `{"segment_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:segment:0:124", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 30 Nov 1999 02:16:00 -0800", "segment_source_family": "enron-segment:58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "segment_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "attribution_status": "unverified_header_claim", "document_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "span_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124", "start": 0, "end": 124, "quote": "We have an executed master agreement with Engage Energy Canada L.P. which we \nreceived signed around the end of August 1999.", "quote_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "independence_status": "not_established", "raw_sha256": "570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "body_sha256": "43ee90e776923d1c8241793276d4e6af45e0b2feb58fc0e776f03f6abd632470", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/906.", "source_family": "enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> We have an executed master agreement with Engage Energy Canada L.P. which we 
> received signed around the end of August 1999.

Source `mail-969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4`; evidence `mail-969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4:0:133:7ff57786f65e338e`; origin `enron-authored:fb75a8a6c37a5d642c7b8bff0b42307e798e60ece1d8a41a60b31e9ce484bedc`.

Attribution and exact offsets: `{"segment_id": "mail-969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4:segment:0:133", "segment_kind": "authored", "claimed_sender": "benjamin.rogers@enron.com", "claimed_date": "Fri, 14 Jan 2000 01:29:00 -0800", "segment_source_family": "enron-segment:7e5950186f7e11f378775cf8f365deceddb40aa7ed09e51b56578f157a4b9c42", "segment_fingerprint": "7e5950186f7e11f378775cf8f365deceddb40aa7ed09e51b56578f157a4b9c42", "attribution_status": "unverified_header_claim", "document_id": "mail-969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4", "span_id": "mail-969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4:0:133", "start": 0, "end": 133, "quote": "Thanks so much for that quick response.  One more favor - are you able to \npull Con Ed Annual report?  The ticker is \"ED\". Thanks\nBen", "quote_fingerprint": "7e5950186f7e11f378775cf8f365deceddb40aa7ed09e51b56578f157a4b9c42", "independence_status": "not_established", "raw_sha256": "969b7f079d6a57208346481bf47749008502240d4d1bb3d26c4e6f2e94e0b4a4", "body_sha256": "7b9acc928bdcf813958f422eb4573937ef617f3cb6a63391b75f6a1a7f6436a6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/all_documents/2026.", "source_family": "enron-authored:fb75a8a6c37a5d642c7b8bff0b42307e798e60ece1d8a41a60b31e9ce484bedc", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Thanks so much for that quick response.  One more favor - are you able to 
> pull Con Ed Annual report?  The ticker is "ED". Thanks
> Ben

Source `mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345`; evidence `mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345:0:700:339ff92f812c7b85`; origin `enron-authored:be9330a903fcc0826387c3c1c7ad060fe86a7320d52a60e5ffc8c9cca6d04e68`.

Attribution and exact offsets: `{"segment_id": "mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345:segment:0:704", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Fri, 17 Dec 1999 07:35:00 -0800", "segment_source_family": "enron-segment:320c9e6d68606e249ebfc6aa22232ef7daaf0cfb5bb48f57ee5934fefdb8befb", "segment_fingerprint": "320c9e6d68606e249ebfc6aa22232ef7daaf0cfb5bb48f57ee5934fefdb8befb", "attribution_status": "unverified_header_claim", "document_id": "mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345", "span_id": "mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345:0:700", "start": 0, "end": 700, "quote": "Hello,\n\nI shall be taking a few days off around Xmas. I shall call you at the end of \nDecember\nwhen I get back to the office.\n\nWith best holiday wishes,\n\n\nVince\n\n\n\n\n\n\"more\" <more@insync.net> on 12/01/99 09:28:09 PM\nTo: Vince J Kaminski/HOU/ECT@ECT\ncc:  \nSubject: Re: Luncheon Meeting\n\n\n\nDear Mr. Kaminski:\n\nHow are you doing? I want to find out if we can meet again for a quick lunch.\n\nYou might know that in Maharashtra, India there is now a new Chief Minister  \n(CEO of the State Government). I am proud to say that he and I are from the \nsame town, Latur.\n\nI would really enjoy talking with you again, at your convenience.\n\nI will call you tomorrow to follow up.\n\nThank you.\n\nSincerely,\n\nMaruti Mo", "quote_fingerprint": "6967b8c15212ecbd4919b8a4d4d54ea26cf8b74d83b1539b1d7f147bead5d2ea", "independence_status": "not_established", "raw_sha256": "27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345", "body_sha256": "a9d5c090e74c406be5189c9d1154c8df8468b26ef709890bc54f1f68982f95c2", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/all_documents/11081.", "source_family": "enron-authored:be9330a903fcc0826387c3c1c7ad060fe86a7320d52a60e5ffc8c9cca6d04e68", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-27f37d339350e5153b89e7ba05a89215b45349a06f4786a9a4cab555c2bfa345 700"}`

> Hello,
> 
> I shall be taking a few days off around Xmas. I shall call you at the end of 
> December
> when I get back to the office.
> 
> With best holiday wishes,
> 
> 
> Vince
> 
> 
> 
> 
> 
> "more" <more@insync.net> on 12/01/99 09:28:09 PM
> To: Vince J Kaminski/HOU/ECT@ECT
> cc:  
> Subject: Re: Luncheon Meeting
> 
> 
> 
> Dear Mr. Kaminski:
> 
> How are you doing? I want to find out if we can meet again for a quick lunch.
> 
> You might know that in Maharashtra, India there is now a new Chief Minister  
> (CEO of the State Government). I am proud to say that he and I are from the 
> same town, Latur.
> 
> I would really enjoy talking with you again, at your convenience.
> 
> I will call you tomorrow to follow up.
> 
> Thank you.
> 
> Sincerely,
> 
> Maruti Mo

**routines / revise**

Mark Taylor's email recalls past dissatisfaction with Notional Quantity language in paper product descriptions, while Jennifer Denny forwards Bob Crane's request to remove 'multiplied by the number of days' due to monthly delivery confusion. This suggests legal and trading collaborate informally on product description wording.

**Candidate tacit rule — revision 2**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from one email chain: Mark Taylor's authored reply and Jennifer Denny's forwarded message quoting Bob Crane. Single episode, no independent confirmation.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: Find other product description change requests from traders to see if this is a recurring pattern.

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:623d10e2c4ab5d7c`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a792031ea2a685e8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:0:363", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 19 Oct 1999 06:54:00 -0700", "segment_source_family": "enron-segment:98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "segment_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363", "start": 0, "end": 363, "quote": "I fully agree with the \"fade\" effect.  But this looks right to me.  As I \nremember it, we were not totally happy with the Notional Quantity language \nbut this was the best we could do.  We were going to make sure that whether \nthe submitted volume was per day or per month was clearly reflected elsewhere \nin the long description.  Not elegant, but adequate.\n\n\n\n\n", "quote_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**expectations / revise**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that they use only two London clearing houses, Bank Paribas and Carr, and comments on their back office quality. This exchange reveals an implicit preference for established clearers and a need for swift confirmation.

Source `mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16`; evidence `mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16:0:700:372088e15f787ebf`; origin `enron-authored:2baf2d4ddc744349275c89ff74394c77f114c1c120e045e43923f10a617ce42d`.

Attribution and exact offsets: `{"segment_id": "mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16:segment:0:730", "segment_kind": "authored", "claimed_sender": "mark.elliott@enron.com", "claimed_date": "Fri, 30 Apr 1999 08:24:00 -0700", "segment_source_family": "enron-segment:b1b592443744446ab8d0a6eacbd0e0265384d994ca6cef0d16ccb5dd9398dda9", "segment_fingerprint": "b1b592443744446ab8d0a6eacbd0e0265384d994ca6cef0d16ccb5dd9398dda9", "attribution_status": "unverified_header_claim", "document_id": "mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16", "span_id": "mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16:0:700", "start": 0, "end": 700, "quote": "Maria,\n\nNot necessarily - it is just that the OMLX got hold of the idea (I am not \nsure wherefrom) that Enron wanted Merrills - I have previously asked Mark \nTaylor, the VP in Legal in Houston,  whether or not Merrills would meet with \nthe commercial peoples' approval and I know that Mark has been trying to find \nthis out, but I have not received word on this as yet.\n\nMay be you can endeavour to find this out??  As I say, I have already \nforwarded to Mark Taylor in Houston the signature versions of the Clearing \nAgreements in the name of Merrills - so if we want to change, no problem, it \nwill just take a few days for us to get new docs raised from the OMLX and \nthen to pass them on to Houst", "quote_fingerprint": "452cac75058a124d848afefb3195145b589418d8891eff304633f2b6dec6d7c3", "independence_status": "not_established", "raw_sha256": "209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16", "body_sha256": "ba49aabbbe55bb88c6db4be0159d67091fc238fbd4aae1a72fed0b25f67c5562", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/260.", "source_family": "enron-authored:2baf2d4ddc744349275c89ff74394c77f114c1c120e045e43923f10a617ce42d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-209e8a9e2ad22f644d2741b5a82b293556204911a985d071b23faa3df7a8ad16 700"}`

> Maria,
> 
> Not necessarily - it is just that the OMLX got hold of the idea (I am not 
> sure wherefrom) that Enron wanted Merrills - I have previously asked Mark 
> Taylor, the VP in Legal in Houston,  whether or not Merrills would meet with 
> the commercial peoples' approval and I know that Mark has been trying to find 
> this out, but I have not received word on this as yet.
> 
> May be you can endeavour to find this out??  As I say, I have already 
> forwarded to Mark Taylor in Houston the signature versions of the Clearing 
> Agreements in the name of Merrills - so if we want to change, no problem, it 
> will just take a few days for us to get new docs raised from the OMLX and 
> then to pass them on to Houst

Source `mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8`; evidence `mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8:2695:3395:123800b29a7b3f1e`; origin `enron-authored:2baf2d4ddc744349275c89ff74394c77f114c1c120e045e43923f10a617ce42d`.

Attribution and exact offsets: `{"segment_id": "mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8:segment:2695:4903", "segment_kind": "forwarded", "claimed_sender": "Maria Nartey", "claimed_date": "29/04/99 19:22", "segment_source_family": "enron-segment:9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "segment_fingerprint": "9026ddd395520106d2d8b23e3b7371b26f905ce49adf6c87aa0ffe99c57cdc1e", "attribution_status": "unverified_header_claim", "document_id": "mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8", "span_id": "mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8:2695:3395", "start": 2695, "end": 3395, "quote": "\nJeff,\n\nWe only use two London clearing houses, Bank Paribas and Carr.  The back \noffice at Carr was not very good when I used to deal with them but I've been \ntold that they are much better now.  Paribas was definitely the better of the \ntwo from a back office point of view.\n\nLet me know if you need anything else.\nRegards,\nMaria.\n\n\n   \n\tEnron Capital & Trade Resources Corp.\n\t\n\tFrom:  Jeff Harbert                           29/04/99 18:45\n\t\n\nTo: Barry Pearce/LON/ECT@ECT\ncc: Maria Nartey/LON/ECT@ECT \nSubject: Re: Documentation from OM  \n\nHi Barry,\n\nRegarding our upcoming Pulpex \"market maker\" role, we're running into a few \nproblems with the clearing function.  I mentioned to Bob that it may m", "quote_fingerprint": "51c499740c7c037a9bb216730b3f8c2702e1c582130734489d03c76499bd2c04", "independence_status": "not_established", "raw_sha256": "78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8", "body_sha256": "ba49aabbbe55bb88c6db4be0159d67091fc238fbd4aae1a72fed0b25f67c5562", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/uk_trading/12.", "source_family": "enron-authored:2baf2d4ddc744349275c89ff74394c77f114c1c120e045e43923f10a617ce42d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-78220388b8cd8ba91a1660864b08ba8c0f8b8ed9d44bf1e5ae24469e83d412f8 3395"}`

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

Mark Elliott's OMLX clearing email reveals informal reliance on Maria Nartey's knowledge of London clearing houses, suggesting tacit expertise routing. Maria's response indicates a preference for established clearers, but this is a single episode.

**Candidate tacit rule — revision 1**

In Enron's London operations, clearing house choices are informally vetted through experienced back-office contacts like Maria Nartey, who rely on past operational quality impressions.

Inference gap: Sources show Mark Elliott asking Maria for confirmation and Maria stating their current clearers, but do not explicitly state that Maria is the go-to expert for clearing house vetting.

Evidence basis: Two emails in one thread: Mark Elliott's request and Maria Nartey's reply, both in April 1999, single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Selecting or confirming clearing houses for OMLX or similar exchange trades.

Exceptions: Unknown; may not apply to other regions or if formal clearing policies exist.

Alternative: Clearing house selection may follow formal criteria, and Maria's comments are just one opinion.

Uncertainty: Single email exchange; no evidence of repeated pattern or formal process.

Next query: Seek other emails discussing clearing house selection or operational quality to see if Maria's input is consistently sought.

Prediction: Future clearing house decisions will involve consultation with Maria or similar back-office staff.

Hypothesis `hypothesis-8c76469081d942d6950fe51636ff919b`; transfer tested: false.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:560e24281fe1a7f2`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:aaf1a1cb6d6055c2`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:372088e15f787ebf`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:123800b29a7b3f1e`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

**contrasts / revise**

Emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Candidate tacit rule — revision 3**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from one email chain: Mark Taylor's recollection of past compromise and Bob Crane's request for change, both in same episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: Find other product description changes in different commodity groups to see if trader consultation is standard.

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:c09378a6d98bd2c5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:973:1673:1a1906c55415b2ac`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:1ec913dfc687b78f`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:0:363", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 19 Oct 1999 06:54:00 -0700", "segment_source_family": "enron-segment:98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "segment_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363", "start": 0, "end": 363, "quote": "I fully agree with the \"fade\" effect.  But this looks right to me.  As I \nremember it, we were not totally happy with the Notional Quantity language \nbut this was the best we could do.  We were going to make sure that whether \nthe submitted volume was per day or per month was clearly reflected elsewhere \nin the long description.  Not elegant, but adequate.\n\n\n\n\n", "quote_fingerprint": "98be54627e8ecf0f9023d82f06f321343aa8414ddca2dbf1b93a699d16eebc68", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:836d309747b519d8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

### 2000-05-05T17:42:00+00:00 — review window 2

**routines / observe**

Carol Clair coordinates counterparty list updates and Annex A comparison for a letter, indicating a routine process where new trades are added to existing lists. Sara Shackleton notes PG&E controls drafting of Schedule, showing external party influence on contract documents.

**Observation — revision 1**

In Enron's legal documentation group, when a counterparty controls drafting, Enron's lawyers wait for their blackline and do not initiate changes, relying on the counterparty's timeline.

Inference gap: Sara states PG&E controls drafting but does not explicitly say this is a standard practice; the inference that Enron always defers is unsupported.

Evidence basis: Sara's email to Jennifer Fraser about PG&E ISDA, single episode, no complementary traces of similar behavior.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: Negotiating ISDA Schedules or similar documents where the counterparty has drafting control.

Exceptions: Unknown; may not apply if Enron has leverage or if urgency requires proactive drafting.

Alternative: Enron might prepare its own draft despite counterparty control, or the statement is specific to PG&E's regulatory context.

Uncertainty: Single email from Sara; no evidence of a general practice across other deals.

Next query: Search for other instances where Enron lawyers mention counterparty drafting control in ISDA negotiations.

Prediction: In future ISDA negotiations with counterparties controlling drafting, Enron will wait for counterparty drafts rather than initiate.

Hypothesis `hypothesis-4e62cc9b4e4d4cad91d4d40a2cbe13e9`; transfer tested: false.

Source `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3`; evidence `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3:0:538:cefbda7bb7e4649f`; origin `enron-authored:5b0a9320e008dbd86bd3074751517dc2f862053e1e89abefa8e5ea57525aed73`.

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

Source `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b`; evidence `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592:66b96369a4b19058`; origin `enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8`.

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

Source `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b`; evidence `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592:836d309747b519d8`; origin `enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8`.

Attribution and exact offsets: `{"segment_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:segment:0:592", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 23 Mar 2000 10:46:00 -0800", "segment_source_family": "enron-segment:f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "segment_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "attribution_status": "unverified_header_claim", "document_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "span_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592", "start": 0, "end": 592, "quote": "We have to respond to comments on the Credit Support Annex and a few items in \nthe Schedule..  We are waiting for copies of standing  PUC orders from PG&E \n(addressing derivatives issues) as well as a blackline of the Schedule since \nPG&E controls the drafting.  Sara\n\n\n   \n\t\n\t\n\tFrom:  Jennifer Fraser                           03/23/2000 06:32 PM\n\t\n\nTo: Sara Shackleton/HOU/ECT@ECT\ncc: Craig Breslau/HOU/ECT@ECT \nSubject: PG&E ISDA\n\nSara:\nIt appears the ball is our court. What are the outstanding issues regarding \nthe PG&E ISDA?\nOur client says he gave everything to you.\nThanks\nJennifer\n\n", "quote_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "independence_status": "not_established", "raw_sha256": "671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "body_sha256": "0287570ad7babdd0d8b1ffe1929fbed23e62dfdd8558130d97c4addd4a2bf15a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/1529.", "source_family": "enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

**expectations / observe**

Emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Candidate tacit rule — revision 4**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from one email chain: Mark Taylor's authored reply and Jennifer Denny's forwarded request from Bob Crane, both in same episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: all: product description paper pulp Bob Crane

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:1c8a6a508a1127de`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a89c535ee3d54ace`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:c9f5997f9c0009f3`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:623d10e2c4ab5d7c`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a792031ea2a685e8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**expertise / observe**

New emails show routine coordination: forwarding inspirational content, requesting presentations, and discussing gas trade assignments. No new tacit knowledge emerges from these disparate exchanges.

Source `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46`; evidence `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700:95fefa87f4820f29`; origin `enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991`.

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

Source `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796`; evidence `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796:0:342:a60847393f475973`; origin `enron-authored:789d0befb0e09d1a6294f9a12825bb472e340c2f137c576bf8d4d70910bbc492`.

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

**contrasts / observe**

Emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Candidate tacit rule — revision 5**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from one email chain: Mark Taylor's recollection (v823b29d9ffcf28fa) and Jennifer Denny forwarding Bob Crane's request (v346d384c6dcea7ac). Single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: all: product description trader input paper pulp

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals about clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  }
]
```

Source `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf`; evidence `mail-253a49933c70fe14b324da472acfdfffdba3a240fdbded74257795f402689bdf:0:447:8069f12188bbcdd4`; origin `enron-authored:425543c9c26d3e4fe8cd81fa048cc9f6a3877929e8665aa945a07df8decf3e6e`.

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

Source `mail-2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632`; evidence `mail-2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632:0:318:3102b896f303656d`; origin `enron-authored:6472193862c11941f6ff80ca9b51a6bcc42ee6d9923dcadd88d7abee0d3c655f`.

Attribution and exact offsets: `{"segment_id": "mail-2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632:segment:0:318", "segment_kind": "authored", "claimed_sender": "kristin.albrecht@enron.com", "claimed_date": "Thu, 06 Apr 2000 08:21:00 -0700", "segment_source_family": "enron-segment:dc40320f983acb5154d2ea1d3a21d8a036b7b9f801c88b9314151dd256726b02", "segment_fingerprint": "dc40320f983acb5154d2ea1d3a21d8a036b7b9f801c88b9314151dd256726b02", "attribution_status": "unverified_header_claim", "document_id": "mail-2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632", "span_id": "mail-2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632:0:318", "start": 0, "end": 318, "quote": "Sally,\nI just wanted to follow up with you on John Postlewaite's options that we \ndiscussed when we enticed him to stay here at Enron.  I asked Kim Melodick \nand Norma Villareal if they knew anything about them and they did not.  I \nknow you spoke to David Oxley about this.  Can I follow up with him?  Thanks.\nKristin", "quote_fingerprint": "dc40320f983acb5154d2ea1d3a21d8a036b7b9f801c88b9314151dd256726b02", "independence_status": "not_established", "raw_sha256": "2271122b9191a6ac11b07d65d53ed133a34334b8496bee7897c42cba4d0c1632", "body_sha256": "86a1ece40273951d35ff1fea309dd84cacd4ebfb37d987176fd53a5c9b924223", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/beck-s/melodick__kim/1.", "source_family": "enron-authored:6472193862c11941f6ff80ca9b51a6bcc42ee6d9923dcadd88d7abee0d3c655f", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Sally,
> I just wanted to follow up with you on John Postlewaite's options that we 
> discussed when we enticed him to stay here at Enron.  I asked Kim Melodick 
> and Norma Villareal if they knew anything about them and they did not.  I 
> know you spoke to David Oxley about this.  Can I follow up with him?  Thanks.
> Kristin

Source `mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302`; evidence `mail-2486aa786ee262af73a2748e12b2cd6da29eca812b52b1048e36099874ef7302:0:632:8fd2dd2a575112a4`; origin `enron-authored:837079e1e4cff149ece31ecd3c90d739b2270466435c86841539a085173ca4f0`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:623d10e2c4ab5d7c`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a792031ea2a685e8`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**routines / revise**

Carol Clair coordinates counterparty list updates and Annex A comparison for a letter, indicating a routine process where new trades are added to existing lists. Sara Shackleton notes PG&E controls drafting of Schedule, showing external party influence on contract documents.

**Observation — revision 2**

In Enron's legal documentation group, when a counterparty controls drafting, Enron's lawyers wait for their blackline and do not initiate changes, relying on the counterparty's timeline.

Inference gap: Sara states PG&E controls drafting but does not explicitly say this is a standard practice; the inference that Enron always defers is unsupported.

Evidence basis: Sara Shackleton's email to Jennifer Fraser states PG&E controls drafting, implying Enron waits for their blackline. Single episode, no other examples.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: Negotiating ISDA Schedules or similar documents where the counterparty has drafting control.

Exceptions: Unknown; may not apply if Enron has leverage or if urgency requires proactive drafting.

Alternative: Enron might prepare its own draft despite counterparty control, or the statement is specific to PG&E's regulatory context.

Uncertainty: Single email from Sara; no evidence of a general practice across other deals.

Next query: Find other ISDA negotiations where Enron initiated drafting despite counterparty control.

Prediction: In future ISDA negotiations with counterparties controlling drafting, Enron will wait for counterparty drafts rather than initiate.

Hypothesis `hypothesis-4e62cc9b4e4d4cad91d4d40a2cbe13e9`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  }
]
```

Source `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3`; evidence `mail-1ad6e09bc7d106f82d392e88340abef9b6b27fb0df6b364b857c7b732e4dc9f3:0:538:cefbda7bb7e4649f`; origin `enron-authored:5b0a9320e008dbd86bd3074751517dc2f862053e1e89abefa8e5ea57525aed73`.

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

Source `mail-16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108`; evidence `mail-16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108:0:159:387ab2abbf1965ef`; origin `enron-authored:a329d9132e093a1b6ca6d089c556be4a5fae26919d86fcc687da8e4937d0aaa8`.

Attribution and exact offsets: `{"segment_id": "mail-16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108:segment:0:159", "segment_kind": "authored", "claimed_sender": "carol.clair@enron.com", "claimed_date": "Tue, 18 Apr 2000 06:03:00 -0700", "segment_source_family": "enron-segment:161f8ee50126652cea3af8760f54fa3c2c18578cdab2f3396f47b3aa54775792", "segment_fingerprint": "161f8ee50126652cea3af8760f54fa3c2c18578cdab2f3396f47b3aa54775792", "attribution_status": "unverified_header_claim", "document_id": "mail-16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108", "span_id": "mail-16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108:0:159", "start": 0, "end": 159, "quote": "Angela:\nWe plan to send the draft ISDA to Carissa.  In the mean time, is there \nanything that needs to be discussed with respect to the Annex A letter?\nCArol  ", "quote_fingerprint": "161f8ee50126652cea3af8760f54fa3c2c18578cdab2f3396f47b3aa54775792", "independence_status": "not_established", "raw_sha256": "16ecf4e2c187ee57aa4552012dd04759f75f8a674dff2e3f8134bb6637b54108", "body_sha256": "295eca4ad82abbd5bc813fda7c937cec7c2fe3f82fb65dc7cbb9e82f40229669", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/stclair-c/sent/127.", "source_family": "enron-authored:a329d9132e093a1b6ca6d089c556be4a5fae26919d86fcc687da8e4937d0aaa8", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Angela:
> We plan to send the draft ISDA to Carissa.  In the mean time, is there 
> anything that needs to be discussed with respect to the Annex A letter?
> CArol  

Source `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b`; evidence `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592:836d309747b519d8`; origin `enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8`.

Attribution and exact offsets: `{"segment_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:segment:0:592", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 23 Mar 2000 10:46:00 -0800", "segment_source_family": "enron-segment:f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "segment_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "attribution_status": "unverified_header_claim", "document_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "span_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592", "start": 0, "end": 592, "quote": "We have to respond to comments on the Credit Support Annex and a few items in \nthe Schedule..  We are waiting for copies of standing  PUC orders from PG&E \n(addressing derivatives issues) as well as a blackline of the Schedule since \nPG&E controls the drafting.  Sara\n\n\n   \n\t\n\t\n\tFrom:  Jennifer Fraser                           03/23/2000 06:32 PM\n\t\n\nTo: Sara Shackleton/HOU/ECT@ECT\ncc: Craig Breslau/HOU/ECT@ECT \nSubject: PG&E ISDA\n\nSara:\nIt appears the ball is our court. What are the outstanding issues regarding \nthe PG&E ISDA?\nOur client says he gave everything to you.\nThanks\nJennifer\n\n", "quote_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "independence_status": "not_established", "raw_sha256": "671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "body_sha256": "0287570ad7babdd0d8b1ffe1929fbed23e62dfdd8558130d97c4addd4a2bf15a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/1529.", "source_family": "enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

**expectations / revise**

Email chain about paper product descriptions shows Mark Taylor recalling past compromise on Notional Quantity language, while Bob Crane requests removal of 'multiplied by number of days' due to monthly delivery. This suggests legal and trading collaborate informally on contract language.

**Candidate tacit rule — revision 1**

In Enron's paper/pulp trading, legal and trading collaborate informally on product description language, with legal relying on memory of past compromises and traders like Bob Crane influencing wording.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from same email chain: Mark Taylor's authored reply and forwarded message from Jennifer deBoisblanc Denny relaying Bob Crane's request. Single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups or if formal guidelines exist.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: Search for other product description discussions involving traders and legal to see if this pattern repeats.

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-f75a3006cec843048b7e462282df2071`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals after prediction to test trader involvement in product description changes.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals after prediction to test clearing house consultation pattern.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  }
]
```

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:bfebdf959ebaf445`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:688b50c928dd88fc`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:1c8a6a508a1127de`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a89c535ee3d54ace`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**expertise / revise**

New emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Candidate tacit rule — revision 6**

In Enron's paper/pulp trading, product description language is negotiated with traders like Bob Crane, and legal relies on informal memory of past compromises.

Inference gap: Sources show Mark Taylor's recollection and Bob Crane's request but do not state a standing rule for consulting traders on all descriptions.

Evidence basis: Two segments from one email chain: Mark Taylor's authored reply and forwarded Jennifer deBoisblanc Denny message quoting Bob Crane. Single episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Drafting or revising long descriptions for paper/pulp product types in trading agreements.

Exceptions: Unknown; may not apply to other commodity groups.

Alternative: Legal may have formal guidelines for all product descriptions, and Bob Crane's input is only one-off.

Uncertainty: Single email chain; no evidence of repeated pattern or formal process.

Next query: Search for other product description changes in paper/pulp to see if trader consultation is consistent.

Prediction: Future product description changes will involve trader input and legal will recall past compromises.

Hypothesis `hypothesis-661169a273884af2a956ea414887817a`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader consultation.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-05-05T17:42:00+00:00",
    "arrival_sequence": 44000
  }
]
```

Source `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46`; evidence `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700:95fefa87f4820f29`; origin `enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991`.

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

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:dacfe721ca7be5d3`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

Source `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796`; evidence `mail-2fb9194d137cfcb6f75b7f75dc0e394d116d402e7b620ba564265c004809e796:0:342:a60847393f475973`; origin `enron-authored:789d0befb0e09d1a6294f9a12825bb472e340c2f137c576bf8d4d70910bbc492`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:0:363:1c8a6a508a1127de`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

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

Source `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a`; evidence `mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597:a89c535ee3d54ace`; origin `enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b`.

Attribution and exact offsets: `{"segment_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:segment:2060:2615", "segment_kind": "forwarded", "claimed_sender": "Jennifer deBoisblanc Denny", "claimed_date": "19/10/99 16:03", "segment_source_family": "enron-segment:10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "segment_fingerprint": "10eac2a5638d88692bfd53d73a5173fae48c8abc86b3102a440e30311df99091", "attribution_status": "unverified_header_claim", "document_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "span_id": "mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a:2060:2597", "start": 2060, "end": 2597, "quote": "\n\nDave,\nThe first long product type description below defines a paper product. In all \npaper/pulp products, with the exception of the second one below, \nthe description uses the words \"volume submitted multiplied by the number of \ndays\".\nBob Crane of Paper / Pulp Trading, said this confusing due to the commodity \nis monthly delivey. He would like the words \"multiplied by the number of \ndays\" removed from the long descriptions of the paper/pulp product types. \nShould we delete the whole sentence possibly? (See second desription belo", "quote_fingerprint": "77391c044f97e9e879435189298c42a6c01893a13224d669b9bde461d5ac1a89", "independence_status": "not_established", "raw_sha256": "627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a", "body_sha256": "2e3df3a0546f9dd8034082bd12965ef6349cfa797e04f3211ae5d14a1b8e438e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/551.", "source_family": "enron-authored:d36f18ed47b2c8bbfca620f6581c42671da5e0e1a908271e0a42d9b9a03cbe7b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-627822101d693c0d7a62deadca909030987a166d1d7e2452301118009188203a 2597"}`

> 
> 
> Dave,
> The first long product type description below defines a paper product. In all 
> paper/pulp products, with the exception of the second one below, 
> the description uses the words "volume submitted multiplied by the number of 
> days".
> Bob Crane of Paper / Pulp Trading, said this confusing due to the commodity 
> is monthly delivey. He would like the words "multiplied by the number of 
> days" removed from the long descriptions of the paper/pulp product types. 
> Should we delete the whole sentence possibly? (See second desription belo

**contrasts / revise**

New email announces Research Group gets two personal days per year at supervisor discretion, per Vince's decision. This is explicit policy, not tacit. Other emails show routine coordination but no new tacit rules.

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9c355b06d9d92f8f`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

### 2000-06-30T20:55:00+00:00 — review window 3

**routines / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 1**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting access for Mary Cook; no other emails show the outcome or process.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: all: database access approval process

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address paper product description changes.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals about clearing house decisions.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:ae5e5c00d61dbe33`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177`; evidence `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266:dc4582293e0e8cf2`; origin `enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e`.

Attribution and exact offsets: `{"segment_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:segment:0:266", "segment_kind": "authored", "claimed_sender": "clement.lau@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:22:00 -0700", "segment_source_family": "enron-segment:3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "segment_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "attribution_status": "unverified_header_claim", "document_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "span_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266", "start": 0, "end": 266, "quote": "I have saved the first info memo (generic version, w/o mentioned of Orion) \nunder \"EGC12-Generic-051100\" and various site pictures and maps under \n\"Pictures\" folder, both in o:/_dropbox.\n\nI will continue transfering file to the o:_dropbox over the next few days.\n\n  ", "quote_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "independence_status": "not_established", "raw_sha256": "27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "body_sha256": "21a1b7ec9a36c79908e6474294f323c67e3aae49b1e218fdaf244a9816cb2b3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/genco_jv_ipo/437.", "source_family": "enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I have saved the first info memo (generic version, w/o mentioned of Orion) 
> under "EGC12-Generic-051100" and various site pictures and maps under 
> "Pictures" folder, both in o:/_dropbox.
> 
> I will continue transfering file to the o:_dropbox over the next few days.
> 
>   

Source `mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35`; evidence `mail-2a791176db9a3dda24a4f8c3fe0fb047ece08adc959d48b89898241d3c8fab35:0:700:15505919d601f62f`; origin `enron-authored:65e7e9472635370bc4ea7e4f151503152a5f1d199728dd32d836f64e1c1f44b5`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:836d309747b519d8`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**expectations / observe**

New emails show scheduling, data reporting, and routine coordination. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 1**

In Enron's Research group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw announcing Vince's decision; no other episodes observed.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: Search for other mentions of personal days or time-off policies in Enron emails.

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals about clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:9beece743ad8ecf3`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

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

Source `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69`; evidence `mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100:ee4307f02b6f5e79`; origin `enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10`.

Attribution and exact offsets: `{"segment_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:segment:0:100", "segment_kind": "authored", "claimed_sender": "david.delainey@enron.com", "claimed_date": "Thu, 29 Jun 2000 03:04:00 -0700", "segment_source_family": "enron-segment:3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "segment_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "attribution_status": "unverified_header_claim", "document_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "span_id": "mail-47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69:0:100", "start": 0, "end": 100, "quote": "Nella, sorry to see you go; however, best of luck in all your future \nendeavours.\n\nRegards\nDelainey\n", "quote_fingerprint": "3ec19e2ee49c4cda8e826d649a0350ac6743524e1832367c060ff1033f9c7eaf", "independence_status": "not_established", "raw_sha256": "47e648ef51e7be9cf023ef4421495958b08f2f139ab27e74f7d459d4026cca69", "body_sha256": "b32d061cee56a113ba341f453b605ca474cc052559df0ac2cd74a5d98f3b60c1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/delainey-d/sent/544.", "source_family": "enron-authored:6fafb7dbcdcab606ac839898da0a6ee19d7f139558e0a63345e8c81b93d43e10", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Nella, sorry to see you go; however, best of luck in all your future 
> endeavours.
> 
> Regards
> Delainey
> 

Source `mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd`; evidence `mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34:3329efc0bde7e301`; origin `enron-authored:0c6e00823bed3980c9cf5751e38ffc3cf0bdd88ad913f32c3921c8d7d7976e91`.

Attribution and exact offsets: `{"segment_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:segment:0:34", "segment_kind": "authored", "claimed_sender": "richard.sanders@enron.com", "claimed_date": "Wed, 14 Jun 2000 04:26:00 -0700", "segment_source_family": "enron-span:mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34", "segment_fingerprint": "01c3d4bad923312343526298157055ca71a2ca680bf43a4c748e892d5518f45e", "attribution_status": "unverified_header_claim", "document_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd", "span_id": "mail-6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd:0:34", "start": 0, "end": 34, "quote": "Call Steve Howard with info. Thx.\n", "quote_fingerprint": "01c3d4bad923312343526298157055ca71a2ca680bf43a4c748e892d5518f45e", "independence_status": "not_established", "raw_sha256": "6555b4f861f959740275eb8e621857a495b07c2b47df7c7f19a32800fb97ffbd", "body_sha256": "72751c00d32b4a0912c1c16aaf8698e71431ab5cf92dddf0c07ef18eb3306df6", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/sanders-r/sent/130.", "source_family": "enron-authored:0c6e00823bed3980c9cf5751e38ffc3cf0bdd88ad913f32c3921c8d7d7976e91", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Call Steve Howard with info. Thx.
> 

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9c355b06d9d92f8f`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

**expertise / observe**

New emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

Source `mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b`; evidence `mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b:0:700:ac781ba3e0a00dee`; origin `enron-authored:61f99e26974b63d6d912bec898e54076383666721d2192f034378bdd6008f131`.

Attribution and exact offsets: `{"segment_id": "mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b:segment:0:720", "segment_kind": "authored", "claimed_sender": "project.team@enron.com", "claimed_date": "Tue, 27 Jun 2000 04:23:00 -0700", "segment_source_family": "enron-segment:189edb8792a858931cc123e160f933009bc0102164dd8d7eeef378a0d6f23fff", "segment_fingerprint": "189edb8792a858931cc123e160f933009bc0102164dd8d7eeef378a0d6f23fff", "attribution_status": "unverified_header_claim", "document_id": "mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b", "span_id": "mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b:0:700", "start": 0, "end": 700, "quote": "As you are probably aware, your department has been selected to participate \nin Project GEM (Global Enron Migration) for the rollout of Windows 2000.  In \npreparation for this rollout, it is imperative that we gather information \nabout your workstation and the applications you use.  To begin this data \ncollection, we have automated the process and your system has just been \ninventoried.   Once this information is received, we will be working with \nyour department coordinator to consolidate this information to ensure this \ntransition is as smooth as possible.\n\nThe GEM team would like to thank you for your participation.  If you have any \nquestions, please call Steve Dubaniewicz Deployment Man", "quote_fingerprint": "7ee7b4430f56f4804532035a96cdcd692b26c29c7257751bf9f0b65edf0b2bff", "independence_status": "not_established", "raw_sha256": "22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b", "body_sha256": "143e93834cb867b4cda55e57671a1e9f952e9df566b45f87c050d25dc74aef55", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/hain-m/discussion_threads/31.", "source_family": "enron-authored:61f99e26974b63d6d912bec898e54076383666721d2192f034378bdd6008f131", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-22ad622dafe5300ceb193a3b6bed807801f5951cd32afd660b51a2819ec2936b 700"}`

> As you are probably aware, your department has been selected to participate 
> in Project GEM (Global Enron Migration) for the rollout of Windows 2000.  In 
> preparation for this rollout, it is imperative that we gather information 
> about your workstation and the applications you use.  To begin this data 
> collection, we have automated the process and your system has just been 
> inventoried.   Once this information is received, we will be working with 
> your department coordinator to consolidate this information to ensure this 
> transition is as smooth as possible.
> 
> The GEM team would like to thank you for your participation.  If you have any 
> questions, please call Steve Dubaniewicz Deployment Man

Source `mail-380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca`; evidence `mail-380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca:0:375:f48d71d3e6126ced`; origin `enron-authored:45308ee7727dc0578f456eee8f4cd5f476a056c741e9a41c8198b1d9d1dc26e1`.

Attribution and exact offsets: `{"segment_id": "mail-380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca:segment:0:375", "segment_kind": "authored", "claimed_sender": "peter.keavey@enron.com", "claimed_date": "Thu, 25 May 2000 03:06:00 -0700", "segment_source_family": "enron-segment:f7a280c688dd1b5a5e0bef29ab0122f60ea6cfcca09af5ed82ca63929c3bd343", "segment_fingerprint": "f7a280c688dd1b5a5e0bef29ab0122f60ea6cfcca09af5ed82ca63929c3bd343", "attribution_status": "unverified_header_claim", "document_id": "mail-380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca", "span_id": "mail-380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca:0:375", "start": 0, "end": 375, "quote": "Louise,\n\nThose numbers are impressive without a doubt.  The success has had the \nunfortunate consequence of showing the limits of our current internet \ntechnology.  The delays in messages from the stacks to the website have \ngotten worse in recent weeks.  This is only anecdotal evidence but as a \ntrader on the system it has been very frustrating.  \n\n\nRegards, \n\nPete Keavey", "quote_fingerprint": "f7a280c688dd1b5a5e0bef29ab0122f60ea6cfcca09af5ed82ca63929c3bd343", "independence_status": "not_established", "raw_sha256": "380379dcf0a3e7dc1cbdcd994f25e9b2236691a369d9d7c0690108d0619996ca", "body_sha256": "3d67e40fccacc22dbd954756ee6eb9881edbcdd1029360886c56c6ae8a1b8d34", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/keavey-p/_sent_mail/51.", "source_family": "enron-authored:45308ee7727dc0578f456eee8f4cd5f476a056c741e9a41c8198b1d9d1dc26e1", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Louise,
> 
> Those numbers are impressive without a doubt.  The success has had the 
> unfortunate consequence of showing the limits of our current internet 
> technology.  The delays in messages from the stacks to the website have 
> gotten worse in recent weeks.  This is only anecdotal evidence but as a 
> trader on the system it has been very frustrating.  
> 
> 
> Regards, 
> 
> Pete Keavey

Source `mail-33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349`; evidence `mail-33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349:0:217:7e0312fec7eeeaa2`; origin `enron-authored:4445b562ef5fff39f563fa4c26705c06de55dcfdb33edd2d139ee1c642043252`.

Attribution and exact offsets: `{"segment_id": "mail-33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349:segment:0:217", "segment_kind": "authored", "claimed_sender": "karen.lambert@enron.com", "claimed_date": "Wed, 14 Jun 2000 10:06:00 -0700", "segment_source_family": "enron-segment:4605ec7b888bef292b914f65d0725c62b3e73688e21cf30d2c4242fa748c4cb3", "segment_fingerprint": "4605ec7b888bef292b914f65d0725c62b3e73688e21cf30d2c4242fa748c4cb3", "attribution_status": "unverified_header_claim", "document_id": "mail-33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349", "span_id": "mail-33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349:0:217", "start": 0, "end": 217, "quote": "I will attend the offsite Global Conference on Thursday and Friday, June \n15-16, 2000.   If you require assistance with an urgent EOL-related contracts \nmatter during that time, then you may page me at (713) 707-6571.", "quote_fingerprint": "4605ec7b888bef292b914f65d0725c62b3e73688e21cf30d2c4242fa748c4cb3", "independence_status": "not_established", "raw_sha256": "33acd78e23516133c3087022438d87adf0f1e4b9360073c40aba12a43b6ab349", "body_sha256": "18e514a40d50518280dbba898f716aa8eaadf34511cef480f940e51a699f977b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2126.", "source_family": "enron-authored:4445b562ef5fff39f563fa4c26705c06de55dcfdb33edd2d139ee1c642043252", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I will attend the offsite Global Conference on Thursday and Friday, June 
> 15-16, 2000.   If you require assistance with an urgent EOL-related contracts 
> matter during that time, then you may page me at (713) 707-6571.

**contrasts / observe**

New emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 3**

In Enron's legal documentation group, when a counterparty controls drafting, Enron's lawyers wait for their blackline and do not initiate changes, relying on the counterparty's timeline.

Inference gap: Sara states PG&E controls drafting but does not explicitly say this is a standard practice; the inference that Enron always defers is unsupported.

Evidence basis: Single email from Sara Shackleton to Jennifer Fraser about PG&E ISDA, where Sara notes PG&E controls drafting. No other episodes show similar deferral.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: Negotiating ISDA Schedules or similar documents where the counterparty has drafting control.

Exceptions: Unknown; may not apply if Enron has leverage or if urgency requires proactive drafting.

Alternative: Enron might prepare its own draft despite counterparty control, or the statement is specific to PG&E's regulatory context.

Uncertainty: Single email from Sara; no evidence of a general practice across other deals.

Next query: all: ISDA Schedule drafting control counterparty

Prediction: In future ISDA negotiations with counterparties controlling drafting, Enron will wait for counterparty drafts rather than initiate.

Hypothesis `hypothesis-4e62cc9b4e4d4cad91d4d40a2cbe13e9`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-4e62cc9b4e4d4cad91d4d40a2cbe13e9",
    "prediction_id": "prediction-aa865e798bb0414e951b7e40b0f4077e",
    "prediction_arrival_sequence": 44000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test this prediction.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:c09378a6d98bd2c5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc`; evidence `mail-3f31d3f42a60a1b4a083fecdeda013b84173235c740ff16ce611b9fb0c385cbc:0:397:b6815be1350e40cb`; origin `enron-authored:6f580c4f40f2a03c7ee044f389b2140f633e0c5a7367aca49b24de6eadaacfd1`.

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

Source `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b`; evidence `mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592:836d309747b519d8`; origin `enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8`.

Attribution and exact offsets: `{"segment_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:segment:0:592", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 23 Mar 2000 10:46:00 -0800", "segment_source_family": "enron-segment:f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "segment_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "attribution_status": "unverified_header_claim", "document_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "span_id": "mail-671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b:0:592", "start": 0, "end": 592, "quote": "We have to respond to comments on the Credit Support Annex and a few items in \nthe Schedule..  We are waiting for copies of standing  PUC orders from PG&E \n(addressing derivatives issues) as well as a blackline of the Schedule since \nPG&E controls the drafting.  Sara\n\n\n   \n\t\n\t\n\tFrom:  Jennifer Fraser                           03/23/2000 06:32 PM\n\t\n\nTo: Sara Shackleton/HOU/ECT@ECT\ncc: Craig Breslau/HOU/ECT@ECT \nSubject: PG&E ISDA\n\nSara:\nIt appears the ball is our court. What are the outstanding issues regarding \nthe PG&E ISDA?\nOur client says he gave everything to you.\nThanks\nJennifer\n\n", "quote_fingerprint": "f0bf1ec4520b20f4f2009df93f771301ebfec04ea90e821da84bbf9f00dbc13f", "independence_status": "not_established", "raw_sha256": "671b888187d8b5b7e0ea3ffa44e9c1e72437fb11fdd871dbb4bd083085ab236b", "body_sha256": "0287570ad7babdd0d8b1ffe1929fbed23e62dfdd8558130d97c4addd4a2bf15a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/1529.", "source_family": "enron-authored:8a5cec733d5dc1bf57f5c5a67d0c0a0d602df0878a485bc8848b12a3291b7eb8", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

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

**routines / revise**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 2**

In Enron's Research Group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw to Research Group, stating Vince's decision and requesting advance notice for scheduled personal days.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: personal days supervisor discretion Research Group

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:ab6452bf3cc0c1e5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9c355b06d9d92f8f`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

**expectations / revise**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 2**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting access for Mary Cook; no other access requests or approvals visible.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: Search for other database access requests to see if they follow a similar pattern or require approvals.

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:9beece743ad8ecf3`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

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

Source `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46`; evidence `mail-230615e09b8a00dcce01a0ead320bb1bb441e24391c352c2e819aef7d1d31a46:0:700:2af176b6ac79ba7c`; origin `enron-authored:adddfad5b69c476d95414f88459ec7d840a0b8d2fd461f464e8c8566de260991`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:e9e22e6c37a4c775`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:836d309747b519d8`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**expertise / revise**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 3**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting access for Mary Cook; no other access requests in this batch.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: Search for other database access requests to see if they follow a similar pattern or require approvals.

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:79c805318c0a78a3`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177`; evidence `mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266:e3cfa28c4069148e`; origin `enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e`.

Attribution and exact offsets: `{"segment_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:segment:0:266", "segment_kind": "authored", "claimed_sender": "clement.lau@enron.com", "claimed_date": "Tue, 20 Jun 2000 04:22:00 -0700", "segment_source_family": "enron-segment:3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "segment_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "attribution_status": "unverified_header_claim", "document_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "span_id": "mail-27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177:0:266", "start": 0, "end": 266, "quote": "I have saved the first info memo (generic version, w/o mentioned of Orion) \nunder \"EGC12-Generic-051100\" and various site pictures and maps under \n\"Pictures\" folder, both in o:/_dropbox.\n\nI will continue transfering file to the o:_dropbox over the next few days.\n\n  ", "quote_fingerprint": "3f16c9a19172df194fcfdc45c1d212399de68c4a22f8db64f0f37c6863b386be", "independence_status": "not_established", "raw_sha256": "27580d9bd2c2827c530963010c5a91ef74232538dd56da03ca8137420f46a177", "body_sha256": "21a1b7ec9a36c79908e6474294f323c67e3aae49b1e218fdaf244a9816cb2b3b", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/rogers-b/genco_jv_ipo/437.", "source_family": "enron-authored:02f1abe4920dd717ee1344d1ed61c79efa95f9202327c5cca6385197a6aad89e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I have saved the first info memo (generic version, w/o mentioned of Orion) 
> under "EGC12-Generic-051100" and various site pictures and maps under 
> "Pictures" folder, both in o:/_dropbox.
> 
> I will continue transfering file to the o:_dropbox over the next few days.
> 
>   

Source `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920`; evidence `mail-2cb44cfd7f1f426d745290d621cea343298ae954d14620a78466533e22985920:0:700:e12c6291c7bc6e3a`; origin `enron-authored:8de56654b9931e173661475f7bb624552ab62023cae2c46a94deb3ac3188c436`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:836d309747b519d8`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**contrasts / revise**

New emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 3**

In Enron's Research Group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw announcing the policy; no other emails in this batch show actual requests or usage.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: Search for other emails about personal days or time-off requests in Research Group to see if advance notice is consistently required.

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals about clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-06-30T20:55:00+00:00",
    "arrival_sequence": 66000
  }
]
```

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:c09378a6d98bd2c5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:fc345db86410f36a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9c355b06d9d92f8f`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

### 2000-08-16T14:45:00+00:00 — review window 4

**routines / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-661169a273884af2a956ea414887817a",
    "prediction_id": "prediction-fd1cff98aa0b491c9bbb67be5025eac7",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address product description changes or trader input.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  },
  {
    "hypothesis_id": "hypothesis-8c76469081d942d6950fe51636ff919b",
    "prediction_id": "prediction-827cda098a1f444b8f8a1de9d444d13b",
    "prediction_arrival_sequence": 22000,
    "status": "unresolved",
    "explanation": "No new arrivals mention clearing house decisions or consultation with Maria.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011:e079c4d1e46b1477`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

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

Source `mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e`; evidence `mail-3d8749bd2794b5f3ae714cb95f98ab9e3ae8935d0f8aec0a0e7b8b82e773dd8e:0:700:e8183e51c0f17dd4`; origin `enron-authored:d69e95096f83afe3e94c26b62d7374c17ac836169083b2c684abb08fba0f5c3b`.

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

Source `mail-6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc`; evidence `mail-6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc:0:364:86eaf771bb44d5a4`; origin `enron-authored:b2cb02b42fd9cb098596280b06671a2cb6d4662b14cae6a77b175aa5e23c4f26`.

Attribution and exact offsets: `{"segment_id": "mail-6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc:segment:0:364", "segment_kind": "authored", "claimed_sender": "dmitchel@cwt.com", "claimed_date": "Mon, 14 Aug 2000 02:33:00 -0700", "segment_source_family": "enron-segment:3051a73811449a1a9d0b571b3d400151ea7d8c9038a899c3b64db814897b1de8", "segment_fingerprint": "3051a73811449a1a9d0b571b3d400151ea7d8c9038a899c3b64db814897b1de8", "attribution_status": "unverified_header_claim", "document_id": "mail-6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc", "span_id": "mail-6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc:0:364", "start": 0, "end": 364, "quote": "I can't promise this morning, but we will have it this afternoon.  Take\ncare.\n\n\n\n\n\"Sara Shackleton\" <Sara.Shackleton@enron.com> on 08/14/2000 09:26:43 AM\n\nTo:   dmitchel@cwt.com\ncc:\nSubject:  equity confirm\n\n\n\n\nGood morning David!\n     Just hoping that you could have the confirm sent this morning.  I need\nto\nreview with the commercial guys.  Thanks.  Sara\n\n\n\n\n\n\n", "quote_fingerprint": "3051a73811449a1a9d0b571b3d400151ea7d8c9038a899c3b64db814897b1de8", "independence_status": "not_established", "raw_sha256": "6cc020b2771ce30d6d61b7c113e1bac3b688d9eefb377ff1f6c6bbfeb720d3bc", "body_sha256": "7c27d0489083b5f01f72eca19cd59e741d1a62b7394a8637f8ad970228b5c7db", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/notes_inbox/1418.", "source_family": "enron-authored:b2cb02b42fd9cb098596280b06671a2cb6d4662b14cae6a77b175aa5e23c4f26", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I can't promise this morning, but we will have it this afternoon.  Take
> care.
> 
> 
> 
> 
> "Sara Shackleton" <Sara.Shackleton@enron.com> on 08/14/2000 09:26:43 AM
> 
> To:   dmitchel@cwt.com
> cc:
> Subject:  equity confirm
> 
> 
> 
> 
> Good morning David!
>      Just hoping that you could have the confirm sent this morning.  I need
> to
> review with the commercial guys.  Thanks.  Sara
> 
> 
> 
> 
> 
> 
> 

**expectations / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 4**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting full access for new attorney Mary Cook; no other episodes or explicit policy.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: all: database access approval process

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-463629c358b2483d9dd6d1af5ae68d78",
    "prediction_id": "prediction-73f17bf7f7ca497287172fc2ee8e8681",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address database access requests for new attorneys.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  },
  {
    "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
    "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address personal day requests or supervisor notification.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d`; evidence `mail-136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d:0:153:9b6891dc5240b8fc`; origin `enron-authored:7d634981690203165dade41e5fa454acd5573398eca311feb3096e3e3de0994d`.

Attribution and exact offsets: `{"segment_id": "mail-136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d:segment:0:153", "segment_kind": "authored", "claimed_sender": "lisa.costello@enron.com", "claimed_date": "Wed, 26 Jul 2000 09:13:00 -0700", "segment_source_family": "enron-segment:e92e06c60b65d478d9a861a413ef1863222341f56f3d25a6d618be948d6c08a3", "segment_fingerprint": "e92e06c60b65d478d9a861a413ef1863222341f56f3d25a6d618be948d6c08a3", "attribution_status": "unverified_header_claim", "document_id": "mail-136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d", "span_id": "mail-136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d:0:153", "start": 0, "end": 153, "quote": "Attached please find an updated list of Mr. Horton's Direct Reports and \nAssistants.  Please forward any changes to me via lotus notes.\n\nThank you,\nLisa\n", "quote_fingerprint": "e92e06c60b65d478d9a861a413ef1863222341f56f3d25a6d618be948d6c08a3", "independence_status": "not_established", "raw_sha256": "136ced0903c47c54080e31f7edd774934cb5641c95fc5d700c4c1d1f01c7689d", "body_sha256": "7fa12df9558a3226ed3b5eb21da09366470cac198826dd714b3f26d7feaf56a5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/hayslett-r/discussion_threads/128.", "source_family": "enron-authored:7d634981690203165dade41e5fa454acd5573398eca311feb3096e3e3de0994d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Attached please find an updated list of Mr. Horton's Direct Reports and 
> Assistants.  Please forward any changes to me via lotus notes.
> 
> Thank you,
> Lisa
> 

Source `mail-9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610`; evidence `mail-9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610:0:492:73c656a560322118`; origin `enron-authored:da9e68bc2054fc02bb7c3c73608c39b29a0f2a01a038cbab24e68a51ce23cae7`.

Attribution and exact offsets: `{"segment_id": "mail-9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610:segment:0:492", "segment_kind": "authored", "claimed_sender": "michelle.cash@enron.com", "claimed_date": "Thu, 10 Aug 2000 16:24:00 -0700", "segment_source_family": "enron-segment:a7b9bee3cb691a846e09bb8f558e332209dc8f31110db301008beeb9dda47f34", "segment_fingerprint": "a7b9bee3cb691a846e09bb8f558e332209dc8f31110db301008beeb9dda47f34", "attribution_status": "unverified_header_claim", "document_id": "mail-9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610", "span_id": "mail-9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610:0:492", "start": 0, "end": 492, "quote": "Thanks for handling that!  We are looking forward to our trip.  I'll call you \nwhen we get in and let you know our details.  I look forward to seeing you, \nMary Lou, and Peter, if available.  See you soon!  Michelle\n\n\n\n\n\"Bensfield, James\" <jbensfield@milchev.com> on 08/10/2000 04:11:22 PM\nTo: Michelle Cash/HOU/ECT@ECT\ncc:  \nSubject: Orioles\n\n\n\n\n Michelle: The tickets went out FedEx today.  If they don't show up\nat the appropriate time tomorrow, give me a call and we'll track them down.\n\n", "quote_fingerprint": "a7b9bee3cb691a846e09bb8f558e332209dc8f31110db301008beeb9dda47f34", "independence_status": "not_established", "raw_sha256": "9d19e476f0ef8c422b9add8daee92ac1ecd1ed06331362625e8ec84f399d4610", "body_sha256": "f7dd458e4df6548df344403af98e55819e38a0c51b7a80fbd66a5ed83106a68f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/cash-m/sent/312.", "source_family": "enron-authored:da9e68bc2054fc02bb7c3c73608c39b29a0f2a01a038cbab24e68a51ce23cae7", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Thanks for handling that!  We are looking forward to our trip.  I'll call you 
> when we get in and let you know our details.  I look forward to seeing you, 
> Mary Lou, and Peter, if available.  See you soon!  Michelle
> 
> 
> 
> 
> "Bensfield, James" <jbensfield@milchev.com> on 08/10/2000 04:11:22 PM
> To: Michelle Cash/HOU/ECT@ECT
> cc:  
> Subject: Orioles
> 
> 
> 
> 
>  Michelle: The tickets went out FedEx today.  If they don't show up
> at the appropriate time tomorrow, give me a call and we'll track them down.
> 
> 

Source `mail-5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5`; evidence `mail-5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5:0:165:9b83b55f091ffa9f`; origin `enron-authored:eb7d49e140b3a57bdf6fa94b6db12ef526e4f5d905a34d5033e17841052b5363`.

Attribution and exact offsets: `{"segment_id": "mail-5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5:segment:0:165", "segment_kind": "authored", "claimed_sender": "richard.sanders@enron.com", "claimed_date": "Sat, 05 Aug 2000 08:26:00 -0700", "segment_source_family": "enron-segment:84409960485ad70761c3f1d18873f764359ccb6e820b4058e6aa40d47e0a3dc0", "segment_fingerprint": "84409960485ad70761c3f1d18873f764359ccb6e820b4058e6aa40d47e0a3dc0", "attribution_status": "unverified_header_claim", "document_id": "mail-5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5", "span_id": "mail-5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5:0:165", "start": 0, "end": 165, "quote": "I have not heard anything about it since I spoke with you last month. My \nguess is Mark is not focused on this search. Don't do anything. I will keep \nyou posted\n\n\n\n", "quote_fingerprint": "84409960485ad70761c3f1d18873f764359ccb6e820b4058e6aa40d47e0a3dc0", "independence_status": "not_established", "raw_sha256": "5cba57935abc2d0e64b0483fcc0d7630fd941b6946a063c9c01cf4a9e45fddc5", "body_sha256": "3b0bdf8ef3a9acac5694fcc24b1979d6a2e0078383148e2a2783cf4883386b27", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/sanders-r/all_documents/378.", "source_family": "enron-authored:eb7d49e140b3a57bdf6fa94b6db12ef526e4f5d905a34d5033e17841052b5363", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I have not heard anything about it since I spoke with you last month. My 
> guess is Mark is not focused on this search. Don't do anything. I will keep 
> you posted
> 
> 
> 
> 

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:fc345db86410f36a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**expertise / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Candidate tacit rule — revision 1**

In Enron's trading groups, informal referrals to specific individuals (e.g., David Port, Bjorn Hagelman) are used to fill interview slots when preferred candidates are unavailable.

Inference gap: The email shows Vince suggesting alternatives but does not state a rule for how interviewers are chosen or that informal referrals are standard.

Evidence basis: Single episode: Vince's email to Sean about replacing Ted Murphy, with forwarded context showing scheduling difficulties.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Scheduling interviews for candidates when originally requested interviewers are unavailable.

Exceptions: Unknown; may not apply if formal HR processes override.

Alternative: The suggestion may be a one-off based on availability, not a standing practice.

Uncertainty: Single email chain; no evidence of repeated pattern across other scheduling contexts.

Next query: Search for other interview scheduling emails to see if similar informal referrals occur.

Prediction: Future interview scheduling will involve informal suggestions of alternative interviewers from managers.

Hypothesis `hypothesis-6b58c0603ca14670b25041fd041221a6`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-463629c358b2483d9dd6d1af5ae68d78",
    "prediction_id": "prediction-73f17bf7f7ca497287172fc2ee8e8681",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address database access requests for new attorneys.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  },
  {
    "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
    "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address personal day requests or supervisor notifications.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1`; evidence `mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1:0:24:c32244f064d4ad41`; origin `enron-authored:ffe1e353c36489484da8209e0af06a1b9e7797c38dcd1e2f1fc7ddc36cfc4d0e`.

Attribution and exact offsets: `{"segment_id": "mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1:segment:0:24", "segment_kind": "authored", "claimed_sender": "richard.sanders@enron.com", "claimed_date": "Tue, 25 Jul 2000 08:59:00 -0700", "segment_source_family": "enron-span:mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1:0:24", "segment_fingerprint": "ffec1142978c8f5487a991e82632375d29650c830b9a18f7fa878c142a8658cb", "attribution_status": "unverified_header_claim", "document_id": "mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1", "span_id": "mail-95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1:0:24", "start": 0, "end": 24, "quote": "He is taken care of.\n\n\n\n", "quote_fingerprint": "ffec1142978c8f5487a991e82632375d29650c830b9a18f7fa878c142a8658cb", "independence_status": "not_established", "raw_sha256": "95febc159f8280495b1330195edc57433c2eb1de340c04772e180de36ed688e1", "body_sha256": "26cdaf9f4bc2419d47fb93d82e13844120a94c7e7c0053e1ccffde2b62419fc1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/sanders-r/sent/194.", "source_family": "enron-authored:ffe1e353c36489484da8209e0af06a1b9e7797c38dcd1e2f1fc7ddc36cfc4d0e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> He is taken care of.
> 
> 
> 
> 

Source `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61`; evidence `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79:75e842317a54d197`; origin `enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f`.

Attribution and exact offsets: `{"segment_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:segment:0:79", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Wed, 26 Jul 2000 01:19:00 -0700", "segment_source_family": "enron-span:mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79", "segment_fingerprint": "39476e6ea626db0767906f98396e9dcfc4b1b6da85982d6f528ddf8853477ac3", "attribution_status": "unverified_header_claim", "document_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "span_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79", "start": 0, "end": 79, "quote": "Sean,\n\nThanks. I appreciate it. Try David Port or Bjorn Hagelman.\n\nVince\n\n\n\n\n\n\n", "quote_fingerprint": "39476e6ea626db0767906f98396e9dcfc4b1b6da85982d6f528ddf8853477ac3", "independence_status": "not_established", "raw_sha256": "35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "body_sha256": "aefdc9626e21504f830d707579c56f2703b398aa23c872da131c7fc66f0f437f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/2341.", "source_family": "enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Sean,
> 
> Thanks. I appreciate it. Try David Port or Bjorn Hagelman.
> 
> Vince
> 
> 
> 
> 
> 
> 
> 

Source `mail-1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142`; evidence `mail-1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142:0:184:aa6774f3a019c151`; origin `enron-authored:36f9df4c5aa8caaa9c66ba18ed165bad1e5eb42e5385716e4080e1f7a8978ae6`.

Attribution and exact offsets: `{"segment_id": "mail-1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142:segment:0:184", "segment_kind": "authored", "claimed_sender": "john.lavorato@enron.com", "claimed_date": "Thu, 27 Jul 2000 07:02:00 -0700", "segment_source_family": "enron-segment:5f6d401b4888bbaf7635e3b147db70195bd3e51ffa008ac396b8300bedde0732", "segment_fingerprint": "5f6d401b4888bbaf7635e3b147db70195bd3e51ffa008ac396b8300bedde0732", "attribution_status": "unverified_header_claim", "document_id": "mail-1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142", "span_id": "mail-1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142:0:184", "start": 0, "end": 184, "quote": "Ed\n\nThis stuff looks good.\n\nWhy don't you combine all your stuff, maybe include the org chart also and \nsee if we can get a 3 or 4 page report.  Send it to me and I'll run if by \nDave.", "quote_fingerprint": "5f6d401b4888bbaf7635e3b147db70195bd3e51ffa008ac396b8300bedde0732", "independence_status": "not_established", "raw_sha256": "1ba0236a3c54a7e8f31e3cca73f3b2a0d05d67a80348e3d7eb10c66dcce3e142", "body_sha256": "5a9c6241d877cc32456605acb5cc28c1685531b0510df1bbf1c174e7223a108d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/lavorato-j/all_documents/300.", "source_family": "enron-authored:36f9df4c5aa8caaa9c66ba18ed165bad1e5eb42e5385716e4080e1f7a8978ae6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Ed
> 
> This stuff looks good.
> 
> Why don't you combine all your stuff, maybe include the org chart also and 
> see if we can get a 3 or 4 page report.  Send it to me and I'll run if by 
> Dave.

Source `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61`; evidence `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79:836d309747b519d8`; origin `enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f`.

Attribution and exact offsets: `{"segment_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:segment:0:79", "segment_kind": "authored", "claimed_sender": "vince.kaminski@enron.com", "claimed_date": "Wed, 26 Jul 2000 01:19:00 -0700", "segment_source_family": "enron-span:mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79", "segment_fingerprint": "39476e6ea626db0767906f98396e9dcfc4b1b6da85982d6f528ddf8853477ac3", "attribution_status": "unverified_header_claim", "document_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "span_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:0:79", "start": 0, "end": 79, "quote": "Sean,\n\nThanks. I appreciate it. Try David Port or Bjorn Hagelman.\n\nVince\n\n\n\n\n\n\n", "quote_fingerprint": "39476e6ea626db0767906f98396e9dcfc4b1b6da85982d6f528ddf8853477ac3", "independence_status": "not_established", "raw_sha256": "35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "body_sha256": "aefdc9626e21504f830d707579c56f2703b398aa23c872da131c7fc66f0f437f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/2341.", "source_family": "enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Sean,
> 
> Thanks. I appreciate it. Try David Port or Bjorn Hagelman.
> 
> Vince
> 
> 
> 
> 
> 
> 
> 

Source `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61`; evidence `mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:205:358:836d309747b519d8`; origin `enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f`.

Attribution and exact offsets: `{"segment_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:segment:205:358", "segment_kind": "forwarded", "claimed_sender": "Sean Grady@ENRON", "claimed_date": "07/25/2000 03:51 PM", "segment_source_family": "enron-segment:04d7c88f45b5947bc24fe6007ebd414cc218479f5491ba4207bd0e89dae0dca4", "segment_fingerprint": "04d7c88f45b5947bc24fe6007ebd414cc218479f5491ba4207bd0e89dae0dca4", "attribution_status": "unverified_header_claim", "document_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "span_id": "mail-35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61:205:358", "start": 205, "end": 358, "quote": "\nI scheduled Bill Bradford for Bruce James but was unable to schedule Ted \nMurphy.  Is there anybody that could replace Mr. Murphy as an interviewer?\n\n\n\n", "quote_fingerprint": "04d7c88f45b5947bc24fe6007ebd414cc218479f5491ba4207bd0e89dae0dca4", "independence_status": "not_established", "raw_sha256": "35e31d9791988f633da33ab10eeb3b1d35f1e8c3e6793699381c98f48dc0ce61", "body_sha256": "aefdc9626e21504f830d707579c56f2703b398aa23c872da131c7fc66f0f437f", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kaminski-v/_sent_mail/2341.", "source_family": "enron-authored:91fe445833cadce7fa7750d26e76b11f43a97bf6ff0c70db254c4e4ae093a90f", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> 
> I scheduled Bill Bradford for Bruce James but was unable to schedule Ted 
> Murphy.  Is there anybody that could replace Mr. Murphy as an interviewer?
> 
> 
> 
> 

**contrasts / observe**

New emails show routine coordination: forwarding attachments, requesting reports, and scheduling meetings. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 4**

In Enron's Research Group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw to Research Group, stating Vince's decision on personal days.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: all: personal days supervisor discretion

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

Source `mail-3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e`; evidence `mail-3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e:0:219:00a53fc36f2679b1`; origin `enron-authored:ac1a469592cb01f7a10d1f4823d2e9a65c0c0d195d53e944b027594c530b7855`.

Attribution and exact offsets: `{"segment_id": "mail-3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e:segment:0:219", "segment_kind": "authored", "claimed_sender": "eric.thode@enron.com", "claimed_date": "Thu, 06 Jul 2000 02:28:00 -0700", "segment_source_family": "enron-segment:11554df17c86472ee704d22cff64ad28bd56b95e0666a83c40d15b319dfca1ce", "segment_fingerprint": "11554df17c86472ee704d22cff64ad28bd56b95e0666a83c40d15b319dfca1ce", "attribution_status": "unverified_header_claim", "document_id": "mail-3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e", "span_id": "mail-3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e:0:219", "start": 0, "end": 219, "quote": "Attached is the final version of the EnronOnline/Metals press release.  It is \nset for release today.  If you have any last minute changes, please get them \nto me ASAP via e-mail or phone at ext. 3-9053.  Thanks.\n\nEric\n", "quote_fingerprint": "11554df17c86472ee704d22cff64ad28bd56b95e0666a83c40d15b319dfca1ce", "independence_status": "not_established", "raw_sha256": "3150412436a659c68e0f0dedb5b257f127e69cb70bb0eb1b6f744bff5d54660e", "body_sha256": "3ae32fd769fe750739848b18e242d0ab92b3492791d99f02b58e8c06a59d96ee", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/2513.", "source_family": "enron-authored:ac1a469592cb01f7a10d1f4823d2e9a65c0c0d195d53e944b027594c530b7855", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Attached is the final version of the EnronOnline/Metals press release.  It is 
> set for release today.  If you have any last minute changes, please get them 
> to me ASAP via e-mail or phone at ext. 3-9053.  Thanks.
> 
> Eric
> 

Source `mail-2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992`; evidence `mail-2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992:0:109:d361c6ad20bf9325`; origin `enron-authored:6e0cf077e58a52910bec09b0f0c8d50ace6b6ac721aeaf4ee5a4fbb80c2e7f05`.

Attribution and exact offsets: `{"segment_id": "mail-2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992:segment:0:109", "segment_kind": "authored", "claimed_sender": "deb.korkmas@enron.com", "claimed_date": "Fri, 21 Jul 2000 03:00:00 -0700", "segment_source_family": "enron-segment:1e854395eeb5e1840ea204b90558c6d357b1a07062a5724603f568d78b654169", "segment_fingerprint": "1e854395eeb5e1840ea204b90558c6d357b1a07062a5724603f568d78b654169", "attribution_status": "unverified_header_claim", "document_id": "mail-2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992", "span_id": "mail-2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992:0:109", "start": 0, "end": 109, "quote": "Tana, my list shows he is with RAC (Corp) so I did not elect him to ENA.  Is \nhe supposed to be ENA?  Deb\n\n\n\n", "quote_fingerprint": "1e854395eeb5e1840ea204b90558c6d357b1a07062a5724603f568d78b654169", "independence_status": "not_established", "raw_sha256": "2b6897048e02d1120509da8820539c29aafb3ba37cd22aa56c390965a9c56992", "body_sha256": "f3894cf650a2261d2f817549a08ef1febafe7fe8b8af823721394947c600f82d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/notes_inbox/1018.", "source_family": "enron-authored:6e0cf077e58a52910bec09b0f0c8d50ace6b6ac721aeaf4ee5a4fbb80c2e7f05", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Tana, my list shows he is with RAC (Corp) so I did not elect him to ENA.  Is 
> he supposed to be ENA?  Deb
> 
> 
> 
> 

Source `mail-32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad`; evidence `mail-32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad:0:202:922f5ff2100a06a0`; origin `enron-authored:bb6fd5fc5f895cda121edbf5d5f289d89199ba79c9cbf23352034eebc8408a49`.

Attribution and exact offsets: `{"segment_id": "mail-32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad:segment:0:202", "segment_kind": "authored", "claimed_sender": "tera.moss@enron.com", "claimed_date": "Thu, 13 Jul 2000 01:39:00 -0700", "segment_source_family": "enron-segment:08cea3b5e19daf304b48844af3435d1e9c0c4cd6c00772b9950b325ced0234de", "segment_fingerprint": "08cea3b5e19daf304b48844af3435d1e9c0c4cd6c00772b9950b325ced0234de", "attribution_status": "unverified_header_claim", "document_id": "mail-32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad", "span_id": "mail-32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad:0:202", "start": 0, "end": 202, "quote": "Please plan to attend a meeting to discuss the supply of gas to Ponderosa \nPine Energy (Cornhusker) on July 13 from 3:00 to 4:00 in conference room \n30C1. Call John Griffith @ ext. 36247 with questions.", "quote_fingerprint": "08cea3b5e19daf304b48844af3435d1e9c0c4cd6c00772b9950b325ced0234de", "independence_status": "not_established", "raw_sha256": "32464eb26aec6fc3fbb88d36f332833b0da60d3a4e0b77b3b64b336ab88651ad", "body_sha256": "35e767bf0d3bf5d4805918d288054d4e92ae465acdfceda3c1f8f074e7d29df1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/farmer-d/discussion_threads/1660.", "source_family": "enron-authored:bb6fd5fc5f895cda121edbf5d5f289d89199ba79c9cbf23352034eebc8408a49", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Please plan to attend a meeting to discuss the supply of gas to Ponderosa 
> Pine Energy (Cornhusker) on July 13 from 3:00 to 4:00 in conference room 
> 30C1. Call John Griffith @ ext. 36247 with questions.

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:ab6452bf3cc0c1e5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

**routines / revise**

New email shows Enron lobbyist Chris Long reporting successful opposition to CFTC amendment and upcoming House/Senate actions. No new tacit rule emerges; this is explicit legislative update.

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:311:1011:956f5ce3f304fecf`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

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

Source `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb`; evidence `mail-206e8f6f00c06b4fd4136235b9fe87bae0b959492b9efdb7c9382372685bfafb:1011:1292:0076952d251bd2f6`; origin `enron-authored:62401e2c4bf34884049f44ea7d2bcadaec420d07c890fb954ce2282822504ef6`.

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

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 5**

In Enron's Research Group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw to Research Group, announcing Vince's decision; no follow-up or other episodes.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: personal days request approval process supervisor

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
    "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test the prediction about personal day requests.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:6db49ff06de6f556`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:ab6452bf3cc0c1e5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

**expertise / revise**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 5**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting access for Mary Cook; no other related emails in this batch.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: all: database access approval process

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-463629c358b2483d9dd6d1af5ae68d78",
    "prediction_id": "prediction-73f17bf7f7ca497287172fc2ee8e8681",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address database access for new attorneys; prediction remains untested.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  },
  {
    "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
    "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly address personal day requests; prediction remains untested.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:79c805318c0a78a3`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:3065286d3dfeb1df`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:fc345db86410f36a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**contrasts / revise**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 6**

In Enron's Research Group, personal days are granted at supervisor discretion, but employees are expected to notify in advance when possible.

Inference gap: The email states the policy but does not explicitly say how employees should request or whether advance notice is always required.

Evidence basis: Single email from Shirley Crenshaw to Research Group, stating Vince's decision; no other episodes.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: An employee needs time off for personal business not covered by vacation or sick leave.

Exceptions: Unknown; may not apply if supervisor denies or if emergency prevents advance notice.

Alternative: Personal days might be formally tracked and require HR approval despite the email.

Uncertainty: Single email from Shirley; no evidence of how consistently this is applied across groups.

Next query: all: personal days supervisor discretion

Prediction: Future requests for personal days will be made to supervisors with advance notice when possible.

Hypothesis `hypothesis-21ada4b4c2d0418680efd8522c343f2e`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-21ada4b4c2d0418680efd8522c343f2e",
    "prediction_id": "prediction-ffc12ebe2d32479dbd9504bc9d14783d",
    "prediction_arrival_sequence": 66000,
    "status": "unresolved",
    "explanation": "No new arrivals directly test the prediction about personal day requests.",
    "evidence": [],
    "virtual_time": "2000-08-16T14:45:00+00:00",
    "arrival_sequence": 88000
  }
]
```

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9c355b06d9d92f8f`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:ab6452bf3cc0c1e5`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

### 2000-09-19T15:13:00+00:00 — review window 5

**expectations / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 1**

In Enron's legal/HR functions, process improvements like RIF selection are initiated informally by senior staff forwarding ideas, not through formal channels.

Inference gap: The email shows Michelle forwarding Pat's idea but does not state a rule for how process improvements are typically initiated.

Evidence basis: Single episode involving Michelle Cash, Pat Mackin, and Brian; no complementary traces of similar initiatives.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: When an employee identifies a need for a standardized process in HR or legal operations.

Exceptions: Unknown; may not apply if formal project management exists.

Alternative: The forwarding may be a one-off request, not a standing practice.

Uncertainty: Single email chain; no evidence of repeated pattern.

Next query: all: RIF selection process Willrich

Prediction: Future process improvement ideas will be forwarded informally to managers for consideration.

Hypothesis `hypothesis-9a8f2ef42f69424d9dbb9b3187bffcbb`; transfer tested: false.

Source `mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5`; evidence `mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:0:351:725be7848efd2328`; origin `enron-authored:65ef5233e04b56c6dba6c660b8f9dd273f97917e6ec90388a1ddb679ba0fcb0e`.

Attribution and exact offsets: `{"segment_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:segment:0:351", "segment_kind": "authored", "claimed_sender": "michelle.cash@enron.com", "claimed_date": "Tue, 29 Aug 2000 06:20:00 -0700", "segment_source_family": "enron-segment:558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "segment_fingerprint": "558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "attribution_status": "unverified_header_claim", "document_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5", "span_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:0:351", "start": 0, "end": 351, "quote": "Brian, \n\nPat Mackin requested that I forward this on to you.   I think he has a good \nidea here to look at a process for RIF selection.  Currently, it is done on \nan ad-hoc basis, with plans being prepared for each situation.  \n\nPat, do you still have a copy of the one you prepared a while back?  It would \nbe an excellent start.\n\nThanks.\n\nMichelle\n\n", "quote_fingerprint": "558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "independence_status": "not_established", "raw_sha256": "a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5", "body_sha256": "f6b0544e5375b8adbd6a3b737f1c263f52b1f5f987357b8fd7178ebef7ef9c79", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/cash-m/all_documents/418.", "source_family": "enron-authored:65ef5233e04b56c6dba6c660b8f9dd273f97917e6ec90388a1ddb679ba0fcb0e", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Brian, 
> 
> Pat Mackin requested that I forward this on to you.   I think he has a good 
> idea here to look at a process for RIF selection.  Currently, it is done on 
> an ad-hoc basis, with plans being prepared for each situation.  
> 
> Pat, do you still have a copy of the one you prepared a while back?  It would 
> be an excellent start.
> 
> Thanks.
> 
> Michelle
> 
> 

Source `mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb`; evidence `mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb:434:1134:d75175266cdce6ab`; origin `enron-authored:107521f08341c54ee231a1f6b74eceae5d39cdd16b6c22fd8bc557de935ad55d`.

Attribution and exact offsets: `{"segment_id": "mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb:segment:434:1710", "segment_kind": "forwarded", "claimed_sender": "Jeff Dasovich", "claimed_date": "09/08/2000 06:44 PM", "segment_source_family": "enron-segment:e62eb286dc49a27b01ab92b687aa24ee28880bea715c5abe9afe84bfc9299c8e", "segment_fingerprint": "e62eb286dc49a27b01ab92b687aa24ee28880bea715c5abe9afe84bfc9299c8e", "attribution_status": "unverified_header_claim", "document_id": "mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb", "span_id": "mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb:434:1134", "start": 434, "end": 1134, "quote": "\nJohn/Gia:\n\nYou asked that we attempt to evaluate our activities.  Working with TW, I've \nvalued this one.\n\nThe California Commission ruled that the \"Hector Road\" natural gas recent \npoint in California ought to be made a primary receipt point.  This would \nhave had the effect of TW losing access right to 200 MMcf/d of capacity at \nSoCalGas' Needles receipt point.\n\nBest case scenario:  Under SFV rates, loss to TW is commodity rates (wash) \nand the fuel margin.  TW calculates the fuel margin to be $5.8MM/yr.\n\nBad case:  If shippers on TW try to make the case that TW is at fault for \nlosing the primary access rights, then TW is at risk for the demand component \nof the contracts associated with", "quote_fingerprint": "8ef2308c7300d641b8d9d918d5afcc8ce9c0699682ae081535eef1542878ed7c", "independence_status": "not_established", "raw_sha256": "0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb", "body_sha256": "e9f10e97e5f7312277a3041f8c713cf63502d57cd307cb789854eed42d81de3a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/dasovich-j/sent/297.", "source_family": "enron-authored:107521f08341c54ee231a1f6b74eceae5d39cdd16b6c22fd8bc557de935ad55d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-0b1b7f3275c95795c162f08a121cdd4cb47cbc1eb9de7a6c2548ada9e4d4d4cb 1134"}`

> 
> John/Gia:
> 
> You asked that we attempt to evaluate our activities.  Working with TW, I've 
> valued this one.
> 
> The California Commission ruled that the "Hector Road" natural gas recent 
> point in California ought to be made a primary receipt point.  This would 
> have had the effect of TW losing access right to 200 MMcf/d of capacity at 
> SoCalGas' Needles receipt point.
> 
> Best case scenario:  Under SFV rates, loss to TW is commodity rates (wash) 
> and the fuel margin.  TW calculates the fuel margin to be $5.8MM/yr.
> 
> Bad case:  If shippers on TW try to make the case that TW is at fault for 
> losing the primary access rights, then TW is at risk for the demand component 
> of the contracts associated with

Source `mail-105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239`; evidence `mail-105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239:277:774:e7edfa30f5935064`; origin `enron-authored:9abb3711bc6b2926542caee125431c9f33802d0436c769ddb1f45f8d474476f4`.

Attribution and exact offsets: `{"segment_id": "mail-105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239:segment:277:774", "segment_kind": "forwarded", "claimed_sender": "Heather Kroll@ECT", "claimed_date": "09/12/2000 10:44 AM", "segment_source_family": "enron-segment:d1a9de751fb2f82898d71ea39462359405d4937b7633c1ec8f695ce1fa3cc74e", "segment_fingerprint": "d1a9de751fb2f82898d71ea39462359405d4937b7633c1ec8f695ce1fa3cc74e", "attribution_status": "unverified_header_claim", "document_id": "mail-105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239", "span_id": "mail-105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239:277:774", "start": 277, "end": 774, "quote": "\nBen,\n\nI spoke with the VA Power contact today who is responsible for the \ninterconnection agreement.  His name is Wayne Duman (804.257.4096, \nWayne_Duman@dom.com).  \n\nHe suggested e-mailing him dates when Enron was available to go to Richmond \nto discuss the interconnect.  I don't know if you want to go or if you plan \non sending one of the developers, but will you schedule this meeting (since I \nwon't be negotiating this part of it).\n\nThanks.  Let me know if you have any problems.\n\nHeather\n", "quote_fingerprint": "d1a9de751fb2f82898d71ea39462359405d4937b7633c1ec8f695ce1fa3cc74e", "independence_status": "not_established", "raw_sha256": "105b414dbccab0cea6f3c31d56b26cfd9824399008af09a313e66d90cae3a239", "body_sha256": "e5df4a26e5e46504596eb09a6764281537958438eefba317a17ed0e02d0d2a5c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/_sent_mail/3557.", "source_family": "enron-authored:9abb3711bc6b2926542caee125431c9f33802d0436c769ddb1f45f8d474476f4", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> 
> Ben,
> 
> I spoke with the VA Power contact today who is responsible for the 
> interconnection agreement.  His name is Wayne Duman (804.257.4096, 
> Wayne_Duman@dom.com).  
> 
> He suggested e-mailing him dates when Enron was available to go to Richmond 
> to discuss the interconnect.  I don't know if you want to go or if you plan 
> on sending one of the developers, but will you schedule this meeting (since I 
> won't be negotiating this part of it).
> 
> Thanks.  Let me know if you have any problems.
> 
> Heather
> 

Source `mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5`; evidence `mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:0:351:836d309747b519d8`; origin `enron-authored:65ef5233e04b56c6dba6c660b8f9dd273f97917e6ec90388a1ddb679ba0fcb0e`.

Attribution and exact offsets: `{"segment_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:segment:0:351", "segment_kind": "authored", "claimed_sender": "michelle.cash@enron.com", "claimed_date": "Tue, 29 Aug 2000 06:20:00 -0700", "segment_source_family": "enron-segment:558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "segment_fingerprint": "558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "attribution_status": "unverified_header_claim", "document_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5", "span_id": "mail-a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5:0:351", "start": 0, "end": 351, "quote": "Brian, \n\nPat Mackin requested that I forward this on to you.   I think he has a good \nidea here to look at a process for RIF selection.  Currently, it is done on \nan ad-hoc basis, with plans being prepared for each situation.  \n\nPat, do you still have a copy of the one you prepared a while back?  It would \nbe an excellent start.\n\nThanks.\n\nMichelle\n\n", "quote_fingerprint": "558cd8b54640ba15c0bf745e5b18f83e449cd1c4b3d20730ed2e9aa5cc9ad25c", "independence_status": "not_established", "raw_sha256": "a603a4d447435d7cfd1fdeacb14edb617546c801874b0536f4137981c631e6c5", "body_sha256": "f6b0544e5375b8adbd6a3b737f1c263f52b1f5f987357b8fd7178ebef7ef9c79", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/cash-m/all_documents/418.", "source_family": "enron-authored:65ef5233e04b56c6dba6c660b8f9dd273f97917e6ec90388a1ddb679ba0fcb0e", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Brian, 
> 
> Pat Mackin requested that I forward this on to you.   I think he has a good 
> idea here to look at a process for RIF selection.  Currently, it is done on 
> an ad-hoc basis, with plans being prepared for each situation.  
> 
> Pat, do you still have a copy of the one you prepared a while back?  It would 
> be an excellent start.
> 
> Thanks.
> 
> Michelle
> 
> 

**expertise / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 6**

In Enron's legal group, new attorneys are granted database access upon request without formal approval, relying on the requester's authority.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting full access for Mary Cook, showing a direct request without mention of approval steps.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and a colleague requests access to a shared database.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email; no evidence of a formal process or exceptions.

Next query: Search for other access request emails to see if they mention approval or are granted directly.

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-463629c358b2483d9dd6d1af5ae68d78`; transfer tested: false.

Source `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd`; evidence `mail-1804ad07f424a03f81d34fd9f8ecd9d6951b8f8ee7f98fd3061753bb1a4291cd:0:700:8335d3abb85a5f54`; origin `enron-authored:3a272a9087b13cb3b961842df6b967041118e47887c85632d553b7475a1e77c1`.

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

Source `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692`; evidence `mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:0:31:937608d2f1210038`; origin `enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c`.

Attribution and exact offsets: `{"segment_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:segment:0:31", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 24 Aug 2000 03:05:00 -0700", "segment_source_family": "enron-span:mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:0:31", "segment_fingerprint": "43bf31c5b27d04d4fa38770fed598d595b485d1ec0d98ad2f9b156891f698a4c", "attribution_status": "unverified_header_claim", "document_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "span_id": "mail-57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692:0:31", "start": 0, "end": 31, "quote": "Call me when you have a chance\n", "quote_fingerprint": "43bf31c5b27d04d4fa38770fed598d595b485d1ec0d98ad2f9b156891f698a4c", "independence_status": "not_established", "raw_sha256": "57dfaac9984ed95573466972a9a57baca08d23aca014ad514f6e1e67104e0692", "body_sha256": "392a48d2e75d5616da3a338a125149bc944ba3d319f16519ea5fa1aadb4db9a1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/notes_inbox/1278.", "source_family": "enron-authored:c99845acd58275bf87f80e4a1fa1472b6fcb2fa63945688f7d1e30c20dd6a78c", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Call me when you have a chance
> 

Source `mail-27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63`; evidence `mail-27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63:0:108:8c9c552fd494b55f`; origin `enron-authored:302e58799274cd93438dfb5a75485c6aaeaf88903d443090f945eaaf5e911cd0`.

Attribution and exact offsets: `{"segment_id": "mail-27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63:segment:0:108", "segment_kind": "authored", "claimed_sender": "kay.mann@enron.com", "claimed_date": "Tue, 12 Sep 2000 03:52:00 -0700", "segment_source_family": "enron-segment:8429c4c08be28e474ea7efbc25c28c8f3bbf3abcd382a11425addff4ff8106bc", "segment_fingerprint": "8429c4c08be28e474ea7efbc25c28c8f3bbf3abcd382a11425addff4ff8106bc", "attribution_status": "unverified_header_claim", "document_id": "mail-27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63", "span_id": "mail-27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63:0:108", "start": 0, "end": 108, "quote": "Please add Lisa Bills, Chris Herron and Mitch Robinson.  You have Lisa's info \non the GE list.\n\nThanks,\n\nKay", "quote_fingerprint": "8429c4c08be28e474ea7efbc25c28c8f3bbf3abcd382a11425addff4ff8106bc", "independence_status": "not_established", "raw_sha256": "27900e33a4efd64302c092aca0fcc46ff315cbcd74227d51abce16948ebc9a63", "body_sha256": "9e140806d87c7e56cdf566dc011329e2823eff4576aaacf7014f2f4a606abf50", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/mann-k/_sent_mail/3556.", "source_family": "enron-authored:302e58799274cd93438dfb5a75485c6aaeaf88903d443090f945eaaf5e911cd0", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Please add Lisa Bills, Chris Herron and Mitch Robinson.  You have Lisa's info 
> on the GE list.
> 
> Thanks,
> 
> Kay

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:fc345db86410f36a`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

**contrasts / observe**

New emails show routine coordination: database access requests, file transfers, and meeting scheduling. No clear tacit rule emerges from these disparate exchanges.

**Observation — revision 1**

In Enron's legal group, when a new attorney joins, colleagues request database access directly from IT contact without formal approval, expecting prompt grant.

Inference gap: The email requests access but does not state the approval process or whether such requests are routinely granted without further checks.

Evidence basis: Single email from Tana Jones to Mike requesting full access for new attorney Mary Cook; no other episodes observed.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A new attorney joins and needs access to shared legal databases.

Exceptions: Unknown; may require manager approval for sensitive databases.

Alternative: Access requests might need formal approval from IT or database administrators.

Uncertainty: Single email from Tana Jones; no evidence of a formal process or exceptions.

Next query: Search for other database access requests to see if they follow a similar informal pattern.

Prediction: Future access requests for new attorneys will be granted promptly without additional approval steps.

Hypothesis `hypothesis-ef8f9e2a091841bb80d5e82a8aa14342`; transfer tested: false.

Source `mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024`; evidence `mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:0:192:33d01506a79e4720`; origin `enron-authored:1784c6113af7fad88f6dd1260062d49823fc555919b6e1e8897a87f638cf9659`.

Attribution and exact offsets: `{"segment_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:segment:0:192", "segment_kind": "authored", "claimed_sender": "brant.reves@enron.com", "claimed_date": "Fri, 08 Sep 2000 07:50:00 -0700", "segment_source_family": "enron-segment:57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "segment_fingerprint": "57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "attribution_status": "unverified_header_claim", "document_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024", "span_id": "mail-561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024:0:192", "start": 0, "end": 192, "quote": "After reviewing new information i am comforatable amending the existing \nMaster Agreement's credit line from $2.25MM to $3.00.\n\nLet me know if I can be of any futher assistance.\n\nthanks\nbrant\n", "quote_fingerprint": "57415c23dcb785f8f07379ab975d08812ae5d3e79ba4dbf4e5c8b1647bfe54e8", "independence_status": "not_established", "raw_sha256": "561bd133233c56d8def1dc80b462f30e5da007edcb7e590089aa0169dd758024", "body_sha256": "eb9cd68df2d3da1085d6e2cd89f5c82c9bd2e6100e376d472a63b3829fa6d3e2", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/notes_inbox/1575.", "source_family": "enron-authored:1784c6113af7fad88f6dd1260062d49823fc555919b6e1e8897a87f638cf9659", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> After reviewing new information i am comforatable amending the existing 
> Master Agreement's credit line from $2.25MM to $3.00.
> 
> Let me know if I can be of any futher assistance.
> 
> thanks
> brant
> 

Source `mail-7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b`; evidence `mail-7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b:0:286:7ce7811828bd8852`; origin `enron-authored:e291928833624a9c21d32d466d78db27e48a02e31efaa8295d1a2b54dbe7afc5`.

Attribution and exact offsets: `{"segment_id": "mail-7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b:segment:0:286", "segment_kind": "authored", "claimed_sender": "chris.dorland@enron.com", "claimed_date": "Wed, 23 Aug 2000 00:50:00 -0700", "segment_source_family": "enron-segment:f6e88b7964ae405d5f53600c1fd68e214f4d5ad09fc51d2bfbd43c9a7146a642", "segment_fingerprint": "f6e88b7964ae405d5f53600c1fd68e214f4d5ad09fc51d2bfbd43c9a7146a642", "attribution_status": "unverified_header_claim", "document_id": "mail-7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b", "span_id": "mail-7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b:0:286", "start": 0, "end": 286, "quote": "Tricia,\n\nI want to exercise some Enron stock options but don't know who I should call. \nDo you have a name and/or phone number of someone? I also don't know what \ninformation I need to have in order to exercise. Could you give me a call \n(x6910) and help me out. \n\nThanx,\n\nChris Dorland", "quote_fingerprint": "f6e88b7964ae405d5f53600c1fd68e214f4d5ad09fc51d2bfbd43c9a7146a642", "independence_status": "not_established", "raw_sha256": "7f703562f2aa4c842728f912bfa07c4e86c35b64ccf0ef52dc0014d59612752b", "body_sha256": "269e0e947c43719a91ecb5f44a464b281dc98410031d86c6d3399659c2069aab", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/dorland-c/discussion_threads/182.", "source_family": "enron-authored:e291928833624a9c21d32d466d78db27e48a02e31efaa8295d1a2b54dbe7afc5", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Tricia,
> 
> I want to exercise some Enron stock options but don't know who I should call. 
> Do you have a name and/or phone number of someone? I also don't know what 
> information I need to have in order to exercise. Could you give me a call 
> (x6910) and help me out. 
> 
> Thanx,
> 
> Chris Dorland

Source `mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b`; evidence `mail-540f7a651c9967c838e0edac8da21053ca1238b0c460b4935483a4a65915540b:281:454:cc5ff96d73049a30`; origin `enron-authored:981f4642ef9e1014847536a39507724e46ad80141c0190d0b6f95fa137aebfc4`.

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

Source `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876`; evidence `mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180:79c805318c0a78a3`; origin `enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22`.

Attribution and exact offsets: `{"segment_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:segment:0:180", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 27 Jun 2000 03:13:00 -0700", "segment_source_family": "enron-segment:4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "segment_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "attribution_status": "unverified_header_claim", "document_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "span_id": "mail-1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876:0:180", "start": 0, "end": 180, "quote": "Mike,\n\nMary Cook is a new attorney that joined our Group yesterday.  Can you get her \nfull access to the referenced database, and let us know when such access is \ngranted.\n\nThanks!", "quote_fingerprint": "4cbbfbc2bf810c3606b199d79b9c13f81a32ae2e54d07b64c23fe120c2296ef4", "independence_status": "not_established", "raw_sha256": "1a040e8329455c6b01526678a9db571469967195b82ce77941d66db163611876", "body_sha256": "9b7bcfc86d7551f997c55db36548dc48cb240921ed67422d44d2d0b820e45186", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/2328.", "source_family": "enron-authored:ff7fcc52c29174123a6c473472cb7537c6f04115b83eb69006e03ca7fcab3e22", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mike,
> 
> Mary Cook is a new attorney that joined our Group yesterday.  Can you get her 
> full access to the referenced database, and let us know when such access is 
> granted.
> 
> Thanks!

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:32:39.867940+00:00",
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
  "created_at": "2026-09-09T22:33:00.890100+00:00",
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
  "created_at": "2026-09-09T22:33:23.165954+00:00",
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
  "created_at": "2026-09-09T22:33:45.199160+00:00",
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
  "created_at": "2026-09-09T22:34:01.124633+00:00",
  "window": 5,
  "virtual_time": "2000-09-19T15:13:00+00:00",
  "arrival_sequence": 110000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14562,
  "agent_invocations": 4,
  "gate_reason": "reasoning_error_remaining_arrivals_only"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:34:07.900277+00:00",
  "window": 6,
  "virtual_time": "2000-10-18T12:22:00+00:00",
  "arrival_sequence": 132000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 14592,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:34:15.199706+00:00",
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
  "created_at": "2026-09-09T22:34:22.842569+00:00",
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
  "created_at": "2026-09-09T22:34:30.739695+00:00",
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
  "created_at": "2026-09-09T22:34:38.960752+00:00",
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
  "created_at": "2026-09-09T22:34:46.669155+00:00",
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
  "created_at": "2026-09-09T22:34:54.648870+00:00",
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
  "created_at": "2026-09-09T22:35:02.435126+00:00",
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
  "created_at": "2026-09-09T22:35:10.109068+00:00",
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
  "created_at": "2026-09-09T22:35:17.101411+00:00",
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

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:35:26.066075+00:00",
  "window": 16,
  "virtual_time": "2001-05-30T16:14:00+00:00",
  "arrival_sequence": 352000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 11884,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:35:35.467733+00:00",
  "window": 17,
  "virtual_time": "2001-07-05T06:39:00+00:00",
  "arrival_sequence": 374000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 8770,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:35:43.373822+00:00",
  "window": 18,
  "virtual_time": "2001-09-14T18:31:32+00:00",
  "arrival_sequence": 396000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 4442,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:35:51.102083+00:00",
  "window": 19,
  "virtual_time": "2001-10-18T16:44:49+00:00",
  "arrival_sequence": 418000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 4618,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:35:59.320252+00:00",
  "window": 20,
  "virtual_time": "2001-10-31T20:55:41+00:00",
  "arrival_sequence": 440000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 6585,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:36:08.589109+00:00",
  "window": 21,
  "virtual_time": "2001-11-26T10:02:03+00:00",
  "arrival_sequence": 462000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 5250,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:36:17.221027+00:00",
  "window": 22,
  "virtual_time": "2002-01-09T02:37:18+00:00",
  "arrival_sequence": 484000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 4394,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:36:27.568232+00:00",
  "window": 23,
  "virtual_time": "2002-02-07T05:16:01+00:00",
  "arrival_sequence": 506000,
  "admitted": 22000,
  "selected": 32,
  "duplicate_gated": 5708,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:36:30.392774+00:00",
  "window": 24,
  "virtual_time": "2002-12-21T08:24:45+00:00",
  "arrival_sequence": 516182,
  "admitted": 10182,
  "selected": 32,
  "duplicate_gated": 1771,
  "agent_invocations": 0,
  "gate_reason": "reasoning_disabled_after_error"
}
```

## Execution errors

```json
[
  {
    "window": 5,
    "phase": "observe",
    "agent": "routines",
    "error_type": "ValueError"
  }
]
```
