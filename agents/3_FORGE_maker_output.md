# FORGE — Maker Output

---

## BUILD REPORT: PulseRetail Re-Engagement Portal
**Prepared by:** FORGE, Product Engineer  
**Input:** ZARA Design Specification  
**Deployed at:** https://ran-im.github.io/pulseretail-agents  
**Date:** April 2026

---

## 1. Technical Architecture Overview

**Stack:** Vanilla HTML5 / CSS3 / ES6 JavaScript — zero dependencies, zero build step. Deliberate choice: the prototype needs to run anywhere, instantly, with no npm install, no framework, no runtime. It deploys as a single file to GitHub Pages.

**Architecture Pattern:** Single Page Application (SPA) — one `index.html` with embedded CSS and JS.

**Key Technical Decisions:**
| Decision | Rationale |
|---|---|
| Vanilla JS over React/Vue | GitHub Pages, no build pipeline — must run as static HTML |
| CSS custom properties (variables) | Design system consistency, easy theming |
| SVG for score ring | Crisp at all resolutions, fully animatable with CSS |
| CSS `@keyframes` for animations | GPU-accelerated, no JS library overhead |
| `setTimeout` for staggered reveals | Simulates real data loading, improves perceived UX |
| CSS Grid layout | Responsive without media query complexity |

---

## 2. Core Features Built

### Feature 1 — PulseScore Ring (Animated SVG)
- SVG circle with `stroke-dashoffset` animation technique
- Score animates from 0 → 340 on page load (1.8s cubic-bezier easing)
- Numeric counter increments in sync with ring animation
- Green drop-shadow filter simulates neon glow effect
- Progress bar below shows position between current tier (300) and next tier (400)

### Feature 2 — AI Recommendation Cards (3-Product Grid)
- Three product cards with distinct category gradients (yoga / running / gym)
- Eco certification badge overlay (top-right corner)
- `match%` score displayed per product (derived from user segment affinity)
- Hover state: `translateY(-4px)` lift + green border + glow shadow
- "Add to Bag" triggers toast notification with points earned message

### Feature 3 — Engagement Streak Tracker (28-day Calendar)
- 28-cell grid rendered dynamically in JavaScript
- Three states per cell: inactive (grey), active (green checkmark), purchase (gold star)
- Purchase days highlighted to reinforce high-value behaviour
- Summary stats: current streak, bonus points earned, status emoji

### Feature 4 — Community Proof Strip (Staggered Animation)
- Three community activity cards with staggered `setTimeout` reveals (0ms, 200ms, 400ms)
- Slide-in from right + fade opacity transition using CSS class toggle
- Each card shows: avatar, member name, recent action, time elapsed
- Creates sense of live activity without any backend

### Feature 5 — Win-Back Offer Banner
- Persistent top-of-page pulsing CTA banner
- CSS `@keyframes pulse-glow` animation (3s loop) draws eye to offer
- "Claim Offer" button triggers toast; would hook to email capture in production

### Feature 6 — Toast Notification System
- Global `showToast()` function — reusable across all CTAs
- Slide-up animation from bottom-right corner
- Auto-dismisses after 3 seconds
- Simulates the "something happened" feedback loop critical for engagement

---

## 3. Deployment Instructions

```bash
# 1. Create GitHub repository
gh repo create pulseretail-agents --public --description "PulseRetail Agentic Organisation"

# 2. Initialise and push
git init
git add prototype/index.html
git commit -m "Deploy PulsePass loyalty portal"
git push origin main

# 3. Enable GitHub Pages
# Settings → Pages → Source: Deploy from branch → main → /prototype
# OR: move index.html to root and set source to root /

# Live at: https://ran-im.github.io/pulseretail-agents
```

---

## 4. Feature Implementation Notes

**What works in the prototype:**
- Full visual fidelity to ZARA's design specification
- All 6 interactive features functional
- Responsive down to 375px (iPhone SE)
- Accessible: semantic HTML, sufficient colour contrast ratios

**Production extensions (out of scope for prototype):**
- Connect to real customer database (replace hardcoded Emma / 340 pts data)
- Wire "Add to Bag" to Shopify API
- Replace simulated community feed with real-time websocket events
- A/B test win-back banner copy using Optimizely or native split testing

*— FORGE, Product Engineer*  
*Handoff: Proceed to LYRA (Communicator)*
