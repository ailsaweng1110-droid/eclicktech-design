---
# ── 基础信息 ──────────────────────────────────────────
name: design-spec-extractor
display_name: B 端设计规范提取器
version: "4.0"
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

# ── 触发关键词（辅助触发判断）────────────────────────
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
input: "image（设计稿截图 PNG/JPG）| url（Figma 分享链接）| text（页面描述或补充说明）"
output: "markdown（结构化设计规范文档，8 个维度）| css（Design Token 注入代码块，:root CSS Variables）"

# ── 版本历史 ──────────────────────────────────────────
changelog: "v4.0 2026-04-10 合并两版本；补全圆角/边框/阴影/适配 4 个维度；追问协议升级为三选项含推断性提取；新增 shadcn/ui 支持；新增 B 端场景判断标准 | v3.1 2026-03-01 加入 System Prompt Injection 输出格式；加入框架锁定；加入状态感知色彩 | v1.0 2026-01-01 初版发布，基础 8 维度提取流程"
---

# B 端设计规范提取协议 (v4.0)

---

## 一、B 端场景判断标准

本技能专用于以下场景，遇到灰色地带（如 SaaS 营销官网）时默认**不触发**，需询问用户确认：

- 后台管理系统（Admin Panel）
- 数据平台 / BI 工具
- 企业级 SaaS 产品
- 内部运营工具
- 工业控制台 / 监控平台

**B 端设计的核心特征**：信息密度高、交互状态丰富、功能优先于美观、以桌面端为主。

---

## 二、核心页面覆盖率检查

接收设计稿后，**立即**对照以下清单执行覆盖率检查，缺失阻塞级页面时触发追问协议（见第三节），不得跳过直接提取。

### 阻塞级页面（缺一必须追问）

| 页面 | 提取目标 |
|------|---------|
| 登录页 | 品牌主色、主按钮基础样式、字体首次出现 |
| 主导航 / 侧边栏 | 导航色板、激活状态、层级间距、收起宽度 |
| 数据列表页（Table） | 表格行高、斑马纹、操作列、分页、空状态 |
| 表单页（新建 / 编辑） | 输入框状态、标签对齐、必填标记、校验反馈 |
| 详情页 | 信息展示密度、字体层级、只读状态样式 |

### 增强级页面（缺失时告知影响，不阻塞）

| 页面 | 提取目标 | 缺失影响 |
|------|---------|---------|
| Dashboard / 概览页 | 图表色、数据大字、卡片阴影 | 图表色板和数据字体无法提取 |
| 弹窗 / Modal | 蒙层色、弹窗圆角、操作按钮排列 | 弹窗规范标注为待补充 |
| 空状态 / 错误页 | 功能色真实使用场景 | 功能色语义准确性降低 |
| 移动端适配页 | 断点与响应式规则 | 适配规则无法提取 |

---

## 三、追问协议

检测到缺失阻塞级页面时，**暂停提取**，使用以下话术：

```
我已收到您的设计稿，在开始提取规范前，发现还需要以下页面：

【必须补充（阻塞提取）】
❌ [页面名称] — 缺少后，[具体维度] 无法准确提取

【建议补充（影响准确性）】
⚠️ [页面名称] — 影响：[具体说明]

请选择您希望的处理方式：

A. 📎 补充设计稿后继续（推荐，结果最准确）
B. ⏭️ 跳过缺失页面，仅提取现有页面中可确认的规范，缺失维度标注「待补充」
C. 🔍 推断性提取——基于现有页面的设计语言，对缺失维度进行合理推断，
   所有推断结果将以「[推断]」前缀标注，并注明推断依据，供您核对后使用
```

> ⚠️ 执行说明：用户选择 C 时，推断须遵循以下规则：
> - 推断必须有依据（如"根据登录页主按钮圆角 6px，推断输入框圆角同为 6px"）
> - 禁止无依据臆造，无法推断的维度仍标注「待补充」，不得填入默认值
> - 推断结果置信度分三级：高（同类组件直接参考）/ 中（跨组件类比）/ 低（跨页面泛化）
> - 最终输出须在文档顶部注明"本规范含推断内容，建议补充设计稿后校验"

