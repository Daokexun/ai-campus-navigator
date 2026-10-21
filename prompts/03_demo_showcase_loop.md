# Prompt 03: 真实 Demo 闭环与项目提纯工坊 (End-to-End Demo Showcase)

## 核心法则
**“哪怕只用开源 API 搭过一个能跑通真实闭环的小工具，也胜过简历上抄了 10 个跑不通的 GitHub 开源课设。”**

## 项目提纯四步法则
1. **Why AI (为什么必须是 AI)**：严禁拿 AI 解决本该用 SQL 或正则就能完美解决的伪需求。必须证明非确定性与生成式智能的不可替代性。
2. **Architecture & Pipeline (全链路技术选型)**：
   - 检索链路（Embedding 模型、分块策略、混合检索、重排 Reranker）
   - 大模型链路（Base Model 选型、Prompt 路由、Fallback 保底策略）
3. **Badcase & Iteration (挫折与迭代纪实)**：
   - 真实记录在 V1 版本中被真实用户喷得最惨的 3 个 Badcase 是什么？
   - 你通过什么具体手段（Few-shot 对齐 / 工具调用 / 结构化 JSON Schema）彻底解决了它们？
4. **Data & Metrics (量化结果验证)**：准确率、响应延迟（P95）、Token 消耗、真实使用留存。
