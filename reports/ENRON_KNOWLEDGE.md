# Investigation: EnergyDesk validation endorsement

Run `run-3756cce6b87a47268a010b2d390d6606` · model `deepseek-v4-flash` · status **completed**

**All interpretations are provisional and require independent review.** Citation checks confirm quoted text, not the truth of an assertion or fraud.

## Scope and resource use

```json
{
  "config": {
    "query": "EnergyDesk validation endorsement",
    "cutoff": null,
    "max_queries": 40,
    "max_documents": 160,
    "documents_per_query": 5,
    "body_chars": 7000,
    "max_output_tokens": 2200,
    "rounds": 6,
    "independent": false,
    "synthetic": false
  },
  "quote_checks": {
    "accepted": 72,
    "rejected": 0
  },
  "queries": 40,
  "unique_documents": 40,
  "runtime_usage": {
    "calls": 24,
    "tokens": 388409,
    "cost": 0.17794084
  }
}
```

## Cases and knowledge cards

No supported candidate cards were published. Inspect the forum and run errors.

## Forum

### scout / skeptic

The EnergyDesk validation endorsement thread shows a conflict over who must sign off valuation engines: James New asserts a requirement for both Research and RAC sign-off, while David Port states RAC has never been required to sign off valuation methods and assumes Research endorsement. Vince Kaminski acknowledges model validation cannot be handled internally by Research and opposes sending the full VaR model. Later emails indicate EnergyDesk.com was being discussed for sale to ABB, with concerns about exclusivity with Kiodex. Benign explanations include differing interpretations of internal sign-off policies and evolving business arrangements. Questions: Was there a formal policy document defining sign-off requirements? Did Research eventually endorse EnergyDesk? What was the outcome of the ABB/Kiodex discussions?

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

### scout / bridge

Threads converge on EnergyDesk.com valuation sign-off and external sale. Vince Kaminski (d1:s1) says model validation cannot be handled internally by Research and refuses to send full VaR model, offering reduced RiskMetrics version. Steven Leppard (d1:s5) is uncomfortable signing off EnergyDesk computations for Oslo, citing RAC domain, Research not owning Exotica, and Jan Lillehammer seeking to sell VaR system. David Port (d1:s8) asserts RAC never required to sign off valuation methods, assuming Research endorsement. James New (d1:s11) asks whether sign-off is required. Later, Tom McKeever (d2:s7) discusses ABB acquiring majority stake in EDC, while Jay Fitzgerald (d2:s3) raises exclusivity with Kiodex. Jeff Shankman (d5:s1) wants no proprietary weather data in EnergyDesk.com. Missing: actual sign-off decision, Oslo implementation outcome, and ABB deal resolution.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

### scout / practice

The EnergyDesk validation thread reveals a conflict over who must sign off valuation engines: James New asserts a requirement for Research and RAC sign-off, while David Port states RAC has never been required to sign off valuation methods and assumes Research endorsement. Steven Leppard is uncomfortable signing off without RAC, and Vince Kaminski acknowledges model validation cannot be handled internally by Research. The thread also shows EnergyDesk.com was being considered for sale to ABB while Enron had discussions with Kiodex, raising exclusivity concerns. I need to find ordinary comparison cases of approval workflows and sign-off practices to understand the implicit rules.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

### scout / chronology

The EnergyDesk validation endorsement chain shows a conflict: James New asserts a requirement that valuation engines be signed off by research and RAC, while David Port states RAC has never been required to sign off on valuation methods and that Research-written models are assumed endorsed by Research. Vince Kaminski acknowledges model validation issues cannot be handled internally by Research and declines to send the full VaR model, offering a reduced RiskMetrics-based version. Chronology: James New's email (12/08/2000) precedes David Port's reply (same day), Steven Leppard's forwarding (12/11/2000), and Vince's response (12/18/2000). Later, in Feb 2001, discussions about selling EnergyDesk to ABB and a Kiodex association raise exclusivity concerns. Questions: Was a formal sign-off requirement ever documented? Did Vince's meeting with Ted Murphy/Rick Buy resolve the validation issue? What was the outcome of the ABB due diligence?

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### disclose / bridge

