---
# ── 基础信息 ──────────────────────────────────────────
name: design-spec-extractor-2B
display_name: B 端设计规范提取器
version: "4.1"
description: 从设计稿中提取 B 端设计规范的专项技能。当用户上传设计稿截图、分享 Figma 链接、或提到"设计规范"、"设计系统"、"提取规范"、"总结规范"、"色彩规范"、"字体规范"、"组件规范"等关键词时，必须立即触发此技能。专为 B 端（后台管理系统、数据平台、SaaS 产品、企业工具）场景设计，能自动检测设计稿是否完整，在缺少关键页面时主动向用户索要，最终输出结构化的完整设计规范文档，涵盖颜色、文字、圆角、边框、间距、阴影、排版布局、适配规则等所有维度，并生成可直接注入 AI 开发工具（Claude/Cursor/v0）的 Design Token 代码块。

# ── 作者与归属 ────────────────────────────────────────
author: 产品设计组
maintainer: 产品设计组
license: MIT
repository: ""

# ── 分类与标签 ────────────────────────────────────────
category: design
tags:
  - design-system
  - b2b
  - design-token
  - figma
  - css-variables
  - ui-spec

# ── 兼容性 ────────────────────────────────────────────
compatible_tools:
  - claude-code
  - cursor
  - windsurf
  - gemini-cli
  - codex-cli
  - vs-code-copilot

compatible_frameworks:
  - react-shadcn
  - react-tailwind
  - react-antd
  - vue-element-plus
  - vue-naive-ui
  - css-variables

# ── 触发关键词 ────────────────────────────────────────
triggers:
  - 设计规范
  - 设计系统
  - 提取规范
  - 总结规范
  - 色彩规范
  - 字体规范
  - 组件规范
  - design token
  - design spec
  - figma

# ── 输入 / 输出声明 ───────────────────────────────────
input: "figma-mcp（Figma MCP 直连，精度最高）| image（设计稿截图 PNG/JPG）| url（Figma 分享链接）| text（页面描述或补充说明）"
output: "markdown（结构化设计规范文档）| css（tokens.css）| json（.design-spec-extractor/raw.json）"

# ── 参考文件 ──────────────────────────────────────────
references:
  - path: references/extraction-dimensions.md
    when: 执行提取时，逐维度扫描设计稿
  - path: references/raw-json-schema.md
    when: 生成 raw.json 时，以及检测到规范不一致需要上报时
  - path: references/framework-conversion.md
    when: 用户确认目标框架后，生成框架专属转换产物时

# ── 版本历史 ──────────────────────────────────────────
changelog: "v4.1 2026-04-16 拆分参考文件；Token 必要性三级标注；补全 bg-hover/selected/disabled/sidebar/topbar、primary-disabled、z-index、motion Token；raw.json 独立 schema；不一致检测机制 | v4.0 2026-04-10 合并两版本；追问协议三选项；shadcn/ui 支持；B 端场景判断标准 | v1.0 2026-01-01 初版"
---

# B 端设计规范提取协议 (v4.1)

---

## 参考文件说明

本 Skill 配套三个参考文件，按需读取，不需要一次全部加载：

| 文件 | 读取时机 |
|------|---------|
| `references/extraction-dimensions.md` | 开始提取时，按 8 个维度逐一扫描 |
| `references/raw-json-schema.md` | 生成 raw.json 时 / 检测到不一致时 |
| `references/framework-conversion.md` | 用户确认框架后，生成转换产物时 |

---

## 零、输入源优先级

| 优先级 | 输入源 | 精度 |
|--------|--------|------|
| ⭐ 最高 | Figma MCP 直连 | 精确到 1px / 1 色值 |
| 高 | Figma 分享链接 | 较高 |
| 中 | 设计稿截图 | 中等，存在估算误差 |
| 低 | 文字描述 | 仅作补充，不单独作为提取依据 |

**Figma MCP 服务器地址**：`https://mcp.figma.com/mcp`

各工具连接方式不同（Claude Code / Cursor / Windsurf / VS Code），以各工具官方文档为准。连接后完成 OAuth 授权，粘贴 Figma 链接即可让 AI 读取图层数据。

