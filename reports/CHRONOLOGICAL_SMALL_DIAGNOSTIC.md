# Chronological swarm: tacit knowledge from arriving emails

Run `replay-run-2e65401d5c554abb86335e162950acac` · model `deepseek-v4-flash` · status **partial**

The objective is to infer unwritten routines, implicit expectations, contextual exceptions, and expertise dependencies. These are provisional model interpretations, not validated organizational rules. Discovery time is the replay cursor; inline quoted dates do not backdate knowledge. No fraud-finding objective or retrospective case queries were supplied.

Messages admitted to searchable history greatly outnumber messages inspected by the swarm. Exact quotation checks establish source text, not the correctness of an inferred rule. Model pretraining knowledge is not controlled by the temporal retrieval boundary.

## Protocol and resource use

```json
{
  "id": "replay-run-2e65401d5c554abb86335e162950acac",
  "mode": "chronological_replay",
  "query": "Discover implicit routines and expectations",
  "model": "deepseek-v4-flash",
  "created_at": "2026-09-09T22:18:20.729117+00:00",
  "status": "partial",
  "phase": "revise",
  "config": {
    "batch_size": 2000,
    "max_windows": 2,
    "turns_per_window": 2,
    "documents_per_window": 32,
    "retrieval_per_peer": 1,
    "max_output_tokens": 1800,
    "synthetic": false,
    "seed": 7
  },
  "windows": [
    {
      "window": 1,
      "virtual_time": "1999-07-13T09:39:00+00:00",
      "arrival_sequence": 2000,
      "admitted": 2000,
      "selected": 32,
      "duplicate_gated": 987,
      "agent_invocations": 8,
      "gate_reason": "novel_selected"
    },
    {
      "window": 2,
      "virtual_time": "1999-09-08T16:22:00+00:00",
      "arrival_sequence": 4000,
      "admitted": 2000,
      "selected": 32,
      "duplicate_gated": 1026,
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
    "accepted": 64,
    "rejected": 15
  },
  "replay": {
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrived": 4000,
    "initial_arrived": 0,
    "selected": 64,
    "skipped": 3936,
    "model_calls": 16,
    "windows": 2,
    "eligible": 516182,
    "coverage_complete": false,
    "gate_reason": "novel_selected",
    "retrieval_queries": 8,
    "prompt_exposed_documents": 67
  },
  "coverage_limitations": [
    "All eligible arrivals can be admitted; only sampled novel documents are shown to models.",
    "Unselected or duplicate-gated messages are not established irrelevant.",
    "Outer-header chronology and inline attribution are not authenticated human knowledge times.",
    "Quoted support and later-arrival prediction checks do not validate tacit knowledge transfer."
  ],
  "predictions": [
    {
      "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
      "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
      "prediction": "Future emails about confirmations will reference the Confirmation Desk or similar routing.",
      "window": 1,
      "arrival_sequence": 2000
    },
    {
      "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
      "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
      "prediction": "Future emails will show similar instructions to keep documentation centralized in Houston.",
      "window": 1,
      "arrival_sequence": 2000
    }
  ],
  "runtime_usage": {
    "calls": 16,
    "tokens": 110212,
    "cost": 0.056822479999999995
  },
  "finished_at": "2026-09-09T22:18:53.300225+00:00"
}
```

## Observation timeline

### 1999-07-13T09:39:00+00:00 — review window 1

**routines / observe**

The email thread about the HoustonStreet press release disclaimer reveals a potential tacit practice where Enron employees question legal disclaimers and seek internal clarification before accepting external legal advice, indicating a culture of challenging conservative legal positions. Other emails show routine coordination and document handling without explicit policies.

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:0:196:201ec824fb4d0ce8`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:0:196", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 29 Jun 1999 07:00:00 -0700", "segment_source_family": "enron-segment:d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "segment_fingerprint": "d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:0:196", "start": 0, "end": 196, "quote": "We think the HoustonStreet disclaimer is not just overkill but entirely \nunnecessary.  And I plan to remind all of you of this the next time you claim \nthe Enron lawyers are too conservative!\n\n\n\n\n", "quote_fingerprint": "d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> We think the HoustonStreet disclaimer is not just overkill but entirely 
> unnecessary.  And I plan to remind all of you of this the next time you claim 
> the Enron lawyers are too conservative!
> 
> 
> 
> 
> 

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:492:846:23b2a812630e644d`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:492:846", "segment_kind": "forwarded", "claimed_sender": "Elena Kapralova", "claimed_date": "06/29/99 09:03 AM", "segment_source_family": "enron-segment:ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "segment_fingerprint": "ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:492:846", "start": 492, "end": 846, "quote": "\nRahil,\n\nAccording to Clifford Chance, our European Legal Advisor, this disclaimer \nmust be driven by regulatory and investment issues in US, i.e. SEC \nrequirements. \nIn Europe, the paragraph like this would not be necessary in the ress \nrelease, but as our press release will be issued in US, it may need further \ninvestigation with US lawyers.... \n\n\n\n\n", "quote_fingerprint": "ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> 
> Rahil,
> 
> According to Clifford Chance, our European Legal Advisor, this disclaimer 
> must be driven by regulatory and investment issues in US, i.e. SEC 
> requirements. 
> In Europe, the paragraph like this would not be necessary in the ress 
> release, but as our press release will be issued in US, it may need further 
> investigation with US lawyers.... 
> 
> 
> 
> 
> 

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:1078:1778:fe194645e873e820`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:1078:9102", "segment_kind": "forwarded", "claimed_sender": "Rahil Jafry", "claimed_date": "29/06/99 11:10", "segment_source_family": "enron-segment:5b4db3f90d12aa7d1dddfe47ece2a2a35ff45a4fd46a08701d71770be68d504e", "segment_fingerprint": "5b4db3f90d12aa7d1dddfe47ece2a2a35ff45a4fd46a08701d71770be68d504e", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:1078:1778", "start": 1078, "end": 1778, "quote": "\nPls. note the disclaimer at the end of the message (highlighted in red).\nJustin/Gary, is there a specific legal or PR related reason for this?\nWould we have to make similar disclaimers in our press release?  Gary and I\nare working on draft press releases currently and will forward those for\nyour approval soon.\n\n- R\n******************************************************************************\n***********\n\nTrading Megawatts On the Web: Houston Street Exchange\nLaunches First Fully Web-Based Trading Floor and Portal for\nthe Electric Power Industry\n\nBusiness Wire - June 28, 1999 08:32\nPORTSMOUTH, N.H.--(BUSINESS WIRE)--June 28, 1999-- HoustonStreet.com alters\npower trading\nlandscape by increasi", "quote_fingerprint": "0a335fe8ea2044b4e1d96970856afa6d36ee13e00551eec69fc1f253c7a313cd", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> 
> Pls. note the disclaimer at the end of the message (highlighted in red).
> Justin/Gary, is there a specific legal or PR related reason for this?
> Would we have to make similar disclaimers in our press release?  Gary and I
> are working on draft press releases currently and will forward those for
> your approval soon.
> 
> - R
> ******************************************************************************
> ***********
> 
> Trading Megawatts On the Web: Houston Street Exchange
> Launches First Fully Web-Based Trading Floor and Portal for
> the Electric Power Industry
> 
> Business Wire - June 28, 1999 08:32
> PORTSMOUTH, N.H.--(BUSINESS WIRE)--June 28, 1999-- HoustonStreet.com alters
> power trading
> landscape by increasi

**expectations / observe**

The observed emails show routine legal and administrative tasks, but no clear pattern of tacit knowledge emerges from the limited sample. There are references to forwarding documents to specific desks and using legal assistants for research, but these are explicit instructions or common practices, not unwritten rules. No strong hypotheses can be formed without more contextual evidence.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a`; evidence `mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:0:700:c8ed6ed0f6d68f8a`; origin `enron-authored:1672d27358456954be28d68a91da5ceaf4a7c7595059239d4720129dbc0500e6`.

Attribution and exact offsets: `{"segment_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:segment:0:739", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Mon, 18 Jan 1999 07:10:00 -0800", "segment_source_family": "enron-segment:3adde88b5119039b924dd090064f7cc58afe7e9ef215bcba2ac77ee27767e989", "segment_fingerprint": "3adde88b5119039b924dd090064f7cc58afe7e9ef215bcba2ac77ee27767e989", "attribution_status": "unverified_header_claim", "document_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a", "span_id": "mail-4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a:0:700", "start": 0, "end": 700, "quote": "Thanks for your note.  It is kind of exciting.\n\nI think this attachment is probably the treaty you want.  I'm sorry it didn't \n\"save\" better but I think you can probably print it out legibly.  I have a \ncopy printed from Westlaw.  Let me know if you want me to fax it.\n\n\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 01/18/99 10:16 AM\nTo: Mark - ECT Legal Taylor@ECT\ncc:  \nSubject: Congratulations\n\n\n\n\nMark, congratulations on your promotion to Vice President.\n\nOn a more mundane matter could you have a clerk or legal assistant get me a \ncopy of the Bilateral Investment Treaty between the US and Argentina.  Our \nregulatory and commercial group wants to leave no stone unturned in their \nsear", "quote_fingerprint": "e5e81c88bba67e691fe235f510ffa1a43a4198e9cec9263408d2c033cb3c8ba8", "independence_status": "not_established", "raw_sha256": "4da722b0253a1040d7f07231fda8666d8e091c9ed7b8a79b1c9c5cf25e97d98a", "body_sha256": "9b91c21a6993e65e68fdfc1326d8128d63c360fb9fa5e0753ae9e67ccf2fc770", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/123.", "source_family": "enron-authored:1672d27358456954be28d68a91da5ceaf4a7c7595059239d4720129dbc0500e6", "synthetic": false, "claim_status": "interpretation"}`

> Thanks for your note.  It is kind of exciting.
> 
> I think this attachment is probably the treaty you want.  I'm sorry it didn't 
> "save" better but I think you can probably print it out legibly.  I have a 
> copy printed from Westlaw.  Let me know if you want me to fax it.
> 
> 
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 01/18/99 10:16 AM
> To: Mark - ECT Legal Taylor@ECT
> cc:  
> Subject: Congratulations
> 
> 
> 
> 
> Mark, congratulations on your promotion to Vice President.
> 
> On a more mundane matter could you have a clerk or legal assistant get me a 
> copy of the Bilateral Investment Treaty between the US and Argentina.  Our 
> regulatory and commercial group wants to leave no stone unturned in their 
> sear

Source `mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0`; evidence `mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0:0:73:e9d1624f098fce9f`; origin `enron-raw:39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0`.

