# design-spec-extractor-2B

> B 端设计规范提取器 · v4.1

从设计稿截图或 Figma 链接中，自动提取完整的 B 端设计规范，输出通用 `tokens.css` 及各框架转换文件，可直接注入 Claude / Cursor / v0 等 AI 开发工具。

---

## 能做什么

接收设计稿后，完成三件事：

1. **检查完整性** — 对照内置页面清单判断设计稿覆盖范围，缺失关键页面时按 Token 缺失影响分级追问
2. **系统性提取** — 按 8 个维度（颜色、文字、圆角、边框、间距、阴影、布局、适配）扫描设计稿，生成原始记录 `raw.json` 后归一输出 `tokens.css`
3. **框架转换** — 提取完成后按需转换为 shadcn/ui、Tailwind、Ant Design、Element Plus、Naive UI 各框架格式

---

## 适用场景

专为 **B 端产品**设计，包括后台管理系统、数据平台 / BI 工具、企业级 SaaS、内部运营工具、工业控制台。

遇到 SaaS 营销官网等灰色地带会主动询问确认，不自动触发。

---

## 文件结构

```
design-spec-extractor-2B/
├── SKILL.md                              主技能文件（流程控制，271 行）
├── README.md                             本文档
└── references/
    ├── extraction-dimensions.md          8 个维度的完整提取字段清单
    ├── raw-json-schema.md                raw.json schema + 不一致上报话术
    └── framework-conversion.md          5 种框架的转换规则与代码模板
```

参考文件按需加载，不会每次全部读取：

| 文件 | 读取时机 |
|------|---------|
| `extraction-dimensions.md` | 开始提取时 |
| `raw-json-schema.md` | 生成 raw.json 时 / 检测到规范不一致时 |
| `framework-conversion.md` | 用户确认目标框架后 |

---

## 安装方式

> **前提**：先将本文件夹（`design-spec-extractor-2B/`）下载到本地，再按以下步骤安装。
>
> **重要**：文件夹名必须保持为 `design-spec-extractor-2B`，不要重命名。Claude Code 等工具通过文件夹名识别 Skill，改名后触发关键词匹配可能失效。

将整个文件夹复制到对应工具的 skills 目录：

```
# Claude Code · 项目级（仅当前项目生效）
your-project/.claude/skills/design-spec-extractor-2B/

# Claude Code · 全局（所有项目生效，推荐）
~/.claude/skills/design-spec-extractor-2B/

# Cursor
your-project/.cursor/skills/design-spec-extractor-2B/

# Windsurf
your-project/.windsurf/skills/design-spec-extractor-2B/
```

---

## 触发关键词

上传设计稿并说以下任意内容即可触发：

`设计规范` `设计系统` `提取规范` `总结规范` `色彩规范` `字体规范` `组件规范` `design token` `design spec` `figma`

---

## 输入源

按精度从高到低：

| 输入源 | 精度 | 说明 |
|--------|------|------|
| Figma MCP 直连 | 最高 | AI 直接读取图层数据，颜色/间距均为精确值 |
| Figma 分享链接 | 高 | 通过 Figma API 读取 |
| 设计稿截图 | 中 | 视觉识别，存在估算误差 |
| 文字描述 | 低 | 仅作补充，不单独使用 |

**Figma MCP 连接**：服务器地址 `https://mcp.figma.com/mcp`，各工具配置方式不同，以官方文档为准，连接后完成 OAuth 授权即可。

---

## 使用流程

### 第一步：上传设计稿

Skill 接收后立即执行页面覆盖率检查，对照 5 个阻塞级页面和 4 个增强级页面。

**阻塞级页面**（缺一必须补充或选择处理方式）：

| 页面 | 缺失时无法输出的核心 Token |
|------|--------------------------|
| 登录页 | `--color-primary` 全系列、`--font-family-base`、`--color-bg-page` |
| 主导航 / 侧边栏 | `--color-bg-sidebar`、`--color-bg-topbar`、`--layout-sidebar-width`、`--layout-topbar-height` |
| 数据列表页 | `--color-bg-hover`、`--color-bg-selected`、`--layout-table-row-height` |
| 表单页 | `--color-border-focus/disabled/error`、`--color-bg-disabled`、`--color-text-placeholder` |
| 详情页 | `--color-border-readonly`、字号层级验证 |

### 第二步：选择处理方式（设计稿不完整时）

| 选项 | 说明 |
|------|------|
| A. 补充设计稿 | 等补充后继续，结果最准确 |
| B. 跳过缺失 | 只提取现有内容，缺失 Token 标注「待补充」 |
| C. 推断性提取 | 基于现有设计语言合理推断，结果带「[推断]」标注和置信度 |