The EnergyDesk thread reveals a conflict over sign-off authority: James New asserts a requirement for Research and RAC sign-off, while David Port states RAC has never been required to sign off valuation methods and assumes Research endorsement. Steven Leppard is uncomfortable signing off without RAC, and Vince Kaminski acknowledges model validation cannot be handled internally by Research. Later, EnergyDesk.com is discussed for sale to ABB, with exclusivity concerns regarding Kiodex. Missing: formal policy documentation, resolution of the sign-off dispute, and outcome of the ABB/Kiodex discussions.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### disclose / practice

The EnergyDesk thread exposes a live disagreement about who must sign off valuation engines: James New assumes Research and RAC both sign off, David Port says RAC never has and Research-written models are self-endorsed, and Steven Leppard is uncomfortable signing off without RAC. Vince Kaminski agrees validation cannot be internal to Research but offers no formal rule. The Accro thread shows a multi-step sign-off chain (RAC, Jim Hughes/Stan Horton, Compensation Committee, Creditor Committee) for bonus payouts, suggesting RAC sign-off is required in some contexts. The NETCO email asks whether a RAC-like group will exist post-restructuring, implying RAC's role was central but uncertain. Questions: Was there ever a formal policy document defining sign-off authority? Did Vince's meeting with Ted Murphy/Rick Buy produce a rule? How did the Oslo implementation proceed without a clear sign-off?

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-e1f7da4bdd358d698d433e3c2dc9200d9bcf5e4df237567ad3da0d1a3c529599` — exact quotation checked; interpretation unreviewed.

> spoken to anyone in RAC about this project?  
> 
> The Development Team had, at the time (21/2 years ago), the requirement to go to RAC for project approval. The Asset Management Co. has a "valuation" team that is constantly reviewing Proformas for all the assets and my understanding is that they work closely with RAC guidelines. 
> 
> I think the process will entail:
> 1.	Sign off by RAC.
> 2.	Sign off by Jim Hughes and Stan Horton.
> 3.	Sign off by Compensation Committee.
> 4.	Sign off by Creditor Committee and possibly E&Y even though these are bonuses associated with non-debtor entity.
> 
> Thanks for your help.

### disclose / skeptic

The thread shows a genuine policy ambiguity: James New believes Research and RAC sign-off is required for valuation engines, while David Port asserts RAC has never been required to sign off and assumes Research endorsement. Steven Leppard is uncomfortable signing off without RAC, and Vince Kaminski agrees validation cannot be internal to Research. Benign explanations include differing interpretations of unwritten norms and evolving business contexts. Missing: any formal policy document, the outcome of Vince's discussions with Ted Murphy/Rick Buy, and whether EnergyDesk was ultimately endorsed or sold.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### disclose / chronology

Chronology confirms James New's 12/08/2000 email precedes David Port's same-day reply, Steven Leppard's 12/11/2000 forward, and Vince Kaminski's 12/18/2000 response. The sign-off requirement conflict is unresolved: James asserts a requirement for Research and RAC sign-off, while David Port states RAC has never been required to sign off valuation methods. Vince acknowledges model validation cannot be handled internally by Research and declines to send the full VaR model. Later, in Feb 2001, ABB discussions resume with due diligence anticipated late January, and exclusivity with Kiodex is questioned. Missing: any formal policy document, the outcome of Vince's meeting with Ted Murphy/Rick Buy, and the final ABB/Kiodex resolution.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### retrieve / practice

The EnergyDesk thread reveals a live disagreement about sign-off authority for valuation engines: James New asserts a requirement for Research and RAC sign-off, while David Port states RAC has never been required to sign off and assumes Research endorsement. Steven Leppard is uncomfortable signing off without RAC, and Vince Kaminski agrees validation cannot be internal to Research. Benign explanations include differing interpretations of unwritten norms and evolving business contexts. Missing: any formal policy document, the outcome of Vince's discussions with Ted Murphy/Rick Buy, and whether EnergyDesk was ultimately endorsed or sold.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

### retrieve / skeptic

The thread shows a genuine policy ambiguity: James New believes Research and RAC sign-off is required for valuation engines, while David Port asserts RAC has never been required to sign off and assumes Research endorsement. Steven Leppard is uncomfortable signing off without RAC, and Vince Kaminski agrees validation cannot be internal to Research. Benign explanations include differing interpretations of unwritten norms and evolving business contexts. Missing: any formal policy document, the outcome of Vince's discussions with Ted Murphy/Rick Buy, and whether EnergyDesk was ultimately endorsed or sold.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### retrieve / chronology

The EnergyDesk sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### retrieve / bridge

The EnergyDesk thread shows a live dispute over valuation-engine sign-off: James New asserts Research and RAC sign-off is required, David Port says RAC never signs off and Research self-endorses, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. Separately, the ABB/EDC sale discussions raise exclusivity concerns with Kiodex. Missing: formal policy, outcome of Vince's meeting with Ted Murphy/Rick Buy, and final ABB/Kiodex resolution.

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> Thanks for the information.
> 
> You are aware that earlier discussions with ABB  were suspended when talks commenced with Kiodex re. energydesk.com( EDC).  We have recently resumed discussions with ABB and have had one meeting with them here earlier this month. There seems to be interest on their part in acquiring a majority stake in EDC for cash, and we anticipate due diligence to commence during the week of January 29th. If this happens and we can reach agreement on terms and conditions, including price, we might be able to close a transaction by the end of February. 
> 
> So far, we have made no commitments to ABB re. Enron's future use of EDC and do not anticipate doing so. My earlier query re. EOL and Kiodex came after I had a conversation with John Thompson, during which he mentioned your 

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> A brief update and then a question.
> 
> We are still in discussion with ABB re. Energydesk but the timetable has slipped as a result of their major reorganization announcement in late January. I understand that you are anticipating an announcement  on Kiodex in early March. Are there any exclusivity provisions in your deal with Kiodex that would infringe on the proposed transaction with ABB?
>  
> 
> 

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> Sorry for my late reply.  I have been travelling.
> 
> Not knowing the structure of your deal with ABB, I cannot tell you whether we might have an exclusivity issue or not.  What is the proposed structure of your deal, and what ties does it have with future Enron business or linkages?
> 
> Jay
> 
> 
> 
> 
> 

### challenge / practice

The EnergyDesk sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### challenge / bridge

The EnergyDesk sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> Thanks for the information.
> 
> You are aware that earlier discussions with ABB  were suspended when talks commenced with Kiodex re. energydesk.com( EDC).  We have recently resumed discussions with ABB and have had one meeting with them here earlier this month. There seems to be interest on their part in acquiring a majority stake in EDC for cash, and we anticipate due diligence to commence during the week of January 29th. If this happens and we can reach agreement on terms and conditions, including price, we might be able to close a transaction by the end of February. 
> 
> So far, we have made no commitments to ABB re. Enron's future use of EDC and do not anticipate doing so. My earlier query re. EOL and Kiodex came after I had a conversation with John Thompson, during which he mentioned your 

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> A brief update and then a question.
> 
> We are still in discussion with ABB re. Energydesk but the timetable has slipped as a result of their major reorganization announcement in late January. I understand that you are anticipating an announcement  on Kiodex in early March. Are there any exclusivity provisions in your deal with Kiodex that would infringe on the proposed transaction with ABB?
>  
> 
> 

Source `mail-5dce4a90b760c996cdb5ee07e5516489129b9eebd52450dd97f26595a7aba1e3` — exact quotation checked; interpretation unreviewed.

> 
> Sorry for my late reply.  I have been travelling.
> 
> Not knowing the structure of your deal with ABB, I cannot tell you whether we might have an exclusivity issue or not.  What is the proposed structure of your deal, and what ties does it have with future Enron business or linkages?
> 
> Jay
> 
> 
> 
> 
> 

### challenge / chronology

The EnergyDesk sign-off dispute remains unresolved. James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### challenge / skeptic

The EnergyDesk sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### test / skeptic

The sign-off dispute is unresolved. James New asserts a requirement for Research and RAC sign-off; David Port denies RAC's role and assumes Research endorsement; Steven Leppard is uncomfortable without RAC; Vince Kaminski agrees validation cannot be internal to Research. No formal policy or resolution is present. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### test / chronology

Chronology check: James New's email (12/08/2000 12:38 PM) precedes David Port's reply (08/12/2000 19:54, likely 8 Dec), which precedes Steven Leppard's forward (11/12/2000 09:46) and his email to Vince (11/12/2000 09:59). Vince's response (18 Dec 2000) follows Steven's chaser (18/12/2000 04:25 AM). Dates align. Key discrepancy: James New asserts a requirement for both Research and RAC sign-off, while David Port states RAC has never been required to sign off and assumes Research endorsement. Steven Leppard believes sign-off is RAC's domain, and Vince agrees validation cannot be internal to Research. No formal policy document resolves this. Also note: Vince's response shifts from sign-off to selling a reduced VaR model, suggesting a different concern. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### test / bridge

The EnergyDesk sign-off dispute remains unresolved. James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-1ae28fffd669ae98a6933e0c80cbe6f2411e92ca01c6c6d28ed7bb95d8d54e4a` — exact quotation checked; interpretation unreviewed.

