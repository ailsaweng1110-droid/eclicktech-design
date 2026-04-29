# 易点事务所 AI 观察 · 信息检索规则 v1.0

> 这份文档是给 AI 编辑（Claude / Cursor）看的检索与编辑规范。
> 每次出新一期"易点事务所 AI 观察 👀"时，AI 必须严格按此规则执行。

---

## 一、整体规则

| 维度 | 约束 |
|---|---|
| 时间窗口 | 发布日期 ≤ 7 天的内容才合格，否则剔除 |
| 去重规则 | 同来源 URL / 同主题 / 同主发布方与既有期重复，剔除 |
| 数量约束 | 每栏目 **最少 3 条、最多 6 条**，按重要性降序 |
| 翻译规则 | 英文摘要默认翻译为中文；保留人名 / 产品名 / 公司名英文原文 |
| 标注规则 | 每条文末加 `【来源：媒体/平台/发布方名称】` |
| 排版规则 | "标题 · 日期" 独占一行，描述另起一行；80–150 字 |

## 二、4 大栏目定义

| 编号 | 栏目 | 涵盖范围 |
|---|---|---|
| 01 | AI 模型 / 产品动态 | 基础模型发布、AI 产品更新、AI Infra 动作 |
| 02 | AI + 设计 | AI 设计工具、生成式设计、设计系统 AI、Vibe Design |
| 03 | AI + 海外营销 | B2B/SaaS 增长、海外付费投放、品牌出海、**SEO / GEO / AEO** |
| 04 | 创始人观点 | CEO/创始人长访谈、深度观点文、行业评论 |

> 03 栏目对外文案中**不显示** "(含 SEO / GEO)"，但搜索范围必须覆盖。
> 04 栏目标题简洁化：公司及职位信息放进描述，不放标题。

## 三、栏目 → 关键词

### 01 AI 模型 / 产品动态

```
AI model release, GPT, Claude, Gemini, Llama, AI agent, LLM update,
AI infrastructure, foundation model, frontier model, agentic AI, MCP,
AI chip, AI hardware, multimodal, reasoning model
```

### 02 AI + 设计

```
AI design tool, generative design, design copilot, design agent,
Figma AI, Adobe Firefly, Canva AI, Claude Design, design system AI,
vibe design, design tokens AI, prototype AI, UX AI, UI generation
```

### 03 AI + 海外营销

```
AI marketing, B2B marketing, SaaS growth, international monetization,
paid media trends, performance marketing AI, brand AI, content AI,
GEO, generative engine optimization, AEO, AI search, ChatGPT search,
AI Overviews, Perplexity SEO, LLM citation, localization, going global,
PMF, growth loops, retention AI
```

### 04 创始人观点

```
founder essay, CEO interview, AI startup, scaling AI,
AI product strategy, agentic future, AI moat, distribution moat,
AI regulation opinion, Lenny interview, Stratechery
```

## 四、栏目 → 高权重源（按优先级）

### 01 AI 模型 / 产品动态

1. OpenAI Blog — https://openai.com/blog
2. Anthropic News — https://www.anthropic.com/news
3. Google DeepMind / AI Blog — https://deepmind.google/blog
4. AWS News — https://aws.amazon.com/blogs/aws
5. Microsoft AI Blog — https://blogs.microsoft.com/ai
6. The Verge AI — https://www.theverge.com/ai-artificial-intelligence
7. TechCrunch AI — https://techcrunch.com/category/artificial-intelligence
8. Bloomberg Technology — https://www.bloomberg.com/technology
9. Hugging Face Blog — https://huggingface.co/blog
10. BusinessWire / PR Newswire（厂商发稿源）

### 02 AI + 设计

1. Figma Blog — https://www.figma.com/blog
2. Adobe Blog — https://blog.adobe.com
3. Anthropic News（Claude Design 等）
4. Lenny's Newsletter — https://www.lennysnewsletter.com
5. UX Collective — https://uxdesign.cc
6. Smashing Magazine — https://www.smashingmagazine.com
7. Frame.io Insider — https://blog.frame.io
8. Designer News — https://www.designernews.co （站点不稳定，备用）
9. IxDA Local Events — https://ixda.org/events （仅活动类，法人已解散）

