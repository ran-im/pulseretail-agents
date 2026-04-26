# H9CEAI Final Project — Submission Document
## Build an Agentic Organisation
**Module:** Customer Engagement and Artificial Intelligence (H9CEAI)  
**Programme:** MSCAIBUS1 | National College of Ireland 2026  
**Lecturer:** Victor del Rosal  

---

## Section 1 — Your Organisation (~200 words)

### PulseRetail: Sustainable Activewear for Irish Fitness Enthusiasts

**PulseRetail** is a fictional Irish direct-to-consumer (D2C) sustainable activewear brand founded in 2022. It sells premium yoga, running, and gym apparel to 18–35 year old fitness enthusiasts in Ireland and the UK, with an average order value of €85.

**The Business Challenge:** PulseRetail's repeat purchase rate stands at just 18% — less than half the industry benchmark of 35% (McKinsey, 2025). First-time buyers, acquired at a cost of €22–€28 each, are making one purchase and disappearing. Post-purchase communication consists of a single transactional confirmation email. No loyalty programme. No personalisation. No re-engagement strategy.

**Why an Agentic Approach?** This challenge cannot be solved by a single AI tool. Solving it requires simultaneous expertise in market research, experience design, full-stack development, brand marketing, and strategic operations. A single generalised chatbot cannot credibly perform all of these functions at the level of depth required. An agentic organisation — five specialised agents, each with deep domain expertise, working in a coordinated pipeline — can move from data to strategy to working product in one coordinated cycle. That is precisely what this project demonstrates.

---

## Section 2 — Agent Designs (~500 words)

### The Five Agents of the PulseRetail Agentic Organisation

Each agent was built with a distinct name, personality, and system prompt that firmly anchors them in their archetype. None of the agents overlap. Each one produces output the others cannot.

---

**Agent 1: ARIA — The Researcher**

*Archetype: Deep analysis and pattern recognition*

ARIA is PulseRetail's Customer Intelligence Analyst. Her personality is methodical, data-obsessed, and precise. She never speculates without evidence and is relentlessly sceptical of assumptions. Her system prompt explicitly frames her superpower as "deep analysis and pattern recognition" and instructs her to produce a structured Research Brief covering: Market Context, Customer Behaviour Analysis, Root Cause Findings, Opportunity Statement, and Recommended Focus Areas.

**What ARIA produced:** A five-section Research Brief identifying five root causes of PulseRetail's churn (no post-purchase journey, zero personalisation, absent loyalty infrastructure, passive website, no AI engagement layer) and quantifying the €2.1M annual revenue opportunity.

---

**Agent 2: ZARA — The Designer**

*Archetype: Creative problem-solving and design thinking*

ZARA is PulseRetail's Experience Design Architect. Her personality is visionary, empathetic, and boldly creative. She sees solutions where others see problems and anchors every idea in human emotional truth. Her system prompt instructs her to take ARIA's Research Brief and produce a Design Specification including: Solution Concept, User Journey Map, Feature Specifications, UI/UX Principles, and Handoff Notes for the Maker.

**What ZARA produced:** The "PulsePass" design — a five-feature loyalty intelligence portal with a full 4-touchpoint customer journey map, specific UI/UX principles (dark athletic aesthetic, motion as feedback, frictionless purchase path), and precise technical handoff instructions for FORGE.

---

**Agent 3: FORGE — The Maker**

*Archetype: Technical craftsmanship and rapid prototyping*

FORGE is PulseRetail's Product Engineer. His personality is pragmatic, fast-moving, and shipping-obsessed. He is blunt about what's feasible and proud of what he builds. His system prompt instructs him to take ZARA's Design Specification and build the complete HTML/CSS/JavaScript prototype deployable to GitHub Pages.

**What FORGE produced:** A fully functional single-page web application with six interactive features: animated SVG PulseScore ring, AI recommendation product cards, engagement streak tracker, community proof strip, win-back offer banner, and a toast notification system. Zero dependencies. Deployed live.

**Live prototype:** https://ran-im.github.io/pulseretail-agents

---

