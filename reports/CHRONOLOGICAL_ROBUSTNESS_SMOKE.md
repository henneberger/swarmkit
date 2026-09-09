# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-1db9ede210d54805b76c8631a738293c` · model `deepseek-v4-flash` · status **partial**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-1db9ede210d54805b76c8631a738293c",
  "mode": "chronological_replay",
  "prompt_version": "chronological-tacit-v5",
  "prompt_sha256": "a152641f0742a910122db398adbe9241297426bcde4a5e081da242a131588930",
  "sampling_version": "body-novel-reservoir-subject-cap-v1",
  "query": "Discover implicit routines and expectations",
  "model": "deepseek-v4-flash",
  "created_at": "2026-09-09T22:38:26.488394+00:00",
  "status": "partial",
  "phase": "revise",
  "config": {
    "batch_size": 22000,
    "max_windows": 1,
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
    }
  ],
  "peers": [
    "routines",
    "expectations",
    "expertise",
    "contrasts"
  ],
  "agent_errors": [],
  "reasoning_rejections": 0,
  "quote_checks": {
    "accepted": 27,
    "rejected": 0
  },
  "replay": {
    "virtual_time": "2000-02-18T10:05:00+00:00",
    "arrived": 22000,
    "initial_arrived": 0,
    "selected": 32,
    "skipped": 21968,
    "model_calls": 8,
    "windows": 1,
    "eligible": 516182,
    "coverage_complete": false,
    "gate_reason": "novel_selected",
    "retrieval_queries": 4,
    "prompt_exposed_documents": 32
  },
  "coverage_limitations": [
    "All eligible arrivals can be admitted; only sampled novel documents are shown to models.",
    "Unselected or duplicate-gated messages are not established irrelevant.",
    "Outer-header chronology and inline attribution are not authenticated human knowledge times.",
    "Quoted support and later-arrival prediction checks do not validate tacit knowledge transfer."
  ],
  "validation_rejections": {
    "citations": 0,
    "hypotheses": 2,
    "predictions": 0
  },
  "predictions": [
    {
      "prediction_id": "prediction-3fcd4462953846f3b155e281acbc5059",
      "hypothesis_id": "hypothesis-9e904418254b466fb0952a9e3bfa9a0d",
      "prediction": "Future external software requests will also involve personal referrals to known contacts.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-2cdbd024f49e480bbba71525225bbc45",
      "hypothesis_id": "hypothesis-fe7ebe886b494b91b29807fb4c2e80a2",
      "prediction": "Future requests for HPL legal review will be directed to Gerald Nemec.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-3e416607c9d14d22a4730bd1ff879864",
      "hypothesis_id": "hypothesis-4b74afa35b22463592a6abde33908043",
      "prediction": "Future requests for HPL legal review will be directed to Gerald Nemec.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-277a81b09c2f4e20be0b866e1e842a62",
      "hypothesis_id": "hypothesis-fa42499af77c4f0e90824c88bec9e5bc",
      "prediction": "Future communications about London clearing will likely reference Paribas as the preferred clearer, unless specific circumstances dictate otherwise.",
      "window": 1,
      "arrival_sequence": 22000
    },
    {
      "prediction_id": "prediction-a6409f31f6a44261b3078249a54b3443",
      "hypothesis_id": "hypothesis-e136d976c48b42eb848e0a8917e26405",
      "prediction": "Future requests for HPL legal review will be directed to Gerald Nemec.",
      "window": 1,
      "arrival_sequence": 22000
    }
  ],
  "runtime_usage": {
    "calls": 8,
    "tokens": 50638,
    "cost": 0.026144800000000003
  },
  "finished_at": "2026-09-09T22:38:47.736957+00:00",
  "ledger_delta": {
    "calls": 8,
    "tokens": 50638,
    "cost_usd": 0.026144799999999968
  },
  "ledger_delta_scope": "Shared ledger activity during run; includes concurrent users if any."
}
```

## Observation timeline

### 2000-02-18T10:05:00+00:00 — review window 1

**routines / observe**

Observed scheduling and document coordination across trading, legal, and regulatory contexts. No clear tacit rule emerges from these disparate emails; they show explicit requests and status updates rather than unstated practices.

Source `mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c`; evidence `mail-3a54a2c94985f656cd2fd7bd711d79eb9bd7ba5ec18f9f0cc89ae29f0060b15c:0:546:3565341ccd35b06c`; origin `enron-authored:dac3baa1b4a64e03c09d3da38f6c8454087b5c6fb63c4f2d40c30e0adb7c431d`.

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

Source `mail-cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d`; evidence `mail-cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d:0:384:0e790a23b36d02be`; origin `enron-authored:e663e747901cc436ab3af757b45fc6cd80707b79ca6ad9afeaeea53bbe9a818d`.

Attribution and exact offsets: `{"segment_id": "mail-cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d:segment:0:384", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 07 Dec 1999 08:22:00 -0800", "segment_source_family": "enron-segment:a170ad71c339f85b16096573fdde49d4d06c5f7842bbdd5572e5dc79ee56a9aa", "segment_fingerprint": "a170ad71c339f85b16096573fdde49d4d06c5f7842bbdd5572e5dc79ee56a9aa", "attribution_status": "unverified_header_claim", "document_id": "mail-cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d", "span_id": "mail-cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d:0:384", "start": 0, "end": 384, "quote": "Attached please find a proposed form of Termination Agreement for Canadian \nImperial Bank of Commerce.  Obviously, we need to still input the trades.\n\nPeter,\n\nIt appears that our signers on the trading floor will be offsite in PRC \nmeetings on Thursday.  I need to know ASAP when we plan on signing this \nbecause I am going to have to call around to find an officer that might be \nin.", "quote_fingerprint": "a170ad71c339f85b16096573fdde49d4d06c5f7842bbdd5572e5dc79ee56a9aa", "independence_status": "not_established", "raw_sha256": "cf7adf807f39e3829bb585293bf2ec110485b68a22cd6a87d8c9b34e3072581d", "body_sha256": "c6fcdeaf26bc00c717ce885d5f18cc2778640950b47677ae0828ee237633d183", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/524.", "source_family": "enron-authored:e663e747901cc436ab3af757b45fc6cd80707b79ca6ad9afeaeea53bbe9a818d", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Attached please find a proposed form of Termination Agreement for Canadian 
> Imperial Bank of Commerce.  Obviously, we need to still input the trades.
> 
> Peter,
> 
> It appears that our signers on the trading floor will be offsite in PRC 
> meetings on Thursday.  I need to know ASAP when we plan on signing this 
> because I am going to have to call around to find an officer that might be 
> in.

Source `mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3`; evidence `mail-5d9ed7e0d93cdae76c03696f0f8ce56a17a1bb14ee3c979169635272bf9473f3:1244:1478:fdc02bdbd1832c6f`; origin `enron-authored:76b1fc3f4d89e07d9a7b4dc649d562db49fdbabdfe3816ebbd3cfcc4adac3f4d`.

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

**expectations / observe**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that Enron London uses only Bank Paribas and Carr as clearing houses, with Paribas preferred for back office. The exchange of views suggests an implicit preference for Paribas, but this is based on a single episode.

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

Tana Jones routes OMLX software request to Susan Gill via Mark Elliott, showing informal referral chain. Kevin Moore's truncated Saturday email hints at office move coordination. Shirley Crenshaw announces supervisor-discretionary personal days for Research Group.

**Observation — revision 1**

In Enron legal, when handling external software or agreement requests, staff rely on informal referrals to specific contacts in London rather than formal procedures.

Inference gap: Sources do not state a policy; only one instance of referral. Contrast with other request handling could reveal pattern.

Evidence basis: Single email from Tana Jones referencing Mark Taylor and Mark Elliott; one episode.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: A request involves external software or agreements where direct contact is unknown.

Exceptions: Unknown; no counterexample in current data.

Alternative: Staff might use formal directories or escalate to managers instead of personal referrals.

Uncertainty: Single episode; no evidence of repeated pattern.

Next query: Search for other external software requests to see if similar referral chains occur.

Prediction: Future external software requests will also involve personal referrals to known contacts.

Hypothesis `hypothesis-9e904418254b466fb0952a9e3bfa9a0d`; transfer tested: false.

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:5d87d41de94352fd`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

Source `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2`; evidence `mail-582c73bc151506737119092fe5046bd5117757e8f123a8c3f2f9452aeab441a2:0:700:9bb7a51dbcf9192a`; origin `enron-authored:c42bb06ea062e8d01c8a57355a159f089742eb5909e87b22c674775720d1a839`.

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

Source `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20`; evidence `mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390:836d309747b519d8`; origin `enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174`.

Attribution and exact offsets: `{"segment_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:segment:0:390", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 03 Aug 1999 07:15:00 -0700", "segment_source_family": "enron-segment:23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "segment_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "attribution_status": "unverified_header_claim", "document_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "span_id": "mail-e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20:0:390", "start": 0, "end": 390, "quote": "Mark Taylor asked me to respond to your request about the OMLX  software.  I \nspoke to Mark Elliott in our London office who dealt directly with the OMLX.  \nHe said to contact Susan Gill at the OMLX, who we spoke to on the agreements, \nand she should be able to direct you to their software people.  Her number in \nLondon is 011 44 171 815 8510.  Let me know if I can be of further service.", "quote_fingerprint": "23fad8dfb413940d3195d16a239557e48b41ed31fe02d25fddd93712f1656cd5", "independence_status": "not_established", "raw_sha256": "e73612a28e2059d965e150c91c6fe77ba248991cbb29b8582fb56dd8b7c76e20", "body_sha256": "cdde332525b3b5303301465c2c9610050354dfa70f3ef9a17ccec6d078f6c6fc", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/167.", "source_family": "enron-authored:79fe345be930591c205714e900c0202f3f320131708e8e03439cad7ed4bc7174", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> Mark Taylor asked me to respond to your request about the OMLX  software.  I 
> spoke to Mark Elliott in our London office who dealt directly with the OMLX.  
> He said to contact Susan Gill at the OMLX, who we spoke to on the agreements, 
> and she should be able to direct you to their software people.  Her number in 
> London is 011 44 171 815 8510.  Let me know if I can be of further service.

**contrasts / observe**

Legal review of HPL letters is routed to Gerald Nemec, who handles HPL legal work. Mark Taylor confirms an executed master agreement with Engage Energy Canada. Ben Rogers requests Con Ed annual report. Credit EOL responses are distributed. Richard Sanders finds an email confusing. Mark Taylor notes bcc to mtaylo1@ect.enron.com may not arrive.

**Candidate tacit rule — revision 1**

When legal documents need approval for HPL, they are routed to Gerald Nemec, who acts as the legal contact for HPL, rather than to a general legal group.

Inference gap: The email does not explicitly state Gerald's role; it is inferred from Shari's assumption and Gerald's acceptance. No other episodes confirm this.

Evidence basis: Single forwarded email from Shari Stack to Gerald Nemec, with earlier forwards from Connie Sutton and Cheryl King, all in one chain.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A request involves legal review or approval for HPL-related matters.

Exceptions: Unknown; may differ if another legal contact is specified or if the matter is outside HPL.

Alternative: Legal review might be handled by a centralized legal team, and Gerald is just one of several contacts.

Uncertainty: Only one forwarded email suggests this; no independent confirmation of Gerald's role.

Next query: Search for other emails where legal review for HPL is requested to see if Gerald is consistently the contact.

Prediction: Future requests for HPL legal review will be directed to Gerald Nemec.

Hypothesis `hypothesis-fe7ebe886b494b91b29807fb4c2e80a2`; transfer tested: false.

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:e49ea1e419ec49e4`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7`; evidence `mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124:8f3093923a9dd018`; origin `enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca`.

Attribution and exact offsets: `{"segment_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:segment:0:124", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 30 Nov 1999 02:16:00 -0800", "segment_source_family": "enron-segment:58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "segment_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "attribution_status": "unverified_header_claim", "document_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "span_id": "mail-570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7:0:124", "start": 0, "end": 124, "quote": "We have an executed master agreement with Engage Energy Canada L.P. which we \nreceived signed around the end of August 1999.", "quote_fingerprint": "58d278811902653a736548c675353fa8c6965e72bab3fa7d029bd86f7efb4b8f", "independence_status": "not_established", "raw_sha256": "570a9e1b1fcf8798abad6a5f49a0b46c673fb7849990200740360a33e1874fc7", "body_sha256": "43ee90e776923d1c8241793276d4e6af45e0b2feb58fc0e776f03f6abd632470", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/906.", "source_family": "enron-authored:010b8e294d9edf5abaf33ae150b6b6561554690a25e24da73481f6fc971e5dca", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> We have an executed master agreement with Engage Energy Canada L.P. which we 
> received signed around the end of August 1999.

Source `mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e`; evidence `mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:0:215:ec6fba9603e1372c`; origin `enron-authored:28defc3b74a4ed0b7b03b0199def6f57dccfd06f682a059705453011c0fab339`.

Attribution and exact offsets: `{"segment_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:segment:0:215", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Mon, 23 Aug 1999 13:32:00 -0700", "segment_source_family": "enron-segment:d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "segment_fingerprint": "d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "attribution_status": "unverified_header_claim", "document_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e", "span_id": "mail-156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e:0:215", "start": 0, "end": 215, "quote": "I see what you mean, and I can't explain the bcc - unfortunately, unless they \nuse \"mtaylo1@ect.enron.com\" it doesn't get here.  It must just disappear into \ncyberspace.  Thanks for continuing to send them on.\n\nMark", "quote_fingerprint": "d5997bc073d4c56f42a7658a25d8725e5f6a38adaf0a2c443fdf5d16f00bd107", "independence_status": "not_established", "raw_sha256": "156fa36d9a0f7d2341a9beac51c7dbea02c8ad0ca3b2611c768fc1349a19b22e", "body_sha256": "f9ddcf113f4c34e335ed0bf11b830d26007edd566acdd3656fd7132e0644ee4e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/574.", "source_family": "enron-authored:28defc3b74a4ed0b7b03b0199def6f57dccfd06f682a059705453011c0fab339", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I see what you mean, and I can't explain the bcc - unfortunately, unless they 
> use "mtaylo1@ect.enron.com" it doesn't get here.  It must just disappear into 
> cyberspace.  Thanks for continuing to send them on.
> 
> Mark

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

**routines / revise**

Legal work for HPL is routed to Gerald Nemec based on Shari Stack's assumption and his acceptance, but this is a single episode. No broader tacit rule is established.

**Candidate tacit rule — revision 1**

In Enron legal, HPL-related legal documents are routed to Gerald Nemec, who acts as the point of contact for HPL matters.

Inference gap: The email does not explicitly state Gerald's role; it is inferred from Shari's assumption and Gerald's acceptance. No other episodes confirm this.

Evidence basis: Single episode: Shari Stack forwards HPL letters to Gerald, who accepts. No other HPL-related emails in current data.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A request involves legal review or approval for HPL-related matters.

Exceptions: Unknown; may differ if another legal contact is specified or if the matter is outside HPL.

Alternative: Legal review might be handled by a centralized legal team, and Gerald is just one of several contacts.

Uncertainty: Only one forwarded email suggests this; no independent confirmation of Gerald's role.

Next query: HPL legal review Gerald Nemec

Prediction: Future requests for HPL legal review will be directed to Gerald Nemec.

Hypothesis `hypothesis-4b74afa35b22463592a6abde33908043`; transfer tested: false.

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:8d79bb87a1ef8caf`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:35f1aafc36a2b1fd`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

**expectations / revise**

Mark Elliott asks Maria Nartey to confirm clearing arrangements for OMLX, noting Merrill Lynch may be Houston's clearer. Maria replies that Enron London uses only Bank Paribas and Carr as clearing houses, with Paribas preferred for back office. The exchange suggests an implicit preference for Paribas, but this is based on a single episode.

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

Mark Elliott and Maria Nartey exchange views on OMLX clearing, revealing a preference for Paribas over Carr based on back-office quality. This single episode suggests an informal, experience-based choice of clearing house, but no explicit policy is stated.

**Candidate tacit rule — revision 1**

When selecting clearing houses for London exchange trades, Enron staff rely on informal back-office quality assessments, favoring Bank Paribas over Carr based on past experience.

Inference gap: Sources do not explicitly state a policy or preference; Maria's opinion is personal and based on past dealings. The contrast between Mark's neutral statement and Maria's evaluative reply suggests an informal knowledge hierarchy, but this is not confirmed.

Evidence basis: Two separate emails in the same thread: Mark Elliott's message to Maria Nartey and Maria's reply. Both are authored by different actors in the same episode, discussing OMLX clearing arrangements.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: Choosing clearing houses for London exchange transactions, especially when multiple options are available.

Exceptions: Unknown; may differ if counterparty or regulatory requirements dictate a specific clearer.

Alternative: Selection might be driven by formal vendor assessments or contractual obligations rather than personal experience.

Uncertainty: Single episode; no evidence of repeated pattern or official policy.

Next query: Look for other emails discussing clearing house selection or preferences to see if Paribas is consistently favored.

Prediction: Future communications about London clearing will likely reference Paribas as the preferred clearer, unless specific circumstances dictate otherwise.

Hypothesis `hypothesis-fa42499af77c4f0e90824c88bec9e5bc`; transfer tested: false.

Source `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315`; evidence `mail-5ba60649499446384f0acfabd1a5459dd5e2eb2ec2d7ea91db107fee7586c315:0:611:8a432183b1f9e268`; origin `enron-authored:a80a14acf0b9ed7d66b72bc9719bfc7614eb9e27cd928f172e69fd31dd636dcd`.

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

**contrasts / revise**

Shari Stack forwards HPL letters to Gerald Nemec, assuming he does HPL legal work; Gerald accepts. This single episode suggests informal routing, but no independent confirmation of Gerald's role exists.

**Candidate tacit rule — revision 1**

Legal document approvals for HPL are routed to Gerald Nemec, who acts as the de facto legal contact for HPL, rather than to a centralized legal group.

Inference gap: The email does not explicitly state Gerald's role; it is inferred from Shari's assumption and Gerald's acceptance. No other episodes confirm this.

Evidence basis: Single episode: Shari Stack's forwarded email and Gerald's reply. Both actors are in the same email chain, so this is one episode.

Source counts: {'outer_documents': 1, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: A request involves legal review or approval for HPL-related matters.

Exceptions: Unknown; may differ if another legal contact is specified or if the matter is outside HPL.

Alternative: Legal review might be handled by a centralized legal team, and Gerald is just one of several contacts.

Uncertainty: Only one forwarded email suggests this; no independent confirmation of Gerald's role.

Next query: Find another HPL legal request not routed to Gerald Nemec.

Prediction: Future requests for HPL legal review will be directed to Gerald Nemec.

Hypothesis `hypothesis-e136d976c48b42eb848e0a8917e26405`; transfer tested: false.

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519:e49ea1e419ec49e4`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:214:519", "segment_kind": "forwarded", "claimed_sender": "Shari Stack", "claimed_date": "09/01/99 12:34 PM", "segment_source_family": "enron-segment:77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "segment_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:214:519", "start": 214, "end": 519, "quote": "\nAttached are some letters that Cheryl King from HPL has prepared. I think it \nwould be more appropriate for you ( or someone from your group) to OK these \nas from reading the email, I gather that you do the legal work for HPL. \n\nCan I leave it with you to get with Cheryl King? \n\nMany thanks, \n\nShari  \n\n", "quote_fingerprint": "77ba68a5f5611be6aa2cd2643d0e8216ef7eccf74468aceb3a8ca47bac455b3f", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:d4b1f49440fe7b8b`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

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

Source `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e`; evidence `mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72:836d309747b519d8`; origin `enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6`.

Attribution and exact offsets: `{"segment_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:segment:0:72", "segment_kind": "authored", "claimed_sender": "gerald.nemec@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:11:00 -0700", "segment_source_family": "enron-span:mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "segment_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "attribution_status": "unverified_header_claim", "document_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "span_id": "mail-5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e:0:72", "start": 0, "end": 72, "quote": "No problem.  I will review these and get back with Cheryl.  Thanks.\n\n\n\n\n", "quote_fingerprint": "8bd2e7bf436b72086ce3062235c30945cd3fe21ae2daf94de27bf4575feb0659", "independence_status": "not_established", "raw_sha256": "5ab8ec71065fa37fb7d1cb0595413e1f4fbaa7a2215e5f85ac1eb69886b6c42e", "body_sha256": "246f694ab159f4168ca60efffd348b810d4c3baae0e83b9ceccb10b4517838df", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/nemec-g/sent/171.", "source_family": "enron-authored:670b63843156dcf7d00ebf6a1c767174c8309d16962be21d1c2f65a62dc2fad6", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> No problem.  I will review these and get back with Cheryl.  Thanks.
> 
> 
> 
> 
> 

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:38:47.736524+00:00",
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