---

## 四、框架锁定

开始提取前，询问用户的目标开发框架，以确定输出变量格式：

```
请确认您的目标开发框架，以便我生成对应格式的 Design Token：

1. React + shadcn/ui
2. React + Tailwind CSS
3. React + Ant Design
4. Vue + Element Plus
5. Vue + Naive UI
6. 原生 CSS / CSS Variables
7. 其他（请说明）
```

---

## 五、规范解构维度

### 5.1 状态感知的色彩系统

**品牌色**

| 状态 | 色值 | 使用场景 |
|------|------|---------|
| Primary | # | 主按钮、激活状态、链接 |
| Primary Hover | # | 主按钮悬停 |
| Primary Active | # | 主按钮点击 |
| Primary Focus Ring | # | 键盘焦点环 |
| Secondary | # | 次级按钮、标签 |

**功能色（必须逐一识别，禁止遗漏）**

| 类型 | 默认 | Hover | Light（背景用） | 使用场景 |
|------|------|-------|----------------|---------|
| Success | # | # | # | 成功提示、通过状态 |
| Warning | # | # | # | 警告提示、待处理 |
| Error / Danger | # | # | # | 错误提示、删除操作 |
| Info | # | # | # | 普通提示、说明 |

**中性色板（四级文字色必须全部提取）**

| 层级 | 色值 | 使用场景 |
|------|------|---------|
| 页面背景 | # | 整体页面底色 |
| 卡片背景 | # | 卡片、面板 |
| 弹窗背景 | # | Modal、Drawer |
| 边框-默认 | # | 输入框、表格边框 |
| 边框-Hover | # | 输入框悬停 |
| 边框-Focus | # | 输入框聚焦 |
| 边框-Disabled | # | 禁用状态边框 |
| 边框-Error | # | 校验失败边框 |
| 分割线 | # | 列表分割线 |
| 文字-主要 | # | 标题、核心内容 |
| 文字-次要 | # | 描述、辅助信息 |
| 文字-禁用 | # | 禁用状态文字 |
| 文字-占位符 | # | Placeholder |
| 蒙层色 | # | Modal 背景蒙层 |

**图表色板**（仅 Dashboard 页面存在时提取）

| 系列 | 色值 |
|------|------|
| 系列 1 | # |
| 系列 2 | # |
| … | … |

---

### 5.2 文字排版系统

**字体家族**

```
中文主字体：[PingFang SC / HarmonyOS Sans / 其他]
英文 / 数字字体：[Inter / Roboto / 其他，或与中文相同]
数据大字字体：[与正文相同 / 单独配置]
最小字号限制：[N]px（B 端建议不低于 12px）
```

**字体层级**

| 层级 | 字号 | 字重 | 行高 | 颜色 | 使用场景 |
|------|------|------|------|------|---------|
| 页面标题 H1 | px | | | | 页面大标题 |
| 模块标题 H2 | px | | | | 卡片标题、区块标题 |
| 正文 Body | px | | | | 表格内容、描述 |
| 辅助文字 Caption | px | | | | 时间戳、标签、提示 |
| 按钮文字 | px | | | | 各类按钮 |
| 数据大字 | px | | | | Dashboard 核心指标 |
| 表格表头 | px | | | | Table Header |
| 代码 / 等宽 | px | | | | 如有代码展示 |

---

### 5.3 圆角系统

逐组件记录，识别是否存在统一步进规律（如 2/4/6/8px）：

| 组件 | 圆角值 |
|------|--------|
| 主按钮 | px |
| 次级按钮 / 幽灵按钮 | px |
| 输入框 | px |
| 下拉菜单 | px |
| 卡片 / 面板 | px |
| 弹窗 Modal | px |
| 抽屉 Drawer | px |
| 标签 Tag / Badge | px |
| Tooltip / Popover | px |
| 头像 Avatar | px 或 50% |
| 图片 / 缩略图 | px |
| 进度条 | px |

> ⚠️ B 端约束：默认圆角 > 12px 为异常值，除非设计稿明确使用，否则标注为「待确认」。

---

### 5.4 边框系统

