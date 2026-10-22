#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Campus Navigator - Interactive Prompt Taste & Engineering Depth Evaluator
Run: python cli/taste_evaluator.py --taste-test
"""

import sys
import argparse
import time

BANNER = """
======================================================================
   AI CAMPUS NAVIGATOR // PROMPT TASTE & ARCHITECTURE AUDITOR
   Grounded in Tencent Technical Mentors & Hiring Panel Guidelines
======================================================================
"""

def evaluate_prompt(prompt_text):
    scores = {
        "context_injection": 0,
        "negative_constraints": 0,
        "schema_determinism": 0,
        "fallback_grace": 0
    }
    feedback = []

    lower = prompt_text.lower()
    
    # Check context injection
    if any(k in lower for k in ["context", "background", "role", "input document", "上下文", "背景", "角色"]):
        scores["context_injection"] = 25
        feedback.append("  [PASS] Context injection & role boundary detected (+25)")
    else:
        feedback.append("  [FAIL] Missing structured context injection boundary (-25)")

    # Check negative constraints
    if any(k in lower for k in ["do not", "never", "strictly prohibited", "forbidden", "严禁", "禁止", "不要"]):
        scores["negative_constraints"] = 25
        feedback.append("  [PASS] Hard negative boundary constraints enforced (+25)")
    else:
        feedback.append("  [WARN] Weak negative constraints; prompt prone to hallucination (-25)")

    # Check schema determinism
    if any(k in lower for k in ["json", "schema", "output format", "字段", "键值", "```json"]):
        scores["schema_determinism"] = 25
        feedback.append("  [PASS] Strict schema definition found (+25)")
    else:
        feedback.append("  [FAIL] Output format ambiguous; missing machine-readable schema (-25)")

    # Check fallback grace
    if any(k in lower for k in ["if unknown", "fallback", "return null", "degrade", "insufficient", "优雅降级", "未知时返回", "兜底"]):
        scores["fallback_grace"] = 25
        feedback.append("  [PASS] Resilient edge-case fallback protocol detected (+25)")
    else:
        feedback.append("  [WARN] Missing explicit fallback behavior when uncertainty occurs (-25)")

    total = sum(scores.values())
    return total, feedback

def run_taste_test():
    print(BANNER)
    print("Testing sample: Novice Student Prompt vs. Production Contract Prompt\n")
    
    sample_novice = "Please summarize this document for me and make it good, thanks."
    sample_prod = """
[ROLE & CONTEXT]
You are a senior tech editor. Summarize the following engineering report for executive review.

[NEGATIVE CONSTRAINTS]
1. Strictly DO NOT introduce external unverified metrics.
2. DO NOT use generic filler phrases or marketing hype.

[OUTPUT SCHEMA]
Return strict JSON format:
{
  "summary": "1-sentence executive summary",
  "key_findings": ["finding1", "finding2"],
  "risk_flags": ["risk1", "risk2"]
}
If context is insufficient, set "risk_flags": ["INSUFFICIENT_DATA"] and degrade gracefully.
"""

    print("--- 1. Evaluating Novice Student Prompt ---")
    print(f"Prompt: \"{sample_novice}\"")
    score1, fb1 = evaluate_prompt(sample_novice)
    for f in fb1:
        print(f)
    print(f"-> Total Score: {score1}/100 [Level: Student / API Wrapper Novice]\n")

    time.sleep(0.3)

    print("--- 2. Evaluating Production Contract Prompt ---")
    score2, fb2 = evaluate_prompt(sample_prod)
    for f in fb2:
        print(f)
    print(f"-> Total Score: {score2}/100 [Level: Production-Grade Engineering Candidate]\n")
    print("======================================================================")
    print("Verdict: Production-grade taste enforces negative boundaries & strict schemas.")
    print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="AI Campus Navigator Taste Evaluator")
    parser.add_argument("--taste-test", action="store_true", help="Run comparative prompt taste test")
    parser.add_argument("--eval", type=str, help="Evaluate a specific prompt text")
    args = parser.parse_args()

    if args.taste_test or len(sys.argv) == 1:
        run_taste_test()
    elif args.eval:
        print(BANNER)
        score, fb = evaluate_prompt(args.eval)
        for f in fb:
            print(f)
        print(f"\nFinal Score: {score}/100")

if __name__ == "__main__":
    main()
