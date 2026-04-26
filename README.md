# PulseRetail Agentic Organisation
### H9CEAI Final Project | National College of Ireland 2026

A fully agentic organisation powered by five specialised AI agents collaborating in a sequential pipeline to solve PulseRetail's customer re-engagement crisis.

## Live Demo
- **Loyalty Portal:** https://ran-im.github.io/pulseretail-agents
- **Pipeline Runner:** https://ran-im.github.io/pulseretail-agents/pipeline.html

## The Five Agents

| Agent | Role | Superpower |
|-------|------|------------|
| ARIA | Researcher | Deep analysis & pattern recognition |
| ZARA | Designer | Creative problem-solving & design thinking |
| FORGE | Maker | Technical craftsmanship & rapid prototyping |
| LYRA | Communicator | Persuasion & storytelling |
| CODA | Manager | Leadership & orchestration |

## How to Deploy to Your GitHub Pages

1. **Create a new GitHub repository** (e.g. `pulseretail-agents`)
2. **Upload all files** from this folder to the repo root
3. Go to **Settings → Pages → Source: Deploy from branch → main → / (root)**
4. Your site will be live at `https://YOUR-USERNAME.github.io/pulseretail-agents`

## How to Run the Pipeline

1. Open `pipeline.html` in your browser (or visit the GitHub Pages URL above)
2. Enter your [Anthropic API key](https://console.anthropic.com)
3. Click **Launch Agentic Pipeline**
4. Watch ARIA → ZARA → FORGE → LYRA → CODA run in real time

## Project Structure

```
├── index.html          # PulsePass loyalty portal (working prototype)
├── pipeline.html       # Live agentic pipeline runner interface
├── pipeline.py         # Python orchestrator (run locally with API key)
├── agents/
│   ├── 1_ARIA_researcher_output.md
│   ├── 2_ZARA_designer_output.md
│   ├── 3_FORGE_maker_output.md
│   ├── 4_LYRA_communicator_output.md
│   └── 5_CODA_manager_output.md
└── docs/
    └── H9CEAI_PulseRetail_Submission.pdf
```

## AI Usage
Built with Claude Sonnet 4.6 (Anthropic) via Claude Code CLI.
All agents run on the Anthropic Messages API with streaming.