```
边框粗细：[N]px（B 端通常为 1px）
边框样式：实线 / 虚线 / 无（用背景色区分）

各状态边框色：
  默认：#
  Hover：#
  Focus：#（通常配合 Focus Ring 使用）
  Disabled：#
  Error：#
  Read-only：#

表格边框规则：
  横向边框：是 / 否
  纵向边框：是 / 否
  外边框：是 / 否

分割线：
  颜色：#
  粗细：[N]px
  样式：实线 / 虚线
```

---

### 5.5 间距系统

**基础步进单位**：[4px / 8px / 其他]

**组件内间距（Padding）**

| 组件 | 水平 Padding | 垂直 Padding |
|------|-------------|-------------|
| 主按钮-大 | px | px |
| 主按钮-中 | px | px |
| 主按钮-小 | px | px |
| 输入框 | px | px |
| 卡片 | px | px |
| 弹窗 | px | px |
| 表格单元格 | px | px |
| 下拉选项 | px | px |

**组件间间距（Gap / Margin）**

```
表单标签与输入框间距：[N]px
表单行间距：[N]px
表单列间距（多列表单）：[N]px
列表行间距：[N]px
卡片间距：[N]px
模块间垂直间距：[N]px
栅格列间距 Gutter：[N]px
操作按钮组间距：[N]px
```

**页面级间距**

```
页面内容区水平 Padding：[N]px
页面内容区顶部 Padding：[N]px
侧边栏展开宽度：[N]px
侧边栏收起宽度：[N]px
顶部导航高度：[N]px
面包屑区域高度：[N]px
```

---

### 5.6 阴影系统

逐层级提取，记录完整 CSS 值：

| 层级 | CSS 值 | 使用场景 |
|------|--------|---------|
| 无阴影 | none | 普通卡片、表格行 |
| 轻阴影 | box-shadow: … | 卡片 Hover、固定表头 |
| 中阴影 | box-shadow: … | 下拉菜单、Tooltip |
| 重阴影 | box-shadow: … | Modal、Drawer、全局通知 |

> B 端阴影通常颜色浅、偏移小，常见格式：`0 2px 8px rgba(0,0,0,0.12)`

---

### 5.7 排版布局系统

**整体框架结构**

```
布局模式：左侧边栏 + 顶部导航 / 纯顶部导航 / 混合
侧边栏位置：左 / 右
侧边栏展开宽度：[N]px
侧边栏收起宽度：[N]px
顶部导航高度：[N]px
内容区最大宽度：[N]px 或 无限制
面包屑：有 / 无
```

**栅格系统**

```
列数：12 / 24 / 其他
列宽：自适应 / 固定 [N]px
Gutter（列间距）：[N]px
响应式断点：有 / 无
```

**表单规范**

```
标签对齐方式：顶部对齐 / 左对齐 / 右对齐
标签宽度：[N]px 或 自适应
必填标记位置：标签前 * / 标签后 *
校验提示位置：输入框下方 / 右侧
单行表单列数：1 / 2 / 3
```

**表格规范**

```
行高-标准密度：[N]px
行高-紧凑密度：[N]px
斑马纹：有 / 无（奇偶行背景色）
固定列：操作列固定右侧 / 不固定
操作项间距：[N]px
空状态高度：[N]px
分页位置：右下角 / 居中
```

---

### 5.8 适配规则

```
主要目标设备：桌面端
最小支持宽度：[1280 / 1440 / 1920]px
是否支持响应式：是 / 否

断点设置（如支持响应式）：
  ≥ 1920px：大屏
  ≥ 1440px：标准桌面
  ≥ 1280px：小屏桌面
  < 1280px：横向滚动 / 降级 / 不支持

移动端：不支持 / 独立 App / 有限支持
图表缩放策略：等比缩放 / 固定尺寸 / 自适应高度
```

---

## 六、输出格式：Design Token 注入代码块

提取完成后，生成以下格式的代码块，供用户直接注入 Claude / Cursor / v0 / Copilot：

~~~text
### 🛠️ UI Framework Context
- **Target Framework**: [框架名称]
- **Icon Library**: [Lucide / Heroicons / 其他]
- **Design Density**: High / Compact（Enterprise Standard）