> ⚠️ 通过 Figma MCP 读取时，若源文件存在规范不一致，读取 `references/raw-json-schema.md` 执行不一致检测与上报流程。

---

## 一、B 端场景判断标准

本技能专用于以下场景，遇到灰色地带（如 SaaS 营销官网）时默认**不触发**，需询问用户确认：

- 后台管理系统（Admin Panel）
- 数据平台 / BI 工具
- 企业级 SaaS 产品
- 内部运营工具
- 工业控制台 / 监控平台

---

## 二、核心页面覆盖率检查

接收设计稿后**立即**执行覆盖率检查，缺失阻塞级页面时触发追问协议（见第三节）。

### 页面类型 → Token 覆盖度映射

| 页面 | 能解锁的主要 Token 组 |
|------|---------------------|
| 登录页 | 品牌主色全状态、主按钮圆角、基础字体、页面背景 |
| 主导航 / 侧边栏 | `--color-bg-sidebar`、`--color-bg-topbar`、Layout 宽高 |
| 数据列表页（Table） | `--color-bg-hover`、`--color-bg-selected`、表格行高、分割线 |
| 表单页 | 边框全状态（focus/disabled/error）、`--color-bg-disabled`、placeholder |
| 详情页 | `--color-border-readonly`、字号层级完整性验证 |
| Dashboard | `--color-chart-*`、数据大字、`--font-family-data` |
| 弹窗 / Modal | `--color-overlay`、`--shadow-lg`、`--radius-xl`、`--z-modal` |
| 空状态 / 错误页 | 功能色语义验证 |

### 阻塞级页面（缺一必须追问）

| 页面 | 缺失时无法输出的 `[必要]` Token |
|------|-------------------------------|
| 登录页 | `--color-primary` 全系列、`--font-family-base`、`--color-bg-page` |
| 主导航 / 侧边栏 | `--layout-sidebar-width`、`--layout-topbar-height`、`--color-bg-sidebar`、`--color-bg-topbar` |
| 数据列表页（Table） | `--color-bg-hover`、`--color-bg-selected`、`--layout-table-row-height`、`--color-divider` |
| 表单页 | `--color-border-focus/disabled/error`、`--color-bg-disabled`、`--color-text-placeholder` |
| 详情页 | `--color-border-readonly`、字号体系完整性验证 |

### 增强级页面（缺失告知影响，不阻塞）

| 页面 | 缺失时无法输出的 `[推荐]`/`[可选]` Token |
|------|----------------------------------------|
| Dashboard / 概览页 | `--color-chart-1~N`、`--font-size-xl/2xl` |
| 弹窗 / Modal | `--color-overlay`、`--shadow-lg`、`--radius-xl`、`--z-modal` |
| 空状态 / 错误页 | 功能色语义无法验证 |
| 移动端适配页 | 断点变量 |

---

## 三、追问协议

检测到缺失阻塞级页面时，**暂停提取**，使用以下话术：

```
我已收到您的设计稿，在开始提取规范前，发现还需要以下页面：

【必须补充（阻塞提取）】
❌ [页面名称] — 缺少后，[具体 Token 变量名] 无法准确提取

【建议补充（影响准确性）】
⚠️ [页面名称] — 影响：[具体 Token 变量名] 将标注「待补充」

请选择处理方式：
A. 📎 补充设计稿后继续（推荐，结果最准确）
B. ⏭️ 仅提取现有页面可确认内容，缺失 Token 标注「待补充」
C. 🔍 推断性提取——基于现有页面设计语言合理推断，
   结果带「[推断]」标注和置信度（高/中/低），供您核对后使用
```

> 选择 C 时，推断必须有依据，无法推断的维度仍标注「待补充」，禁止填入默认值。

---

## 四、框架策略

**核心原则**：先提取通用 Token，再按需转换。不在提取阶段锁定框架。

**提取阶段**：始终输出通用格式的 `tokens.css`（标准 CSS Variables + HEX 色值）。

**转换阶段**：提取完成后询问：

