# Stripe Design System

> 本文档由 web-design-extractor 技能自动生成，用于 AI 工具学习参考。
> 来源：https://stripe.com | 提取日期：2025-01-01

---

## 品牌概览

Stripe 是面向开发者和企业的支付基础设施平台。其设计系统传达出**可信赖、精准、现代**的气质，
用深靛蓝底色搭配明亮紫色品牌色，在金融科技行业中建立了辨识度极高的视觉标识。

**情绪关键词**：可信赖 · 精准 · 优雅 · 技术感 · 国际化

**目标受众**：开发者、初创公司 CTO、企业技术决策者

---

## 视觉调性

Stripe 的设计哲学可以概括为"**精工极简**"——每个像素都经过精心考量，绝不拥挤，
绝不随意。其视觉语言的核心特征：

- **深色辅以光亮**：深海蓝（`#0a2540`）作为主文字和锚定色，搭配明亮紫（`#635bff`）作为行动焦点
- **渐变作为叙事工具**：大幅 hero 区域使用多色光晕渐变，传递"技术魔法感"
- **精致的阴影层次**：多层叠加的 box-shadow 制造真实的深度感，不依赖大色块区分层次
- **克制的动效**：过渡时长极短（100~200ms），强调响应感而非炫技

---

## 颜色系统

### 主调色板

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-primary` | `#635bff` | 品牌主色，CTA 按钮，链接，强调 |
| `--color-primary-hover` | `#5851ea` | 主色悬停态 |
| `--color-secondary` | `#0a2540` | 深色背景，主标题，锚定文字 |
| `--color-accent` | `#00d4ff` | 高亮强调，图表数据，图标点缀 |

### 背景层次

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-bg-default` | `#ffffff` | 页面主背景 |
| `--color-bg-subtle` | `#f6f9fc` | 区块背景，分区底色 |
| `--color-surface` | `#ffffff` | 卡片、浮层表面 |

### 语义色

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-danger` | `#df1b41` | 错误、删除、危险操作 |
| `--color-success` | `#09825d` | 成功状态、已完成 |
| `--color-warning` | `#b5740d` | 警告、注意 |
| `--color-info` | `#1a56db` | 信息提示 |

### 文字与边框

| Token | 值 | 用途 |
|-------|-----|------|
| `--color-text-primary` | `#0a2540` | 主要文字 |
| `--color-text-secondary` | `#425466` | 次要文字、说明文字 |
| `--color-text-disabled` | `#8898aa` | 禁用状态 |
| `--color-border` | `#e6ebf1` | 默认边框 |
| `--color-border-strong` | `#c4cdd6` | 强调边框 |

---

## 字体系统

Stripe 使用系统字体栈，在不同平台上呈现原生体验：

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

代码部分使用 Source Code Pro：
```css
font-family: "Source Code Pro", Consolas, monospace;
```

### 字阶

| Token | 值 | 典型用途 |
|-------|-----|---------|
| `--font-size-xs` | `11px` | 标注、角标 |
| `--font-size-sm` | `13px` | 说明文字、表格内容 |
| `--font-size-base` | `16px` | 正文 |
| `--font-size-lg` | `18px` | 大正文、引言 |
| `--font-size-xl` | `20px` | 小标题 |
| `--font-size-2xl` | `24px` | 次级标题 |
| `--font-size-3xl` | `32px` | 区块标题 |
| `--font-size-4xl` | `40px` | 页面标题 |
| `--font-size-5xl` | `52px` | Hero 大标题 |

### 字重规律

- **正文**：400（regular）
- **小标题 / 强调**：500（medium）
- **按钮 / 导航**：600（semibold）
- **大标题**：700（bold）

### 行高规律

- 标题：`1.2`（tight）
- 正文：`1.6`（base）
- 长文章：`1.8`（relaxed）

---

## 间距系统

基准单位：**4px**

| Token | 值 | 常见用途 |
|-------|-----|---------|
| `--space-1` | `4px` | 图标间距、最小 gap |
| `--space-2` | `8px` | 元素内部小间距 |
| `--space-3` | `12px` | 输入框内边距（垂直） |
| `--space-4` | `16px` | 基础内边距，卡片 padding |
| `--space-6` | `24px` | 组件间隔 |
| `--space-8` | `32px` | 区块内间距 |
| `--space-12` | `48px` | 节之间的分隔 |
| `--space-16` | `64px` | 大区块间距 |
| `--space-24` | `96px` | Hero 区域上下留白 |

---

## 形态语言

### 圆角

Stripe 使用**小圆角**，传递专业、精准的感觉，不做过度装饰：

```css
--radius-sm: 3px;     /* 标签、小元素 */
--radius-base: 4px;   /* 默认按钮、输入框 */
--radius-md: 6px;     /* 下拉框、小卡片 */
--radius-lg: 8px;     /* 普通卡片 */
--radius-xl: 12px;    /* 大卡片、弹窗 */
--radius-2xl: 20px;   /* 特色卡片 */
--radius-full: 9999px; /* 胶囊按钮、头像 */
```

