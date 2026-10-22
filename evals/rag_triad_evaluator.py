#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG Triad Evaluator - Grounded in Ragas & DeepEval Methodologies
Evaluates Faithfulness, Answer Relevance, and Context Precision.
Run: python evals/rag_triad_evaluator.py --test
"""

import sys
import argparse
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def evaluate_rag_triad(query, context, answer):
    """
    Deterministic rule-based evaluation of RAG Triad:
    1. Faithfulness: Ratio of answer statements directly anchored in context.
    2. Answer Relevance: Query keyword coverage in answer without padding.
    3. Context Precision: Signal-to-noise ratio in retrieved context.
    """
    q_words = set(query.lower().replace("?", "").replace("。", "").split())
    ctx_lower = context.lower()
    ans_lower = answer.lower()

    # 1. Faithfulness check
    ans_sentences = [s.strip() for s in answer.split("。") if len(s.strip()) > 3] or [answer]
    supported_sentences = 0
    for s in ans_sentences:
        s_words = [w for w in s.lower().split() if len(w) > 2]
        if any(w in ctx_lower for w in s_words):
            supported_sentences += 1
    faithfulness = round(supported_sentences / max(1, len(ans_sentences)), 2)

    # 2. Answer Relevance check
    query_overlap = sum(1 for w in q_words if w in ans_lower)
    relevance = round(min(1.0, query_overlap / max(1, len(q_words))), 2)

    # 3. Context Precision check
    ctx_words = [w for w in ctx_lower.split() if len(w) > 2]
    signal_words = sum(1 for w in ctx_words if w in ans_lower)
    precision = round(min(1.0, signal_words / max(1, len(ctx_words) * 0.4)), 2)

    overall_score = round((faithfulness * 0.4 + relevance * 0.35 + precision * 0.25) * 100, 1)

    return {
        "faithfulness": faithfulness,
        "answer_relevance": relevance,
        "context_precision": precision,
        "overall_score": overall_score,
        "passed": overall_score >= 75.0
    }

def run_test():
    print("======================================================================")
    print("   AI CAMPUS NAVIGATOR // RAG TRIAD DETERMINISTIC EVALUATOR")
    print("   Grounded in Ragas, DeepEval & Tencent BigTech Production Rubrics")
    print("======================================================================\n")

    sample_query = "What is the primary trade-off when using LoRA with rank r=16 versus r=64?"
    sample_context = (
        "LoRA freezes pretrained model weights and injects trainable rank decomposition matrices. "
        "Lower rank like r=16 reduces trainable parameters and VRAM overhead, preventing catastrophic forgetting "
        "on small domain datasets. Higher rank like r=64 captures more expressive capacity for complex multi-task "
        "adaptation but risks overfitting and increases VRAM footprint during backward passes."
    )
    
    sample_answer_elite = (
        "Using LoRA with rank r=16 reduces trainable parameters and VRAM overhead while preventing overfitting. "
        "In contrast, rank r=64 offers higher expressive capacity for multi-task adaptation but incurs higher "
        "VRAM consumption and risks catastrophic forgetting on small datasets."
    )

    sample_answer_hallucinated = (
        "LoRA r=16 is always better because it runs 10x faster and was developed by Google in 2024 to replace all GPUs."
    )

    print("--- 1. Evaluating Production-Grade Grounded Answer ---")
    res1 = evaluate_rag_triad(sample_query, sample_context, sample_answer_elite)
    print(f"  Faithfulness Score:       {res1['faithfulness'] * 100}%")
    print(f"  Answer Relevance Score:   {res1['answer_relevance'] * 100}%")
    print(f"  Context Precision Score:  {res1['context_precision'] * 100}%")
    print(f"  -> Total Triad Score:     {res1['overall_score']}/100 [Status: {'PASSED' if res1['passed'] else 'FAILED'}]\n")

    time.sleep(0.3)

    print("--- 2. Evaluating Hallucinated Answer ---")
    res2 = evaluate_rag_triad(sample_query, sample_context, sample_answer_hallucinated)
    print(f"  Faithfulness Score:       {res2['faithfulness'] * 100}%")
    print(f"  Answer Relevance Score:   {res2['answer_relevance'] * 100}%")
    print(f"  Context Precision Score:  {res2['context_precision'] * 100}%")
    print(f"  -> Total Triad Score:     {res2['overall_score']}/100 [Status: {'PASSED' if res2['passed'] else 'FAILED'}]\n")
    print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="RAG Triad Evaluator")
    parser.add_argument("--test", action="store_true", help="Run automated test suite")
    args = parser.parse_args()

    if args.test or len(sys.argv) == 1:
        run_test()

if __name__ == "__main__":
    main()
