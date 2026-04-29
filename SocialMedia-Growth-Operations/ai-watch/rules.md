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

## 八、飞书表「状态」字段处理规则

飞书表的"状态"列是一个单选字段，控制内容流转。我（AI 编辑）必须严格按以下规则执行：

| 状态值 | 含义 | 出稿时处理 |
|---|---|---|
| **待审**（默认） | 用户尚未审稿 | **略过**，不进 HTML |
| **已审** | 用户确认要发布 | **纳入**，写进公众号 HTML |
| **已排版** | 已经被纳入过 HTML（防重复） | **略过**，不重复处理 |
| **已发布** | 已经发到公众号 | **略过**，不重复处理 |
| **空 / 其它值** | 异常 | **略过**（视同待审） |

### 核心规则一句话

**只有"已审"会被纳入 HTML 排版**。其它状态一律略过。

### 排版后我该做什么

排版完成、HTML 输出给用户之后：

1. 在 Markdown 草稿和 HTML 输出里都标明"本期已纳入 N 条"
2. 主动提示用户："建议把这 N 条在飞书表里状态从「已审」改为「已排版」，避免下次重复"
   （不自动调 webhook 改，因为飞书自动化免费额度有限）

### 用户的状态流转操作

```text
我推送 #NNN 22 条 → 飞书自动化把状态固定填「待审」
↓
用户挑要发的，手动改「已审」
↓
我读飞书表「期数=#NNN AND 状态=已审」的条目 → 出 HTML
↓
用户手动把它们改「已排版」（防止下次重复）
↓
公众号发完后，用户手动改「已发布」（可选，做内容档案用）
```

## 九、合规与本地化规则（强制）

> 公众号面向中国读者，**合规是第一优先级**。内容选题不强制中国/海外比例，谁好选谁，但每条必须过合规与本地化两道闸。

### A. 选题红线（出现即剔除）

| 类别 | 关键词举例 | 处理 |
|---|---|---|
| 涉政 | 中美关系对抗性叙事、地缘政治冲突、领导人言论评价 | 整条剔除 |
| 涉党 / 涉国家制度 | 对任一国政党、政体的评价或对比 | 整条剔除 |
| 涉台 / 港 / 藏 / 疆 | 主权、历史、民族、宗教类讨论 | 整条剔除 |
| 涉宗教族裔 | 伊斯兰、犹太、新疆棉花等敏感族群叙事 | 整条剔除 |
| 涉色情暴力 | 战争场景、犯罪细节、性内容 | 整条剔除 |
| 涉绕审 / 翻墙 | VPN / proxy / 科学上网 / 绕过审查工具 | 整条剔除 |
| 涉版权破解 | 盗版、破解工具、数据爬取灰产 | 整条剔除 |
| 涉股票 / 币圈炒作 | 投资荐股、币圈热度、ICO、Meme 币 | 整条剔除 |
| 涉个人攻击 / 诉讼八卦 | Musk vs Altman 法庭戏码、CEO 私生活 | 整条剔除（仅技术内容除外） |

> 海外创始人观点中如夹杂涉政表述，**保留商业判断部分，删掉政治判断部分**。
> 不确定是否敏感时，**默认剔除**——宁少勿险。

### B. 翻译与本地化处理（每条必做）

| 场景 | 处理 |
|---|---|
| 美元金额 | 括号备注 ≈ 人民币（按 ¥7/USD 折算）。例：$180 → "180 美元（约 ¥1,260）" |
| 海外公司案例 | 必要时补一句"对标国内 XX" |
| 海外术语首次出现 | 给一句中文解释（GEO / AEO / PMF / GTM / ARR / NDR / CAC / LTV / Moat 等） |
| 时间 / 节日 | 按中国语境（"holiday season" → 年终购物季） |
| 人名 / 公司名 | 保留英文原文，必要时备注中文（如 OpenAI、Anthropic） |

### C. 选题原则（不强制中国比例）

- 内容选题"全球视角，谁好选谁"——不预设中国/海外配额
- 国内有好内容自然纳入，没有也不强行凑数
- 04 创始人观点栏，海外/国内创业者公开发言均可

### D. 信息源（中英混合）

英文源详见前文第四节。**中文源在 `feeds.opml` 里已加入下列站点**（fetch.py 自动抓取）：

| 类型 | 站点 |
|---|---|
| AI 行业 | 机器之心、量子位、PingWest 品玩、爱范儿 |
| 创投 / 出海 | 36氪、虎嗅、钛媒体、Founder Park |
| 设计 / 产品 | UI 中国、UISDC（优设网） |

补抓途径（fetch.py 抓不到时主动用）：
- WebSearch + `site:36kr.com / site:huxiu.com / site:tmtpost.com`
- 公众号搜索关键词：拾象、海外独角兽、晚点 LatePost、远川研究所、Founder Park

### E. 公众号发布合规（每篇必查）

- ✅ 链接去掉 `utm_*` 参数（被微信识别为推广会限流）
- ✅ 涉企业经营数据要标注 "据公开报道" 或 "据 XX 媒体报道"
- ✅ 数字精确度避开"投资建议"嫌疑（用 ≈ 而不是绝对数）
- ✅ 配图必须无版权或自有版权（公众号抄查严）
- ✅ 单篇外链建议 ≤ 25 个（超过会被判定为聚合站点限流）
- ✅ 标题不带过多 "!" "？" 等情绪符号
- ✅ 不出现 VPN、翻墙、科学上网、proxy、绕墙 等词
- ✅ 不评价任何国家领导人 / 政治人物的言论与立场
