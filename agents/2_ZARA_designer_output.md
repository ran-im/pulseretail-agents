# ZARA — Designer Output

---

## DESIGN SPECIFICATION: PulseRetail Re-Engagement Engine
**Prepared by:** ZARA, Experience Design Architect  
**Input:** ARIA Research Brief  
**Date:** April 2026

---

## 1. Solution Concept

**The PulseRetail Loyalty Intelligence Portal ("PulsePass")**

ARIA's research reveals a fundamental truth: PulseRetail customers don't leave because they dislike the brand. They leave because the brand stops talking to them. The solution is not a generic loyalty points card — it's a **living, personalised customer home** that makes every returning visitor feel known.

PulsePass is a web-based experience (deployable as a GitHub Page, embeddable into the main site) that serves as the customer's personalised command centre:
- Their purchase history and style profile
- A real-time loyalty score with progress to the next reward
- AI-generated "Your Next Pulse" product recommendations
- Community highlights (showing their tribe)
- A dynamic engagement streak tracker

The emotional design principle: **"Every time you come back, we know you better."**

---

## 2. User Journey Map

```
TOUCHPOINT 1 — Day 3 (Post-Purchase Email)
User receives: "Your order is arriving tomorrow — here's how to style it."
Action: Opens email → clicks "See your PulseProfile"
Landing: PulsePass portal, pre-filled with their purchase

         ↓

TOUCHPOINT 2 — Day 7 (Portal Visit)
User sees: Their loyalty score, "Earn 50 more points for a €10 reward"
User sees: AI recommendation — "Customers who bought X also loved Y"
Action: Browses → potentially re-purchases

         ↓

TOUCHPOINT 3 — Day 14 (Trigger Email)
Condition: User has NOT returned to portal since Day 7
Message: "Your next reward is waiting. You're 1 purchase away."
Action: Returns to portal with specific incentive

         ↓

TOUCHPOINT 4 — Day 30 (Win-Back Email)
Condition: No purchase in 30 days
Message: Personalised, product-specific, limited-time offer
Action: Direct link to recommended product with discount applied
```

---

## 3. Feature Specifications

### Feature 1 — PulseScore (Loyalty Intelligence Meter)
- Visual circular progress indicator showing points balance
- Clear next milestone with reward amount (€5 / €10 / €20 tiers)
- Points awarded for: purchases, reviews, social shares, referrals
- Animated progress on each visit to reinforce momentum

### Feature 2 — AI Recommendation Panel ("Your Next Pulse")
- Displays 3 personalised product cards
- Logic: Category affinity (yoga buyer → yoga) + bestsellers in that category + seasonal relevance
- Each card shows: product image, name, price, sustainability score
- CTA: "Add to Bag" — direct purchase pathway

### Feature 3 — Engagement Streak Tracker
- Calendar-style visualisation of customer activity (visits, purchases, reviews)
- "You've been with Pulse for 47 days" — time-investment psychology
- Streak bonuses: 3 visits in a week = bonus 25 points

### Feature 4 — Community Proof Strip
- Rotating UGC-style testimonial cards from other customers in same segment
- "182 yoga enthusiasts bought this with their Align Leggings"
- Social proof designed to feel organic, not promotional

### Feature 5 — Quick Re-Engagement CTA
- Persistent "Continue Your Journey" button
- If last purchase was >21 days ago: surfaces the win-back offer
- If last purchase was <7 days ago: surfaces complementary product

---

## 4. UI/UX Principles

**Principle 1 — Dark Athletic Aesthetic**  
Colour palette: Deep charcoal (#1a1a2e), electric green (#00f5a0), warm white (#f8f9fa). Reflects activewear energy — serious, premium, athletic.

**Principle 2 — Motion as Feedback**  
Every interaction should respond. Score meters animate. Cards slide in. Streaks pulse. Motion communicates that this is a living system, not a static page.

**Principle 3 — Personal Over Generic**  
Every line of copy uses the customer's first name, purchase history, and segment. "Emma, your Align Leggings are perfect for this" beats "Check out our new arrivals."

**Principle 4 — Frictionless Path to Purchase**  
Maximum two clicks from portal to checkout. No dead ends. Every screen has a clear next action.

**Principle 5 — Trust Through Transparency**  
The portal shows exactly how points are earned, exactly what data is used for recommendations, and includes a clear "Why am I seeing this?" link on all AI recommendations (GDPR-aligned).

---

## 5. Handoff Notes for FORGE (Maker)

**Build this as a single-page HTML/CSS/JS application:**

- Use vanilla JavaScript — no frameworks required for the prototype
- Data can be hardcoded for demonstration (simulate a returning customer "Emma, yoga buyer, 340 points")
- Animate the PulseScore meter using CSS `@keyframes` on load
- Recommendation cards: 3 cards with product image, name, price, sustainability badge
- Community strip: 3 rotating testimonial cards using `setInterval`
- Streak tracker: 7-day calendar grid rendered in JS
- Colour variables: `--pulse-dark: #1a1a2e`, `--pulse-green: #00f5a0`, `--pulse-white: #f8f9fa`
- Mobile-first responsive layout (grid-based)
- Deploy-ready for GitHub Pages (single `index.html` file with embedded CSS/JS)

*— ZARA, Experience Design Architect*  
*Handoff: Proceed to FORGE (Maker)*