> Vince
> Thanks for the quick response.  Agree on #5  just bear in mind it says SCOPE 
> not implement so it is more of a development of a project.
> RE; MG I will keep Tanya apprised of travel plans and give her the option to 
> be in or out as you two see fit.
> Ted
> 
> 
> 
> 
> 

Source `mail-bbcaafebc73c973244ef42236d34dbe0f0088ba0e7fb41ccf750aca87801e07d` — exact quotation checked; interpretation unreviewed.

> 
> overkill to underkill - especially with respect to the VAR process.  I would 
> defer to Anjam/Tanya's opinion as to what is necessary to get an initial 
> comfort level.  Remember that this is the first cut, but it will need to be 
> refined over time to the point where it is credible enough to force someone 
> to take a position down based on the calculatiion.  If this causes some 
> heartburn please refer those people to me.  
> Ted
> 
> 
> 
> 

Source `mail-bbcaafebc73c973244ef42236d34dbe0f0088ba0e7fb41ccf750aca87801e07d` — exact quotation checked; interpretation unreviewed.

> 
> Hi Andreas,
> 
> Here are the issues we would like to discuss on our Thursday meeting in NY:
> 
> 1. Inputs for options valuation, in particular the origins of volatility 
> curves;
> 2. Information on exotic options structures (existing & potential);
> 3. The data flow (are we going to get data from London or NY).
> 4a. Storage of positions information at  MG. How to extract the positions 
> info from
> MG database into spreadsheets.
> 4b. Existing positions structure for each metal.
> 5. Introduction to concentrates trading business, key personnel.
> 
> Best Regards,
> 
> Tanya & Anjam
> 
> 713 853 3997
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