### 第三步：自动提取并生成 raw.json

提取过程中自动生成 `.design-spec-extractor/raw.json`（过程文件，隐藏目录），记录所有原始发现值，含冲突检测结果。

若检测到规范不一致（如同一语义颜色出现两个色值），会暂停并上报，等待确认后继续。

### 第四步：输出 tokens.css

路径：`design-system/tokens.css`

Token 按三级必要性标注输出：
- `[必要]` — 所有 B 端页面必须有，缺失则阻塞
- `[推荐]` — 大多数场景需要，无法提取时注释标注「待补充」
- `[可选]` — 特定页面才需要，无对应页面时整行注释掉

### 第五步：选择框架转换（可选）

```
A. shadcn/ui     → globals.css（HSL 裸值）+ tailwind.config.js
B. Tailwind CSS  → tailwind.config.js
C. Ant Design    → design-system/theme.ts
D. Element Plus  → design-system/el-variables.css
E. Naive UI      → design-system/themeOverrides.ts
F. 暂不需要      → 保持通用格式
```

---

## 输出文件一览

| 文件 | 目录 | 性质 |
|------|------|------|
| `raw.json` | `.design-spec-extractor/` | 过程文件，自动生成，供回溯用 |
| `tokens.css` | `design-system/` | 核心产物，每次必须输出 |
| `globals.css` | `design-system/` | shadcn/ui 专属 |
| `tailwind.config.js` | 项目根目录 | Tailwind / shadcn 专属 |
| `theme.ts` | `design-system/` | Ant Design 专属 |
| `el-variables.css` | `design-system/` | Element Plus 专属 |
| `themeOverrides.ts` | `design-system/` | Naive UI 专属 |

---

## tokens.css 覆盖范围

通用 `tokens.css` 包含以下 Token 组：

| 组 | 主要变量 |
|----|---------|
| 品牌色 | primary（全状态含 disabled）、secondary |
| 功能色 | success / warning / error / info（各含 hover + light） |
| 背景色 | page、card、sidebar、topbar、hover、selected、disabled、modal、tag |
| 边框色 | default、hover、focus、disabled、error、readonly |
| 文字色 | primary、secondary、disabled、placeholder、inverse、link |
| 图表色 | chart-1~N、positive、negative（Dashboard 页面才提取） |
| 文字排版 | font-family、font-size（xs~2xl）、font-weight、line-height |
| 间距 | spacing-unit、xs~2xl |
| 圆角 | radius-xs~xl、full |
| 阴影 | shadow-none~lg、inset |
| 动效 | duration-fast/base/slow、easing-standard/enter/exit |
| 层级 | z-dropdown、z-sticky、z-tooltip、z-modal、z-notification、z-loading |
| 布局 | sidebar-width/collapsed、topbar-height、content-padding、table-row-height |

---

## shadcn/ui 特别说明

shadcn 变量使用 **HSL 裸值格式**，不含 `hsl()` 包裹：

```css
/* ✅ shadcn 正确格式 */
--primary: 221.2 83.2% 53.3%;

/* ❌ 普通 CSS 格式（shadcn 不识别） */
--primary: #1677FF;
```

选择 shadcn 框架时，Skill 会自动将 HEX 转换为 HSL 裸值，并同步输出 `tailwind.config.js` 的颜色映射。

---

## 约束说明

以下约束硬编码在 Skill 中，不会因任何 prompt 绕过：

- 未在设计稿中出现的颜色，不用任何框架默认色填充
- 所有输出必须有具体数值，不允许模糊描述
- 圆角超过 12px 会标注「待确认」（B 端约束）
- tokens.css 中不得出现任何 `[#HEX]` 或 `[N]px` 占位符
- 功能色 4 个（Success / Warning / Error / Info）必须全部覆盖
- 规范不一致必须上报用户确认，不得自行选择

---

## 版本记录

| 版本 | 日期 | 主要更新 |
|------|------|---------|
| v4.1 | 2026-04-16 | 拆分参考文件（主文件从 1003 行压缩至 271 行）；Token 三级必要性标注；补全 bg-hover/selected/disabled/sidebar/topbar、primary-disabled、z-index、motion 等缺失 Token；raw.json 独立 schema；规范不一致检测机制 |
| v4.0 | 2026-04-10 | 合并两版本；追问协议三选项（含推断性提取）；shadcn/ui 支持；B 端场景判断标准 |
| v3.1 | 2026-03-01 | System Prompt Injection 输出格式；框架锁定；状态感知色彩 |
| v1.0 | 2026-01-01 | 初版，基础 8 维度提取 |