### 🎨 Design Tokens
:root {
  /* Brand */
  --color-primary: [#];
  --color-primary-hover: [#];
  --color-primary-active: [#];
  --color-primary-focus-ring: [#];

  /* Functional */
  --color-success: [#];
  --color-warning: [#];
  --color-error: [#];
  --color-info: [#];

  /* Neutral - Background */
  --color-bg-page: [#];
  --color-bg-card: [#];
  --color-bg-modal: [#];

  /* Neutral - Border */
  --color-border-default: [#];
  --color-border-hover: [#];
  --color-border-focus: [#];
  --color-border-disabled: [#];
  --color-border-error: [#];

  /* Neutral - Text */
  --color-text-primary: [#];
  --color-text-secondary: [#];
  --color-text-disabled: [#];
  --color-text-placeholder: [#];

  /* Typography */
  --font-family-base: [字体];
  --font-size-base: [N]px;
  --font-size-sm: [N]px;
  --font-size-lg: [N]px;
  --line-height-base: [N];

  /* Spacing */
  --spacing-unit: [N]px;
  --spacing-xs: [N]px;
  --spacing-sm: [N]px;
  --spacing-md: [N]px;
  --spacing-lg: [N]px;
  --spacing-xl: [N]px;

  /* Radius */
  --radius-sm: [N]px;
  --radius-md: [N]px;
  --radius-lg: [N]px;

  /* Shadow */
  --shadow-sm: [值];
  --shadow-md: [值];
  --shadow-lg: [值];

  /* Layout */
  --sidebar-width: [N]px;
  --sidebar-collapsed-width: [N]px;
  --topbar-height: [N]px;
  --table-row-height: [N]px;
}

### 📐 Layout Heuristics
- **Layout Mode**: [布局结构]
- **Form Label Align**: [Top / Left / Right]
- **Grid Columns**: [12 / 24]
- **Min Viewport**: [N]px
- **Component Rules**:
  - Buttons: 200ms transition, [N]px border-radius
  - Inputs: 2px focus ring, [N]px padding
  - Tables: [N]px row height, operations pinned right

> 📌 若目标框架为 React + shadcn/ui，CSS Variables 须使用 HSL 格式：
> `--primary: 221.2 83.2% 53.3%;`（不含 hsl() 包裹，由 shadcn 自动处理）
> 并同步更新 tailwind.config.js 中的 `colors.primary` 映射。

### 🎯 Execution Task
Apply these tokens to the following request: [USER_PROMPT_HERE]
~~~

---

## 七、约束禁令

- **禁止私自扩充**：未在设计稿中发现的颜色，禁止调用 Tailwind / Element Plus / Ant Design 的默认品牌色填充
- **禁止降密**：B 端场景禁止使用过大间距或 C 端风格超大圆角（> 12px 需有设计稿明确依据）
- **禁止模糊表述**：所有输出必须有具体数值或十六进制色值，禁止"浅蓝色"、"适中字号"等描述
- **禁止遗漏状态**：色彩系统必须覆盖 Default / Hover / Focus / Disabled / Error / Read-only 全状态
- **禁止跨场景套用**：C 端产品的规范不得直接迁移至 B 端，反之亦然

---

## 八、质量自检清单

输出前逐项确认：

- [ ] 所有颜色均有具体 HEX / RGB 色值，无模糊描述
- [ ] 功能色 4 个（Success / Warning / Error / Info）全部覆盖
- [ ] 文字色 4 级（主要 / 次要 / 禁用 / 占位符）全部提取
- [ ] 所有交互状态（Hover / Focus / Disabled / Error / Read-only）均有对应色值
- [ ] 圆角已逐组件记录，无 > 12px 的未标注异常值
- [ ] 间距已识别基础步进单位，并可推导出规律
- [ ] 阴影已记录完整 CSS 值，非"轻/中/重"模糊描述
- [ ] Design Token 代码块格式正确，可直接粘贴使用
- [ ] 所有「待补充」项已明确标注原因
- [ ] 框架变量格式与用户选定框架一致