### test / practice

The EnergyDesk sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy document or resolution is present. Chronology: James's email precedes David's reply, Steven's forward, and Vince's response. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### assess / chronology

Chronology and content align across the EnergyDesk sign-off dispute: James New requests sign-off, David Port denies RAC's role and assumes Research endorsement, Steven Leppard is uncomfortable without RAC, and Vince Kaminski agrees validation cannot be internal to Research. No formal policy or resolution is present. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### assess / bridge

The sign-off dispute remains unresolved. James New asserts a requirement for Research and RAC sign-off; David Port denies RAC's role and assumes Research endorsement; Steven Leppard is uncomfortable without RAC; Vince Kaminski agrees validation cannot be internal to Research. No formal policy or resolution is present. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

### assess / practice

The sign-off dispute remains unresolved: James New asserts a requirement for Research and RAC sign-off; David Port denies RAC's role and assumes Research endorsement; Steven Leppard is uncomfortable without RAC; Vince Kaminski agrees validation cannot be internal to Research. No formal policy or resolution is present. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-24bb5056f15c523e8d008d362a4d2fe0d8c0ffa7ded8fddedf1bd7242c0d68fb` — exact quotation checked; interpretation unreviewed.

> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> Steve,
> 
> Yes, I read it. I am going to talk about it with Ted Murphy and possibly Rick 
> Buy.
> As you have correctly pointed out, the model validation issues cannot
> be handled  internally by Research. 
> 
> The problem is that everybody is swamped right now with
> PRCs and end-of-year issues.
> 
> I don't think we shall send our  full  VaR model under any circumstances.
> We can offer to sell a reduced version based on RiskMetrics.
> 
> By the way, our meeting Tuesday will start at 11:00  a.m., Houston time.
> 
> 
> Vince
> 
> 
> 
> 
> 