**Agent 4: LYRA — The Communicator**

*Archetype: Persuasion and storytelling*

LYRA is PulseRetail's Brand & Marketing Strategist. Her personality is magnetic, persuasive, and culturally attuned. She crafts stories that move people and understands what makes customers feel seen. Her system prompt instructs her to take FORGE's build and produce a complete Go-to-Market Strategy.

**What LYRA produced:** A three-phase launch strategy ("We Missed You, Champion"), a brand messaging framework tailored to four customer segments, three complete email sequences (Day 3, Day 14, Day 30 post-purchase), an Instagram content calendar, and a micro-influencer brief targeting Irish fitness creators.

---

**Agent 5: CODA — The Manager**

*Archetype: Leadership and orchestration*

CODA is PulseRetail's Chief Operating Agent. Her personality is strategic, decisive, and outcome-focused. She sees the whole board and holds every agent accountable to results. Her system prompt instructs her to review the full pipeline and produce an Executive Summary and Operational Plan.

**What CODA produced:** A comprehensive executive summary, strategic alignment assessment across all four prior agents, projected business impact modelling (18% → 35% repeat purchase rate = +€104,040 annual revenue, 18:1 ROI), a 90-day operational roadmap, risk register with five identified risks and mitigations, and a formal board recommendation.

---

## Section 3 — The Pipeline in Action (~300 words + evidence)

### How Work Flows Through the Organisation

The pipeline is strictly sequential. No agent begins without its predecessor's output. This is not five chatbots answering five prompts — it is a chain of dependency where each output structurally constrains and informs the next.

**ARIA → ZARA:** ARIA's five root causes became ZARA's five feature specifications. The Research Brief's "Recommended Focus Areas" (personalised post-purchase journey, loyalty portal, recommendation engine, community hook, behavioural trigger system) map directly to PulsePass's five features. ZARA could not have produced this design without ARIA's segment data.

**ZARA → FORGE:** ZARA's Design Specification included explicit technical handoff notes: use vanilla JavaScript, hardcode customer "Emma / 340 points", animate SVG ring with `stroke-dashoffset`, use `setInterval` for community feed, deploy as single HTML file. FORGE followed these notes precisely. The `--pulse-dark`, `--pulse-green`, `--pulse-white` CSS variables come directly from ZARA's colour palette specification.

**FORGE → LYRA:** LYRA's email sequences reference specific portal features: "You've already earned 170 points," "You're 60 points from your €10 reward," "Your 340 points are still there." These numbers are grounded in FORGE's prototype. LYRA could not have written specific, credible copy without FORGE's working portal to reference.

**LYRA → CODA:** CODA's Executive Summary synthesises all four preceding outputs. The ROI projection draws on ARIA's market data, CODA's operational roadmap maps to LYRA's three-phase GTM timeline, and the risk register addresses FORGE's noted limitation (Shopify integration pending).

**Working Prototype:**  
https://ran-im.github.io/pulseretail-agents

The prototype demonstrates: animated loyalty score, personalised product recommendations, 28-day streak tracker, live community feed, and win-back offer — all described in ZARA's spec, built by FORGE.

*Full agent outputs (transcripts) available in the `/agents/` directory of the GitHub repository.*

---

## Section 4 — Regulatory and Ethical Considerations (~200 words)

### GDPR Implications

PulsePass processes personal data — purchase history, browsing behaviour, segment classification, and loyalty points — to deliver personalised recommendations and re-engagement communications. Under GDPR (Regulation (EU) 2016/679), this requires:

