<p align="center">
  <img src="assets/hero_poster_zh.jpg" alt="鹅厂校招特辑 · AI 时代求职导航 GTM" width="100%" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.18);" />
</p>

<div align="center">

[English](README.md) • **简体中文**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Skill: Antigravity](https://img.shields.io/badge/技能-Antigravity-6366f1.svg?style=flat-square)](SKILL.md)
[![适合人群](https://img.shields.io/badge/适配人群-2026/2027届校招生_%7C_大厂实习-10b981.svg?style=flat-square)](#-高转化校招求职的三大-gtm-战略基石)
[![审核机制](https://img.shields.io/badge/面试官质检-红蓝对抗通过-06b6d4.svg?style=flat-square)](evals/rubric_100_ai_campus.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-欢迎共建-violet.svg?style=flat-square)](CONTRIBUTING.md)

<p align="center">
  <b>在 AI 浪潮重塑技术生态的当下，校招求职的底层评判逻辑已经发生剧变。</b><br>
  别再把简单刷题和套壳代码当做护城河。基于腾讯校园招聘团队一手实战洞察，用“岗位四维象限、Prompt 语感品味、真实 Demo 闭环与青云对抗防守”，重塑这一届校招生的真正大厂竞争力。
</p>

[GTM 理念](#-什么是-ai-校招的-go-to-market-gtm-策略) • [三大战略基石](#-高转化校招求职的三大-gtm-战略基石) • [四步落地路线](#-四步重构大厂校招竞争力gtm-实施路线) • [实战真实对比](#-实战真实对比自嗨刷题简历-vs-本工具重塑的高转化方案) • [极速上手](#-30秒极速上手) • [系列项目规范](docs/ARCHITECTURE.md)

---

</div>

## 🎯 什么是 AI 校招的 Go-to-Market (GTM) 策略？

> **“Think of a go-to-market strategy as the north star that guides your product launch.”**  
> —— 亚马逊官方 GTM 指南

在校招中，很多应届生把绝大多数精力花在刷 500 道 LeetCode、在简历里堆满“熟练掌握 Transformer/RAG/LangChain”这样空洞的自嗨词汇上。简历投出去几百份，结果面试一问三不知，二面就被面试官连环深挖打回原形。

**问题不在你的学历，而在你的定位与交付——你的求职 Portfolio 没有建立大厂面试官的真实信任。**

大厂校招不是做期末考卷，它是你在人才市场上将自己作为一款“高潜力产品”推向顶尖雇主的 **Go-to-Market 过程**：
1. **看清真实岗位版图（Understand Your Audience）**：大厂现在招的到底是什么人？算法研究、工程加速还是 AI 产品？
2. **构建独家品味壁垒（Understand the Competition）**：当人人都能用 AI 写代码时，你对自然语言场景拆解与 Badcase 调优的“品味”在哪里？
3. **完成真实落地闭环（Connect with Your Target Audience）**：哪怕用开源模型 API 做过一个真正有人用的 Demo，也远胜过 10 个跑不通的学术套壳。

**`ai-campus-navigator`** 将腾讯招聘团队（《鹅厂卧谈会》EP11）的实战理念，沉淀为一套可量化、可实操的自动化 Agent 技能。

---

## 🏛️ 高转化校招求职的三大 GTM 战略基石

参考大厂校招用人标准，我们将校招突围拆解为三大底层支柱：

| 战略基石 | 核心操盘抓手 | 落地价值与产出 |
| :--- | :--- | :--- |
| **1. 诊断生态位<br/>(Understand Audience)** | 划分算法研究、推理加速、AI 产品经理与跨界复合四大象限，拒绝无脑盲投。 | 杜绝“专业不对口还硬投”的无效海投，找到竞争壁垒最厚、通过率最高的生态位。 |
| **2. 淬炼品味与语感<br/>(Prompt & Taste)** | 践行“山水画自然语言还原法则”，建立结构化 Prompt 约束与自建 Golden Set 评测集。 | 彻底摆脱只会“调温吹水”的初级水平，展现严谨的 Badcase 诊断与确定性控制能力。 |
| **3. 交付真实 Demo 闭环<br/>(End-to-End Demo)** | 强化 Why AI 论证、Token 经济与延迟控制，记录真实失败与迭代纪实。 | 用具有真实生命力、能解决实际问题的工作流，降维打击简历全是玩具课设的竞争对手。 |

---

## 🔄 四步重构大厂校招竞争力：GTM 实施路线

<p align="center">
  <img src="assets/architecture_zh.svg" alt="鹅厂校招 AI 人才突围四步法架构" width="100%" style="border-radius: 12px;" />
</p>

按照四步递进路线，本工具将校招求职升级为 4 个清晰交付阶段：

### 📍 Step 1. 定位四维象限 (Role Taxonomy)
- **算法研究轨 (Research / 青云计划)**：考核顶级学术论文原创性与前沿 Scaling Law 思考。
- **工程加速轨 (Engineering / System)**：考核推理框架（vLLM/TensorRT-LLM）显存压榨与 Serving 吞吐优化。
- **AI 产品经理轨 (AI Product Manager)**：考核痛点敏锐度、工作流解构力、Prompt 品味与体验闭环。
- **业务复合轨 (Domain + AI Native)**：经管/人文跨界人才，用 AI 原生工具重构传统业务效率。

### 📍 Step 2. 淬炼品味与语感 (Prompt & Taste)
- **自然语言的极致结构化**：拒绝模糊指令，把任务拆解为输入协议、业务负向约束与结构化输出规范。
- **自建评测基准 (Golden Set)**：自建 50+ 条包含对抗性提示词与幻觉高发样本的真实评测集，用数据证明调优效果。

### 📍 Step 3. 打造落地真实闭环 (End-to-End Demo)
- **非 AI 不可的论证 (Why AI)**：清晰阐述传统规则算法为何无法解决此痛点，证明生成式模型的独特价值。
- **工程成本与延迟权衡**：给出 Token 开销预估、缓存机制（Prompt Caching）与 P95 响应延迟控制方案。
- **Badcase 迭代实录**：展示 3 个曾经彻底翻车的案例及通过什么机制彻底解决，展现真实技术沉淀。

### 📍 Step 4. 红蓝对抗与青云答辩 (Adversarial Defense)
- **毒舌面试官抗压审查**：由资深大厂面试官 Agent 进行逐行挑刺，深挖项目真实贡献度。
- **100 分制竞争力质检**：排查学术造假、代码抄袭与空洞自夸，综合得分低于 85 分自动触发底层重构。

---

## 🥊 实战真实对比：自嗨刷题简历 vs 本工具重塑的高转化方案

以一名投递【腾讯 AI 产品经理/技术研究员】的 2026 届应届生为例：

| 模块维度 | ❌ 普通校招生的自嗨式写法 (直接问通用 AI) | 💎 本工具重构后的真实高转化方案 (腾讯面试官认可) |
| :--- | :--- | :--- |
| **自我定位** | “热爱人工智能，熟悉主流大模型，精通 Prompt 提示词工程，具备良好的沟通能力与抗压能力。”<br>*(❌ 全是虚词套话，面试官 3 秒划走)* | **【AI 原生场景重构者 · 兼具工程评测与品味】**<br>主攻垂类搜索与办公协同智能体，拥有 500+ 高难度边界 Badcase 评测集构建经验，主导搭建可复用工作流，降低幻觉率 34%。 |
| **项目描述<br/>(RAG知识库)** | “开发了一款基于 LangChain 的企业级文档问答系统，调用 GPT-4 接口，实现了高效精准检索，获得导师好评。”<br>*(❌ 标准代码套壳，毫无技术含量与思考深度)* | **“🧼 【多级父子切分 + 混合重排企业知识库】”**<br>解决长表格与代码段召回混乱痛点。对比语义分块与递归字符分块，引入 BGE-Reranker 提升首屏准召率至 92%；自建保底 Fallback 路由，Token 开销削减 42%。 |
| **面试现场防守<br/>(连环深挖)** | 面试官：“如果大模型在用户追问时产生幻觉，你怎么排查？”<br>候选人：“我会让用户重新输入，或者调低 temperature。”<br>*(❌ 暴露没有工业级工程直觉)* | **“精准定位五大幻觉源”**：系统区分 Prompt 权重衰减、Context 窗口超限与检索碎片噪声；引入 Few-shot 负向约束与结构化 JSON Schema 校验，前置阻断 90% 格式漂移。 |
| **青云专项突破** | 盲目投递青云计划，把本科课程大作业当科研成果，一轮游被刷。 | **差异化长板战术**：深挖单点极限（如端侧小模型量化与 200ms 极速响应），提供完整交互 Demo 视频与 Badcase 复盘白皮书，实现逆风突围。 |

> 📖 查看完整对决案例文档：[examples/SHOWCASE_COMPARISON.md](examples/SHOWCASE_COMPARISON.md)

---

## 🧠 大厂面试官的三大核心心法

### 1. 真实与自驱远胜于背诵标准答案
面试官最反感“八股文背得滚瓜烂熟，稍微追问一步底层就露怯”。展示你在课外因纯粹的好奇心折腾过的项目，哪怕失败过，也是最闪光的特质。

### 2. 动过手的 Demo 是最好的敲门砖
在 GitHub 上部署一个可以交互的在线 Demo，附带真实用户的体验反馈，比在纸面上写十行“精通”要有说服力一百倍。

### 3. 把品味落在日常表达与结构化思考中
能否用清晰严谨的语言把复杂的系统讲明白？能否快速抓出不合理的 Badcase？这是 AI 时代大厂最看重的核心认知素质。

---

## 📂 项目结构

```text
ai-campus-navigator/
├── SKILL.md                          # Antigravity Agent 技能主控规范
├── README.md                         # 英文官方文档 (English)
├── README_zh.md                      # 中文官方文档 (简体中文)
├── LICENSE                           # MIT 开源协议
├── CONTRIBUTING.md                   # 贡献指南
├── assets/                           # 商业海报与纯矢量架构图
│   ├── hero_poster_zh.jpg            # 中文版高质感商业海报
│   ├── hero_poster_en.jpg            # 英文版高质感商业海报
│   ├── architecture_zh.svg           # 中文四步法架构流程图
│   └── architecture.svg              # 英文四步法架构流程图
├── prompts/                          # 5 大模块化提示词资产工厂
│   ├── 01_ai_role_radar.md           # 岗位四维雷达与生态位诊断
│   ├── 02_prompt_taste_evaluator.md  # Prompt 品味与语感评测引擎
│   ├── 03_demo_showcase_loop.md      # 真实 Demo 闭环与项目提纯工坊
│   ├── 04_qingyun_talent_matrix.md   # 青云计划与顶级技术人才突围矩阵
│   └── 05_adversarial_interviewer_audit.md # 毒舌面试官红蓝对抗质检沙盘
├── templates/                        # 结构化评估与模版
│   └── ai_portfolio_schema.json      # 结构化输出 JSON Schema
├── evals/                            # 质量评估套件
│   └── rubric_100_ai_campus.json     # 100 分制校招竞争力评估模型
├── docs/                             # 技术架构与底层机制
│   └── ARCHITECTURE.md               # 核心架构文档
└── examples/                         # 实战对比与案例
    └── SHOWCASE_COMPARISON.md        # 普通 AI vs 本工具同台残酷对决
```

---

## 🚀 30秒极速上手

### 在 Google Antigravity / Claude Agent 中直接调用
把本技能放入 `.agents/skills/ai-campus-navigator`，在对话中直接唤醒：

```text
/skill ai-campus-navigator
目标方向: 腾讯 AI 产品经理 (或 青云技术专项)
当前背景: 计算机与经管双学位，有一段 RAG 智能体课设与在线 Demo
核心困惑: 感觉大家都在做类似项目，不知道如何在面试官面前突出差异化
```

---

## 🤝 贡献与开源协议

欢迎提交 PR 与 Issue，共同扩充大厂 AI 岗位评测集与真实面经！  
本项目基于 [MIT License](LICENSE) 开源发布。
