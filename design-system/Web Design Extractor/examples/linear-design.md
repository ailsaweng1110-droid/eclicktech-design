# Linear Design System

> 来源：https://linear.app | 提取日期：2026-04-22 | 主题：双主题（light / dark）

---

## 品牌概览

Linear 是面向工程团队和 AI Agent 的产品开发系统。其设计语言高度自律——暗色优先、密度极高、动效克制——传达出「工具本身不应成为负担」的核心哲学。在 SaaS 产品普遍走向「友好圆润」的大背景下，Linear 逆行，用近乎工程图纸般的精准感建立了强烈的品牌辨识度。

**情绪关键词**：精准 · 克制 · 高密度 · 工程感 · 无噪音

**目标受众**：工程师、技术型 PM、高速迭代的产品团队

---

## 视觉调性

Linear 的设计哲学可归纳为**「为速度而设计」**：

- **暗色优先**：产品界面默认暗色，官网提供双主题。暗色底色为近乎纯黑的 `#0F0F10`，不是流行的深灰蓝，而是更接近终端/编辑器的中性黑
- **信息密度**：正文基准 14px（而非惯例 16px），行间距偏紧，在有限空间内呈现更多信息
- **品牌色低调**：主色 `#5E6AD2` 是去饱和的蓝紫，不抢眼，仅用于关键交互点（按钮、链接、选中态）
- **字距紧绷**：大标题 letter-spacing 约 -0.03em，制造「字母贴合」的精工感
- **极小圆角**：按钮约 5px，整体几乎是直角，与圆润风格完全相反

---

## 颜色系统

### 品牌官方色（来自 linear.app/brand）

| 名称 | 值 | 用途 |
|------|-----|------|
| Mercury White | `#F4F5F8` | 亮色模式文字/背景 |
| Nordic Gray | `#222326` | 暗色模式表面色 |

### 亮色主题

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-primary` | `#5E6AD2` | 主操作按钮、链接、选中态 |
| `--color-bg-default` | `#FFFFFF` | 页面背景 |
| `--color-bg-subtle` | `#F7F8F9` | 侧边栏、悬停底色 |
| `--color-bg-raised` | `#F0F1F3` | 标签、badge 背景 |
| `--color-text-primary` | `#1A1A1A` | 主要文字 |
| `--color-text-secondary` | `#6B6F76` | 次要文字、说明 |
| `--color-border` | `#E5E7EB` | 分割线、边框 |

### 暗色主题

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-primary` | `#5E6AD2` | 同亮色（品牌色不变） |
| `--color-bg-default` | `#0F0F10` | 页面背景（近纯黑）|
| `--color-bg-subtle` | `#1A1A1C` | 侧边栏、列表悬停 |
| `--color-bg-raised` | `#222326` | Nordic Gray，卡片/浮层 |
| `--color-text-primary` | `#F4F5F8` | Mercury White，主要文字 |
| `--color-text-secondary` | `#9EA3AB` | 次要文字 |
| `--color-border` | `#2D2D30` | 分割线（极细，几乎隐形） |

### 语义色（双主题共用）

| Token | 值 |
|-------|-----|
| `--color-danger` | `#E5484D` |
| `--color-success` | `#30A46C` |
| `--color-warning` | `#F5A623` |

---

## 字体系统

**主字体**：Inter（几何无衬线，官网及产品界面一致）
**代码字体**：Geist Mono（字形现代，等宽，用于 issue 编号、代码块）

### 字阶

| Token | 值 | 典型用途 |
|-------|-----|---------|
| `--font-size-xs` | `11px` | 角标、版本号 |
| `--font-size-sm` | `12px` | 标签、辅助说明 |
| `--font-size-base` | `14px` | **正文基准**（低于行业惯例，高密度关键） |
| `--font-size-lg` | `16px` | 强调文字、小标题 |
| `--font-size-xl` | `18px` | 次级标题 |
| `--font-size-2xl` | `22px` | 区块标题 |
| `--font-size-3xl` | `28px` | 页面标题 |
| `--font-size-4xl` | `36px` | 大标题 |
| `--font-size-5xl` | `52px` | Hero 展示文字 |

### 字重与字距

- 标题：weight 700，letter-spacing `-0.03em`（贴紧，制造精准感）
- 导航/按钮：weight 500，letter-spacing `-0.01em`
- 正文：weight 400，letter-spacing `-0.01em`
- 数字/代码：Geist Mono，weight 400/500

---

## 间距系统

**基准单位：4px**

| Token | 值 | 常见场景 |
|-------|-----|---------|
| `--space-1` | `4px` | 图标与文字间距 |
| `--space-2` | `8px` | 列表项内边距（垂直）|
| `--space-3` | `12px` | 紧凑组件内边距 |
| `--space-4` | `16px` | 标准内边距，卡片 padding |
| `--space-6` | `24px` | 组件间隔 |
| `--space-8` | `32px` | 区块内间距 |
| `--space-12` | `48px` | 节之间的分隔 |
| `--space-16` | `64px` | 大区块留白 |

**密度特征**：Linear 整体间距偏紧，列表行高约 32px，导航高度约 48px，比同类产品节省约 20% 的垂直空间。

