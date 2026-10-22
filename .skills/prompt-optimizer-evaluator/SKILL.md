---
name: prompt-optimizer-evaluator
description: Autonomous prompt evaluation, classification, negative constraint enforcement, and variant generation engine. Grounded in OpenAI Cookbook, Anthropic Skill Specs, and Tencent Technical Mentor practices.
suggest_when: The user or candidate wants to evaluate prompt quality, upgrade naive student prompts to production-grade contracts, or benchmark prompt performance.
---

# Prompt Optimizer & Evaluator Skill

## Overview
This skill operates as an autonomous prompt calibration engineer. It analyzes raw prompt text, detects missing production constraints, generates 3 optimized contract variants, and produces synthetic edge-case tests.

## 7-Step Execution Protocol
1. **Define Scope**: Extract user task domain (Summarization, RAG Extraction, Agentic Tool-Use, Code Gen).
2. **Classify Technique**: Label prompting strategy (Zero-Shot, Few-Shot, Chain-of-Thought, ReAct, XML-Delimited).
3. **Audit Missing Constraints (P0-P3 Severity)**:
   - **P0**: Missing JSON/Schema determinism or undefined output type.
   - **P1**: Missing hard negative boundary constraints ("DO NOT fabricate external facts").
   - **P2**: Ambiguous context boundaries (missing XML `<context>` or Markdown fences).
   - **P3**: Absence of graceful degradation protocol when confidence is low.
4. **Generate 3 Calibrated Variants**:
   - *Variant A (Minimal Production Contract)*: Fast, low-latency, strict schema.
   - *Variant B (Chain-of-Thought Guarded)*: High-accuracy, step-by-step reasoning with hidden scratchpad.
   - *Variant C (ReAct / Tool-Use Protocol)*: Multi-turn autonomous tool invocation schema.
5. **Generate Synthetic Test Suite**: Produce 3 test inputs (1 happy path, 1 adversarial jailbreak attempt, 1 boundary hallucination probe).
6. **Output Structured Report**: Return formatted markdown matching production enterprise standards.