### assess / skeptic

The sign-off dispute remains unresolved. James New asserts a requirement for Research and RAC sign-off; David Port denies RAC's role and assumes Research endorsement; Steven Leppard is uncomfortable without RAC; Vince Kaminski agrees validation cannot be internal to Research. No formal policy or resolution is present. Missing: outcome of Vince's meeting with Ted Murphy/Rick Buy, any formal sign-off policy, and final disposition of EnergyDesk for Oslo or ABB.

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> I would like to try to clear up a few things regarding the proposed 
> implementation of EnergyDesk into Oslo. 
> 
> I thought that it was a requirement that all valuation engines (and any 
> future changes to the valuation code) are required to be signed off by 
> research and RAC before they can be used to value the firm's positions. If 
> this is true then this is all I am looking to get onto the project plan the 
> time estimates you need to complete your review process. If there is no 
> requirement for RAC or research to sign off new or changed valuation engines 
> then I will trouble you no further.
> 
> Thanks James
> 
> 
> 
> 
> 
> 
> 
> 
> 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> James
> 
> I called and left a voicemail but I thought for the benefit of the CC's on 
> this, my view is that RAC have never been required to sign off on valuation 
> methods. The standard models used at Enron, like SPRDOPT and other routines 
> in Exotica.xls are written by Research and therefore I have always assumed 
> endorsed by Research. Having said that I do believe firmly that all RAC - MRM 
> folks should have a deep understanding of the way products are valued and be 
> able to assess and challenge a method. 
> 
> I am also happy to provide assistance in the process of designing a method 
> but I wouldn't want either of us to feel that RAC are in the way of progress 
> by being embedded in a project plan. 
> 
> In this instance, given the appropriate documentation, I would imagine the 
> time taken to 

Source `mail-648360b12bde560a3a42eed83a628c0f1ba12e59ed150fa6cb18d42d2c1fbd49` — exact quotation checked; interpretation unreviewed.

> 
> Hi Vince
> 
> James New from London Risk Mgt has asked me to sign off the computations in 
> EnergyDesk.com for use in Oslo office's new system.  I'm a little 
> uncomfortable with this since:
> 1. Sign off of models is something that I've been brought up to consider to 
> be the domain of RAC.  They disagree in part (see below), which leads me to...
> 2. London Research is not the "owner" of Exotica, and we don't necessarily 
> have the time/resource/expertise to audit Houston Research's code.  Indeed, 
> can Research group sign off their own efforts?  By definition the originating 
> group for a piece of code thinks it's OK, or they wouldn't have written it 
> that way.
> 3. I'm concerned about Research group code being sold to external clients 
> without Research involvement.  (I received a query a couple of 