- **Lawful basis:** Legitimate interest (post-purchase engagement) or explicit consent for marketing emails, clearly captured at checkout.
- **Transparency:** Every AI recommendation surfaces a "Why am I seeing this?" link (specified in ZARA's design). Customers must be informed when automated profiling influences what they are shown.
- **Data minimisation:** Only the data required for personalisation should be collected. PulsePass uses category affinity and purchase history — no sensitive data categories.
- **Right to erasure:** Customers can request deletion of their loyalty profile at any time. The portal must include a clear data deletion pathway.

### EU AI Act Considerations

PulseRetail's Re-Engagement Engine is a **low-risk AI system** under the EU AI Act (2024). It uses AI for product recommendation and engagement timing — neither of which qualifies as high-risk (healthcare, employment, credit) under Annex III. However, transparency obligations apply: customers should know they are interacting with AI-driven recommendations, not human curation.

### Trust

For the customer, trust hinges on one question: *does this feel helpful or manipulative?* PulsePass is designed to feel like a reward — points earned, recommendations earned, a community found. The win-back banner is honest about the offer. The email sequences are personal without being intrusive. The "double points" incentive is genuine, not fabricated urgency. If PulseRetail honours the rewards and keeps the data use transparent, customers will feel seen — not surveilled.

---

## Section 5 — Reflection (~300 words)

### What Worked

The pipeline architecture worked better than expected. The most striking outcome was how much richer each agent's output became because of the preceding agent's work. LYRA's email sequences are specific and credible — "You're 60 points from your €10 reward" — because FORGE had already built a portal where 340 points was the hardcoded customer state. A single agent asked to write marketing emails could not have produced that specificity. The handoff created emergent depth.

The separation of personality and domain expertise also worked well. ARIA's clinical, data-driven voice is distinct from ZARA's visionary tone, which is distinct from FORGE's blunt engineer voice. These are not the same language model producing five slightly different responses — they are genuinely different professional identities producing different types of work product.

### What Didn't Work

The prototype requires a real backend to become production-ready. FORGE correctly flagged this: Emma's 340 points are hardcoded. In production, every customer would need live data from Shopify and a recommendation engine consuming real purchase history. The current prototype is a high-fidelity demonstration, not a live system. This is acceptable at prototype stage but significant for deployment.

CODA's risk register identified that low portal adoption — customers not clicking through from emails to the portal — is the highest probability risk. The pipeline produced a beautiful portal, but if the Day-3 email subject line is wrong, no one will ever see it.

### What I Learned About Multi-Agent Collaboration

The handoff is the hardest part — and the most important. An agent that produces clean, structured, explicitly-labelled output (ARIA's numbered root causes, ZARA's bullet-pointed handoff notes) creates far more usable input for the next agent than one that produces prose. Structured outputs are the connective tissue of multi-agent systems.

The five archetypes also reflect a genuine truth about how organisations work. Research, design, engineering, marketing, and management are not interchangeable. Each has a distinct epistemology. The best outcome comes from five genuine specialists, not one generalist wearing five hats.

### If I Had More Time

I would build the Shopify integration, replace the hardcoded customer data with real personalisation, and run the Day-3 email sequence through an A/B test with live customers. I would also explore whether CODA could monitor post-launch performance data and trigger ARIA to re-run the analysis cycle — creating a self-improving feedback loop rather than a one-shot pipeline.

---

## AI Usage Declaration

This project was built using **Claude Sonnet 4.6** (Anthropic, 2026) via Claude Code CLI.

| Agent | Model | Key Prompt |
|---|---|---|
| ARIA | Claude Sonnet 4.6 | System prompt: Customer Intelligence Analyst with pattern recognition superpower |
| ZARA | Claude Sonnet 4.6 | System prompt: Experience Design Architect with design thinking superpower |
| FORGE | Claude Sonnet 4.6 | System prompt: Product Engineer with rapid prototyping superpower |
| LYRA | Claude Sonnet 4.6 | System prompt: Brand & Marketing Strategist with persuasion superpower |
| CODA | Claude Sonnet 4.6 | System prompt: Chief Operating Agent with leadership & orchestration superpower |

All AI-generated content was reviewed and edited for accuracy. The orchestration logic, system prompt design, agent personality definition, and critical evaluation of outputs are the student's original contribution.

---

*Word count (excluding headers, tables, code): ~2,100 words*  
*Submission format: This document (PDF/Word) + GitHub repository*  
*GitHub repository: https://github.com/ran-im/pulseretail-agents*  
*Live prototype: https://ran-im.github.io/pulseretail-agents*
