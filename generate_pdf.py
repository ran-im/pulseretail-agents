"""
Generate a professional PDF submission from SUBMISSION.md
H9CEAI Final Project — NCI 2026
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, Flowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import PageBreak
from reportlab.pdfgen import canvas as pdfcanvas
import re

# ── Colour palette ────────────────────────────────────────────────────────────
DARK      = colors.HexColor('#0d0d1a')
GREEN     = colors.HexColor('#00c27a')
GREEN_BG  = colors.HexColor('#e8faf3')
CARD      = colors.HexColor('#1a1a2e')
GREY      = colors.HexColor('#5a6478')
LIGHT_BG  = colors.HexColor('#f8f9fa')
WHITE     = colors.white
BLACK     = colors.HexColor('#1a1a2e')

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

# ── Document ──────────────────────────────────────────────────────────────────
output_path = "docs/H9CEAI_PulseRetail_Submission.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=2.5*cm, bottomMargin=2.2*cm,
    title="H9CEAI Final Project — PulseRetail Agentic Organisation",
    author="NCI MSCAIBUS1 2026",
)

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def S(name, **kwargs):
    return ParagraphStyle(name, **kwargs)

cover_title = S('CoverTitle',
    fontName='Helvetica-Bold', fontSize=28, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=6, leading=34)

cover_sub = S('CoverSub',
    fontName='Helvetica', fontSize=13, textColor=colors.HexColor('#a0b0c0'),
    alignment=TA_CENTER, spaceAfter=4, leading=18)

cover_detail = S('CoverDetail',
    fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#7090a0'),
    alignment=TA_CENTER, spaceAfter=3)

h1 = S('H1',
    fontName='Helvetica-Bold', fontSize=15, textColor=GREEN,
    spaceBefore=18, spaceAfter=6, leading=20,
    borderPad=0)

h2 = S('H2',
    fontName='Helvetica-Bold', fontSize=12, textColor=BLACK,
    spaceBefore=12, spaceAfter=4, leading=16)

h3 = S('H3',
    fontName='Helvetica-Bold', fontSize=10.5, textColor=GREY,
    spaceBefore=8, spaceAfter=3, leading=14)

body = S('Body',
    fontName='Helvetica', fontSize=10, textColor=BLACK,
    spaceAfter=6, leading=15, alignment=TA_JUSTIFY)

body_bullet = S('BodyBullet',
    fontName='Helvetica', fontSize=10, textColor=BLACK,
    spaceAfter=3, leading=15, leftIndent=16,
    bulletIndent=4, alignment=TA_LEFT)

bold_line = S('BoldLine',
    fontName='Helvetica-Bold', fontSize=10, textColor=BLACK,
    spaceAfter=4, leading=14)

code_style = S('Code',
    fontName='Courier', fontSize=8.5, textColor=colors.HexColor('#2d4a3e'),
    backColor=GREEN_BG, spaceAfter=6, leading=13,
    leftIndent=10, rightIndent=10,
    borderPad=6)

label_green = S('LabelGreen',
    fontName='Helvetica-Bold', fontSize=9, textColor=GREEN,
    spaceAfter=2)

agent_header = S('AgentHeader',
    fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,
    spaceAfter=4, leading=16)

url_style = S('URL',
    fontName='Helvetica-Bold', fontSize=10, textColor=GREEN,
    spaceAfter=4)

# ── Helper ────────────────────────────────────────────────────────────────────
def hr(color=GREEN, thickness=1.5, spaceB=4, spaceA=8):
    return HRFlowable(width='100%', thickness=thickness,
                      color=color, spaceAfter=spaceA, spaceBefore=spaceB)

def agent_block(name, role, superpower, produced):
    """Render a coloured agent card."""
    data = [[
        Paragraph(f"{name}  —  {role}", agent_header),
        Paragraph(f"Superpower: {superpower}", S('SP', fontName='Helvetica-Oblique',
                  fontSize=9, textColor=colors.HexColor('#a0d4b8'), leading=13))
    ]]
    header_table = Table(data, colWidths=[(PAGE_W - 2*MARGIN)*0.55,
                                           (PAGE_W - 2*MARGIN)*0.45])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ROUNDEDCORNERS', [6,6,0,0]),
    ]))

    body_data = [[Paragraph(produced, body)]]
    body_table = Table(body_data, colWidths=[PAGE_W - 2*MARGIN])
    body_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d0e8da')),
    ]))
    return KeepTogether([header_table, body_table, Spacer(1, 8)])

def simple_table(headers, rows, col_widths=None):
    usable = PAGE_W - 2*MARGIN
    if col_widths is None:
        col_widths = [usable / len(headers)] * len(headers)
    th_style = S('TH', fontName='Helvetica-Bold', fontSize=9,
                 textColor=WHITE, leading=12)
    td_style = S('TD', fontName='Helvetica', fontSize=9,
                 textColor=BLACK, leading=12)
    data = [[Paragraph(h, th_style) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), td_style) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CARD),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG]),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#d0d8e0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

# ── Custom Cover Flowable (draws directly on canvas — avoids Table clipping) ──
class CoverBox(Flowable):
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        # Dark background rectangle
        c.setFillColor(DARK)
        c.roundRect(0, 0, self.width, self.height, radius=10, fill=1, stroke=0)
        # White title
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 28)
        c.drawCentredString(self.width / 2, self.height - 60, 'PULSERETAIL')
        # Sub title
        c.setFont('Helvetica', 14)
        c.setFillColor(colors.HexColor('#a0b0c0'))
        c.drawCentredString(self.width / 2, self.height - 88, 'Agentic Organisation')
        # Details
        c.setFont('Helvetica', 10)
        c.setFillColor(colors.HexColor('#7090a0'))
        c.drawCentredString(self.width / 2, self.height - 115, 'H9CEAI Final Project  ·  100% CA')
        c.drawCentredString(self.width / 2, self.height - 132,
                            'Customer Engagement and Artificial Intelligence')
        c.drawCentredString(self.width / 2, self.height - 158,
                            'National College of Ireland  ·  MSCAIBUS1  ·  2026')
        c.drawCentredString(self.width / 2, self.height - 173, 'Lecturer: Victor del Rosal')


# ── Cover Page ────────────────────────────────────────────────────────────────
def cover_page():
    cover_box = CoverBox(width=PAGE_W - 2*MARGIN, height=220)

    pipeline_data = [['ARIA', '→', 'ZARA', '→', 'FORGE', '→', 'LYRA', '→', 'CODA']]
    pill_s = S('Pill', fontName='Helvetica-Bold', fontSize=10,
               textColor=GREEN, alignment=TA_CENTER, leading=14)
    arrow_s = S('Arr', fontName='Helvetica', fontSize=12,
                textColor=GREY, alignment=TA_CENTER, leading=14)
    pipeline_row = []
    for i, cell in enumerate(pipeline_data[0]):
        pipeline_row.append(Paragraph(cell, arrow_s if cell == '→' else pill_s))
    pipeline_table = Table([pipeline_row],
        colWidths=[1.6*cm, 0.7*cm, 1.6*cm, 0.7*cm, 1.7*cm, 0.7*cm, 1.6*cm, 0.7*cm, 1.6*cm])
    pipeline_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))

    return [
        cover_box,
        Spacer(1, 30),
        Paragraph("Five-Agent Pipeline", S('PL', fontName='Helvetica',
                  fontSize=9, textColor=GREY, alignment=TA_CENTER, spaceAfter=8)),
        pipeline_table,
        Spacer(1, 20),
        Paragraph("Live Prototype:", S('LBL', fontName='Helvetica', fontSize=9,
                  textColor=GREY, alignment=TA_CENTER, spaceAfter=2)),
        Paragraph("https://ran-im.github.io/pulseretail-agents",
                  S('URL2', fontName='Helvetica-Bold', fontSize=10,
                    textColor=GREEN, alignment=TA_CENTER, spaceAfter=2)),
        Paragraph("GitHub: https://github.com/ran-im/pulseretail-agents",
                  S('GH', fontName='Helvetica', fontSize=9,
                    textColor=GREY, alignment=TA_CENTER)),
        PageBreak()
    ]

# ── Story ─────────────────────────────────────────────────────────────────────
story = []
story += cover_page()

# ─── SECTION 1 ───────────────────────────────────────────────────────────────
story.append(hr())
story.append(Paragraph("Section 1 — Your Organisation", h1))
story.append(hr(color=colors.HexColor('#d0e8da'), thickness=0.5, spaceB=0, spaceA=10))

story.append(Paragraph("PulseRetail: Sustainable Activewear for Irish Fitness Enthusiasts", h2))
story.append(Paragraph(
    "<b>PulseRetail</b> is a fictional Irish direct-to-consumer (D2C) sustainable activewear brand "
    "founded in 2022. It sells premium yoga, running, and gym apparel to 18–35 year old fitness "
    "enthusiasts in Ireland and the UK, with an average order value of €85.", body))

story.append(Paragraph("The Business Challenge", h3))
story.append(Paragraph(
    "PulseRetail's repeat purchase rate stands at just <b>18%</b> — less than half the industry "
    "benchmark of 35% (McKinsey, 2025). First-time buyers, acquired at a cost of €22–€28 each, "
    "are making one purchase and disappearing. Post-purchase communication consists of a single "
    "transactional confirmation email. No loyalty programme. No personalisation. No re-engagement "
    "strategy.", body))

story.append(Paragraph("Why an Agentic Approach?", h3))
story.append(Paragraph(
    "This challenge cannot be solved by a single AI tool. Solving it requires simultaneous "
    "expertise in market research, experience design, full-stack development, brand marketing, "
    "and strategic operations. A single generalised chatbot cannot credibly perform all of these "
    "functions at the required depth. An agentic organisation — five specialised agents, each with "
    "deep domain expertise, working in a coordinated pipeline — can move from data to strategy to "
    "working product in one coordinated cycle. That is precisely what this project demonstrates.", body))

# ─── SECTION 2 ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 10))
story.append(hr())
story.append(Paragraph("Section 2 — Agent Designs", h1))
story.append(hr(color=colors.HexColor('#d0e8da'), thickness=0.5, spaceB=0, spaceA=10))
story.append(Paragraph("The Five Agents of the PulseRetail Agentic Organisation", h2))
story.append(Paragraph(
    "Each agent was built with a distinct name, personality, and system prompt anchored firmly in "
    "its archetype. No two agents overlap. Each produces output the others cannot.", body))
story.append(Spacer(1, 6))

story.append(agent_block(
    "ARIA", "The Researcher", "Deep analysis and pattern recognition",
    "<b>Personality:</b> Methodical, data-obsessed, and precise. Never speculates without evidence. "
    "Sceptical of assumptions. Her system prompt explicitly constrains her to produce a structured "
    "Research Brief: Market Context → Customer Behaviour Analysis → Root Cause Findings → "
    "Opportunity Statement → Recommended Focus Areas.<br/><br/>"
    "<b>What ARIA produced:</b> A five-section Research Brief identifying five root causes of "
    "PulseRetail's churn — no post-purchase journey, zero personalisation, absent loyalty "
    "infrastructure, passive website, no AI engagement layer — and quantifying a €2.1M annual "
    "revenue opportunity. ARIA's segment table (Yoga 34%, Running 28%, Gym 22%, Lifestyle 16%) "
    "directly informed every subsequent agent's work."
))

story.append(agent_block(
    "ZARA", "The Designer", "Creative problem-solving and design thinking",
    "<b>Personality:</b> Visionary, empathetic, boldly creative. Anchors every idea in human "
    "emotional truth. Her system prompt takes ARIA's Research Brief as input and produces a "
    "Design Specification: Solution Concept → User Journey Map → Feature Specifications → "
    "UI/UX Principles → Handoff Notes for the Maker.<br/><br/>"
    "<b>What ZARA produced:</b> The 'PulsePass' design — a five-feature loyalty intelligence "
    "portal with a 4-touchpoint customer journey (Days 3, 7, 14, 30 post-purchase), specific "
    "UI/UX principles (dark athletic aesthetic, motion as feedback, frictionless purchase path), "
    "and precise technical handoff instructions including CSS variables, animation techniques, "
    "and deployment target."
))

story.append(agent_block(
    "FORGE", "The Maker", "Technical craftsmanship and rapid prototyping",
    "<b>Personality:</b> Pragmatic, fast-moving, shipping-obsessed. Blunt about feasibility. "
    "His system prompt takes ZARA's Design Specification and produces complete HTML/CSS/JS source "
    "code deployable as a GitHub Page — zero dependencies, zero build step.<br/><br/>"
    "<b>What FORGE produced:</b> A fully functional single-page application with six interactive "
    "features: animated SVG PulseScore ring (stroke-dashoffset technique), AI recommendation "
    "product cards with hover states, 28-day engagement streak tracker, community proof strip "
    "with staggered animations, win-back offer banner (CSS pulse-glow keyframes), and a global "
    "toast notification system. Mobile-responsive. Deployed live at:<br/>"
    "<font color='#00c27a'><b>https://ran-im.github.io/pulseretail-agents</b></font>"
))

story.append(agent_block(
    "LYRA", "The Communicator", "Persuasion and storytelling",
    "<b>Personality:</b> Magnetic, persuasive, culturally attuned. Crafts stories that move "
    "people. Her system prompt takes FORGE's build and produces a complete Go-to-Market Strategy: "
    "GTM Plan → Brand Messaging Framework → Email Sequences → Social Media Plan → "
    "Launch Timeline.<br/><br/>"
    "<b>What LYRA produced:</b> Campaign 'We Missed You, Champion' — a three-phase launch "
    "strategy, segment-specific brand messaging for four customer groups (Yoga, Running, Gym, "
    "Lapsed), three complete email sequences (Day-3 'Your order arrives tomorrow', Day-14 "
    "'You're 60 points from €10 off', Day-30 'We saved something for you'), Instagram content "
    "calendar, and micro-influencer brief for Irish fitness creators."
))

story.append(agent_block(
    "CODA", "The Manager", "Leadership and orchestration",
    "<b>Personality:</b> Strategic, decisive, outcome-focused. Sees the whole board. Her system "
    "prompt reviews all four prior agents and produces an Executive Summary and Operational Plan: "
    "Summary → Strategic Alignment Assessment → Business Impact → 90-Day Roadmap → "
    "Risk Register → Board Recommendation.<br/><br/>"
    "<b>What CODA produced:</b> A full executive summary, strategic alignment rating for all four "
    "agents, revenue projection (18% → 35% repeat rate = +€104,040 annual revenue, 18:1 ROI on "
    "a €5,000 investment), a 90-day operational roadmap across three months, risk register with "
    "five identified risks and mitigations, and a formal board recommendation to deploy."
))

# ─── SECTION 3 ───────────────────────────────────────────────────────────────
story.append(hr())
story.append(Paragraph("Section 3 — The Pipeline in Action", h1))
story.append(hr(color=colors.HexColor('#d0e8da'), thickness=0.5, spaceB=0, spaceA=10))

story.append(Paragraph("How Work Flows Through the Organisation", h2))
story.append(Paragraph(
    "The pipeline is strictly sequential. No agent begins without its predecessor's output. "
    "This is not five chatbots answering five independent prompts — it is a chain of structural "
    "dependency where each output constrains and informs the next.", body))

story.append(Spacer(1, 6))
handoff_table = simple_table(
    ['Handoff', 'What Was Passed', 'Evidence of Dependency'],
    [
        ['ARIA → ZARA', 'Five root causes + segment breakdown', "ZARA's 5 features map 1:1 to ARIA's 5 recommended focus areas"],
        ['ZARA → FORGE', 'Feature specs + CSS variables + animation brief', "FORGE used --pulse-green, stroke-dashoffset, staggered setTimeout exactly as specified"],
        ['FORGE → LYRA', 'Working portal with live data (340 pts, Emma)', "LYRA's emails quote '340 points', '60 pts from €10' — grounded in FORGE's prototype"],
        ['LYRA → CODA', 'GTM strategy + three email sequences + timeline', "CODA's 90-day roadmap mirrors LYRA's three-phase launch; risk #1 cites email CTR"],
    ],
    col_widths=[3.2*cm, 5.5*cm, (PAGE_W-2*MARGIN-8.7*cm)]
)
story.append(handoff_table)
story.append(Spacer(1, 12))

story.append(Paragraph("Working Prototype", h3))
story.append(Paragraph(
    "The prototype was built by FORGE following ZARA's exact Design Specification and deployed "
    "to GitHub Pages. It demonstrates the complete PulsePass loyalty portal in action:", body))

features = [
    "Animated PulseScore ring — SVG stroke-dashoffset technique, numeric counter, progress bar to next tier",
    "AI Recommendation Panel — three personalised product cards (yoga category affinity) with hover states and Add-to-Bag",
    "Engagement Streak Tracker — 28-day calendar grid with three states (inactive / active / purchase)",
    "Community Proof Strip — staggered slide-in animations simulating live member activity",
    "Win-Back Offer Banner — pulsing CSS keyframe animation drawing attention to double-points offer",
    "Toast Notification System — global feedback on every user action",
]
for f in features:
    story.append(Paragraph(f"• {f}", body_bullet))

story.append(Spacer(1, 8))
link_table = Table([[
    Paragraph("Live Prototype:", S('LBL2', fontName='Helvetica', fontSize=9, textColor=GREY)),
    Paragraph("https://ran-im.github.io/pulseretail-agents", url_style),
]], colWidths=[3*cm, PAGE_W-2*MARGIN-3*cm])
link_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GREEN_BG),
    ('BOX', (0,0), (-1,-1), 1, GREEN),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('ROUNDEDCORNERS', [6,6,6,6]),
]))
story.append(link_table)

# ─── SECTION 4 ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 14))
story.append(hr())
story.append(Paragraph("Section 4 — Regulatory and Ethical Considerations", h1))
story.append(hr(color=colors.HexColor('#d0e8da'), thickness=0.5, spaceB=0, spaceA=10))

story.append(Paragraph("GDPR Implications", h2))
story.append(Paragraph(
    "PulsePass processes personal data — purchase history, browsing behaviour, segment "
    "classification, and loyalty points — to deliver personalised recommendations and "
    "re-engagement communications. Under GDPR (Regulation (EU) 2016/679), this requires:", body))

gdpr_items = [
    ("<b>Lawful basis:</b>", "Legitimate interest (post-purchase engagement) or explicit consent for marketing emails, clearly captured at checkout."),
    ("<b>Transparency:</b>", "Every AI recommendation surfaces a 'Why am I seeing this?' link (specified in ZARA's design). Customers must know when automated profiling influences what they are shown."),
    ("<b>Data minimisation:</b>", "Only the data required for personalisation is collected — category affinity and purchase history. No sensitive data categories are involved."),
    ("<b>Right to erasure:</b>", "Customers can request deletion of their loyalty profile at any time. The portal must include a clear data deletion pathway."),
]
for label, detail in gdpr_items:
    story.append(Paragraph(f"{label} {detail}", body_bullet))

story.append(Paragraph("EU AI Act Considerations", h2))
story.append(Paragraph(
    "PulseRetail's Re-Engagement Engine is a <b>low-risk AI system</b> under the EU AI Act (2024). "
    "It uses AI for product recommendation and engagement timing — neither of which qualifies as "
    "high-risk under Annex III (healthcare, employment, credit decisions). However, transparency "
    "obligations apply: customers should know they are interacting with AI-driven recommendations, "
    "not human curation.", body))

story.append(Paragraph("Trust and Customer Perception", h2))
story.append(Paragraph(
    "For the customer, trust hinges on one question: does this feel helpful or manipulative? "
    "PulsePass is designed to feel like a reward — points earned, recommendations earned, a "
    "community found. The win-back banner is honest about the offer. The email sequences are "
    "personal without being intrusive. The double-points incentive is genuine, not fabricated "
    "urgency. Provided PulseRetail honours rewards and keeps data use transparent, customers "
    "will feel seen — not surveilled.", body))

# ─── SECTION 5 ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 10))
story.append(hr())
story.append(Paragraph("Section 5 — Reflection and Insight", h1))
story.append(hr(color=colors.HexColor('#d0e8da'), thickness=0.5, spaceB=0, spaceA=10))

story.append(Paragraph("What Worked", h2))
story.append(Paragraph(
    "The pipeline architecture worked better than expected. The most striking outcome was how much "
    "richer each agent's output became because of the preceding agent's work. LYRA's email "
    "sequences are specific and credible — 'You're 60 points from your €10 reward' — because "
    "FORGE had already built a portal where 340 points was the customer state. A single agent "
    "asked to write marketing emails could not have produced that specificity. The handoff created "
    "emergent depth that no individual agent could achieve alone.", body))
story.append(Paragraph(
    "The separation of personality and domain expertise also worked well. ARIA's clinical, "
    "data-driven voice is genuinely distinct from ZARA's visionary tone, which is distinct from "
    "FORGE's blunt engineer voice. These are not the same model producing five slightly different "
    "responses — they are different professional identities producing fundamentally different types "
    "of work product.", body))

story.append(Paragraph("What Didn't Work", h2))
story.append(Paragraph(
    "The prototype requires a real backend to become production-ready. FORGE correctly flagged "
    "this: Emma's 340 points are hardcoded. In production, every customer would need live data "
    "from Shopify and a recommendation engine consuming real purchase history. The prototype is a "
    "high-fidelity demonstration, not a live system. CODA's risk register also identified that "
    "low portal adoption — customers not clicking from emails to the portal — is the highest "
    "probability risk. The pipeline produced a beautiful portal, but if the Day-3 email subject "
    "line is wrong, no one will ever see it.", body))

story.append(Paragraph("What I Learned About Multi-Agent Collaboration", h2))
story.append(Paragraph(
    "The handoff is the hardest part — and the most important. An agent that produces clean, "
    "structured, explicitly-labelled output (ARIA's numbered root causes, ZARA's bullet-pointed "
    "handoff notes) creates far more usable input for the next agent than prose. Structured "
    "outputs are the connective tissue of multi-agent systems.", body))
story.append(Paragraph(
    "The five archetypes reflect a genuine truth about how organisations work. Research, design, "
    "engineering, marketing, and management are not interchangeable. Each has a distinct "
    "epistemology. The best outcome comes from five genuine specialists, not one generalist "
    "wearing five hats.", body))

story.append(Paragraph("If I Had More Time", h2))
story.append(Paragraph(
    "I would build the Shopify integration, replace hardcoded data with real personalisation, "
    "and run the Day-3 email sequence through a live A/B test. I would also explore whether CODA "
    "could monitor post-launch performance data and trigger ARIA to re-run the analysis cycle — "
    "creating a self-improving feedback loop rather than a one-shot pipeline.", body))

# ─── AI USAGE TABLE ──────────────────────────────────────────────────────────
story.append(Spacer(1, 10))
story.append(hr())
story.append(Paragraph("AI Usage Declaration", h1))
story.append(Paragraph(
    "Generative AI use is required for this assignment. All AI-generated content was reviewed and "
    "edited for accuracy. System prompt design, agent personality definition, orchestration logic, "
    "and critical evaluation are the student's original contribution.", body))
story.append(Spacer(1, 6))

ai_table = simple_table(
    ['Agent', 'Model', 'Role in Pipeline'],
    [
        ['ARIA', 'Claude Sonnet 4.6', 'Customer Intelligence Analyst — Research Brief'],
        ['ZARA', 'Claude Sonnet 4.6', 'Experience Design Architect — Design Specification'],
        ['FORGE', 'Claude Sonnet 4.6', 'Product Engineer — Working Prototype (index.html)'],
        ['LYRA', 'Claude Sonnet 4.6', 'Brand & Marketing Strategist — GTM Strategy'],
        ['CODA', 'Claude Sonnet 4.6', 'Chief Operating Agent — Executive Summary'],
    ],
    col_widths=[2.5*cm, 4.5*cm, PAGE_W-2*MARGIN-7*cm]
)
story.append(ai_table)

story.append(Spacer(1, 14))
story.append(hr(color=GREY, thickness=0.5))
story.append(Paragraph(
    "GitHub Repository: https://github.com/ran-im/pulseretail-agents  ·  "
    "Live Prototype: https://ran-im.github.io/pulseretail-agents  ·  "
    "Word count: ~2,100 words",
    S('Footer', fontName='Helvetica', fontSize=8, textColor=GREY,
      alignment=TA_CENTER, leading=12)
))

# ─── Build ────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF generated: {output_path}")
