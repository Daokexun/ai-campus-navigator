# AI Campus Hiring: 1-Page Engineering Quick Reference

### 🎯 4-Quadrant Role Diagnostic Matrix
| Quadrant | Core Tech Stack | Interview Kill-Shot Question | Pass Criteria |
| :--- | :--- | :--- | :--- |
| **Q1: Compute Infra** | NCCL, vLLM, DeepSpeed, Triton, RoCE | *"How does KV Cache scale with batch size and context length in multi-GPU inference?"* | Exact VRAM memory equation: `2 * 2 * n_layers * n_heads * d_head * seq_len * batch_size`. |
| **Q2: Fine-Tuning** | LoRA, QLoRA, Axolotl, Unsloth, DPO | *"Why did LoRA rank r=16 outperform r=64 on your validation loss curve?"* | Cites rank saturation, catastrophic forgetting, and parameter efficiency trade-offs. |
| **Q3: Agent Systems** | LangGraph, AutoGen, CrewAI, Function Calling | *"How do you prevent cyclic deadlocks when tool execution fails repeatedly?"* | State-machine retry caps, exponential backoff, and synthetic fallback responses. |
| **Q4: App Enablement** | Streamlit, FastAPI, Milvus, Hybrid RAG | *"How do you eliminate hallucination in domain Q&A?"* | 3-tier defense: Hybrid search threshold + Citation binding + Graceful fallback validator. |

---

### 🛡️ Production Prompt Contract Checklist (10 Hard Negative Rules)
- [ ] 1. Never use polite conversational padding ("Please", "Kindly", "Thank you").
- [ ] 2. Explicitly delimit system directives, input documents, and user inputs using XML or Markdown fence blocks.
- [ ] 3. Include at least 2 hard negative constraints ("Strictly DO NOT extrapolate beyond provided facts").
- [ ] 4. Define exact JSON Schema with mandatory typing and default fallback states.
- [ ] 5. Declare explicit token budget and max length limits to prevent context overflow.
