# ML System Design 4-Stage Interview Scaffold
> Grounded in Chip Huyen's *Machine Learning System Design Interview* & Tencent Technical Architect Rubrics.

## Stage 1: Clarify Problem & Define Metrics (5-10 min)
- **Business Goal**: User engagement, GMV lift, operational cost reduction, latency SLA.
- **ML Metric vs Business Metric**:
  - Offline Metrics: Recall@K, NDCG@10, ROC-AUC, Perplexity, Hallucination Error Rate.
  - Online Metrics: P99 Latency (<50ms), Throughput (QPS), CTR lift, Churn reduction.
- **System Constraints**: Compute budget ($/month), VRAM limits, edge vs cloud inference, privacy compliance.

## Stage 2: Data Engineering & Pipeline Architecture (10-15 min)
- **Data Ingestion**: Streaming (Kafka/Flink) vs Batch (Spark/Airflow).
- **Feature Store**: Low-latency online read (Redis/DynamoDB) + Historical offline training store (Parquet/S3).
- **Labeling & Drift**: Weak supervision, active learning, data drift detection via Population Stability Index (PSI).

## Stage 3: Modeling & Algorithmic Trade-offs (15-20 min)
- **Model Hierarchy**: Baseline heuristic → Compact Classical (GBDT/LightGBM) → Deep Dual-Tower → Foundation Model (SFT/LoRA).
- **Adaptation Strategy**:
  - Prompt Engineering: Lowest cost, high agility, token-bound.
  - Hybrid RAG: External dynamic knowledge, hallucination mitigation via citation binding.
  - Domain Fine-Tuning (LoRA/QLoRA): Specialized syntax, tone alignment, domain-specific terminology.

## Stage 4: Serving, Deployment & Continuous Monitoring (10 min)
- **Inference Optimization**: Model quantization (AWQ/GPTQ INT4), vLLM PagedAttention, KV Cache pooling.
- **Resilience Protocol**: Fallback cascades (LLM -> Small SLM -> Cached rule-based response).
- **Rollout Strategy**: Shadow deployment -> 5% Canary A/B test -> Automated circuit breaker rollback.
