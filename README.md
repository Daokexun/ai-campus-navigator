<div align="right">
  <a href="README_zh.md">简体中文</a> | <b>English</b>
</div>

<div align="center">

<img src="assets/hero_poster_en.jpg" alt="AI-Era Campus Recruitment Navigator & Engineering Engine" width="100%" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);" />

# AI-Era Campus Recruitment Navigator & Engineering Engine
### Engineering insights distilled from Tencent technical leads and hiring mentors

**A systematic framework to transcend API-wrapper commoditization, master prompt taste, and ship live 48h demos.**

</div>

---

### 📖 Editorial Background

> **"In the era where AI is accessible to everyone, a new graduate's core competitive advantage is never about running an open-source tutorial script. It is about understanding the commercial causalities behind code, mastering production-grade prompt taste, and delivering live testable systems."**  
> — Tencent Technical Mentors & Hiring Panels

Across AI-era campus hiring, technical candidates consistently stumble into three common blindspots:

1. **The API-Wrapper Trap**: Resumes saturated with "built an AI knowledge base using LangChain," yet freezing when asked about token budgets, VRAM allocations, or production p99 latency tradeoffs.
2. **Ambiguous Career Taxonomy**: Lacking clear distinction between Infrastructure (Infra), Fine-Tuning, Agentic Workflows, and Application-layer enablement, leading to unfocused applications.
3. **Screenshot-Only Portfolios**: Presenting static screenshots and terminal logs instead of end-to-end, live interactive prototypes that hiring managers can test on their phones during the interview.

This playbook synthesizes guidance from senior engineering interviewers: **4-Quadrant Role Taxonomy, Prompt Taste Building, 48-Hour Live Demo Prototyping, and Adversarial Architecture Defense**.

---

### 🏛️ Four Core Pillars

Modeled after modern SaaS engineering publication standards:

| Pillar | Strategic Purpose | Core Execution Mechanism |
| :--- | :--- | :--- |
| **01 4-Quadrant Role Taxonomy**<br>`prompts/01_ai_career_compass.md` | Align candidate capabilities with high-leverage roles | Classifies positions across Infrastructure, Domain Fine-Tuning, Agent Systems, and App Enablement. |
| **02 Production Prompt Taste**<br>`prompts/02_prompt_taste_builder.md` | Elevate from novice queries to robust contracts | Replaces vague prompts with multi-modal context injection, negative edge constraints, and strict schema validation. |
| **03 48-Hour Demo Loop**<br>`prompts/03_interactive_demo_loop.md` | Ship testable prototypes in under 48 hours | Uses Streamlit and Gradio on serverless containers to deliver mobile-accessible, live test environments. |
| **04 Technical Depth Probes**<br>`prompts/04_technical_depth_probe.md` | Defend against senior architectural challenges | Stress-tests VRAM memory math, throughput vs. latency tradeoffs, hallucination mitigation, and graceful degradation. |

---

### 📐 System Architecture

The following diagram illustrates the candidate journey from role classification to interactive demo deployment and panel defense:

<div align="center">
  <img src="assets/architecture.png" alt="System Architecture Diagram" width="100%" />
</div>

---

### 🥊 Tactical Breakdown: API Wrapper Novice vs. Engineering Candidate

| Interview Challenge | Generic Wrapper Novice | Production-Grade Candidate |
| :--- | :--- | :--- |
| **"How do you mitigate hallucinations in your RAG pipeline?"** | Naive prompt pleading: "We added 'do not make things up' to the prompt and ran default LangChain vector search." | **3-Tier Production Defense**: "Prompt pleading cannot reliably eliminate hallucination. We enforce three layers: 1. **Retrieval**: Hybrid dense + sparse search with a strict similarity threshold; 2. **Inference**: Strict citation constraints linking outputs to passage IDs; 3. **Post-Processing**: Fact-verification validator that triggers graceful degradation if entity matching drops below 85%." |
| **Demonstrating Project Portfolio** | Scrolling through a terminal log or showing static presentation slides. | **Live Interactive Verification**: "The system is live on a serverless container. Here is a QR code you can scan on your mobile browser right now to test live query latency, rate limiting, and structured JSON outputs under real network conditions." |
| **"What fails first if production traffic spikes 10x?"** | Vague guessing: "Probably the server CPU runs out, so we add bigger cloud instances." | **Bottleneck Isolation & Caching Strategy**: "The bottleneck is downstream LLM token-per-minute (TPM) quotas and vector DB query latency. To survive 10x spikes, we introduced a semantic Redis cache that absorbs 42% of repetitive queries, while routing high-latency generation jobs into an async Celery task queue." |

---

### 📂 Repository Structure

```text
ai-campus-navigator/
├── assets/
│   ├── hero_poster_en.jpg           # Dropbox-style English publication banner
│   ├── hero_poster_zh.jpg           # Chinese publication banner
│   ├── architecture.svg             # English vector architecture diagram
│   └── architecture_zh.svg          # Chinese vector architecture diagram
├── prompts/
│   ├── 01_ai_career_compass.md          # 4-quadrant role navigation workbench
│   ├── 02_prompt_taste_builder.md       # Production prompt taste calibration
│   ├── 03_interactive_demo_loop.md      # 48-hour live demo shipping manual
│   ├── 04_technical_depth_probe.md      # 10 deep architectural interview probes
│   └── 05_github_showcase_architect.md  # High-impact GitHub README engineering
├── templates/
│   └── candidate_profile_schema.json    # Candidate competency evaluation schema
├── evals/
│   └── rubric_100_ai_campus.json        # 100-point AI campus interview rubric
├── docs/
│   └── ARCHITECTURE.md                  # Comprehensive AI campus navigator whitepaper
├── examples/
│   └── SHOWCASE_COMPARISON.md           # Novice wrapper vs. production project comparison
├── SKILL.md                             # Antigravity / Claude Agent Skill specification
├── README.md                            # English documentation (current file)
└── README_zh.md                     # Chinese documentation
```

---

### 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/Daokexun/ai-campus-navigator.git

# Inspect the prompt taste builder workbench
cat prompts/02_prompt_taste_builder.md
```

---

### 📄 License & Community

This project is open-sourced under the [MIT License](LICENSE). Contributions from hiring managers, AI engineers, and educators are welcomed via [CONTRIBUTING.md](CONTRIBUTING.md).