Attribution and exact offsets: `{"segment_id": "mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0:segment:0:73", "segment_kind": "authored", "claimed_sender": "larry.hunter@enron.com", "claimed_date": "Thu, 08 Jul 1999 00:41:00 -0700", "segment_source_family": "enron-span:mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0:0:73", "segment_fingerprint": "7a639b7e46d659728686ef276c54a169ef0eefd04951bd79248f6e68dd25c124", "attribution_status": "unverified_header_claim", "document_id": "mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0", "span_id": "mail-39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0:0:73", "start": 0, "end": 73, "quote": "Sara,\n\nEnclosed is the Portucel confirm for your records.\n\nThanks,\nJoe\n\n\n", "quote_fingerprint": "7a639b7e46d659728686ef276c54a169ef0eefd04951bd79248f6e68dd25c124", "independence_status": "not_established", "raw_sha256": "39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0", "body_sha256": "39174fdefc81c5183ce01f860dd6a5f17c00122a385d2d365484f005965ae1b1", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/164.", "source_family": "enron-raw:39fbee07d8e81a0d385bc1957f35ebb9a3e35d425e38416bd9102e34df3a0ce0", "synthetic": false, "claim_status": "interpretation"}`

> Sara,
> 
> Enclosed is the Portucel confirm for your records.
> 
> Thanks,
> Joe
> 
> 
> 

**expertise / observe**

The emails show informal coordination around risk matrices, regulatory due diligence, and internal processes, with references to specific individuals and unspoken expectations about information sharing and task ownership.

Source `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be`; evidence `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:0:243:261e05e80c61330e`; origin `enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59`.

Attribution and exact offsets: `{"segment_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:segment:0:243", "segment_kind": "authored", "claimed_sender": "steven.kean@enron.com", "claimed_date": "Wed, 10 Mar 1999 10:03:00 -0800", "segment_source_family": "enron-segment:ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "segment_fingerprint": "ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "attribution_status": "unverified_header_claim", "document_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "span_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:0:243", "start": 0, "end": 243, "quote": "FYI.  I had started an informal discussion group to work on \npolitical/regulatory risk..  I included Jane, Jim Bouillian, and Scott Gahn.  \nJane sent me the atached as an example of how her group approaches issues in \nthe acquisition context.\n", "quote_fingerprint": "ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "independence_status": "not_established", "raw_sha256": "0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "body_sha256": "839bf533f8039c5bab7c20e136c383aee803689de4fb702c6d3bc81c8fff0cb8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/discussion_threads/122.", "source_family": "enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59", "synthetic": false, "claim_status": "interpretation"}`

> FYI.  I had started an informal discussion group to work on 
> political/regulatory risk..  I included Jane, Jim Bouillian, and Scott Gahn.  
> Jane sent me the atached as an example of how her group approaches issues in 
> the acquisition context.
> 

Source `mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332`; evidence `mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332:0:494:44414038be57a752`; origin `enron-authored:96d98d1c294d466f880b02925b57a881b64a8e1e3891e36cd86c463a4bce5524`.

Attribution and exact offsets: `{"segment_id": "mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332:segment:0:494", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 02:53:00 -0700", "segment_source_family": "enron-segment:8ee239188a012528c12624719e7db39ab7502a6acf053e823c3eab71e343d710", "segment_fingerprint": "8ee239188a012528c12624719e7db39ab7502a6acf053e823c3eab71e343d710", "attribution_status": "unverified_header_claim", "document_id": "mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332", "span_id": "mail-1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332:0:494", "start": 0, "end": 494, "quote": "The draft is ready to go but we need one (1) item from credit.  Hopefully, \nthis should be resolved within the hour!  Do you want a copy?  SS\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 09:04 AM\nTo: Sara Shackleton@ECT\ncc:  \nSubject: PC draft\n\n\n\n\nAre we any closer to having a draft ready?  The business guys lost an \nopportunity to trade a couple of weeks ago when power prices shot upward. \nPrices are now coming back down and they would like to be able to transact \nsoon.\n\n\n", "quote_fingerprint": "8ee239188a012528c12624719e7db39ab7502a6acf053e823c3eab71e343d710", "independence_status": "not_established", "raw_sha256": "1e1e7de3438147a7287b46185cff2a555c2aaf64b0a05c4ce7a47b74fe970332", "body_sha256": "fbd09aef60bbf9d9b773bbb1d41178a067211055860abd752b0d78eb4455c777", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/85.", "source_family": "enron-authored:96d98d1c294d466f880b02925b57a881b64a8e1e3891e36cd86c463a4bce5524", "synthetic": false, "claim_status": "interpretation"}`

> The draft is ready to go but we need one (1) item from credit.  Hopefully, 
> this should be resolved within the hour!  Do you want a copy?  SS
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 09:04 AM
> To: Sara Shackleton@ECT
> cc:  
> Subject: PC draft
> 
> 
> 
> 
> Are we any closer to having a draft ready?  The business guys lost an 
> opportunity to trade a couple of weeks ago when power prices shot upward. 
> Prices are now coming back down and they would like to be able to transact 
> soon.
> 
> 
> 

Source `mail-3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65`; evidence `mail-3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65:0:352:460a5c8348634ef9`; origin `enron-authored:352e6253a899f97990fff236b3933d28ed847f9568b5771f8e6d1433fb28c192`.

Attribution and exact offsets: `{"segment_id": "mail-3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65:segment:0:352", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 20 Apr 1999 04:07:00 -0700", "segment_source_family": "enron-segment:fb34b7d2ad8ff2efcabae5b9176951aa42dd2c94386e224773a2b65e0c76fd8a", "segment_fingerprint": "fb34b7d2ad8ff2efcabae5b9176951aa42dd2c94386e224773a2b65e0c76fd8a", "attribution_status": "unverified_header_claim", "document_id": "mail-3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65", "span_id": "mail-3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65:0:352", "start": 0, "end": 352, "quote": "Scott:\n\nI have a call scheduled with Martin for tomorrow morning to discuss these \nCFTC  issues.  I'll let you know how it goes.\n\nI have also not forgotten your request for my view on Martin's tenure in \nHouston.  I have mixed feelings that are difficult to put down in writing and \nI'm hoping we can take a few minutes in New Orleans to discuss.\n\nMark", "quote_fingerprint": "fb34b7d2ad8ff2efcabae5b9176951aa42dd2c94386e224773a2b65e0c76fd8a", "independence_status": "not_established", "raw_sha256": "3ec305ab264c9141b3532c152b9b47e43fc32acf9d8b7ad36b18ab88896f5e65", "body_sha256": "09bda3709ac9cc8022a2ccb7f6bd9d66c7ed30c83888ed7b34a9977d6f41ff1e", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/246.", "source_family": "enron-authored:352e6253a899f97990fff236b3933d28ed847f9568b5771f8e6d1433fb28c192", "synthetic": false, "claim_status": "interpretation"}`

> Scott:
> 
> I have a call scheduled with Martin for tomorrow morning to discuss these 
> CFTC  issues.  I'll let you know how it goes.
> 
> I have also not forgotten your request for my view on Martin's tenure in 
> Houston.  I have mixed feelings that are difficult to put down in writing and 
> I'm hoping we can take a few minutes in New Orleans to discuss.
> 
> Mark

**contrasts / observe**

The emails reveal coordination issues between Houston and London/other offices regarding deal documentation, legal reviews, and personnel reporting. There are indications of unwritten practices about where documentation originates and how reporting lines are determined.

Source `mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b`; evidence `mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:0:618:d63b172119c85389`; origin `enron-authored:c116c5780a1f2976cd3eab81555d2b55668954824ac90f80d58a431d4804e8e6`.

Attribution and exact offsets: `{"segment_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:segment:0:618", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 14 May 1999 04:43:00 -0700", "segment_source_family": "enron-segment:8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "segment_fingerprint": "8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "attribution_status": "unverified_header_claim", "document_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b", "span_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:0:618", "start": 0, "end": 618, "quote": "London traders are transacting from London in the names of both ECT(Houston) \nand ECTRIC(London) with DAPSA and Sempra.  The deal tickets are still being \nsent to Houston for confirmation preparation (rather than from London where \nthe trade is actually consummated).  With respect to Sempra, we were \npreviously advised that Sempra would not transact directly with ECTRIC absent \na Master but this cannot be accurate because some Sempra deal tickets recite \nECTRIC's name.    \n\nThis message is FYI if there are no regulatory issues involved.\n\nHouston will certainly document back-to-back internal transactions. \n\nSara", "quote_fingerprint": "8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "independence_status": "not_established", "raw_sha256": "0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b", "body_sha256": "1c7f289ff89337bcbf0a9121c9c9e88d30ceed454afa989f3cfe0fc8783b3310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/37.", "source_family": "enron-authored:c116c5780a1f2976cd3eab81555d2b55668954824ac90f80d58a431d4804e8e6", "synthetic": false, "claim_status": "interpretation"}`

> London traders are transacting from London in the names of both ECT(Houston) 
> and ECTRIC(London) with DAPSA and Sempra.  The deal tickets are still being 
> sent to Houston for confirmation preparation (rather than from London where 
> the trade is actually consummated).  With respect to Sempra, we were 
> previously advised that Sempra would not transact directly with ECTRIC absent 
> a Master but this cannot be accurate because some Sempra deal tickets recite 
> ECTRIC's name.    
> 
> This message is FYI if there are no regulatory issues involved.
> 
> Houston will certainly document back-to-back internal transactions. 
> 
> Sara

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

Source `mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9`; evidence `mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:2620:2889:9ef87732aabb5f58`; origin `enron-authored:7949400ff5062e572b08432966db2852ce00f6fdc686e10ecde8216c26b349df`.

Attribution and exact offsets: `{"segment_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:segment:2620:2924", "segment_kind": "forwarded", "claimed_sender": "Karen E Campos", "claimed_date": "02/10/99 07:27 PM", "segment_source_family": "enron-segment:8a73981b353796a76d97b9de4f16f8b7277e6362c965921e230d90b80526a111", "segment_fingerprint": "8a73981b353796a76d97b9de4f16f8b7277e6362c965921e230d90b80526a111", "attribution_status": "unverified_header_claim", "document_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9", "span_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:2620:2889", "start": 2620, "end": 2889, "quote": "\nRandy/ Scott:\n\nI don't know if you remember or not, but last year I had a question as to who \nBrent would report to and who's budget it should hit.\nHe's now in Scott rc but he's a Sr. Counsel.  Shouldn't he be in Randy's rc? \nPlease advise.\n\nThanks,\nKaren\n\n\n\n\n\n\n\n\n\n\n\n\n", "quote_fingerprint": "b307ce1b97e28b1b37250cb7465bb4f82861ded8451b9baf215a7203ed964b4c", "independence_status": "not_established", "raw_sha256": "93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9", "body_sha256": "98bcdbe5a365e954a1c648b1c25426ae9e0b63843fdf76397422d5a22a8505db", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/168.", "source_family": "enron-authored:7949400ff5062e572b08432966db2852ce00f6fdc686e10ecde8216c26b349df", "synthetic": false, "claim_status": "interpretation"}`

> 
> Randy/ Scott:
> 
> I don't know if you remember or not, but last year I had a question as to who 
> Brent would report to and who's budget it should hit.
> He's now in Scott rc but he's a Sr. Counsel.  Shouldn't he be in Randy's rc? 
> Please advise.
> 
> Thanks,
> Karen
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 

