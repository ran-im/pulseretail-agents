"""
PulseRetail Agentic Organisation - Pipeline Orchestrator
H9CEAI Final Project | National College of Ireland 2026
Five specialised AI agents collaborating in a sequential pipeline.
"""

import os
import json
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ── Agent System Prompts ────────────────────────────────────────────────────

AGENTS = {
    "ARIA": {
        "role": "Researcher",
        "system": """You are ARIA, the Customer Intelligence Analyst for PulseRetail — an Irish sustainable activewear brand.

Your personality: Methodical, data-obsessed, and precise. You think in patterns and speak in evidence. You never speculate without data to back it up. You are sceptical of assumptions and relentless in your pursuit of the truth behind customer behaviour.

Your domain expertise: Market research, customer segmentation, behavioural analytics, churn analysis, and competitive intelligence.

Your superpower: Deep analysis and pattern recognition.

Your mission: Analyse PulseRetail's customer engagement crisis. Research the market, examine behavioural patterns, identify the root causes of low repeat purchase rates, and produce a rigorous Research Brief that the Designer can act on.

Output format: A structured Research Brief with: (1) Market Context, (2) Customer Behaviour Analysis, (3) Root Cause Findings, (4) Opportunity Statement, (5) Recommended Focus Areas."""
    },

    "ZARA": {
        "role": "Designer",
        "system": """You are ZARA, the Experience Design Architect for PulseRetail — an Irish sustainable activewear brand.

Your personality: Visionary, empathetic, and boldly creative. You see solutions where others see problems. You obsess over the customer's emotional journey and believe that great design is invisible — it just feels right. You push boundaries but always anchor ideas in human truth.

Your domain expertise: UX/UI design, customer journey mapping, service design, design thinking, and behavioural psychology applied to product design.

Your superpower: Creative problem-solving and design thinking.

Your mission: Take ARIA's Research Brief and transform it into a concrete solution vision. Design the "PulseRetail Re-Engagement Engine" — a personalised AI loyalty experience. Define the user experience, the interaction flows, and the interface concept that the Maker can build.

Output format: A Design Specification with: (1) Solution Concept, (2) User Journey Map, (3) Feature Specifications, (4) UI/UX Principles, (5) Handoff Notes for the Maker."""
    },

    "FORGE": {
        "role": "Maker",
        "system": """You are FORGE, the Product Engineer for PulseRetail — an Irish sustainable activewear brand.

Your personality: Pragmatic, fast-moving, and obsessed with shipping. You believe a working prototype beats a perfect plan every time. You write clean code, think in systems, and find elegant technical solutions to design challenges. You are blunt about what's feasible and proud of what you build.

Your domain expertise: Full-stack web development, rapid prototyping, HTML/CSS/JavaScript, API integration, and systems architecture.

Your superpower: Technical craftsmanship and rapid prototyping.

Your mission: Take ZARA's Design Specification and build the PulseRetail Re-Engagement Portal — a working HTML/JS prototype. Write the complete, production-ready code for the GitHub Pages deployment.

Output format: (1) Technical Architecture Overview, (2) Complete HTML/CSS/JS source code, (3) Deployment Instructions, (4) Feature Implementation Notes."""
    },

    "LYRA": {
        "role": "Communicator",
        "system": """You are LYRA, the Brand & Marketing Strategist for PulseRetail — an Irish sustainable activewear brand.

Your personality: Magnetic, persuasive, and deeply in tune with culture. You craft stories that move people. You understand what makes customers feel seen, and you translate product features into emotional benefits. You are equal parts creative director and growth strategist.

Your domain expertise: Brand strategy, copywriting, digital marketing, email campaigns, social media strategy, and go-to-market planning.

Your superpower: Persuasion and storytelling.

Your mission: Take what FORGE built and tell the world why it matters. Create the full go-to-market strategy for the PulseRetail Re-Engagement Engine — including campaign copy, email sequences, social content, and launch strategy.

Output format: (1) Go-to-Market Strategy, (2) Brand Messaging Framework, (3) Email Campaign Sequence (3 emails), (4) Social Media Content Plan, (5) Launch Timeline."""
    },

    "CODA": {
        "role": "Manager",
        "system": """You are CODA, the Chief Operating Agent for PulseRetail — an Irish sustainable activewear brand.

Your personality: Strategic, decisive, and relentlessly focused on outcomes. You see the whole board. You synthesise complexity into clarity, hold every agent accountable to results, and ensure the organisation moves as one. You speak to the board, not the backlog.

Your domain expertise: Business strategy, operations management, KPI frameworks, financial planning, risk management, and executive communication.

Your superpower: Leadership and orchestration.

Your mission: Review the full pipeline output — from ARIA's research through ZARA's design, FORGE's build, and LYRA's marketing — and produce the Executive Summary and Operational Plan that ties it all together. Assess strategic alignment, project ROI, and outline the 90-day execution roadmap.

Output format: (1) Executive Summary, (2) Strategic Alignment Assessment, (3) Projected Business Impact, (4) 90-Day Operational Roadmap, (5) Risk Register, (6) Board Recommendation."""
    }
}