### 阴影

Stripe 的阴影特征：**多层叠加、颜色偏蓝、软边缘**：

```css
--shadow-sm: 0 1px 1px rgba(0,0,0,0.03), 0 3px 6px rgba(18,42,66,0.04);
--shadow-base: 0 2px 5px -1px rgba(50,50,93,0.25), 0 1px 3px -1px rgba(0,0,0,0.3);
--shadow-md: 0 6px 12px -2px rgba(50,50,93,0.25), 0 3px 7px -3px rgba(0,0,0,0.3);
--shadow-lg: 0 13px 27px -5px rgba(50,50,93,0.25), 0 8px 16px -8px rgba(0,0,0,0.3);
```

---

## 动效规范

Stripe 的动效以**快速响应**为核心，让界面感觉即时而流畅：

| Token | 值 | 用途 |
|-------|-----|------|
| `--duration-fast` | `100ms` | 颜色变化、边框变化 |
| `--duration-base` | `200ms` | 位移、展开、淡入 |
| `--duration-slow` | `350ms` | 页面级动画、大幅滑入 |

缓动函数：
```css
--easing-default: ease;
--easing-spring: cubic-bezier(0.34, 1.56, 0.64, 1);  /* 弹性反弹 */
--easing-enter: cubic-bezier(0, 0, 0.2, 1);           /* 快进慢出 */
--easing-exit: cubic-bezier(0.4, 0, 1, 1);            /* 快出 */
```

---

## 布局规范

### 栅格

- 12 列栅格，gutter：32px
- 内容区最大宽度：`740px`（文章/说明文字）
- 全宽最大宽度：`1140px`

### 断点

```css
@media (min-width: 576px)  { /* sm  */ }
@media (min-width: 768px)  { /* md  */ }
@media (min-width: 992px)  { /* lg  */ }
@media (min-width: 1200px) { /* xl  */ }
```

---

## 组件规律

### Button

```css
/* Primary */
.btn-primary {
  background: var(--color-primary);
  color: #fff;
  padding: 10px 20px;
  border-radius: var(--radius-base);
  font-weight: 600;
  font-size: var(--font-size-sm);
  border: none;
  transition: background var(--duration-fast) var(--easing-default),
              box-shadow var(--duration-fast) var(--easing-default);
}
.btn-primary:hover {
  background: var(--color-primary-hover);
  box-shadow: var(--shadow-md);
}
```

### Input

- 边框：`1px solid var(--color-border)`
- 聚焦：`box-shadow: 0 0 0 3px rgba(99, 91, 255, 0.15)`
- 高度：40px（默认），32px（小）
- 圆角：`var(--radius-base)`

### Card

- 背景：`var(--color-surface)`
- 边框：`1px solid var(--color-border)`
- 阴影：`var(--shadow-sm)` → hover 时升为 `var(--shadow-md)`
- 内边距：`var(--space-6)`（24px）
- 圆角：`var(--radius-lg)`（8px）

### Badge / Tag

- 高度：20px ~ 24px
- 内边距：4px 8px
- 圆角：`var(--radius-full)`（胶囊形）
- 字号：`var(--font-size-xs)` 11px
- 字重：600

---

## 设计原则

从 Stripe 的视觉系统中推断出的核心设计哲学：

1. **层次即可信**：通过精心设计的阴影、字重和颜色浓度建立视觉层级，让用户直觉知道"什么最重要"
2. **克制胜于堆砌**：每个元素的出现都有充分理由，留白是设计的一部分
3. **技术感与温度并存**：系统字体 + 精准 token 传递技术严谨感，渐变 + 光感装饰带来视觉温度
4. **响应优先于炫技**：动效极短，让交互感觉即时，而非表演性的
5. **品牌色即焦点**：紫色只用在最重要的行动点上，稀缺性让它保持力量

---

## AI 使用说明

将以下 system prompt 前缀加入你的 AI 工具：

```
请严格参考以下 Stripe 设计规范文档来生成 UI 代码。
所有颜色、字体、间距、圆角必须使用文档中定义的 CSS 变量，
不得使用硬编码或自行决定的样式值。
视觉调性应体现"精工极简"，深靛蓝 + 亮紫品牌色，小圆角，精致阴影。

[粘贴本文档内容]
```

**推荐工具**：Claude、Cursor、GitHub Copilot、v0.dev、Lovable

**推荐场景**：
- 快速搭建与 Stripe 风格一致的 SaaS 页面
- 设计新产品时参考成熟设计系统的决策逻辑
- 向团队成员介绍设计系统规范

---

*本文档由 web-design-extractor 技能生成 · 仅供参考学习使用*
