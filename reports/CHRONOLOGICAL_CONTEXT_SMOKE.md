# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-e91f2af7a7f54a79a16fa2ca0f1adf51` · model `deepseek-v4-flash` · status **partial**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-e91f2af7a7f54a79a16fa2ca0f1adf51",
  "mode": "chronological_replay",
  "prompt_version": "chronological-tacit-v4",
  "prompt_sha256": "232a45ae242a55d137fa6ddc831bcdf4bcded4518527d470e7426af416cf1919",
  "sampling_version": "body-novel-reservoir-subject-cap-v1",
  "query": "Discover implicit routines and expectations",
  "model": "deepseek-v4-flash",
  "created_at": "2026-09-09T22:31:43.632193+00:00",
  "status": "partial",
  "phase": "revise",
  "config": {
    "batch_size": 4000,
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
      "virtual_time": "1999-09-08T16:22:00+00:00",
      "arrival_sequence": 4000,
      "admitted": 4000,
      "selected": 32,
      "duplicate_gated": 2013,
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
    "accepted": 26,
    "rejected": 0
  },
  "replay": {
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrived": 4000,
    "initial_arrived": 0,
    "selected": 32,
    "skipped": 3968,
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
    "hypotheses": 3,
    "predictions": 0
  },
  "predictions": [
    {
      "prediction_id": "prediction-8bbd19d257bd40d1979b106a2f18c7d8",
      "hypothesis_id": "hypothesis-b50ba9d52c0e404780ddc7429eefcba9",
      "prediction": "Future emails will show Tana Jones being consulted for London office logistics or event planning.",
      "window": 1,
      "arrival_sequence": 4000
    },
    {
      "prediction_id": "prediction-07bde20c6939427d964e6fd929f54da1",
      "hypothesis_id": "hypothesis-f0407e7389c54becb103a320b74dd3d1",
      "prediction": "Future emails will show Tana Jones being consulted for special projects or London office logistics, but not for routine confirmation desk legal questions.",
      "window": 1,
      "arrival_sequence": 4000
    },
    {
      "prediction_id": "prediction-5ecadae156c04a1387663da11e78ddce",
      "hypothesis_id": "hypothesis-18c76bbcbb8d41e6ab9ba2db98cb7c16",
      "prediction": "Future emails will show Tana Jones coordinating legal sign-off for other documents or being consulted for special legal projects.",
      "window": 1,
      "arrival_sequence": 4000
    }
  ],
  "runtime_usage": {
    "calls": 8,
    "tokens": 48742,
    "cost": 0.025110799999999996
  },
  "finished_at": "2026-09-09T22:32:02.136933+00:00",
  "ledger_delta": {
    "calls": 8,
    "tokens": 48742,
    "cost_usd": 0.02511079999999999
  },
  "ledger_delta_scope": "Shared ledger activity during run; includes concurrent users if any."
}
```

## Observation timeline

### 1999-09-08T16:22:00+00:00 — review window 1

**routines / observe**

Tana Jones seeks confirmation that Meteo France's Paris address is standard over Toulouse. Mark Taylor asks about launch materials. Dan Hyvl awaits contract number for Mercado Gas Services. Sara Shackleton announces quarterly rotation of confirmation desk calls to legal, excluding Tana Jones. Mark Taylor approves Brent as primary contact. Carol Clair questions setoff rights expansion.

Source `mail-0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33`; evidence `mail-0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33:0:434:1757413fca5ec5ff`; origin `enron-authored:a97f037597af6f1e5dcdec830b316420797db29cdc68ad0903eb4670971e6b46`.

Attribution and exact offsets: `{"segment_id": "mail-0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33:segment:0:434", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Wed, 25 Aug 1999 03:35:00 -0700", "segment_source_family": "enron-segment:ff0f0ac6c09029bf0aa76fb6e5b73046136683a8683d19213041cda0fe2cddb6", "segment_fingerprint": "ff0f0ac6c09029bf0aa76fb6e5b73046136683a8683d19213041cda0fe2cddb6", "attribution_status": "unverified_header_claim", "document_id": "mail-0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33", "span_id": "mail-0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33:0:434", "start": 0, "end": 434, "quote": "Michael Corbally just wanted me to confirm the following with you.  Per the \nlist of Datasources you sent me, for France we've got Meteo France listed at \nthe Paris address.  We had a confirm earlier this year using Meteo France \nwhere we used their Toulouse address.  I just wanted to confirm that the \naddress we want as the standard address will be the Meteo France out of \nParis, not Toulouse.  If you'll just confirm that for me.", "quote_fingerprint": "ff0f0ac6c09029bf0aa76fb6e5b73046136683a8683d19213041cda0fe2cddb6", "independence_status": "not_established", "raw_sha256": "0a28ceafd8aa2adc418bc6bb7e3a529aeaf4ccb0408673fbc2dd3d318e90aa33", "body_sha256": "7c9cff6758dab32026c7b647f01c7e283b0c11ced3d5f97ea5b8868e21bf06ca", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/218.", "source_family": "enron-authored:a97f037597af6f1e5dcdec830b316420797db29cdc68ad0903eb4670971e6b46", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Michael Corbally just wanted me to confirm the following with you.  Per the 
> list of Datasources you sent me, for France we've got Meteo France listed at 
> the Paris address.  We had a confirm earlier this year using Meteo France 
> where we used their Toulouse address.  I just wanted to confirm that the 
> address we want as the standard address will be the Meteo France out of 
> Paris, not Toulouse.  If you'll just confirm that for me.

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47:d70dc2f78763ad57`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:0:47", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 02 Sep 1999 01:44:00 -0700", "segment_source_family": "enron-span:mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "segment_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "start": 0, "end": 47, "quote": "My apologies for leaving your names out!  Sara\n", "quote_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> My apologies for leaving your names out!  Sara
> 

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:02d086fc33babefc`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

**expectations / observe**

Mark Taylor shares a treaty with Brent Hendry, who congratulates him on VP promotion. Shari Stack announces ECT name changes effective Sept 1. Mark asks about Louise's forwarded link. D'Arcy Carroll details a Champion-Elektro energy deal. ECT management schedules performance workshops. Mark Skilling exchanges personal emails with Tom.

Source `mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a`; evidence `mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:404:739:c9ace60088826ac0`; origin `enron-authored:1672d27358456954be28d68a91da5ceaf4a7c7595059239d4720129dbc0500e6`.

Attribution and exact offsets: `{"segment_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:segment:404:739", "segment_kind": "forwarded", "claimed_sender": "Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL", "claimed_date": "01/18/99 10:16 AM", "segment_source_family": "enron-segment:0c6955e519a4dbb74eaecdabe631db238896de25d87c41eb3f96c59cc4fc53ec", "segment_fingerprint": "0c6955e519a4dbb74eaecdabe631db238896de25d87c41eb3f96c59cc4fc53ec", "attribution_status": "unverified_header_claim", "document_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a", "span_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:404:739", "start": 404, "end": 739, "quote": "\n\n\n\nMark, congratulations on your promotion to Vice President.\n\nOn a more mundane matter could you have a clerk or legal assistant get me a \ncopy of the Bilateral Investment Treaty between the US and Argentina.  Our \nregulatory and commercial group wants to leave no stone unturned in their \nsearch for how to deal with the ENARGAS.\n\n\n", "quote_fingerprint": "0c6955e519a4dbb74eaecdabe631db238896de25d87c41eb3f96c59cc4fc53ec", "independence_status": "not_established", "raw_sha256": "4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a", "body_sha256": "9b91c21a6993e65e68fdfc1326d8128d63c360fb9fa5e0753ae9e67ccf2fc770", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/123.", "source_family": "enron-authored:1672d27358456954be28d68a91da5ceaf4a7c7595059239d4720129dbc0500e6", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> 
> 
> 
> 
> Mark, congratulations on your promotion to Vice President.
> 
> On a more mundane matter could you have a clerk or legal assistant get me a 
> copy of the Bilateral Investment Treaty between the US and Argentina.  Our 
> regulatory and commercial group wants to leave no stone unturned in their 
> search for how to deal with the ENARGAS.
> 
> 
> 

Source `mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191`; evidence `mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:0:700:9bbdc61597348882`; origin `enron-authored:b793d71f2899ad1e9e68043990052496cd1e8f9934794bcd0baad52938469f9b`.

Attribution and exact offsets: `{"segment_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:segment:0:1233", "segment_kind": "authored", "claimed_sender": "shari.stack@enron.com", "claimed_date": "Mon, 30 Aug 1999 12:33:00 -0700", "segment_source_family": "enron-segment:96871ad3003e0689da9718fbc4a793121283e0f1206eef4a5bc2027e7469c3d2", "segment_fingerprint": "96871ad3003e0689da9718fbc4a793121283e0f1206eef4a5bc2027e7469c3d2", "attribution_status": "unverified_header_claim", "document_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191", "span_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:0:700", "start": 0, "end": 700, "quote": "Just to let you know that in preparation for Sept. 1st, we need to go ahead \nand prepare for the name changes in our template fax letterheads, \ndocumentation, confirmations, account details, etc... from ECT to \"Enron \nNorth America Corp.\"  and ECT Canada to \"Enron Canada Corp.\", so that we send \nout correct correspondence on Wed. and thereafter.  There may be more places \nin your world where those names need to be changed  and we will rely on each \nof you to spot and make the change. \n\nSara and I have drafted a form letter which announces that the name changes \nare effective Sept. 1st. The letter is being prepared and will be \n\"auto-faxed\" tomorrow to counterparties whose fax numbers are on ", "quote_fingerprint": "7126a2279058ac4b945ff021ca48fd79094ef2cbec3f44c48e586f46e5c4fb76", "independence_status": "not_established", "raw_sha256": "093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191", "body_sha256": "e1d0ec2d8644f42b74dfcd392999cc3161c79e3e03af4b163eb423fc81a09c3d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/434.", "source_family": "enron-authored:b793d71f2899ad1e9e68043990052496cd1e8f9934794bcd0baad52938469f9b", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191 700"}`

> Just to let you know that in preparation for Sept. 1st, we need to go ahead 
> and prepare for the name changes in our template fax letterheads, 
> documentation, confirmations, account details, etc... from ECT to "Enron 
> North America Corp."  and ECT Canada to "Enron Canada Corp.", so that we send 
> out correct correspondence on Wed. and thereafter.  There may be more places 
> in your world where those names need to be changed  and we will rely on each 
> of you to spot and make the change. 
> 
> Sara and I have drafted a form letter which announces that the name changes 
> are effective Sept. 1st. The letter is being prepared and will be 
> "auto-faxed" tomorrow to counterparties whose fax numbers are on 

Source `mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf`; evidence `mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf:280:980:0431526dcac516da`; origin `enron-authored:398559c6d2469909dbb843db9a6d6993746e65635befb7013ae5ddc591917726`.

Attribution and exact offsets: `{"segment_id": "mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf:segment:280:1182", "segment_kind": "forwarded", "claimed_sender": "D'Arcy Carroll", "claimed_date": "24/08/99 02:18 PM ---------------------------", "segment_source_family": "enron-segment:bc2656592d5967e5a9f77f3a7a746341eb2fdcafdd4dabb38ed650159b6db723", "segment_fingerprint": "bc2656592d5967e5a9f77f3a7a746341eb2fdcafdd4dabb38ed650159b6db723", "attribution_status": "unverified_header_claim", "document_id": "mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf", "span_id": "mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf:280:980", "start": 280, "end": 980, "quote": "\nPls find overview listed re ECE-Champion-Elektro transaction:\n\nECE selling equivalent of 3MW (Peak- and Off-peak) energy eg consumption\ntake-or-pay for period Sep - Oct - Nov\nPrice will be R$42.75 which represents 5% discount to present average\nElektro rate of R$45\nECE wants to adjust on a monthly basis the R$42.75 sales price downward \nshould the price of PPI UK A$ cut size 80g index or the PPI UK A4  Reels 60g \nindex average below Strike Price x (Pounds per Metric Ton).  The adjustment \nwill be based on formula: Avg. Monthly hedged volume * (Index avg-Strike \nPrice) * R$/Pound spot price\n\nWe are trying to finalize negotiations this afternoon re both the energy sale \nand the incorporated i", "quote_fingerprint": "e67eae370cf35f48d5c655cd1d6640d346912b9fbf096ef2cee9a1f1206f83c7", "independence_status": "not_established", "raw_sha256": "3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf", "body_sha256": "f0a9f69ffbdeb8af12b2fe356742a57b4acc33e9e1838b2514b11b942adf6ea2", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/401.", "source_family": "enron-authored:398559c6d2469909dbb843db9a6d6993746e65635befb7013ae5ddc591917726", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-3c68b1a600b41d57485c24c6e5d4dfe78ec27ea7dd7d8c48bc09946b8ab467bf 980"}`

> 
> Pls find overview listed re ECE-Champion-Elektro transaction:
> 
> ECE selling equivalent of 3MW (Peak- and Off-peak) energy eg consumption
> take-or-pay for period Sep - Oct - Nov
> Price will be R$42.75 which represents 5% discount to present average
> Elektro rate of R$45
> ECE wants to adjust on a monthly basis the R$42.75 sales price downward 
> should the price of PPI UK A$ cut size 80g index or the PPI UK A4  Reels 60g 
> index average below Strike Price x (Pounds per Metric Ton).  The adjustment 
> will be based on formula: Avg. Monthly hedged volume * (Index avg-Strike 
> Price) * R$/Pound spot price
> 
> We are trying to finalize negotiations this afternoon re both the energy sale 
> and the incorporated i

**expertise / observe**

Tana Jones asks Mark Taylor if he was serious about a Friday conversation, indicating a private matter. Mark Taylor coordinates conference logistics, delegating t-shirt sizes to Suzanne Adams and London attendee selection to Tana. Sara Shackleton handles a swap deal entry error, showing informal routing. Steven Kean advises on Frankfurt dinner organization, suggesting caution about German Consulate support.

**Observation — revision 1**

Tana Jones is the informal coordinator for London office conference participation and possibly other special projects.

Inference gap: The email does not state Tana's role or why she is the contact; it only shows Mark Taylor instructing her to let him know who will come.

Evidence basis: Single episode: Mark Taylor's email to Suzanne Adams, forwarded, mentions Tana will inform about London attendees. No other emails in this batch show Tana's coordination role.

Source counts: {'outer_documents': 1, 'segment_families': 1, 'independent_episodes': 'not established by these counts'}

Applies when: When planning events or projects that involve the London office or require coordination with Tana's network.

Exceptions: Unknown; may not apply if Tana is unavailable or if the matter is outside her domain.

Alternative: Mark Taylor might directly contact London staff or use another coordinator for different projects.

Uncertainty: Only one email shows this delegation; no other evidence confirms Tana's role beyond this instance.

Next query: Search for other emails where Tana Jones is asked to coordinate or provide information about London office activities.

Prediction: Future emails will show Tana Jones being consulted for London office logistics or event planning.

Hypothesis `hypothesis-b50ba9d52c0e404780ddc7429eefcba9`; transfer tested: false.

Source `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166`; evidence `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240:5c0e4ee914701b13`; origin `enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98`.

Attribution and exact offsets: `{"segment_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:segment:0:240", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Wed, 12 May 1999 10:42:00 -0700", "segment_source_family": "enron-segment:6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "segment_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "attribution_status": "unverified_header_claim", "document_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "span_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240", "start": 0, "end": 240, "quote": "I think we are doing Hawaiian shirts - we just don't want everyone to know \nyet.  Yes - please include all the offices - also include Singapore & Buenos \nAires.  Tana will let you know which people in the London office will be \ncoming.\n\n\n\n\n", "quote_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "independence_status": "not_established", "raw_sha256": "49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "body_sha256": "659e733b7dd4c7346a2db58b91ddb87d0d398019536473f4c667ea1f68aec782", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/287.", "source_family": "enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I think we are doing Hawaiian shirts - we just don't want everyone to know 
> yet.  Yes - please include all the offices - also include Singapore & Buenos 
> Aires.  Tana will let you know which people in the London office will be 
> coming.
> 
> 
> 
> 
> 

Source `mail-1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d`; evidence `mail-1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d:0:317:cc5c019412d31c36`; origin `enron-authored:601f5520cf200a93fda594bba779a08d032a711c2abc49404a649a4136e5095c`.

Attribution and exact offsets: `{"segment_id": "mail-1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d:segment:0:317", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Mon, 26 Jul 1999 03:16:00 -0700", "segment_source_family": "enron-segment:85b4f6b2339cd1817b0c54da0d42471c04946bbe7eb635b4807f07e97eb6c846", "segment_fingerprint": "85b4f6b2339cd1817b0c54da0d42471c04946bbe7eb635b4807f07e97eb6c846", "attribution_status": "unverified_header_claim", "document_id": "mail-1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d", "span_id": "mail-1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d:0:317", "start": 0, "end": 317, "quote": "I spoke with Dale Neuner (confirm desk) a few minutes ago.  It seems that \nScott Neal sent the deal ticket to EI and not ECT.  We have retrieved the \nticket and Dale is talking to Scott about having the deal entered into trade \ncapture.  Dale is in touch with Brent and will advise when deal has been \nentered.  SS\n\n\n", "quote_fingerprint": "85b4f6b2339cd1817b0c54da0d42471c04946bbe7eb635b4807f07e97eb6c846", "independence_status": "not_established", "raw_sha256": "1a4f80f960163e96b0eade8d64bf31725ab58a3623057daf8daa8059a4194f4d", "body_sha256": "1102541b75a5ccdc1aaf2bd0b6faabadee8020db775de2fa18b59f377937fac3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/261.", "source_family": "enron-authored:601f5520cf200a93fda594bba779a08d032a711c2abc49404a649a4136e5095c", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I spoke with Dale Neuner (confirm desk) a few minutes ago.  It seems that 
> Scott Neal sent the deal ticket to EI and not ECT.  We have retrieved the 
> ticket and Dale is talking to Scott about having the deal entered into trade 
> capture.  Dale is in touch with Brent and will advise when deal has been 
> entered.  SS
> 
> 
> 

Source `mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6`; evidence `mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:0:205:b03d9dc2eddc90f2`; origin `enron-authored:ff447c441eb02129f2150cc5fe4e4d521387d5a5a95a6fb4accb398a5e5c9215`.

Attribution and exact offsets: `{"segment_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:segment:0:205", "segment_kind": "authored", "claimed_sender": "steven.kean@enron.com", "claimed_date": "Mon, 30 Aug 1999 02:42:00 -0700", "segment_source_family": "enron-segment:3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "segment_fingerprint": "3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "attribution_status": "unverified_header_claim", "document_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6", "span_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:0:205", "start": 0, "end": 205, "quote": "Another bit of background re Frankfurt (see below).  I would be a little bit \nmore insistent on German Consulate support than Herr Sturm suggests \n(otherwise this could become a black hole for your time).\n", "quote_fingerprint": "3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "independence_status": "not_established", "raw_sha256": "35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6", "body_sha256": "d8355135268aa1cb53c8d3bdb9b823baf4caf4a6b1811fe341118924b6919b28", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/calendar/untitled/127.", "source_family": "enron-authored:ff447c441eb02129f2150cc5fe4e4d521387d5a5a95a6fb4accb398a5e5c9215", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Another bit of background re Frankfurt (see below).  I would be a little bit 
> more insistent on German Consulate support than Herr Sturm suggests 
> (otherwise this could become a black hole for your time).
> 

Source `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166`; evidence `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240:836d309747b519d8`; origin `enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98`.

Attribution and exact offsets: `{"segment_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:segment:0:240", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Wed, 12 May 1999 10:42:00 -0700", "segment_source_family": "enron-segment:6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "segment_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "attribution_status": "unverified_header_claim", "document_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "span_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240", "start": 0, "end": 240, "quote": "I think we are doing Hawaiian shirts - we just don't want everyone to know \nyet.  Yes - please include all the offices - also include Singapore & Buenos \nAires.  Tana will let you know which people in the London office will be \ncoming.\n\n\n\n\n", "quote_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "independence_status": "not_established", "raw_sha256": "49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "body_sha256": "659e733b7dd4c7346a2db58b91ddb87d0d398019536473f4c667ea1f68aec782", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/287.", "source_family": "enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> I think we are doing Hawaiian shirts - we just don't want everyone to know 
> yet.  Yes - please include all the offices - also include Singapore & Buenos 
> Aires.  Tana will let you know which people in the London office will be 
> coming.
> 
> 
> 
> 
> 

**contrasts / observe**

Recent emails show coordination on legal/compliance tasks: updating agreements, boycott lists, credit matrices, and market descriptions. No explicit tacit rules yet; mostly explicit instructions and status updates.

Source `mail-5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9`; evidence `mail-5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9:0:527:0a79438801b1cc40`; origin `enron-authored:d998339528b9e67d636f86b9db572d083e77fe46ea17d84a1e682b9cdbb108ec`.

Attribution and exact offsets: `{"segment_id": "mail-5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9:segment:0:527", "segment_kind": "authored", "claimed_sender": "jeff.blumenthal@enron.com", "claimed_date": "Mon, 02 Aug 1999 11:04:00 -0700", "segment_source_family": "enron-segment:d71e11eb5f09a23a45277c23425ecb303b210fbfc6dfa3052e5d77268952144d", "segment_fingerprint": "d71e11eb5f09a23a45277c23425ecb303b210fbfc6dfa3052e5d77268952144d", "attribution_status": "unverified_header_claim", "document_id": "mail-5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9", "span_id": "mail-5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9:0:527", "start": 0, "end": 527, "quote": "Louise and Mark,\n\nAs we discussed in our meeting last Thursday, set forth below is the most \nrecent list of the boycott countries for you to take into account when making \nthe appropriate system changes to prohibit trading with counterparties \nlocated in such countries:\n\nBahrain\n\nIraq\n\nKuwait\n\nLebanon\n\nLibya\n\nOman\n\nQatar\n\nSaudi Arabia\n\nSyria\n\nUnited Arab Emirates\n\nRepublic of Yemen\n\nThis list is published quarterly, so we will inform you of any changes to the \nlist as they are published in the future.\n\nBest regards,\n\nJeff", "quote_fingerprint": "d71e11eb5f09a23a45277c23425ecb303b210fbfc6dfa3052e5d77268952144d", "independence_status": "not_established", "raw_sha256": "5aa6741486ccc3d304f0a49dd9a1abb7e94ae9a3a60085c1bc9774c130aefdb9", "body_sha256": "b247d875dc3b84da3014621155c0a533b1d6e198e40d874a3fc87d70d240ec1d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/504.", "source_family": "enron-authored:d998339528b9e67d636f86b9db572d083e77fe46ea17d84a1e682b9cdbb108ec", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Louise and Mark,
> 
> As we discussed in our meeting last Thursday, set forth below is the most 
> recent list of the boycott countries for you to take into account when making 
> the appropriate system changes to prohibit trading with counterparties 
> located in such countries:
> 
> Bahrain
> 
> Iraq
> 
> Kuwait
> 
> Lebanon
> 
> Libya
> 
> Oman
> 
> Qatar
> 
> Saudi Arabia
> 
> Syria
> 
> United Arab Emirates
> 
> Republic of Yemen
> 
> This list is published quarterly, so we will inform you of any changes to the 
> list as they are published in the future.
> 
> Best regards,
> 
> Jeff

Source `mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da`; evidence `mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:0:700:f0f937539b980e5f`; origin `enron-authored:38c2abba0b1a96038deefec45fc2ebf1a908969dd978e206de53f6afde414312`.

Attribution and exact offsets: `{"segment_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:segment:0:825", "segment_kind": "authored", "claimed_sender": "frank.davis@enron.com", "claimed_date": "Wed, 08 Sep 1999 02:07:00 -0700", "segment_source_family": "enron-segment:601c582ec90fac6b96439c141892baf8e132abc7763492275a3118227d6e37ac", "segment_fingerprint": "601c582ec90fac6b96439c141892baf8e132abc7763492275a3118227d6e37ac", "attribution_status": "unverified_header_claim", "document_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da", "span_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:0:700", "start": 0, "end": 700, "quote": "Debbie/Tom,\n\nAttached is a new version of the counterparty and product type matrix.  The \ncounterparties are broken into three sections.  The first section contains \ncounterparties that were included in credits original approved list with \nlimits noted.  The second section contains counterparties that were included \nin credits second approved list without any limits noted.  The third and last \nsection contains counterparties that will be included in the initial \nmailshot, but have not yet been reviewed by credit.  Please note that there \nare also new product types in row 7 that were not on any of the matrices you \nhave previously reviewed.  These new product types are highlighted in yellow \n", "quote_fingerprint": "e6287fe99bf988639fc3769fc3ce32a9f86a2f53756d8fcd2fe92ea2e5a95d90", "independence_status": "not_established", "raw_sha256": "5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da", "body_sha256": "49f7644b25c770cb02628c53a42a9e6723ab2972355f1547940459be7a28d6d7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/online_trading/294.", "source_family": "enron-authored:38c2abba0b1a96038deefec45fc2ebf1a908969dd978e206de53f6afde414312", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da 700"}`

> Debbie/Tom,
> 
> Attached is a new version of the counterparty and product type matrix.  The 
> counterparties are broken into three sections.  The first section contains 
> counterparties that were included in credits original approved list with 
> limits noted.  The second section contains counterparties that were included 
> in credits second approved list without any limits noted.  The third and last 
> section contains counterparties that will be included in the initial 
> mailshot, but have not yet been reviewed by credit.  Please note that there 
> are also new product types in row 7 that were not on any of the matrices you 
> have previously reviewed.  These new product types are highlighted in yellow 
> 

Source `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c`; evidence `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279:f441252fb452e676`; origin `enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473`.

Attribution and exact offsets: `{"segment_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:segment:0:279", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:13:00 -0700", "segment_source_family": "enron-segment:45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "segment_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "attribution_status": "unverified_header_claim", "document_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "span_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279", "start": 0, "end": 279, "quote": "Awais,\n\nI have forwarded the descriptions you have sent us thus far to the respective \nLegal Trading Lawyers to sign off as far any legal issues we may have with \nthe descriptions.  I understand your deadline is the end of the week.\n\nWhen can I expect the remaining descriptions?", "quote_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "independence_status": "not_established", "raw_sha256": "49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "body_sha256": "11fc2b55e6d8082c4012d2a78beaf77ab478f459b95522fd04bd03b0841367b8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/247.", "source_family": "enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Awais,
> 
> I have forwarded the descriptions you have sent us thus far to the respective 
> Legal Trading Lawyers to sign off as far any legal issues we may have with 
> the descriptions.  I understand your deadline is the end of the week.
> 
> When can I expect the remaining descriptions?

**routines / revise**

Sara Shackleton forwards a notice that confirmation desk calls to legal now route quarterly to designated paralegals, excluding Tana Jones. This explicit instruction may signal an unstated shift in Tana's role, but no tacit rule is yet inferable from this single episode.

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:df65718c030f60ca`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47:d70dc2f78763ad57`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:0:47", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 02 Sep 1999 01:44:00 -0700", "segment_source_family": "enron-span:mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "segment_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "start": 0, "end": 47, "quote": "My apologies for leaving your names out!  Sara\n", "quote_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> My apologies for leaving your names out!  Sara
> 

**expectations / revise**

Shari Stack's email about ECT name changes and Sara Shackleton's apology for omitted names suggest a coordination episode where distribution lists are error-prone and require follow-up. The confirmation desk routing excludes Tana Jones, who is also delegated London conference attendee selection, indicating she has a special projects role.

**Candidate tacit rule — revision 1**

Tana Jones is the informal coordinator for special projects and London office logistics, despite being excluded from routine confirmation desk legal routing.

Inference gap: The sources do not explicitly state Tana's role or why she is excluded from legal routing but delegated London attendee selection. The contrast between her exclusion from routine tasks and inclusion in special coordination suggests an implicit specialization.

Evidence basis: Two separate emails: one from Sara Shackleton announcing Tana's exclusion from legal routing due to special projects, and one from Mark Taylor delegating London attendee selection to Tana. These are distinct episodes involving different actors.

Source counts: {'outer_documents': 2, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: When tasks require cross-office coordination or special project handling outside standard confirmation desk procedures.

Exceptions: Unknown; may not apply if Tana is unavailable or if the task is routine legal routing.

Alternative: Tana's exclusion from legal routing might be temporary, and her London coordination role might be a one-off delegation.

Uncertainty: Only two separate emails show Tana's involvement; no explicit statement defines her overall role or responsibilities.

Next query: Look for emails where Tana Jones is assigned or declines special projects or London coordination tasks.

Prediction: Future emails will show Tana Jones being consulted for special projects or London office logistics, but not for routine confirmation desk legal questions.

Hypothesis `hypothesis-f0407e7389c54becb103a320b74dd3d1`; transfer tested: false.

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47:5aade328aa4e02dd`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:0:47", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 02 Sep 1999 01:44:00 -0700", "segment_source_family": "enron-span:mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "segment_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:0:47", "start": 0, "end": 47, "quote": "My apologies for leaving your names out!  Sara\n", "quote_fingerprint": "e61f1989909861f567bdefb2405801d389ee5f85ca1ac00985c24bbaa629b86e", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> My apologies for leaving your names out!  Sara
> 

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:60bfcbbec1c0c234`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

Source `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166`; evidence `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240:e8a40a7bca365bd1`; origin `enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98`.

Attribution and exact offsets: `{"segment_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:segment:0:240", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Wed, 12 May 1999 10:42:00 -0700", "segment_source_family": "enron-segment:6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "segment_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "attribution_status": "unverified_header_claim", "document_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "span_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240", "start": 0, "end": 240, "quote": "I think we are doing Hawaiian shirts - we just don't want everyone to know \nyet.  Yes - please include all the offices - also include Singapore & Buenos \nAires.  Tana will let you know which people in the London office will be \ncoming.\n\n\n\n\n", "quote_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "independence_status": "not_established", "raw_sha256": "49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "body_sha256": "659e733b7dd4c7346a2db58b91ddb87d0d398019536473f4c667ea1f68aec782", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/287.", "source_family": "enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> I think we are doing Hawaiian shirts - we just don't want everyone to know 
> yet.  Yes - please include all the offices - also include Singapore & Buenos 
> Aires.  Tana will let you know which people in the London office will be 
> coming.
> 
> 
> 
> 
> 

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:02d086fc33babefc`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

Source `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166`; evidence `mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240:836d309747b519d8`; origin `enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98`.

Attribution and exact offsets: `{"segment_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:segment:0:240", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Wed, 12 May 1999 10:42:00 -0700", "segment_source_family": "enron-segment:6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "segment_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "attribution_status": "unverified_header_claim", "document_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "span_id": "mail-49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166:0:240", "start": 0, "end": 240, "quote": "I think we are doing Hawaiian shirts - we just don't want everyone to know \nyet.  Yes - please include all the offices - also include Singapore & Buenos \nAires.  Tana will let you know which people in the London office will be \ncoming.\n\n\n\n\n", "quote_fingerprint": "6c85719e78f4bbbfd19d12978193a152b98ff0638f7a2a8549e7a82108720086", "independence_status": "not_established", "raw_sha256": "49f99b3e4bc5ce90f78f854d17b77d8d867f74eee74ead46bf55c84290168166", "body_sha256": "659e733b7dd4c7346a2db58b91ddb87d0d398019536473f4c667ea1f68aec782", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/287.", "source_family": "enron-authored:750be89dfa9a6f014c3a23b2de37764d19f65019aaed1d597610c4972cd86d98", "synthetic": false, "claim_status": "attributed_statement", "excerpt_truncated": false, "next_read": null}`

> I think we are doing Hawaiian shirts - we just don't want everyone to know 
> yet.  Yes - please include all the offices - also include Singapore & Buenos 
> Aires.  Tana will let you know which people in the London office will be 
> coming.
> 
> 
> 
> 
> 

**expertise / revise**

Recent emails show explicit instructions for legal/compliance tasks, but also reveal informal coordination roles. Tana Jones is repeatedly involved in logistics and legal routing, suggesting she holds tacit knowledge of contacts and workflows. Steven Kean's advice on Frankfurt indicates awareness of external relations risks.

**Candidate tacit rule — revision 1**

Tana Jones is the informal gatekeeper for legal review of market descriptions, despite being excluded from routine confirmation desk legal routing.

Inference gap: The sources do not explicitly state Tana's role in legal routing; they show her forwarding descriptions and being excluded from routine legal calls, suggesting a special project role.

Evidence basis: Two separate emails: one shows Tana forwarding descriptions to legal lawyers (v596f2cf19a7c6640), another shows her excluded from routine legal routing (v098c6d19c5f68ff9). The contrast implies she handles special legal projects.

Source counts: {'outer_documents': 2, 'segment_families': 2, 'independent_episodes': 'not established by these counts'}

Applies when: When new market descriptions or similar legal-sensitive materials need sign-off from legal trading lawyers.

Exceptions: Unknown; may not apply if Tana is unavailable or if the matter is outside her domain.

Alternative: Another coordinator might handle legal routing for different projects, or Tana's role is temporary.

Uncertainty: Only one email shows Tana forwarding descriptions; no other evidence confirms her role as gatekeeper.

Next query: Find emails where Tana Jones coordinates legal sign-off for other documents or where another person handles such routing.

Prediction: Future emails will show Tana Jones coordinating legal sign-off for other documents or being consulted for special legal projects.

Hypothesis `hypothesis-18c76bbcbb8d41e6ab9ba2db98cb7c16`; transfer tested: false.

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:857db9f02e6d0b14`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

Source `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c`; evidence `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279:79af274ef52857a7`; origin `enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473`.

Attribution and exact offsets: `{"segment_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:segment:0:279", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:13:00 -0700", "segment_source_family": "enron-segment:45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "segment_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "attribution_status": "unverified_header_claim", "document_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "span_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279", "start": 0, "end": 279, "quote": "Awais,\n\nI have forwarded the descriptions you have sent us thus far to the respective \nLegal Trading Lawyers to sign off as far any legal issues we may have with \nthe descriptions.  I understand your deadline is the end of the week.\n\nWhen can I expect the remaining descriptions?", "quote_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "independence_status": "not_established", "raw_sha256": "49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "body_sha256": "11fc2b55e6d8082c4012d2a78beaf77ab478f459b95522fd04bd03b0841367b8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/247.", "source_family": "enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Awais,
> 
> I have forwarded the descriptions you have sent us thus far to the respective 
> Legal Trading Lawyers to sign off as far any legal issues we may have with 
> the descriptions.  I understand your deadline is the end of the week.
> 
> When can I expect the remaining descriptions?

Source `mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6`; evidence `mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:0:205:b03d9dc2eddc90f2`; origin `enron-authored:ff447c441eb02129f2150cc5fe4e4d521387d5a5a95a6fb4accb398a5e5c9215`.

Attribution and exact offsets: `{"segment_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:segment:0:205", "segment_kind": "authored", "claimed_sender": "steven.kean@enron.com", "claimed_date": "Mon, 30 Aug 1999 02:42:00 -0700", "segment_source_family": "enron-segment:3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "segment_fingerprint": "3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "attribution_status": "unverified_header_claim", "document_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6", "span_id": "mail-35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6:0:205", "start": 0, "end": 205, "quote": "Another bit of background re Frankfurt (see below).  I would be a little bit \nmore insistent on German Consulate support than Herr Sturm suggests \n(otherwise this could become a black hole for your time).\n", "quote_fingerprint": "3ad457d27ce0ad4c5bcf6afd1922d97564cb7343a8e723f46dec56216721ccde", "independence_status": "not_established", "raw_sha256": "35067dca17a155aad8ccfebca425839b779a034843e36d16d9bd368d5159d7f6", "body_sha256": "d8355135268aa1cb53c8d3bdb9b823baf4caf4a6b1811fe341118924b6919b28", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/calendar/untitled/127.", "source_family": "enron-authored:ff447c441eb02129f2150cc5fe4e4d521387d5a5a95a6fb4accb398a5e5c9215", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Another bit of background re Frankfurt (see below).  I would be a little bit 
> more insistent on German Consulate support than Herr Sturm suggests 
> (otherwise this could become a black hole for your time).
> 

Source `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c`; evidence `mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279:f441252fb452e676`; origin `enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473`.

Attribution and exact offsets: `{"segment_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:segment:0:279", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Wed, 01 Sep 1999 10:13:00 -0700", "segment_source_family": "enron-segment:45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "segment_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "attribution_status": "unverified_header_claim", "document_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "span_id": "mail-49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c:0:279", "start": 0, "end": 279, "quote": "Awais,\n\nI have forwarded the descriptions you have sent us thus far to the respective \nLegal Trading Lawyers to sign off as far any legal issues we may have with \nthe descriptions.  I understand your deadline is the end of the week.\n\nWhen can I expect the remaining descriptions?", "quote_fingerprint": "45bb45cc5d42297c693e5df773b8de6a8980c958ff29cd43ae91b3fe35d3f15a", "independence_status": "not_established", "raw_sha256": "49341df2f901555800250780d6ac2cc96910faf3361a6d4cba6f4ed1f0b2240c", "body_sha256": "11fc2b55e6d8082c4012d2a78beaf77ab478f459b95522fd04bd03b0841367b8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/247.", "source_family": "enron-authored:f555627f1871622662da48e9a66c4beefbef66e66e6d68f09cd7252e4141c473", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": false, "next_read": null}`

> Awais,
> 
> I have forwarded the descriptions you have sent us thus far to the respective 
> Legal Trading Lawyers to sign off as far any legal issues we may have with 
> the descriptions.  I understand your deadline is the end of the week.
> 
> When can I expect the remaining descriptions?

Source `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9`; evidence `mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301:02d086fc33babefc`; origin `enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86`.

Attribution and exact offsets: `{"segment_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:segment:601:1357", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "09/01/99 06:58 PM", "segment_source_family": "enron-segment:86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "segment_fingerprint": "86ade902b592eefe6e0fc7f676856bbfcd8e07fc96deaa50df5107630868a207", "attribution_status": "unverified_header_claim", "document_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "span_id": "mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9:601:1301", "start": 601, "end": 1301, "quote": "\nEffective immediately, all questions from the confirmation desk to legal \nshould be routed to a designated paralegal on a quarterly basis (with the \nexception of the very first rotation) as follows:\n\nSusan Bailey - X34737  September 1, 1999 - December 31, 1999\nSusan Flynn  -  X30975                    January 1, 2000       - March 31, \n2000\nMarie Heard -  X33907                     April 1, 2000             - June \n30, 2000\n\nYou will be advised of subsequent rotations.  Please do NOT route calls to \nTana Jones who will be spending most of her time working on special projects \nfor our group.\n\nThis procedure should not affect any existing arrangements you may have with \na particular attorney.", "quote_fingerprint": "a2931a4e7d1e5bad2a11b9a4a1b2ff7e0b4785b063d7d57318642970f6504766", "independence_status": "not_established", "raw_sha256": "68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9", "body_sha256": "aa876dde4780bd176fa9448e87ff9969d8dbef4653634f5f2c313f5906a3b600", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/458.", "source_family": "enron-authored:359859f746af6d6fb6b7480dacf15267206c1fe778559229b906482a92a00b86", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-68963f1ed6e5774791df98837014892aac17ff73553ef1215675ed702bb553b9 1301"}`

> 
> Effective immediately, all questions from the confirmation desk to legal 
> should be routed to a designated paralegal on a quarterly basis (with the 
> exception of the very first rotation) as follows:
> 
> Susan Bailey - X34737  September 1, 1999 - December 31, 1999
> Susan Flynn  -  X30975                    January 1, 2000       - March 31, 
> 2000
> Marie Heard -  X33907                     April 1, 2000             - June 
> 30, 2000
> 
> You will be advised of subsequent rotations.  Please do NOT route calls to 
> Tana Jones who will be spending most of her time working on special projects 
> for our group.
> 
> This procedure should not affect any existing arrangements you may have with 
> a particular attorney.

**contrasts / revise**

Frank Davis sends a new counterparty/product matrix with sections for approved, second approved, and unreviewed counterparties, plus new product types. This is an explicit instruction to update systems, not a tacit rule.

Source `mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da`; evidence `mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:0:700:f0f937539b980e5f`; origin `enron-authored:38c2abba0b1a96038deefec45fc2ebf1a908969dd978e206de53f6afde414312`.

Attribution and exact offsets: `{"segment_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:segment:0:825", "segment_kind": "authored", "claimed_sender": "frank.davis@enron.com", "claimed_date": "Wed, 08 Sep 1999 02:07:00 -0700", "segment_source_family": "enron-segment:601c582ec90fac6b96439c141892baf8e132abc7763492275a3118227d6e37ac", "segment_fingerprint": "601c582ec90fac6b96439c141892baf8e132abc7763492275a3118227d6e37ac", "attribution_status": "unverified_header_claim", "document_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da", "span_id": "mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da:0:700", "start": 0, "end": 700, "quote": "Debbie/Tom,\n\nAttached is a new version of the counterparty and product type matrix.  The \ncounterparties are broken into three sections.  The first section contains \ncounterparties that were included in credits original approved list with \nlimits noted.  The second section contains counterparties that were included \nin credits second approved list without any limits noted.  The third and last \nsection contains counterparties that will be included in the initial \nmailshot, but have not yet been reviewed by credit.  Please note that there \nare also new product types in row 7 that were not on any of the matrices you \nhave previously reviewed.  These new product types are highlighted in yellow \n", "quote_fingerprint": "e6287fe99bf988639fc3769fc3ce32a9f86a2f53756d8fcd2fe92ea2e5a95d90", "independence_status": "not_established", "raw_sha256": "5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da", "body_sha256": "49f7644b25c770cb02628c53a42a9e6723ab2972355f1547940459be7a28d6d7", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/online_trading/294.", "source_family": "enron-authored:38c2abba0b1a96038deefec45fc2ebf1a908969dd978e206de53f6afde414312", "synthetic": false, "claim_status": "interpretation", "excerpt_truncated": true, "next_read": "read: mail-5620ebf1bd369f86e47d990e17a2c1287bbfd4c28eb686178df11a47ecb2b8da 700"}`

> Debbie/Tom,
> 
> Attached is a new version of the counterparty and product type matrix.  The 
> counterparties are broken into three sections.  The first section contains 
> counterparties that were included in credits original approved list with 
> limits noted.  The second section contains counterparties that were included 
> in credits second approved list without any limits noted.  The third and last 
> section contains counterparties that will be included in the initial 
> mailshot, but have not yet been reviewed by credit.  Please note that there 
> are also new product types in row 7 that were not on any of the matrices you 
> have previously reviewed.  These new product types are highlighted in yellow 
> 

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:32:02.136083+00:00",
  "window": 1,
  "virtual_time": "1999-09-08T16:22:00+00:00",
  "arrival_sequence": 4000,
  "admitted": 4000,
  "selected": 32,
  "duplicate_gated": 2013,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```
