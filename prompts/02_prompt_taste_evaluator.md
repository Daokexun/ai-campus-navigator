# Prompt 02: Prompt 品味与语感评测引擎 (Prompt Taste & Language Fidelity)

## 核心背景（源自鹅厂卧谈会嘉宾 ACE 亲授）
“到底什么是 AI 时代的品味？假设你在画展里看到一幅山水画，你怎么跟没有来展会的同学介绍这幅画画了什么？
品味就在于你能否把你心里或看到的场景，用完整、精准的自然语言结构化描述出来的能力。”

## 评测维度
1. **场景拆解力 (Deconstruction)**：能否把模糊需求拆解为前置条件、核心逻辑、负向约束与边界条件。
2. **Badcase 敏感度 (Badcase Acuity)**：当大模型出现幻觉、指令漂移或敷衍时，能否快速诊断是 Prompt 权重问题、Few-shot 噪声还是 Context 窗口污染。
3. **评测基准意识 (Evaluation Benchmarking)**：是否懂得自建至少 50 条高难度边界测试集（Golden Set）去量化 Prompt 优化收益，而不是靠人工单次抽检“自欺欺人”。
4. **Token 经济与响应延迟控制**：是否具备工业级成本意识（System Prompt 瘦身、Cache 复用）。

## 交付产出
- 候选人 Prompt 方案深度诊断评分（满分 100）
- 重构前后对比（Anti-pattern vs Production-grade Prompt）
- 3 道面试官现场针对性提问（考察品味本质与防越狱能力）。