### 03 AI + 海外营销

1. SaaStr — https://www.saastr.com
2. Marketing Brew — https://www.marketingbrew.com
3. Lenny's Newsletter
4. HubSpot Marketing Blog — https://blog.hubspot.com/marketing
5. Search Engine Land — https://searchengineland.com
6. Search Engine Journal — https://www.searchenginejournal.com
7. Ahrefs Blog — https://ahrefs.com/blog
8. Backlinko — https://backlinko.com/blog
9. Aleyda Solis — https://www.aleydasolis.com
10. EMARKETER — https://www.emarketer.com
11. Stratechery — https://stratechery.com

### 04 创始人观点

1. Lenny's Newsletter（创始人深访为主）
2. Stratechery
3. Substack（个人博客生态：Justin Bartak、Ariel Sakin、Packy McCormick…）
4. LinkedIn Pulse（爆款长文）
5. a16z / Future / Not Boring — https://a16z.com / https://www.notboring.co
6. First Round Review — https://review.firstround.com
7. Reforge — https://www.reforge.com/blog

## 五、抓取与排序顺序

1. 优先抓官方 / 一手发布源（厂商 News、博客）
2. 再抓垂直媒体的"数据 / 长文 / 测评"
3. 再抓个人 / 创始人 / 时事评论
4. 同类话题多源命中时，保留官方一手 + 1 篇最佳二手解读
5. 每栏内按重要性降序排：旗舰发布 > 主流厂商动作 > 数据报告 > 评论观点

## 六、单条信息标准模板

```markdown
**标题（中文译名）· 日期（M/D）**
描述（80–150 字，中文，含背景 + 核心信息 + 价值判断）
[原文链接](URL) 【来源：发布方】
```

> 创始人观点条目额外要求：标题不带公司/职位，描述首句必须交代"X 是 [公司][职位]"。

## 七、每周一标准操作流程（SOP）

### 用户的输入

每周一上午用户会跟我说一句类似的话："出 #002"、"出本周这期"、"开始这周的 AI 观察"。

### 我的执行步骤

1. **读候选库**：打开 `ai-watch/output/{当前 ISO 周编号}.md`（例：`2026-W19.md`）
2. **判定期数**：在飞书表里查最大的 `#NNN` 期数 +1，或按用户指定（默认从 `#002` 开始递增）
3. **逐栏精修**：按本规则第三/四节的关键词与来源优先级，从候选库里每栏选 3–6 条
4. **翻译 + 描述**：按第六节模板写中文标题（保留人名/产品英文）+ 80–150 字描述
5. **创始人栏特殊**：标题不带公司/职位，描述首句必须 "X 是 [公司][职位]"
6. **打分**：按来源给 importance 评分（旗舰一手=5，主流厂商/垂直媒体=4，个人/二手=3）
7. **复用推送脚本**：参考 `_push_curated.py` 的结构（已 gitignore，本地保留），改 `ISSUE` 与 `CURATED` 后跑：
   ```bash
   cd ai-watch && .venv/bin/python _push_curated.py
   ```
8. **告诉用户**："已推 N 条到飞书 #NNN，去飞书审"
9. **等待用户审完**，用户会说"可以排版了 / #NNN 出 HTML"
10. **调 media-formatter skill** 输出公众号 HTML

### 用户的两次动作（一周内）

- 周一上午：跟 Claude 说"出 #NNN"
- 审完后：跟 Claude 说"可以排版了"

### 期数命名规则

| 来源 | 期数前缀 | 例 |
|---|---|---|
| 自动抓的原始 RSS（已废弃，不再推飞书） | `#YYYY-WXX` | `#2026-W18` |
| AI 精修后的成品（飞书表唯一保留的格式） | `#NNN` 三位数顺序 | `#001`、`#002`、`#012` |