**routines / revise**

The email thread about the HoustonStreet press release disclaimer reveals a potential tacit practice where Enron employees question legal disclaimers and seek internal clarification before accepting external legal advice, indicating a culture of challenging conservative legal positions. Other emails show routine coordination and document handling without explicit policies.

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:0:196:201ec824fb4d0ce8`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:0:196", "segment_kind": "authored", "claimed_sender": "mark.taylor@enron.com", "claimed_date": "Tue, 29 Jun 1999 07:00:00 -0700", "segment_source_family": "enron-segment:d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "segment_fingerprint": "d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:0:196", "start": 0, "end": 196, "quote": "We think the HoustonStreet disclaimer is not just overkill but entirely \nunnecessary.  And I plan to remind all of you of this the next time you claim \nthe Enron lawyers are too conservative!\n\n\n\n\n", "quote_fingerprint": "d52a96dd4b2a30deec87b8742f18d548c02ddca0d9707fae93258c081181d391", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> We think the HoustonStreet disclaimer is not just overkill but entirely 
> unnecessary.  And I plan to remind all of you of this the next time you claim 
> the Enron lawyers are too conservative!
> 
> 
> 
> 
> 

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:492:846:23b2a812630e644d`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:492:846", "segment_kind": "forwarded", "claimed_sender": "Elena Kapralova", "claimed_date": "06/29/99 09:03 AM", "segment_source_family": "enron-segment:ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "segment_fingerprint": "ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:492:846", "start": 492, "end": 846, "quote": "\nRahil,\n\nAccording to Clifford Chance, our European Legal Advisor, this disclaimer \nmust be driven by regulatory and investment issues in US, i.e. SEC \nrequirements. \nIn Europe, the paragraph like this would not be necessary in the ress \nrelease, but as our press release will be issued in US, it may need further \ninvestigation with US lawyers.... \n\n\n\n\n", "quote_fingerprint": "ef9bd810df32405064a24ebf2a2068a022c742c4cef8541548a12c931c882dfd", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> 
> Rahil,
> 
> According to Clifford Chance, our European Legal Advisor, this disclaimer 
> must be driven by regulatory and investment issues in US, i.e. SEC 
> requirements. 
> In Europe, the paragraph like this would not be necessary in the ress 
> release, but as our press release will be issued in US, it may need further 
> investigation with US lawyers.... 
> 
> 
> 
> 
> 

Source `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450`; evidence `mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:1078:1778:fe194645e873e820`; origin `enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392`.

Attribution and exact offsets: `{"segment_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:segment:1078:9102", "segment_kind": "forwarded", "claimed_sender": "Rahil Jafry", "claimed_date": "29/06/99 11:10", "segment_source_family": "enron-segment:5b4db3f90d12aa7d1dddfe47ece2a2a35ff45a4fd46a08701d71770be68d504e", "segment_fingerprint": "5b4db3f90d12aa7d1dddfe47ece2a2a35ff45a4fd46a08701d71770be68d504e", "attribution_status": "unverified_header_claim", "document_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "span_id": "mail-24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450:1078:1778", "start": 1078, "end": 1778, "quote": "\nPls. note the disclaimer at the end of the message (highlighted in red).\nJustin/Gary, is there a specific legal or PR related reason for this?\nWould we have to make similar disclaimers in our press release?  Gary and I\nare working on draft press releases currently and will forward those for\nyour approval soon.\n\n- R\n******************************************************************************\n***********\n\nTrading Megawatts On the Web: Houston Street Exchange\nLaunches First Fully Web-Based Trading Floor and Portal for\nthe Electric Power Industry\n\nBusiness Wire - June 28, 1999 08:32\nPORTSMOUTH, N.H.--(BUSINESS WIRE)--June 28, 1999-- HoustonStreet.com alters\npower trading\nlandscape by increasi", "quote_fingerprint": "0a335fe8ea2044b4e1d96970856afa6d36ee13e00551eec69fc1f253c7a313cd", "independence_status": "not_established", "raw_sha256": "24f509de32537ed187eb6d6bd317d900300c6a16075283826260018a7481e450", "body_sha256": "5d134f8e2842763b28340a59bc108eb32c4bad60031e4a521f4a298072ed34c3", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/sent/327.", "source_family": "enron-authored:2924feafb1160e5fc3fbbaff47650d6d7568d1278e949d8ed9e0e2b1baf9c392", "synthetic": false, "claim_status": "interpretation"}`

> 
> Pls. note the disclaimer at the end of the message (highlighted in red).
> Justin/Gary, is there a specific legal or PR related reason for this?
> Would we have to make similar disclaimers in our press release?  Gary and I
> are working on draft press releases currently and will forward those for
> your approval soon.
> 
> - R
> ******************************************************************************
> ***********
> 
> Trading Megawatts On the Web: Houston Street Exchange
> Launches First Fully Web-Based Trading Floor and Portal for
> the Electric Power Industry
> 
> Business Wire - June 28, 1999 08:32
> PORTSMOUTH, N.H.--(BUSINESS WIRE)--June 28, 1999-- HoustonStreet.com alters
> power trading
> landscape by increasi

**expectations / revise**

The email evidence reveals recurring patterns of informal coordination and implicit expectations around document routing, legal review, and reporting lines, suggesting tacit practices beyond explicit instructions.

**Candidate rule — revision 1**

Confirmation-related documents are routed to the Confirmation Desk for handling, regardless of the originating office or individual.

Applies when: When a confirmation termination letter or similar confirmation document needs processing.

Exceptions: If the document is not confirmation-related or if specific instructions override the default routing.

Alternative: Routing may depend on the type of document or the recipient's role, not a blanket rule.

Uncertainty: Only one instance observed; no explicit policy cited.

Next query: all: confirmation desk termination letter

Prediction: Future emails about confirmations will reference the Confirmation Desk or similar routing.

Hypothesis `hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a`; transfer tested: false.

**Candidate rule — revision 1**

Legal documents intended for external customers must originate from Houston, with other offices only receiving blind copies and not being referenced in communications.

Applies when: When drafting or sending legal documents to customers, especially involving non-Houston offices.

Exceptions: If the customer is in a jurisdiction where local documentation is required, or if Houston explicitly delegates.

Alternative: The rule may apply only to certain types of documents or specific projects.

Uncertainty: Based on a single instruction from Brent Hendry; may not be a general practice.

Next query: all: blind copy customer documentation Houston

Prediction: Future emails will show similar instructions to keep documentation centralized in Houston.

Hypothesis `hypothesis-54af0a26f69245cfbfbdab226982a021`; transfer tested: false.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:6d82936102ef9e76`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:5bd13348a93eb074`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**expertise / revise**

The emails reveal informal coordination around risk matrices, regulatory due diligence, and internal processes, with references to specific individuals and unspoken expectations about information sharing and task ownership.

Source `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be`; evidence `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:0:243:261e05e80c61330e`; origin `enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59`.

Attribution and exact offsets: `{"segment_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:segment:0:243", "segment_kind": "authored", "claimed_sender": "steven.kean@enron.com", "claimed_date": "Wed, 10 Mar 1999 10:03:00 -0800", "segment_source_family": "enron-segment:ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "segment_fingerprint": "ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "attribution_status": "unverified_header_claim", "document_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "span_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:0:243", "start": 0, "end": 243, "quote": "FYI.  I had started an informal discussion group to work on \npolitical/regulatory risk..  I included Jane, Jim Bouillian, and Scott Gahn.  \nJane sent me the atached as an example of how her group approaches issues in \nthe acquisition context.\n", "quote_fingerprint": "ae1cb0cfe4c374107ae9655c79bdd39404edc3b6db020145f6eaff2c473d8b48", "independence_status": "not_established", "raw_sha256": "0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "body_sha256": "839bf533f8039c5bab7c20e136c383aee803689de4fb702c6d3bc81c8fff0cb8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/discussion_threads/122.", "source_family": "enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59", "synthetic": false, "claim_status": "interpretation"}`

> FYI.  I had started an informal discussion group to work on 
> political/regulatory risk..  I included Jane, Jim Bouillian, and Scott Gahn.  
> Jane sent me the atached as an example of how her group approaches issues in 
> the acquisition context.
> 

Source `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be`; evidence `mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:532:787:9aa6535525172088`; origin `enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59`.