---

## 形态语言

### 圆角

Linear 使用**极小圆角**，是市面上圆角最小的主流 SaaS 之一：

```css
--radius-sm:   3px;   /* 标签、badge */
--radius-base: 5px;   /* 按钮、输入框 */
--radius-md:   7px;   /* 下拉菜单 */
--radius-lg:   10px;  /* 卡片、面板 */
--radius-xl:   14px;  /* 弹窗、侧边抽屉 */
--radius-full: 9999px;/* 头像、状态圆点 */
```

**设计含义**：小圆角传递「工具感」而非「消费感」，与 Notion（12px）、Linear 的竞品形成显著差异。

### 阴影

暗色模式特殊处理：阴影颜色更深（`rgba(0,0,0,0.4+)`）同时加一层极细的白色描边（`rgba(255,255,255,0.04)`）来模拟玻璃边缘的光感，增强层次而不显突兀。

---

## 动效规范

Linear 的动效核心原则：**快到感觉不像在动**。

| Token | 值 | 用途 |
|-------|-----|------|
| `--duration-fast` | `100ms` | 颜色/边框切换（hover） |
| `--duration-base` | `150ms` | 下拉展开、弹层出现 |
| `--duration-slow` | `250ms` | 页面级滑入、复杂动画 |

缓动：以 ease-out 为主（`cubic-bezier(0.25, 0.46, 0.45, 0.94)`），快进慢出，强调「已响应」的即时感，而非「正在动画」的表演感。

**无装饰性动画**：Linear 不使用加载骨架屏的渐变扫光、入场时的弹跳效果等装饰动画，所有动效服务于功能反馈。

---

## 布局规范

- **导航高度**：约 48px，sticky，背景半透明模糊（`backdrop-filter: blur`）
- **内容最大宽度**：营销页 1200px，文章/Method 页 680px（偏窄，专注阅读）
- **栅格**：12 列，gutter 24px
- **断点**：640 / 768 / 1024 / 1280px（标准 Tailwind 断点）

---

## 组件规律

### Button

```css
/* Primary */
padding: 6px 14px;          /* 紧凑，高度约 30px */
border-radius: var(--radius-base);  /* 5px */
font-size: var(--font-size-sm);     /* 12px */
font-weight: 500;
background: var(--color-primary);   /* #5E6AD2 */
transition: opacity 100ms ease-out;

/* hover: 不改变背景色，改为降低透明度 */
opacity: 0.85;
```

### Input

- 边框：`1px solid var(--color-border)`，无填充背景（透明）
- 聚焦：`box-shadow: 0 0 0 2px rgba(94,106,210,0.4)`（品牌色光晕，较细）
- 高度：28px（小）/ 32px（默认）/ 36px（大）
- 圆角：`var(--radius-base)` 5px

### Issue 列表行（核心组件）

```
高度: 32px
padding: 0 12px
hover 背景: var(--color-bg-subtle)
字号: 14px，weight 400
状态图标: 16×16px，圆形，左对齐
优先级图标: 12×12px
```

### Badge / Label

- 高度：18px
- 内边距：2px 6px
- 圆角：`var(--radius-sm)` 3px
- 字号：11px，weight 500
- 颜色：用户自定义（7色系），背景为色值 15% 透明度

### Navigation

- 高度：48px
- 背景：`rgba(15,15,16,0.8)` + `backdrop-filter: blur(12px)`（暗色）
- 链接：font-size 14px，weight 400 → hover weight 500
- 无下划线，依靠 weight 变化表达 hover 态

---

## 设计原则

从 Linear 的整体视觉系统推断出的核心设计哲学：

1. **速度即设计**：每一个设计决策都服务于「让用户更快完成任务」——更小的字号、更紧的间距、更短的动效，都是为了减少认知摩擦
2. **克制即品牌**：品牌色 `#5E6AD2` 在整个界面中出现频率极低，只在最需要引导注意力时出现，「稀缺性」让它保持力量
3. **暗色是默认，不是选项**：产品设计暗色优先，不是「提供暗色模式」而是「以暗色为基准适配亮色」
4. **工具感 > 消费感**：小圆角、高密度、无装饰动画，拒绝消费品的「友好」美学，建立工程师信任的「专业工具」感
5. **噪音为零**：任何无法减少认知负担的视觉元素都不应存在

---

## 如何使用本文档

将以下内容作为 system prompt 前缀加入你的 AI 工具：

> 请严格参考以下 Linear 设计规范文档来生成 UI 代码。
> 核心原则：暗色优先、高密度、极小圆角（5px）、字号基准 14px、动效极短（150ms）。
> 所有颜色通过 CSS 变量引用，支持 light/dark 双主题切换。
> 禁止使用圆润风格、装饰性动画、过大的留白。
>
> [粘贴本文档内容]

**推荐工具**：Claude、Cursor、GitHub Copilot、v0.dev

**推荐场景**：
- 构建面向工程师的内部工具、Dashboard
- 需要「高信息密度」布局的管理后台
- 参考 Linear 风格打造自己的 issue tracker / 项目管理工具

---

*本文档由 web-design-extractor 技能生成 · 来源 linear.app · 仅供参考学习使用*