```
通用 tokens.css 已生成。如需转换为特定框架格式，请告知：

A. shadcn/ui     → HSL 裸值 + shadcn 变量名 + globals.css
B. Tailwind CSS  → tailwind.config.js extend 配置
C. Ant Design    → theme.token 覆盖对象（theme.ts）
D. Element Plus  → el-* CSS 变量覆盖
E. Naive UI      → themeOverrides 对象
F. 暂不需要      → 保持通用格式
```

> 用户选 F 或不回复时直接输出通用格式。转换规则详见 `references/framework-conversion.md`。

---

## 五、提取执行

**读取 `references/extraction-dimensions.md`，按 8 个维度逐一扫描设计稿。**

Token 必要性三级：
- `[必要]` 缺失则阻塞 tokens.css 输出
- `[推荐]` 缺失则在 tokens.css 末尾注释标注「待补充」
- `[可选]` 有对应页面才提取，无则整行注释掉，不留占位符

---

## 六、输出流程

### 阶段一：raw.json（自动生成，每次必须）

路径：`.design-spec-extractor/raw.json`

记录所有原始发现值（含冗余和冲突），不做任何筛选。
格式和写入规则详见 `references/raw-json-schema.md`。

### 阶段二：tokens.css（必须输出）

路径：`design-system/tokens.css`

- 所有占位符替换为真实值，禁止保留 `[#HEX]` 或 `[N]px`
- `[可选]` Token 无对应页面时整行注释掉
- `[推荐]` Token 无法提取时用注释标注「待补充 — 原因：xxx」
- 文件头部注明提取来源、时间、Token 等级说明

### 阶段三：框架转换文件（按需输出）

用户确认框架后，读取 `references/framework-conversion.md` 生成对应文件。

### 文件输出清单

| 文件 | 目录 | 性质 | 何时生成 |
|------|------|------|---------|
| `raw.json` | `.design-spec-extractor/` | 过程文件 | 每次提取**自动生成** |
| `tokens.css` | `design-system/` | 必须产物 | 每次提取**必须输出** |
| `globals.css` | `design-system/` | 框架产物 | 用户选 shadcn 时 |
| `tailwind.config.js` | 项目根目录 | 框架产物 | 用户选 Tailwind / shadcn 时 |
| `theme.ts` | `design-system/` | 框架产物 | 用户选 Ant Design 时 |
| `el-variables.css` | `design-system/` | 框架产物 | 用户选 Element Plus 时 |
| `themeOverrides.ts` | `design-system/` | 框架产物 | 用户选 Naive UI 时 |

---

## 七、约束禁令

- **禁止私自扩充**：未在设计稿中发现的颜色，禁止用任何框架默认色填充
- **禁止降密**：B 端场景禁止超大间距或圆角 > 12px（无设计稿依据）
- **禁止模糊表述**：所有输出必须有具体数值或 HEX 色值
- **禁止遗漏状态**：色彩系统必须覆盖 Default / Hover / Focus / Disabled / Error / Read-only
- **禁止跨场景套用**：C 端规范不得迁移至 B 端，反之亦然
- **禁止保留占位符**：tokens.css 中不得出现任何 `[#HEX]` 或 `[N]px`

---

## 八、质量自检清单

- [ ] `raw.json` 已生成，含所有维度原始发现值，无遗漏
- [ ] `raw.json` 中的 `conflicts_detected` 已全部上报用户确认
- [ ] 所有 `[必要]` Token 均有真实 HEX / px 值，无占位符残留
- [ ] 功能色 4 个（Success / Warning / Error / Info）及 Hover / Light 变体全部覆盖
- [ ] 文字色 4 级（主要 / 次要 / 禁用 / 占位符）全部提取
- [ ] 交互状态（Hover / Focus / Disabled / Error / Read-only）均有对应色值
- [ ] `[可选]` Token 无对应页面时已整行注释，不留占位符
- [ ] `[推荐]` Token 无法提取时已注释标注「待补充」，不留占位符
- [ ] `tokens.css` 与 `raw.json` 数值一致，无归一阶段引入的错误
- [ ] 用户选择框架转换时，转换产物与 `tokens.css` 数值一致
- [ ] shadcn 转换时，所有颜色已从 HEX 正确换算为 HSL 裸值格式