Attribution and exact offsets: `{"segment_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:segment:532:787", "segment_kind": "forwarded", "claimed_sender": "\"Jane Wilson/ENRON_DEVELOPMENT\" AT ENRON_DEVELOPMENT@CCMAIL on 01/14/99", "claimed_date": null, "segment_source_family": "enron-segment:298677248be2d55b4fa0279104fdba73d830009cc3ece3482334c3c470bb816a", "segment_fingerprint": "298677248be2d55b4fa0279104fdba73d830009cc3ece3482334c3c470bb816a", "attribution_status": "unverified_header_claim", "document_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "span_id": "mail-0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be:532:787", "start": 532, "end": 787, "quote": "\n\nSubject:\nRisk Matrix\n\n---------------------------------\n\n\nAttached is a sample draft risk matrix that my group does on a regular basis \nin the process of regulatory due diligence.\n\n(See attached file: Guatemalariskmetrix.doc)\n - Guatemalariskmetrix.doc\n", "quote_fingerprint": "298677248be2d55b4fa0279104fdba73d830009cc3ece3482334c3c470bb816a", "independence_status": "not_established", "raw_sha256": "0cd4cb6553be4b02d041ef4c1797e439cb1e7a420b8bc9790835dc2b959534be", "body_sha256": "839bf533f8039c5bab7c20e136c383aee803689de4fb702c6d3bc81c8fff0cb8", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/kean-s/discussion_threads/122.", "source_family": "enron-authored:90a7c3a0e2c0d643de3de8827256270cb90c63e84ad97fee88533a8ceebe7a59", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> Subject:
> Risk Matrix
> 
> ---------------------------------
> 
> 
> Attached is a sample draft risk matrix that my group does on a regular basis 
> in the process of regulatory due diligence.
> 
> (See attached file: Guatemalariskmetrix.doc)
>  - Guatemalariskmetrix.doc
> 

**contrasts / revise**

The emails reveal coordination issues between Houston and London/other offices regarding deal documentation, legal reviews, and personnel reporting. There are indications of unwritten practices about where documentation originates and how reporting lines are determined.

Source `mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b`; evidence `mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:0:618:d63b172119c85389`; origin `enron-authored:c116c5780a1f2976cd3eab81555d2b55668954824ac90f80d58a431d4804e8e6`.

Attribution and exact offsets: `{"segment_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:segment:0:618", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 14 May 1999 04:43:00 -0700", "segment_source_family": "enron-segment:8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "segment_fingerprint": "8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "attribution_status": "unverified_header_claim", "document_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b", "span_id": "mail-0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b:0:618", "start": 0, "end": 618, "quote": "London traders are transacting from London in the names of both ECT(Houston) \nand ECTRIC(London) with DAPSA and Sempra.  The deal tickets are still being \nsent to Houston for confirmation preparation (rather than from London where \nthe trade is actually consummated).  With respect to Sempra, we were \npreviously advised that Sempra would not transact directly with ECTRIC absent \na Master but this cannot be accurate because some Sempra deal tickets recite \nECTRIC's name.    \n\nThis message is FYI if there are no regulatory issues involved.\n\nHouston will certainly document back-to-back internal transactions. \n\nSara", "quote_fingerprint": "8f5794d9b98d406e287b3aa8f1fb8959df63a3ce61225c9ef97ad13e6bb30766", "independence_status": "not_established", "raw_sha256": "0822a67f09faf66a5e12033a24daf2bae7b46afeb28cfc230cb00a80472fa94b", "body_sha256": "1c7f289ff89337bcbf0a9121c9c9e88d30ceed454afa989f3cfe0fc8783b3310", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/37.", "source_family": "enron-authored:c116c5780a1f2976cd3eab81555d2b55668954824ac90f80d58a431d4804e8e6", "synthetic": false, "claim_status": "interpretation"}`

> London traders are transacting from London in the names of both ECT(Houston) 
> and ECTRIC(London) with DAPSA and Sempra.  The deal tickets are still being 
> sent to Houston for confirmation preparation (rather than from London where 
> the trade is actually consummated).  With respect to Sempra, we were 
> previously advised that Sempra would not transact directly with ECTRIC absent 
> a Master but this cannot be accurate because some Sempra deal tickets recite 
> ECTRIC's name.    
> 
> This message is FYI if there are no regulatory issues involved.
> 
> Houston will certainly document back-to-back internal transactions. 
> 
> Sara

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

Source `mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9`; evidence `mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:2620:2889:9ef87732aabb5f58`; origin `enron-authored:7949400ff5062e572b08432966db2852ce00f6fdc686e10ecde8216c26b349df`.

Attribution and exact offsets: `{"segment_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:segment:2620:2924", "segment_kind": "forwarded", "claimed_sender": "Karen E Campos", "claimed_date": "02/10/99 07:27 PM", "segment_source_family": "enron-segment:8a73981b353796a76d97b9de4f16f8b7277e6362c965921e230d90b80526a111", "segment_fingerprint": "8a73981b353796a76d97b9de4f16f8b7277e6362c965921e230d90b80526a111", "attribution_status": "unverified_header_claim", "document_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9", "span_id": "mail-93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9:2620:2889", "start": 2620, "end": 2889, "quote": "\nRandy/ Scott:\n\nI don't know if you remember or not, but last year I had a question as to who \nBrent would report to and who's budget it should hit.\nHe's now in Scott rc but he's a Sr. Counsel.  Shouldn't he be in Randy's rc? \nPlease advise.\n\nThanks,\nKaren\n\n\n\n\n\n\n\n\n\n\n\n\n", "quote_fingerprint": "b307ce1b97e28b1b37250cb7465bb4f82861ded8451b9baf215a7203ed964b4c", "independence_status": "not_established", "raw_sha256": "93b91d18b7d3a1d7533e13d556fcaec33db34a0def52bf4d43d74e504876aff9", "body_sha256": "98bcdbe5a365e954a1c648b1c25426ae9e0b63843fdf76397422d5a22a8505db", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/168.", "source_family": "enron-authored:7949400ff5062e572b08432966db2852ce00f6fdc686e10ecde8216c26b349df", "synthetic": false, "claim_status": "interpretation"}`

> 
> Randy/ Scott:
> 
> I don't know if you remember or not, but last year I had a question as to who 
> Brent would report to and who's budget it should hit.
> He's now in Scott rc but he's a Sr. Counsel.  Shouldn't he be in Randy's rc? 
> Please advise.
> 
> Thanks,
> Karen
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 

### 1999-09-08T16:22:00+00:00 — review window 2

**routines / observe**

The emails show informal coordination around document routing and legal review, with hints of unwritten practices about centralizing customer-facing documentation in Houston and routing confirmations to a specific desk. However, evidence is limited and mostly single instances.

Source `mail-2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55`; evidence `mail-2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55:0:561:ccb49c5d7f5b0e0a`; origin `enron-authored:e82be5e988deae44bf6e76940ff096cce48bd0769e24275219ab6e8332280c76`.

Attribution and exact offsets: `{"segment_id": "mail-2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55:segment:0:561", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Thu, 02 Sep 1999 07:39:00 -0700", "segment_source_family": "enron-segment:ef2bcd1b8837cc8e888ee59f959c3641d6a7ff1bc3170feae3a83a5c5f2dabc5", "segment_fingerprint": "ef2bcd1b8837cc8e888ee59f959c3641d6a7ff1bc3170feae3a83a5c5f2dabc5", "attribution_status": "unverified_header_claim", "document_id": "mail-2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55", "span_id": "mail-2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55:0:561", "start": 0, "end": 561, "quote": "Please take a look at the proposed language.  You will need to consider the \ntime period before which a Market Disruption Event will kick in.:\n\nPostponement:  For the purposes of the definition of \"Price Source \nDisruption,\" as set forth in Section 7.4(c)(i) of the Commodity Definitions,\n   the Maximum Days of Disruption shall be [thirty-two/sixty-four] days after \nthe last date of publication of World Pulp Monthly,\n   or any successor publication, published by Resource Information Systems, \nInc. or its successor for the applicable \n   Calculation Period.", "quote_fingerprint": "ef2bcd1b8837cc8e888ee59f959c3641d6a7ff1bc3170feae3a83a5c5f2dabc5", "independence_status": "not_established", "raw_sha256": "2482b571e12098e63a8ebe2f909ec19b2df68ab4562b066a6e72b0c0b3e0bb55", "body_sha256": "2a443c3a64625a1bac80aa0709ddc7ab902b693130c2e35e528c293d74662976", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/465.", "source_family": "enron-authored:e82be5e988deae44bf6e76940ff096cce48bd0769e24275219ab6e8332280c76", "synthetic": false, "claim_status": "interpretation"}`

> Please take a look at the proposed language.  You will need to consider the 
> time period before which a Market Disruption Event will kick in.:
> 
> Postponement:  For the purposes of the definition of "Price Source 
> Disruption," as set forth in Section 7.4(c)(i) of the Commodity Definitions,
>    the Maximum Days of Disruption shall be [thirty-two/sixty-four] days after 
> the last date of publication of World Pulp Monthly,
>    or any successor publication, published by Resource Information Systems, 
> Inc. or its successor for the applicable 
>    Calculation Period.

Source `mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77`; evidence `mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:0:69:fcf97a4eea3f5d36`; origin `enron-authored:e7720d4674e626f6d15780f3179b0172a8e1b374be96ee3bbcd2d429ebff2001`.

Attribution and exact offsets: `{"segment_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:segment:0:69", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Tue, 27 Jul 1999 01:47:00 -0700", "segment_source_family": "enron-span:mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:0:69", "segment_fingerprint": "da9c56909b8c12e6aba4534dd8f41409ee6241822ec74f82918874360edf4f49", "attribution_status": "unverified_header_claim", "document_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77", "span_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:0:69", "start": 0, "end": 69, "quote": "Are any of these yours?  What's the status?  We need to respond.  SS\n", "quote_fingerprint": "da9c56909b8c12e6aba4534dd8f41409ee6241822ec74f82918874360edf4f49", "independence_status": "not_established", "raw_sha256": "656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77", "body_sha256": "ba27aa6f7f0dce99f42bcd1643eb173d13c54d2fca656b19c18dd8e92307882d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/271.", "source_family": "enron-authored:e7720d4674e626f6d15780f3179b0172a8e1b374be96ee3bbcd2d429ebff2001", "synthetic": false, "claim_status": "interpretation"}`

> Are any of these yours?  What's the status?  We need to respond.  SS
> 

Source `mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77`; evidence `mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:462:557:39eff140433adaa9`; origin `enron-authored:e7720d4674e626f6d15780f3179b0172a8e1b374be96ee3bbcd2d429ebff2001`.

Attribution and exact offsets: `{"segment_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:segment:462:557", "segment_kind": "forwarded", "claimed_sender": "Sara Shackleton", "claimed_date": "06/29/99 09:20 AM", "segment_source_family": "enron-segment:7fca7bb9160625e0d30b07bc3c421a4f97b942092bd67d7103913b72336ffbac", "segment_fingerprint": "7fca7bb9160625e0d30b07bc3c421a4f97b942092bd67d7103913b72336ffbac", "attribution_status": "unverified_header_claim", "document_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77", "span_id": "mail-656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77:462:557", "start": 462, "end": 557, "quote": "\nI have three Canadian utilities almost ready to go; checking Canadian legal \nissues.  Sara\n\n\n\n", "quote_fingerprint": "7fca7bb9160625e0d30b07bc3c421a4f97b942092bd67d7103913b72336ffbac", "independence_status": "not_established", "raw_sha256": "656b5fcf333c0311a37f23aa7e73057899bfdb226de7023d98c53a8de3926b77", "body_sha256": "ba27aa6f7f0dce99f42bcd1643eb173d13c54d2fca656b19c18dd8e92307882d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/271.", "source_family": "enron-authored:e7720d4674e626f6d15780f3179b0172a8e1b374be96ee3bbcd2d429ebff2001", "synthetic": false, "claim_status": "interpretation"}`

> 
> I have three Canadian utilities almost ready to go; checking Canadian legal 
> issues.  Sara
> 
> 
> 
> 

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**expectations / observe**

The emails show informal coordination and implicit expectations around document routing, legal review, and reporting lines, but no clear unwritten rules emerge from the limited evidence.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
    "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction were found that reference the Confirmation Desk or similar routing; the prediction remains unresolved.",
    "evidence": [],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  },
  {
    "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
    "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction were found that show instructions to keep documentation centralized in Houston; the prediction remains unresolved.",
    "evidence": [],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  }
]
```

Source `mail-02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed`; evidence `mail-02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed:184:356:778266c9e711c100`; origin `enron-authored:3172372703429b7cebbcc92788a5aff413d3b4542bb28dcb6c26fc8d2dc9a32d`.

Attribution and exact offsets: `{"segment_id": "mail-02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed:segment:184:356", "segment_kind": "forwarded", "claimed_sender": "Shawna Flynn", "claimed_date": "07/02/99 12:05 PM", "segment_source_family": "enron-segment:754d29f3f4592398df734d18db0d03fc8c59dbfb696a322a5c8a474da5e228ba", "segment_fingerprint": "754d29f3f4592398df734d18db0d03fc8c59dbfb696a322a5c8a474da5e228ba", "attribution_status": "unverified_header_claim", "document_id": "mail-02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed", "span_id": "mail-02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed:184:356", "start": 184, "end": 356, "quote": "\nHey Joe- This is the GTC to use with all Spot Deals with Houston Pipe Line \nCompany. Please take out the space between Section 2.3 and 3.  Let me know \nwhat you think? sf\n", "quote_fingerprint": "754d29f3f4592398df734d18db0d03fc8c59dbfb696a322a5c8a474da5e228ba", "independence_status": "not_established", "raw_sha256": "02b75a32990b1f1048bbeabedf6dab3b09ca497f92c17d5fa8359ff8e1d7f4ed", "body_sha256": "ae239b9ca46ec0da02974cf5fcd53ec23e535c9923216b477382d432dcf5bfcf", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/hyvl-d/miscellaneous/asset_group/21.", "source_family": "enron-authored:3172372703429b7cebbcc92788a5aff413d3b4542bb28dcb6c26fc8d2dc9a32d", "synthetic": false, "claim_status": "interpretation"}`

> 
> Hey Joe- This is the GTC to use with all Spot Deals with Houston Pipe Line 
> Company. Please take out the space between Section 2.3 and 3.  Let me know 
> what you think? sf
> 

Source `mail-9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62`; evidence `mail-9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62:0:143:7c05de86394ff93b`; origin `enron-authored:b302113dd610a201c42dd9a794f129fea0a69da950d45ea69b7212ea3e8585e8`.

Attribution and exact offsets: `{"segment_id": "mail-9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62:segment:0:143", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 07 Sep 1999 07:12:00 -0700", "segment_source_family": "enron-segment:65b38f60d37343eb595921cb0a606642acb34395bb646f118668e187a2299409", "segment_fingerprint": "65b38f60d37343eb595921cb0a606642acb34395bb646f118668e187a2299409", "attribution_status": "unverified_header_claim", "document_id": "mail-9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62", "span_id": "mail-9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62:0:143", "start": 0, "end": 143, "quote": "I guess I still need your market descriptions for LPG, Oil & Oil Products and \nPlastics and Petrochem.  Will I have them by the end of the day?", "quote_fingerprint": "65b38f60d37343eb595921cb0a606642acb34395bb646f118668e187a2299409", "independence_status": "not_established", "raw_sha256": "9d4b9f93eea6334eab2df8f567cb50ce6533c6bf720622f12ae856b3ec0a1c62", "body_sha256": "28f1748703f6605df2dd82f5490657164c2f74b38f0cd6c55985e6fb0b7e437a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/279.", "source_family": "enron-authored:b302113dd610a201c42dd9a794f129fea0a69da950d45ea69b7212ea3e8585e8", "synthetic": false, "claim_status": "interpretation"}`

> I guess I still need your market descriptions for LPG, Oil & Oil Products and 
> Plastics and Petrochem.  Will I have them by the end of the day?

Source `mail-2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034`; evidence `mail-2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034:0:490:e1c0355f423eb29f`; origin `enron-authored:a5f8468eacd8a75d66ddd55dd6a346a02df51eafae857a1069fc096b6a17c322`.

Attribution and exact offsets: `{"segment_id": "mail-2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034:segment:0:490", "segment_kind": "authored", "claimed_sender": "ggalata@enron.co.uk", "claimed_date": "Mon, 02 Aug 1999 08:33:00 -0700", "segment_source_family": "enron-segment:7b2dd171b480a2fa549f4f385852fda577d133e12e5bb11503293ac5e7749821", "segment_fingerprint": "7b2dd171b480a2fa549f4f385852fda577d133e12e5bb11503293ac5e7749821", "attribution_status": "unverified_header_claim", "document_id": "mail-2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034", "span_id": "mail-2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034:0:490", "start": 0, "end": 490, "quote": "Ken,\n\nI finally found Franco Bernabe's work number: +39-06-3600-4741\n      +39-06-3600-4742\n\nHe actually returned my call (I had left a message with his secretary\nsaying that you were looking to talk to him). He mentioned that IMI (the\nItalian investment bank) would like to do a joint-venture with us to\ndevelop a power trading structure. He will put me in contact with someone\nat IMI.\n\nYou can reach him at any of the above numbers.\n\nBest wishes\n\nGiuseppe Galata\nECT London (Italian Team)", "quote_fingerprint": "7b2dd171b480a2fa549f4f385852fda577d133e12e5bb11503293ac5e7749821", "independence_status": "not_established", "raw_sha256": "2d2aca219285d61ae6c3ea523c4981253e5ed2dc9a041fe0cf1507c1df7cb034", "body_sha256": "0aa24c71acd91f0dff328b3d9a352806b1050b4970298aaffcb03c4c8043ef8c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/lay-k/all_documents/4.", "source_family": "enron-authored:a5f8468eacd8a75d66ddd55dd6a346a02df51eafae857a1069fc096b6a17c322", "synthetic": false, "claim_status": "interpretation"}`

> Ken,
> 
> I finally found Franco Bernabe's work number: +39-06-3600-4741
>       +39-06-3600-4742
> 
> He actually returned my call (I had left a message with his secretary
> saying that you were looking to talk to him). He mentioned that IMI (the
> Italian investment bank) would like to do a joint-venture with us to
> develop a power trading structure. He will put me in contact with someone
> at IMI.
> 
> You can reach him at any of the above numbers.
> 
> Best wishes
> 
> Giuseppe Galata
> ECT London (Italian Team)

**expertise / observe**

The emails show informal coordination around document preparation, legal review, and internal processes, with references to specific individuals and unspoken expectations about information sharing and task ownership.

Source `mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191`; evidence `mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:0:700:e8c51d7d2b9cda0f`; origin `enron-authored:b793d71f2899ad1e9e68043990052496cd1e8f9934794bcd0baad52938469f9b`.

Attribution and exact offsets: `{"segment_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:segment:0:1233", "segment_kind": "authored", "claimed_sender": "shari.stack@enron.com", "claimed_date": "Mon, 30 Aug 1999 12:33:00 -0700", "segment_source_family": "enron-segment:96871ad3003e0689da9718fbc4a793121283e0f1206eef4a5bc2027e7469c3d2", "segment_fingerprint": "96871ad3003e0689da9718fbc4a793121283e0f1206eef4a5bc2027e7469c3d2", "attribution_status": "unverified_header_claim", "document_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191", "span_id": "mail-093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191:0:700", "start": 0, "end": 700, "quote": "Just to let you know that in preparation for Sept. 1st, we need to go ahead \nand prepare for the name changes in our template fax letterheads, \ndocumentation, confirmations, account details, etc... from ECT to \"Enron \nNorth America Corp.\"  and ECT Canada to \"Enron Canada Corp.\", so that we send \nout correct correspondence on Wed. and thereafter.  There may be more places \nin your world where those names need to be changed  and we will rely on each \nof you to spot and make the change. \n\nSara and I have drafted a form letter which announces that the name changes \nare effective Sept. 1st. The letter is being prepared and will be \n\"auto-faxed\" tomorrow to counterparties whose fax numbers are on ", "quote_fingerprint": "7126a2279058ac4b945ff021ca48fd79094ef2cbec3f44c48e586f46e5c4fb76", "independence_status": "not_established", "raw_sha256": "093a12d03852f926fb8178991c4ef73750a485efcf0035a810ae3cc0d2ad1191", "body_sha256": "e1d0ec2d8644f42b74dfcd392999cc3161c79e3e03af4b163eb423fc81a09c3d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/434.", "source_family": "enron-authored:b793d71f2899ad1e9e68043990052496cd1e8f9934794bcd0baad52938469f9b", "synthetic": false, "claim_status": "interpretation"}`

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

Source `mail-0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563`; evidence `mail-0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563:0:370:167e2d7024a2029d`; origin `enron-authored:aa7e317b3432782b10ba5dfcd8d30654ed24f3287f3f27c14811b222e6bff766`.

Attribution and exact offsets: `{"segment_id": "mail-0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563:segment:0:370", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Wed, 25 Aug 1999 03:48:00 -0700", "segment_source_family": "enron-segment:3345ab576fc96a717ba127340967e0352969fe0d92815bcc96b6705fb8757efc", "segment_fingerprint": "3345ab576fc96a717ba127340967e0352969fe0d92815bcc96b6705fb8757efc", "attribution_status": "unverified_header_claim", "document_id": "mail-0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563", "span_id": "mail-0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563:0:370", "start": 0, "end": 370, "quote": "Attached is the first report identifying financial master trading agreements \ngenerated by ECT's derivatives legal group.  This report will be updated and \ndistributed weekly.  It only reflects documentation originated by Houston's \nlegal department and the status of negotiations.  If you have any questions, \nplease call me at 713/853-5620 or e-mail.  Thanks.  Sara\n\n\n", "quote_fingerprint": "3345ab576fc96a717ba127340967e0352969fe0d92815bcc96b6705fb8757efc", "independence_status": "not_established", "raw_sha256": "0e5bdd6efe45281b156034836a7a9180c88bd542e4880742f4d1104b63040563", "body_sha256": "e50b62369a7dc4591391d61dc7cc6db7945d7579981f9ac02825770a85aede90", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/414.", "source_family": "enron-authored:aa7e317b3432782b10ba5dfcd8d30654ed24f3287f3f27c14811b222e6bff766", "synthetic": false, "claim_status": "interpretation"}`

> Attached is the first report identifying financial master trading agreements 
> generated by ECT's derivatives legal group.  This report will be updated and 
> distributed weekly.  It only reflects documentation originated by Houston's 
> legal department and the status of negotiations.  If you have any questions, 
> please call me at 713/853-5620 or e-mail.  Thanks.  Sara
> 
> 
> 

Source `mail-759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2`; evidence `mail-759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2:0:247:f2e0205495693bc2`; origin `enron-authored:a61c2413af30da638694e84760d88ffd34790956376a5717c6edb2c1f1339a8a`.

Attribution and exact offsets: `{"segment_id": "mail-759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2:segment:0:247", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 07 Sep 1999 05:51:00 -0700", "segment_source_family": "enron-segment:e245f0cba73250d447825428ba651f69e2989a2413ad29b39737277f2f8fc4b7", "segment_fingerprint": "e245f0cba73250d447825428ba651f69e2989a2413ad29b39737277f2f8fc4b7", "attribution_status": "unverified_header_claim", "document_id": "mail-759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2", "span_id": "mail-759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2:0:247", "start": 0, "end": 247, "quote": "I spoke to Steve Kean's assistant, and told her your deadline to get all \nthese descriptions done was the end of today.  She said she would pass the \nword on and try and get you comments by the end of the day.  Let me know if \nthat doesn't happen.", "quote_fingerprint": "e245f0cba73250d447825428ba651f69e2989a2413ad29b39737277f2f8fc4b7", "independence_status": "not_established", "raw_sha256": "759821639eb64bf03c8fe7f24129f1033e83f41fbf59a9f3ebe74e5c064ae2e2", "body_sha256": "8e5151c596dd0ed5b0ac51f737c0799ec4002e8505cc72bb9587935895a68e51", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/275.", "source_family": "enron-authored:a61c2413af30da638694e84760d88ffd34790956376a5717c6edb2c1f1339a8a", "synthetic": false, "claim_status": "interpretation"}`

> I spoke to Steve Kean's assistant, and told her your deadline to get all 
> these descriptions done was the end of today.  She said she would pass the 
> word on and try and get you comments by the end of the day.  Let me know if 
> that doesn't happen.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**contrasts / observe**

The emails show coordination around travel, document drafts, and confirmations, with some evidence of centralized documentation and routing practices, but no clear tacit rules emerge from this batch alone.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
    "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction; unresolved.",
    "evidence": [
      {
        "id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce",
        "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
        "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
        "claim": "Tana Jones forwards a termination letter to Melba Lozano on the Confirmation Desk for handling, indicating a specific routing practice for confirmations.",
        "source": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120",
          "segment_kind": "authored",
          "claimed_sender": "tana.jones@enron.com",
          "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700",
          "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120",
          "start": 0,
          "end": 120,
          "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
          "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "independence_status": "not_established",
          "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.",
          "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  },
  {
    "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
    "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction; unresolved.",
    "evidence": [
      {
        "id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f",
        "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
        "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
        "claim": "Brent Hendry instructs Sara Shackleton to blind copy him on drafts but not reference his office in communications to the customer, ensuring all documentation to the customer comes from Houston.",
        "source": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134",
          "segment_kind": "authored",
          "claimed_sender": "sara.shackleton@enron.com",
          "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700",
          "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700",
          "start": 0,
          "end": 700,
          "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
          "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f",
          "independence_status": "not_established",
          "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.",
          "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  }
]
```

Source `mail-ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec`; evidence `mail-ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec:0:322:b62c327b1d04edd7`; origin `enron-authored:71cda716a594c652d774611937c11fd8c3e1419c4ed1e6bc086b3411c08ede50`.

Attribution and exact offsets: `{"segment_id": "mail-ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec:segment:0:322", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Fri, 03 Sep 1999 00:45:00 -0700", "segment_source_family": "enron-segment:f8d9731059f52fe704df81d0a7663fd23f14c758898bec6fe0124939997f6079", "segment_fingerprint": "f8d9731059f52fe704df81d0a7663fd23f14c758898bec6fe0124939997f6079", "attribution_status": "unverified_header_claim", "document_id": "mail-ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec", "span_id": "mail-ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec:0:322", "start": 0, "end": 322, "quote": "Bob,\n\nPer your request, attached are the online trading GTC's.  It looks like Mark \nhas all of them, not just financial.  I'm going to talk to Stacy about this \nwhen she gets in, because I know she was talking about adding it in.  I'll \nget back to you.\n\n    \n\n     \n\n      \n\n     \n\n      \n\n      \n\n     \n\n       \n\n\n      ", "quote_fingerprint": "f8d9731059f52fe704df81d0a7663fd23f14c758898bec6fe0124939997f6079", "independence_status": "not_established", "raw_sha256": "ca06076058e3fe8a8dec9295a40a18f6fd71e54fa7ed012c387ffbe3a7b933ec", "body_sha256": "5fc69b33d9426e39ffbb2638145edd359e2a2908fa052046291459083037ad20", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/sent/257.", "source_family": "enron-authored:71cda716a594c652d774611937c11fd8c3e1419c4ed1e6bc086b3411c08ede50", "synthetic": false, "claim_status": "interpretation"}`

> Bob,
> 
> Per your request, attached are the online trading GTC's.  It looks like Mark 
> has all of them, not just financial.  I'm going to talk to Stacy about this 
> when she gets in, because I know she was talking about adding it in.  I'll 
> get back to you.
> 
>     
> 
>      
> 
>       
> 
>      
> 
>       
> 
>       
> 
>      
> 
>        
> 
> 
>       

Source `mail-3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00`; evidence `mail-3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00:0:111:29fb8a8f6102f8a7`; origin `enron-authored:ff4260b7f94a0533e5615f50db606eb10510ba1ef5362fe78a132bc8230189c8`.

Attribution and exact offsets: `{"segment_id": "mail-3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00:segment:0:111", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 06 Aug 1999 02:01:00 -0700", "segment_source_family": "enron-segment:fcbea2e3678ece537b7419ce04bd1146725f2adf3cd0be5e0e1270b6ef4e490b", "segment_fingerprint": "fcbea2e3678ece537b7419ce04bd1146725f2adf3cd0be5e0e1270b6ef4e490b", "attribution_status": "unverified_header_claim", "document_id": "mail-3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00", "span_id": "mail-3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00:0:111", "start": 0, "end": 111, "quote": "FYI:  We have several \"Total\" agreements.  I don't know the relationship.  \nAre these commodities global?   SS\n", "quote_fingerprint": "fcbea2e3678ece537b7419ce04bd1146725f2adf3cd0be5e0e1270b6ef4e490b", "independence_status": "not_established", "raw_sha256": "3823ef661edb003ad6dd4986d28f0fd3e13b7d5cdce2afe70d5ab4034d08ab00", "body_sha256": "222b1eb1a5fdbbe0c807b8f0480dcd35db5101670fce96ba10bc28198169e61d", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/348.", "source_family": "enron-authored:ff4260b7f94a0533e5615f50db606eb10510ba1ef5362fe78a132bc8230189c8", "synthetic": false, "claim_status": "interpretation"}`

> FYI:  We have several "Total" agreements.  I don't know the relationship.  
> Are these commodities global?   SS
> 

Source `mail-c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef`; evidence `mail-c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef:0:686:894fa7b18b307d0e`; origin `enron-authored:041a96882aac30464374a638acb6dc3dceb4f2b0ee2c85314e426c801bb6ed6e`.

Attribution and exact offsets: `{"segment_id": "mail-c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef:segment:0:686", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Wed, 04 Aug 1999 08:05:00 -0700", "segment_source_family": "enron-segment:5564395e85ad4cc5ee4955e8220424f318e57f24335a57fc9110c0736b5fb8af", "segment_fingerprint": "5564395e85ad4cc5ee4955e8220424f318e57f24335a57fc9110c0736b5fb8af", "attribution_status": "unverified_header_claim", "document_id": "mail-c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef", "span_id": "mail-c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef:0:686", "start": 0, "end": 686, "quote": "Just to update you:\n\n1.  I think that our travel plans are fairly well set and I know that Kaye \nhas spoken with you on several items.\n2.  Mark wanted to be sure that in Sao Paulo, meetings were being scheduled \nwith outside counsel (which I believe Andrea is handling), with Randy Young \n(can you attend to that please?) and ESA necessary commercials (Andrea \nhandling?).\n3.  Mark wanted to make certain that we got on Don Black's calendar while in \nB.A.  Could you look into that as well?\n\nFor my own edification, who are Luiz Maurer and Orlando Gonzalez?\n\nPlease let me know if there is anything elso you need form me. \n\nI'll bring you up to date on Hickerson shortly.\n\nThanks,  Sara", "quote_fingerprint": "5564395e85ad4cc5ee4955e8220424f318e57f24335a57fc9110c0736b5fb8af", "independence_status": "not_established", "raw_sha256": "c116d53f24f4ad4ebc0d230e5b6caeb01ef100f0077486260cf45103f9684eef", "body_sha256": "a9444f10c86d99e860f4e29e28c5e0268b3ffa3284b906ebcf0dda3ffd11b52a", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/all_documents/339.", "source_family": "enron-authored:041a96882aac30464374a638acb6dc3dceb4f2b0ee2c85314e426c801bb6ed6e", "synthetic": false, "claim_status": "interpretation"}`

> Just to update you:
> 
> 1.  I think that our travel plans are fairly well set and I know that Kaye 
> has spoken with you on several items.
> 2.  Mark wanted to be sure that in Sao Paulo, meetings were being scheduled 
> with outside counsel (which I believe Andrea is handling), with Randy Young 
> (can you attend to that please?) and ESA necessary commercials (Andrea 
> handling?).
> 3.  Mark wanted to make certain that we got on Don Black's calendar while in 
> B.A.  Could you look into that as well?
> 
> For my own edification, who are Luiz Maurer and Orlando Gonzalez?
> 
> Please let me know if there is anything elso you need form me. 
> 
> I'll bring you up to date on Hickerson shortly.
> 
> Thanks,  Sara

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**routines / revise**

The emails show informal coordination around document routing and legal review, with hints of unwritten practices about centralizing customer-facing documentation in Houston and routing confirmations to a specific desk. However, evidence is limited and mostly single instances.

**Candidate rule — revision 2**

Confirmation-related documents are routed to the Confirmation Desk for handling, regardless of the originating office or individual.

Applies when: When a confirmation termination letter or similar confirmation document needs processing.

Exceptions: If the document is not confirmation-related or if specific instructions override the default routing.

Alternative: Routing may depend on the type of document or the recipient's role, not a blanket rule.

Uncertainty: Only one instance observed; no explicit policy cited.

Next query: all: confirmation desk Melba Lozano

Prediction: Future emails about confirmations will reference the Confirmation Desk or similar routing.

Hypothesis `hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
    "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "The only new arrival is the same email as before, so no new corroboration.",
    "evidence": [
      {
        "id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02",
        "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
        "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
        "claim": "Tana Jones forwards a termination letter to Melba Lozano on the Confirmation Desk, indicating a specific routing practice for confirmations.",
        "source": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120",
          "segment_kind": "authored",
          "claimed_sender": "tana.jones@enron.com",
          "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700",
          "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120",
          "start": 0,
          "end": 120,
          "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
          "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "independence_status": "not_established",
          "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.",
          "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  },
  {
    "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
    "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "The only new arrival is the same email as before, so no new corroboration.",
    "evidence": [
      {
        "id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f",
        "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
        "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
        "claim": "Brent Hendry instructs Sara Shackleton to blind copy him on drafts but not reference his office in communications to the customer, ensuring all documentation to the customer comes from Houston.",
        "source": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134",
          "segment_kind": "authored",
          "claimed_sender": "sara.shackleton@enron.com",
          "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700",
          "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700",
          "start": 0,
          "end": 700,
          "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
          "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f",
          "independence_status": "not_established",
          "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.",
          "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  }
]
```

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:1e766d07e4d23218`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:ad655fde8f180eaf`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:a7b4453bce441a69`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**expectations / revise**

The emails show informal coordination around document routing, legal review, and reporting lines, but no clear unwritten rules emerge from the limited evidence.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
    "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction; unresolved.",
    "evidence": [
      {
        "id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02",
        "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
        "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
        "claim": "Tana Jones forwards a termination letter to Melba Lozano on the Confirmation Desk, indicating a specific routing practice for confirmations.",
        "source": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120",
          "segment_kind": "authored",
          "claimed_sender": "tana.jones@enron.com",
          "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700",
          "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120",
          "start": 0,
          "end": 120,
          "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.",
          "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932",
          "independence_status": "not_established",
          "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f",
          "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.",
          "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  },
  {
    "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
    "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals after the prediction; unresolved.",
    "evidence": [
      {
        "id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f",
        "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
        "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
        "claim": "Brent Hendry instructs Sara Shackleton to blind copy him on drafts but not reference his office in communications to the customer, ensuring all documentation to the customer comes from Houston.",
        "source": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
        "valid": true,
        "semantic_status": "unreviewed",
        "metadata": {
          "segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134",
          "segment_kind": "authored",
          "claimed_sender": "sara.shackleton@enron.com",
          "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700",
          "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d",
          "attribution_status": "unverified_header_claim",
          "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700",
          "start": 0,
          "end": 700,
          "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully",
          "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f",
          "independence_status": "not_established",
          "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b",
          "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c",
          "offset_basis": "decoded-body-v1",
          "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.",
          "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252",
          "synthetic": false,
          "claim_status": "interpretation"
        }
      }
    ],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  }
]
```

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203:c0d10adf1c95dca5`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:503:26895", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "segment_fingerprint": "cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203", "start": 503, "end": 1203, "quote": "\n\n\nThe Option Investor Newsletter          1-17-98\nSunday             Part 3 of 7\n\n******************************************\nTLAB - Tellabs $85.94 (+11.63)(P3W $10.18)\n\nTellabs is quickly becoming a powerhouse in the Telecom\nequipment industry. With their TITAN and CABLESPAN systems,\nand its DXX multiplexers, TLAB is raking in the money from\ncustomers among the telephone companies, cable operators,\nand government agencies.  Though they faded from news of\ntheir failed merger of Ciena, Tellabs is still a major\nplayer.\n\nWow!  What a play.  TLAB gave up only $0.44 in Thursday's\nturmoil and came smokin' back $5.25 on Friday to close at\n$85.94.  Technicals look outstanding with a small\nconsolidat", "quote_fingerprint": "616ca10f948d5e07cda03144558c1691485e3a43c236f83d7b2103f4c81615dc", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter          1-17-98
> Sunday             Part 3 of 7
> 
> ******************************************
> TLAB - Tellabs $85.94 (+11.63)(P3W $10.18)
> 
> Tellabs is quickly becoming a powerhouse in the Telecom
> equipment industry. With their TITAN and CABLESPAN systems,
> and its DXX multiplexers, TLAB is raking in the money from
> customers among the telephone companies, cable operators,
> and government agencies.  Though they faded from news of
> their failed merger of Ciena, Tellabs is still a major
> player.
> 
> Wow!  What a play.  TLAB gave up only $0.44 in Thursday's
> turmoil and came smokin' back $5.25 on Friday to close at
> $85.94.  Technicals look outstanding with a small
> consolidat

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008:4f312cbfeac6cc17`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:54308:82729", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "segment_fingerprint": "0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008", "start": 54308, "end": 55008, "quote": "\n\n\nThe Option Investor Newsletter            1-17-98\nSunday                5  of  7\n\n*****************************************\nCOVERED CALL SECTION FOR JANUARY 17, 1999\n*****************************************\nTrading lessons...\n\nThis week we are going discuss one of the many pitfalls that you\nwill eventually encounter as a trader; Incorrect Information...\n\nOccasionally, we will discover an error in a stock or option quote\nand usually it comes to us \"the hard way\". Last week, we offered\na position on Reliance Bancorp (RELY) and it turns out that the\noption quoted was for another stock. It was not a research error\nor miss-type, just erroneous quote information provided to the\ntrading public.", "quote_fingerprint": "2981912f73de1ab71401d93c81d2903cd7e2353aa99e342b36a87790125c06a8", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter            1-17-98
> Sunday                5  of  7
> 
> *****************************************
> COVERED CALL SECTION FOR JANUARY 17, 1999
> *****************************************
> Trading lessons...
> 
> This week we are going discuss one of the many pitfalls that you
> will eventually encounter as a trader; Incorrect Information...
> 
> Occasionally, we will discover an error in a stock or option quote
> and usually it comes to us "the hard way". Last week, we offered
> a position on Reliance Bancorp (RELY) and it turns out that the
> option quoted was for another stock. It was not a research error
> or miss-type, just erroneous quote information provided to the
> trading public.

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432:536035e983bbb964`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:83232:110953", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "segment_fingerprint": "d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432", "start": 83232, "end": 83432, "quote": "\n\n\nThe Option Investor Newsletter              1-17-98\nSunday                   2  of  7\n\n*****************************************************\nComing Events\n******************************************", "quote_fingerprint": "006451b8f3ee12410e2eafde9d98164b558e2999dd80d5929850a58c66ca3d76", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter              1-17-98
> Sunday                   2  of  7
> 
> *****************************************************
> Coming Events
> ******************************************

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**expertise / revise**

The emails show informal coordination around document preparation, legal review, and internal processes, with references to specific individuals and unspoken expectations about information sharing and task ownership.

**Candidate rule — revision 3**

Confirmation-related documents are routed to the Confirmation Desk for handling, regardless of the originating office or individual.

Applies when: When a confirmation termination letter or similar confirmation document needs processing.

Exceptions: If the document is not confirmation-related or if specific instructions override the default routing.

Alternative: Routing may depend on the type of document or the recipient's role, not a blanket rule.

Uncertainty: Only one instance observed; no explicit policy cited.

Next query: all: confirmation desk termination

Prediction: Future emails about confirmations will reference the Confirmation Desk or similar routing.

Hypothesis `hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a`; transfer tested: false.

**Prediction Checks**

```json
[
  {
    "hypothesis_id": "hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a",
    "prediction_id": "prediction-a5fac4267f8d4c9c8b00c21b73dece6f",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals since prediction; unresolved.",
    "evidence": [],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  },
  {
    "hypothesis_id": "hypothesis-54af0a26f69245cfbfbdab226982a021",
    "prediction_id": "prediction-1f5d5ca167ce4ed2988f227e50def82b",
    "prediction_arrival_sequence": 2000,
    "status": "unresolved",
    "explanation": "No new arrivals since prediction; unresolved.",
    "evidence": [],
    "virtual_time": "1999-09-08T16:22:00+00:00",
    "arrival_sequence": 4000
  }
]
```

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203:470b52763df27109`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:503:26895", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "segment_fingerprint": "cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203", "start": 503, "end": 1203, "quote": "\n\n\nThe Option Investor Newsletter          1-17-98\nSunday             Part 3 of 7\n\n******************************************\nTLAB - Tellabs $85.94 (+11.63)(P3W $10.18)\n\nTellabs is quickly becoming a powerhouse in the Telecom\nequipment industry. With their TITAN and CABLESPAN systems,\nand its DXX multiplexers, TLAB is raking in the money from\ncustomers among the telephone companies, cable operators,\nand government agencies.  Though they faded from news of\ntheir failed merger of Ciena, Tellabs is still a major\nplayer.\n\nWow!  What a play.  TLAB gave up only $0.44 in Thursday's\nturmoil and came smokin' back $5.25 on Friday to close at\n$85.94.  Technicals look outstanding with a small\nconsolidat", "quote_fingerprint": "616ca10f948d5e07cda03144558c1691485e3a43c236f83d7b2103f4c81615dc", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter          1-17-98
> Sunday             Part 3 of 7
> 
> ******************************************
> TLAB - Tellabs $85.94 (+11.63)(P3W $10.18)
> 
> Tellabs is quickly becoming a powerhouse in the Telecom
> equipment industry. With their TITAN and CABLESPAN systems,
> and its DXX multiplexers, TLAB is raking in the money from
> customers among the telephone companies, cable operators,
> and government agencies.  Though they faded from news of
> their failed merger of Ciena, Tellabs is still a major
> player.
> 
> Wow!  What a play.  TLAB gave up only $0.44 in Thursday's
> turmoil and came smokin' back $5.25 on Friday to close at
> $85.94.  Technicals look outstanding with a small
> consolidat

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008:e5d7bc5c63fe0b3a`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:54308:82729", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "segment_fingerprint": "0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008", "start": 54308, "end": 55008, "quote": "\n\n\nThe Option Investor Newsletter            1-17-98\nSunday                5  of  7\n\n*****************************************\nCOVERED CALL SECTION FOR JANUARY 17, 1999\n*****************************************\nTrading lessons...\n\nThis week we are going discuss one of the many pitfalls that you\nwill eventually encounter as a trader; Incorrect Information...\n\nOccasionally, we will discover an error in a stock or option quote\nand usually it comes to us \"the hard way\". Last week, we offered\na position on Reliance Bancorp (RELY) and it turns out that the\noption quoted was for another stock. It was not a research error\nor miss-type, just erroneous quote information provided to the\ntrading public.", "quote_fingerprint": "2981912f73de1ab71401d93c81d2903cd7e2353aa99e342b36a87790125c06a8", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter            1-17-98
> Sunday                5  of  7
> 
> *****************************************
> COVERED CALL SECTION FOR JANUARY 17, 1999
> *****************************************
> Trading lessons...
> 
> This week we are going discuss one of the many pitfalls that you
> will eventually encounter as a trader; Incorrect Information...
> 
> Occasionally, we will discover an error in a stock or option quote
> and usually it comes to us "the hard way". Last week, we offered
> a position on Reliance Bancorp (RELY) and it turns out that the
> option quoted was for another stock. It was not a research error
> or miss-type, just erroneous quote information provided to the
> trading public.

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432:30dce4611178f5e2`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:83232:110953", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "segment_fingerprint": "d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432", "start": 83232, "end": 83432, "quote": "\n\n\nThe Option Investor Newsletter              1-17-98\nSunday                   2  of  7\n\n*****************************************************\nComing Events\n******************************************", "quote_fingerprint": "006451b8f3ee12410e2eafde9d98164b558e2999dd80d5929850a58c66ca3d76", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter              1-17-98
> Sunday                   2  of  7
> 
> *****************************************************
> Coming Events
> ******************************************

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b`; evidence `mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700:dc4ca3a354b3b94f`; origin `enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252`.

Attribution and exact offsets: `{"segment_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:segment:0:1134", "segment_kind": "authored", "claimed_sender": "sara.shackleton@enron.com", "claimed_date": "Fri, 18 Jun 1999 07:15:00 -0700", "segment_source_family": "enron-segment:b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "segment_fingerprint": "b6bd37446318d1bad30ef409c2f15a6ca544e2478e3a0ce162b4580a0c98891d", "attribution_status": "unverified_header_claim", "document_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "span_id": "mail-37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b:0:700", "start": 0, "end": 700, "quote": "Just received this message this very minute.  The draft already went.  Sorry.\n\n\nFrom: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM\nTo: Sara Shackleton/HOU/ECT@ECT\ncc:  \nSubject: Re: PC draft\n\n\n\n\nYou can copy me with a blind copy.  Do not reference this office in any cover \nletters or emails to the customer.  I will not distribute the copy to the \ncommercial guys here so that I can ensure that all documentation that goes to \nthe customer comes from Houston.  Thanks.\n\n\n\nFrom: \"Sara Shackleton/HOU/ECT\" AT ECT@ccMail on 18/06/99 09:53 AM CDT\n\nTo:   Brent Hendry/ENRON_DEVELOPMENT\ncc:\nSubject:  Re: PC draft\n\n\nThe draft is ready to go but we need one (1) item from credit. Hopefully", "quote_fingerprint": "828b7f737dcc5b42607f0cccec00c1259a9d49805d0c4d18bb2efa142214905f", "independence_status": "not_established", "raw_sha256": "37b176f68f6b2ff8c80e85d1ac85de42fb48a3989a900d5d315e576e40eaf72b", "body_sha256": "76a81d7fdd64298a11ba7814b8aeb13c3e7d904170e177007ccc7f69aa949c2c", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/shackleton-s/sent/87.", "source_family": "enron-authored:e522818dc5f2e9b3d3a0377c8e1774b29c618ac690f8bc474a93192bd9cb0252", "synthetic": false, "claim_status": "interpretation"}`

> Just received this message this very minute.  The draft already went.  Sorry.
> 
> 
> From: Brent Hendry AT ENRON_DEVELOPMENT@CCMAIL on 06/18/99 11:39 AM
> To: Sara Shackleton/HOU/ECT@ECT
> cc:  
> Subject: Re: PC draft
> 
> 
> 
> 
> You can copy me with a blind copy.  Do not reference this office in any cover 
> letters or emails to the customer.  I will not distribute the copy to the 
> commercial guys here so that I can ensure that all documentation that goes to 
> the customer comes from Houston.  Thanks.
> 
> 
> 
> From: "Sara Shackleton/HOU/ECT" AT ECT@ccMail on 18/06/99 09:53 AM CDT
> 
> To:   Brent Hendry/ENRON_DEVELOPMENT
> cc:
> Subject:  Re: PC draft
> 
> 
> The draft is ready to go but we need one (1) item from credit. Hopefully

**contrasts / revise**

The emails show informal coordination around document routing and legal review, with hints of unwritten practices about centralizing customer-facing documentation in Houston and routing confirmations to a specific desk. However, evidence is limited and mostly single instances.

**Candidate rule — revision 4**

Confirmation-related documents are routed to the Confirmation Desk for handling, regardless of the originating office or individual.

Applies when: When a confirmation termination letter or similar confirmation document needs processing.

Exceptions: If the document is not confirmation-related or if specific instructions override the default routing.

Alternative: Routing may depend on the type of document or the recipient's role, not a blanket rule.

Uncertainty: Only one instance observed; no explicit policy cited.

Next query: all: confirmation desk routing

Prediction: Future emails about confirmations will reference the Confirmation Desk or similar routing.

Hypothesis `hypothesis-aabee79ecf5a43d4a91b67de49a7dd3a`; transfer tested: false.

**Candidate rule — revision 2**

Legal documents intended for external customers must originate from Houston, with other offices only receiving blind copies and not being referenced in communications.

Applies when: When drafting or sending legal documents to customers, especially involving non-Houston offices.

Exceptions: If the customer is in a jurisdiction where local documentation is required, or if Houston explicitly delegates.

Alternative: The rule may apply only to certain types of documents or specific projects.

Uncertainty: Based on a single instruction from Brent Hendry; may not be a general practice.

Next query: all: Houston documentation customer

Prediction: Future emails will show similar instructions to keep documentation centralized in Houston.

Hypothesis `hypothesis-54af0a26f69245cfbfbdab226982a021`; transfer tested: false.

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203:b52a650d7d232dff`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:503:26895", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "segment_fingerprint": "cba5bcfd110d42653b4ae52beb03c106b11f2f27f8a8cdb9047d7a1f7005a4da", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:503:1203", "start": 503, "end": 1203, "quote": "\n\n\nThe Option Investor Newsletter          1-17-98\nSunday             Part 3 of 7\n\n******************************************\nTLAB - Tellabs $85.94 (+11.63)(P3W $10.18)\n\nTellabs is quickly becoming a powerhouse in the Telecom\nequipment industry. With their TITAN and CABLESPAN systems,\nand its DXX multiplexers, TLAB is raking in the money from\ncustomers among the telephone companies, cable operators,\nand government agencies.  Though they faded from news of\ntheir failed merger of Ciena, Tellabs is still a major\nplayer.\n\nWow!  What a play.  TLAB gave up only $0.44 in Thursday's\nturmoil and came smokin' back $5.25 on Friday to close at\n$85.94.  Technicals look outstanding with a small\nconsolidat", "quote_fingerprint": "616ca10f948d5e07cda03144558c1691485e3a43c236f83d7b2103f4c81615dc", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter          1-17-98
> Sunday             Part 3 of 7
> 
> ******************************************
> TLAB - Tellabs $85.94 (+11.63)(P3W $10.18)
> 
> Tellabs is quickly becoming a powerhouse in the Telecom
> equipment industry. With their TITAN and CABLESPAN systems,
> and its DXX multiplexers, TLAB is raking in the money from
> customers among the telephone companies, cable operators,
> and government agencies.  Though they faded from news of
> their failed merger of Ciena, Tellabs is still a major
> player.
> 
> Wow!  What a play.  TLAB gave up only $0.44 in Thursday's
> turmoil and came smokin' back $5.25 on Friday to close at
> $85.94.  Technicals look outstanding with a small
> consolidat

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008:d00abd83144865ae`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:54308:82729", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "segment_fingerprint": "0d99927b12eebf5541f9ea38435c031c31ffb7ed537aea5998a0862d2dc01bea", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:54308:55008", "start": 54308, "end": 55008, "quote": "\n\n\nThe Option Investor Newsletter            1-17-98\nSunday                5  of  7\n\n*****************************************\nCOVERED CALL SECTION FOR JANUARY 17, 1999\n*****************************************\nTrading lessons...\n\nThis week we are going discuss one of the many pitfalls that you\nwill eventually encounter as a trader; Incorrect Information...\n\nOccasionally, we will discover an error in a stock or option quote\nand usually it comes to us \"the hard way\". Last week, we offered\na position on Reliance Bancorp (RELY) and it turns out that the\noption quoted was for another stock. It was not a research error\nor miss-type, just erroneous quote information provided to the\ntrading public.", "quote_fingerprint": "2981912f73de1ab71401d93c81d2903cd7e2353aa99e342b36a87790125c06a8", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter            1-17-98
> Sunday                5  of  7
> 
> *****************************************
> COVERED CALL SECTION FOR JANUARY 17, 1999
> *****************************************
> Trading lessons...
> 
> This week we are going discuss one of the many pitfalls that you
> will eventually encounter as a trader; Incorrect Information...
> 
> Occasionally, we will discover an error in a stock or option quote
> and usually it comes to us "the hard way". Last week, we offered
> a position on Reliance Bancorp (RELY) and it turns out that the
> option quoted was for another stock. It was not a research error
> or miss-type, just erroneous quote information provided to the
> trading public.

Source `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988`; evidence `mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432:1aa285bc3528faed`; origin `enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e`.

Attribution and exact offsets: `{"segment_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:segment:83232:110953", "segment_kind": "forwarded", "claimed_sender": "xtrials@optioninvestor.com (Option Investor Newsletter     Trials)", "claimed_date": "01/18/99 08:27 AM ---------------------------", "segment_source_family": "enron-segment:d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "segment_fingerprint": "d9bfd20c5149da99763aee1e5efc7ae7373d4db808054ff1d3176c95062601c9", "attribution_status": "unverified_header_claim", "document_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "span_id": "mail-7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988:83232:83432", "start": 83232, "end": 83432, "quote": "\n\n\nThe Option Investor Newsletter              1-17-98\nSunday                   2  of  7\n\n*****************************************************\nComing Events\n******************************************", "quote_fingerprint": "006451b8f3ee12410e2eafde9d98164b558e2999dd80d5929850a58c66ca3d76", "independence_status": "not_established", "raw_sha256": "7a59011844d82fb64787e8689811796370f08243cf0fd3e794ecfe4889794988", "body_sha256": "8c1af5cd8e5776f1966f5bff12ef30801ec80d5ca5ca8b5dfb890cc8df0254e5", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/taylor-m/all_documents/121.", "source_family": "enron-authored:61d929a47736bb4c7fd32923734b1486ccf460e07f9e2efc6028020410afd17e", "synthetic": false, "claim_status": "interpretation"}`

> 
> 
> 
> The Option Investor Newsletter              1-17-98
> Sunday                   2  of  7
> 
> *****************************************************
> Coming Events
> ******************************************

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:efdc70ae7dd209ce`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:195692f1ce9f4b02`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

Source `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f`; evidence `mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120:6d82936102ef9e76`; origin `enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0`.

Attribution and exact offsets: `{"segment_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:segment:0:120", "segment_kind": "authored", "claimed_sender": "tana.jones@enron.com", "claimed_date": "Tue, 06 Jul 1999 03:37:00 -0700", "segment_source_family": "enron-segment:dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "segment_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "attribution_status": "unverified_header_claim", "document_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "span_id": "mail-8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f:0:120", "start": 0, "end": 120, "quote": "I have passed on the confirmation termination letter you sent me to Melba \nLozano on the Confirmation Desk for handling.", "quote_fingerprint": "dba260a3ecee235dee957f78cd7b145eeb6324cc156c57a6b06134c822a1d932", "independence_status": "not_established", "raw_sha256": "8f9266daf200cb00920b7143abeba902bc0575168d3c79899c32e59adc16021f", "body_sha256": "9c9ca0dc4806f01e28b8bc82abbfa8f44130a8a9a3adeadbe4d1181ae2007258", "offset_basis": "decoded-body-v1", "raw_locator": "file:///Users/henneberger/swarm/data/enron/enron_mail_20150507.tar.gz!/maildir/jones-t/all_documents/117.", "source_family": "enron-authored:5e6b55ad4187c017c9291bc78c9d7308634a686e83dc799717fb01883f0caea0", "synthetic": false, "claim_status": "interpretation"}`

> I have passed on the confirmation termination letter you sent me to Melba 
> Lozano on the Confirmation Desk for handling.

## Admission, gating, and retrieval audit

The full machine-readable companion export contains the ordered event log. The following records expose selection and model-call gates.

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:18:37.426274+00:00",
  "window": 1,
  "virtual_time": "1999-07-13T09:39:00+00:00",
  "arrival_sequence": 2000,
  "admitted": 2000,
  "selected": 32,
  "duplicate_gated": 987,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```

```json
{
  "kind": "arrival_window",
  "created_at": "2026-09-09T22:18:53.299717+00:00",
  "window": 2,
  "virtual_time": "1999-09-08T16:22:00+00:00",
  "arrival_sequence": 4000,
  "admitted": 2000,
  "selected": 32,
  "duplicate_gated": 1026,
  "agent_invocations": 8,
  "gate_reason": "novel_selected"
}
```
