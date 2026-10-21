<p align="center">
  <img src="assets/hero_poster_en.jpg" alt="BigTech AI Campus Navigator GTM" width="100%" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.18);" />
</p>

<div align="center">

**English** • [简体中文](README_zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Skill: Antigravity](https://img.shields.io/badge/Skill-Antigravity-6366f1.svg?style=flat-square)](SKILL.md)
[![Target Audience](https://img.shields.io/badge/Audience-2026/2027_Grads_%7C_BigTech_Interns-10b981.svg?style=flat-square)](#-three-strategic-gtm-pillars)
[![Quality Gate](https://img.shields.io/badge/Audit-Adversarial_Passed-06b6d4.svg?style=flat-square)](evals/rubric_100_ai_campus.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-violet.svg?style=flat-square)](CONTRIBUTING.md)

<p align="center">
  <b>As artificial intelligence transforms engineering paradigms, the fundamental rubric for campus recruiting has radically evolved.</b><br>
  Stop treating LeetCode grinding and wrapper tutorials as your moat. Grounded in direct insights from Tencent Campus Recruiting PMs and interviewers, this system re-engineers candidate competitiveness through role taxonomy, prompt engineering taste, end-to-end interactive demos, and adversarial defense.
</p>

[GTM Philosophy](#-what-is-a-gtm-strategy-for-ai-campus-recruiting) • [Core Pillars](#-three-strategic-gtm-pillars) • [4-Step Roadmap](#-four-step-gtm-implementation-roadmap) • [Live Comparison](#-real-world-comparison-generic-leetcode-resume-vs-ai-navigator-system) • [Quickstart](#-quickstart) • [Architecture](docs/ARCHITECTURE.md)

---

</div>

## 🎯 What is a GTM Strategy for AI Campus Recruiting?

> **“Think of a go-to-market strategy as the north star that guides your product launch.”**  
> —— Amazon Ads Official GTM Guide

In campus hiring, candidates spend months grinding 500 algorithm problems and filling resumes with hollow buzzwords like *"proficient in LLMs, RAG, and LangChain"*. They submit hundreds of applications, only to crumble in technical interviews when challenged on real-world engineering constraints.

**The issue is not university pedigree. The bottleneck is positioning and product closure: the candidate's portfolio fails to earn the trust of BigTech interviewers.**

Campus job-seeking is a product launch. You are bringing an elite high-potential product (yourself) to market:
1. **Understand Your Audience**: What are top engineering teams actually hiring for right now? Foundational research, inference optimization, or AI Product Managers?
2. **Build Defensible Moats**: When everyone can generate code with AI, where is your natural language scene deconstruction and prompt taste?
3. **Deliver Real-World Closures**: A working, deployed prototype with authentic user feedback outperforms ten static classroom homework repos.

**`ai-campus-navigator`** distills insights from Tencent's recruitment team (*Tencent Bedtime Talks* EP11) into an autonomous, standardized Agent Skill.

---

## 🏛️ Three Strategic GTM Pillars

| Strategic Pillar | Core Operational Engine | Practical Value & Output |
| :--- | :--- | :--- |
| **1. Role Taxonomy Precision<br/>(Understand Audience)** | Classifies candidates across Research (Qingyun), System/Inference, AI PM, and Domain+AI tracks. | Eliminates blind applications and targets roles where the candidate holds unfair structural advantages. |
| **2. Prompt Taste & Language Fidelity<br/>(Prompt & Taste)** | Applies the "Landscape Painting Natural Language Fidelity" standard to prompt engineering and test suites. | Moves beyond superficial chat prompts into production-grade constraints, badcase triage, and Golden Sets. |
| **3. End-to-End Demo Closure<br/>(Interactive Demo)** | Demands explicit "Why AI" justification, token economy budgets, and authentic iteration logs. | Replaces unverified toy code with battle-tested workflows that prove end-to-end problem-solving mastery. |

---

## 🔄 Four-Step GTM Implementation Roadmap

<p align="center">
  <img src="assets/architecture.svg" alt="AI Campus Navigator 4-Stage Architecture" width="100%" style="border-radius: 12px;" />
</p>

### 📍 Step 1. Role Taxonomy Precision
- **Algorithm Research (Qingyun Track)**: Original research contributions, top-tier publications, and deep pre-training/alignment thinking.
- **Inference & Systems**: vLLM/TensorRT-LLM kernel optimization, quantization, and high-throughput model serving.
- **AI Product Manager**: Problem discovery, workflow orchestration, prompt architecture, and user experience loops.
- **Domain + AI Hybrid**: Cross-functional talent applying AI-native workflows to multiply operational output 10x.

### 📍 Step 2. Prompt Taste & Language Fidelity
- **Structured Natural Language**: Transforms ambiguous requests into rigorous input protocols, negative guardrails, and deterministic schema outputs.
- **Golden Evaluation Sets**: Builds 50+ adversarial test cases to measure factual drift, hallucination rates, and prompt performance objectively.

### 📍 Step 3. End-to-End Demo Closure
- **The "Why AI" Proof**: Demonstrates why traditional rule-based algorithms or SQL fail, proving generative AI is strictly required.
- **Token & Latency Economics**: Analyzes cost-per-call, prompt caching efficiencies, and P95 latency thresholds.
- **Authentic Failure Triage**: Documents real catastrophic failures and the architectural interventions that resolved them.

### 📍 Step 4. Adversarial Red-Team Defense
- **Skeptical Interviewer Grilling**: Simulates a senior Tencent technical architect stress-testing claims line by line.
- **100-Point Quality Gate**: Flags academic exaggeration, wrapper libraries, and boilerplate claims before any real interview.

---

## 🥊 Real-World Comparison: Generic LeetCode Resume vs. AI Navigator System

| Dimension | ❌ Generic Candidate (Direct ChatGPT Output) | 💎 AI Navigator Candidate (BigTech Approved) |
| :--- | :--- | :--- |
| **Positioning** | *"Passionate about AI, familiar with mainstream LLMs and Prompt Engineering, strong teamwork and stress tolerance."*<br>*(Hollow buzzwords; dismissed within 3 seconds)* | **【AI-Native Workflow Architect · Engineering & Taste】**<br>Specialized in vertical search and agentic collaboration. Built 500+ boundary test sets, orchestrating reliable workflows with a 34% drop in hallucinations. |
| **Project Description<br/>(RAG System)** | *"Built an enterprise Q&A system based on LangChain calling GPT-4, achieving accurate retrieval and praise from professors."*<br>*(Zero architectural depth; obvious wrapper code)* | **“🧼 【Parent-Child Chunking + Hybrid Rerank Knowledge Base】”**<br>Solved retrieval failures in nested tables. Evaluated semantic vs recursive chunking, integrated BGE-Reranker for 92% top-3 recall, and slashed token costs 42% via fallback routing. |
| **Interview Defense** | Interviewer: *"How do you diagnose hallucinations during conversational follow-ups?"*<br>Candidate: *"I ask the user to rephrase or lower temperature."*<br>*(Reveals zero industrial engineering intuition)* | **“5-Stage Root Cause Triage”**: Pinpoints attention weight decay, context window overflow, or retrieval noise. Implements few-shot negative guardrails and strict JSON schema validation to block 90% of drift. |
| **Young Talent Track** | Blindly applies to top-tier programs with basic class projects; screened out in resume triage. | **Asymmetric Depth Strategy**: Maximizes single-point breakthroughs (e.g. edge quantization with 200ms response) backed by interactive video demos and failure retrospectives. |

---

## 🧠 Core Interviewer Mindset

### 1. Curiosity Beats Rehearsed Answers
Recruiters despise memorized textbook answers that collapse under deep inspection. Showing genuine technical experiments you explored out of curiosity is 10x more compelling.

### 2. A Living Demo is the Ultimate Lever
A deployed interactive URL with real user analytics completely overshadows ten lines of "proficient in" on a paper resume.

### 3. Clear Structure Reflects Cognitive Rigor
Can you explain a complex multi-agent system in plain language? Can you diagnose failure modes calmly? These are the enduring skills BigTech prioritizes.

---

## 📂 Project Structure

```text
ai-campus-navigator/
├── SKILL.md                          # Antigravity Agent Skill Specification
├── README.md                         # Project Presentation (English)
├── README_zh.md                      # Project Presentation (简体中文)
├── LICENSE                           # MIT Open-Source License
├── CONTRIBUTING.md                   # Contribution Guidelines
├── assets/                           # High-Impact Commercial Posters & SVGs
│   ├── hero_poster_en.jpg            # English Commercial Ad Poster
│   ├── hero_poster_zh.jpg            # Chinese Commercial Ad Poster
│   ├── architecture.svg              # English 4-Stage GTM Architecture
│   └── architecture_zh.svg           # Chinese 4-Stage GTM Architecture
├── prompts/                          # 5 Modular Prompt Engines
│   ├── 01_ai_role_radar.md           # 4-Quadrant Role Taxonomy Diagnostic
│   ├── 02_prompt_taste_evaluator.md  # Prompt Taste & Language Fidelity
│   ├── 03_demo_showcase_loop.md      # End-to-End Demo Showcase Loop
│   ├── 04_qingyun_talent_matrix.md   # Top-Tier Young Talent Strategy
│   └── 05_adversarial_interviewer_audit.md # Skeptical Interviewer Gatekeeper
├── templates/                        # Evaluation Schemas
│   └── ai_portfolio_schema.json      # Structured JSON Output Schema
├── evals/                            # Quality Benchmarks
│   └── rubric_100_ai_campus.json     # 100-Point Evaluation Rubric
├── docs/                             # Engineering Architecture
│   └── ARCHITECTURE.md               # Technical Pipeline Architecture
└── examples/                         # Real-World Benchmarks
    └── SHOWCASE_COMPARISON.md        # Generic Candidate vs. Navigator Benchmark
```

---

## 🚀 Quickstart

### Invoke in Google Antigravity or Claude Agent
Place in `.agents/skills/ai-campus-navigator`:

```text
/skill ai-campus-navigator
Target Role: Tencent AI Product Manager (or Qingyun Track)
Current Background: Computer Science & Business, built an interactive RAG demo
Core Dilemma: Project looks similar to others, need to prove defensible moats
```

---

## 🤝 Contributing & License

Contributions, new company rubrics, and interview cases are welcome!  
Distributed under the [MIT License](LICENSE).