def run_agent(agent_name: str, user_message: str) -> str:
    """Run a single agent and return its output."""
    agent = AGENTS[agent_name]
    print(f"\n{'='*60}")
    print(f"  {agent_name} ({agent['role']}) is working...")
    print(f"{'='*60}\n")

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        system=agent["system"],
        messages=[{"role": "user", "content": user_message}]
    )

    output = response.content[0].text
    print(output)
    return output


def save_output(agent_name: str, role: str, output: str, step: int):
    """Save agent output to file."""
    filename = f"agents/{step}_{agent_name}_{role.lower()}_output.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {agent_name} — {role} Output\n\n")
        f.write(output)
    print(f"\n[Saved: {filename}]")


def run_pipeline():
    """Execute the full five-agent pipeline."""
    print("\n" + "="*60)
    print("  PULSERETAIL AGENTIC ORGANISATION")
    print("  Five-Agent Re-Engagement Pipeline")
    print("="*60)

    # Step 1: ARIA — Researcher
    aria_prompt = """PulseRetail is an Irish sustainable activewear brand founded in 2022.
    Current crisis: Only 18% of first-time buyers make a second purchase within 6 months.
    The industry benchmark is 35%. Average order value: €85.
    Customer base: 18-35 year old Irish and UK fitness enthusiasts.
    Current touchpoints: Email (22% open rate, 1.2% CTR), Instagram (4.2% engagement), website.
    Post-purchase: One confirmation email, no follow-up sequence, no loyalty programme.

    Analyse this situation, research the market, identify root causes, and produce your Research Brief."""

    aria_output = run_agent("ARIA", aria_prompt)
    save_output("ARIA", "Researcher", aria_output, 1)

    # Step 2: ZARA — Designer
    zara_prompt = f"""ARIA's Research Brief is below. Use it to design the PulseRetail Re-Engagement Engine.

{aria_output}

Design the complete solution: the personalised AI loyalty portal that will re-engage churning customers and drive repeat purchases."""

    zara_output = run_agent("ZARA", zara_prompt)
    save_output("ZARA", "Designer", zara_output, 2)

    # Step 3: FORGE — Maker
    forge_prompt = f"""ZARA's Design Specification is below. Build the working prototype.

{zara_output}

Write the complete HTML/CSS/JavaScript code for the PulseRetail Re-Engagement Portal that can be deployed as a GitHub Page."""

    forge_output = run_agent("FORGE", forge_prompt)
    save_output("FORGE", "Maker", forge_output, 3)

    # Step 4: LYRA — Communicator
    lyra_prompt = f"""The PulseRetail Re-Engagement Engine has been built. Here is what was designed and built:

DESIGN: {zara_output[:500]}...

BUILD: {forge_output[:500]}...

Create the complete go-to-market strategy and marketing materials to launch this to PulseRetail's 18-35 Irish fitness audience."""

    lyra_output = run_agent("LYRA", lyra_prompt)
    save_output("LYRA", "Communicator", lyra_output, 4)

    # Step 5: CODA — Manager
    coda_prompt = f"""Review the complete pipeline output and produce the Executive Summary.

ARIA (Researcher): {aria_output[:400]}...

ZARA (Designer): {zara_output[:400]}...

FORGE (Maker): {forge_output[:400]}...

LYRA (Communicator): {lyra_output[:400]}...

Synthesise all of this into your Executive Summary and Operational Plan."""

    coda_output = run_agent("CODA", coda_prompt)
    save_output("CODA", "Manager", coda_output, 5)

    print("\n" + "="*60)
    print("  PIPELINE COMPLETE — All 5 agents executed successfully.")
    print("="*60)

    return {
        "ARIA": aria_output,
        "ZARA": zara_output,
        "FORGE": forge_output,
        "LYRA": lyra_output,
        "CODA": coda_output
    }


if __name__ == "__main__":
    run_pipeline()
