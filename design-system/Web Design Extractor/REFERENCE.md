# Web Design Extractor — 技术参考文档

本文档是 SKILL.md 的补充说明，记录各类 design token 的提取方法、CSS 解析规则与常见模式。

---

## 1. CSS 变量提取优先级

```
优先级 1：:root { --var: value }           ← 最可靠
优先级 2：[data-theme="light"] { ... }     ← 主题感知
优先级 3：.component { property: value }   ← 组件级
优先级 4：内联 style="..."               ← 覆盖值
优先级 5：Tailwind class 反推            ← 最后手段
```

---

## 2. 颜色提取常见模式

### shadcn/ui 模式
```css
:root {
  --background: 0 0% 100%;      /* HSL 无括号 */
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
}
```
→ 转换：`hsl(var(--primary))` = `hsl(222.2 47.4% 11.2%)`

### Tailwind 配置模式
从 class 名称反推：`bg-blue-600` → `#2563eb`（Tailwind v3 默认色板）

### CSS 变量别名模式
```css
:root {
  --blue-500: #3b82f6;
  --color-primary: var(--blue-500);  /* 别名 */
}
```
→ 需要递归解析到最终值

### 暗色模式双变量
```css
:root { --bg: #ffffff; }
[data-theme="dark"] { --bg: #0a0a0a; }
@media (prefers-color-scheme: dark) { :root { --bg: #0a0a0a; } }
```
→ 在 tokens.json 中记录为：
```json
"color.bg.default": { "light": "#ffffff", "dark": "#0a0a0a" }
```

---

## 3. 字体提取规则

### Google Fonts 检测
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700" rel="stylesheet">
```
→ 提取：Inter, weights: 400/500/700

### @font-face 本地字体
```css
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-weight: 400;
}
```
→ 记录字体名，注明为本地字体（无法在 preview.html 中引用）

### 字阶推断逻辑
从 h1~h6、p、small 等标签的 font-size 值，构建 type scale。
常见模式：
- **1.25 比例**（Major Third）: 12, 15, 18, 23, 28, 35, 44px
- **1.333 比例**（Perfect Fourth）: 12, 16, 21, 28, 37, 50px
- **自定义 Tailwind**：text-xs(12) text-sm(14) text-base(16) text-lg(18) text-xl(20) text-2xl(24)...

---

## 4. 间距反推方法

从以下属性中提取间距值，归纳成 scale：
- `padding`, `margin`：组件内外边距
- `gap`：Flex/Grid 间隔
- `top/right/bottom/left`：绝对定位偏移

**归纳规律**：
1. 找出所有出现的间距值（去重）
2. 判断基准单位（通常是 4px 或 8px）
3. 构建倍数关系表

示例：收集到 `4, 8, 12, 16, 20, 24, 32, 40, 48, 64` → 4px 基准，scale 为 1~16

---

## 5. 阴影层次分析

常见阴影层次：
```
sm:   0 1px 2px rgba(0,0,0,0.05)                         ← 微阴影
base: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)
md:   0 4px 6px -1px rgba(0,0,0,0.1)
lg:   0 10px 15px -3px rgba(0,0,0,0.1)
xl:   0 20px 25px -5px rgba(0,0,0,0.1)
2xl:  0 25px 50px -12px rgba(0,0,0,0.25)                 ← 强悬浮
```

**品牌特征判断**：
- 无阴影 → 极简风格，依赖边框
- 彩色阴影（如 `rgba(99,102,241,0.3)`）→ 强品牌色
- 大模糊小偏移 → 现代 neumorphism
- 多层叠加阴影 → 精致 Material 风格

---

## 6. 圆角语义

| 值范围 | 风格含义 |
|--------|---------|
| 0 | 企业/政府，严肃 |
| 2~4px | 轻微柔化，大多数 SaaS |
| 6~8px | 友好，消费品 |
| 10~16px | 圆润，偏消费向 |
| 20px+ | 极圆，卡片化设计 |
| 9999px | 胶囊按钮，现代感 |

---

## 7. 组件视觉特征提取

### Button 特征清单
```
尺寸：height, padding-x, font-size, icon-size
形态：border-radius, border-width, border-color
颜色：bg, text, border（默认 / hover / active / disabled）
字重：font-weight
变体：primary, secondary, ghost, outline, destructive, link
特效：hover scale, shadow, transition duration
```

### Input 特征清单
```
边框：border-color, border-width, border-radius
聚焦：focus-ring color, focus-ring width, focus-ring offset
尺寸：height, padding-x, padding-y, font-size
状态：error border-color, disabled opacity
label：floating / static / above
```

### Card 特征清单
```
容器：border-radius, box-shadow, border, background
内边距：padding（通常 16px~24px）
分割：divider 颜色、使用频率
交互：hover shadow / lift 效果
```

---

## 8. preview.html 结构模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{SiteName} Design Preview</title>
  <style>
    /* ===== TOKEN DEFINITIONS ===== */
    :root {
      /* Colors */
      --color-primary: ...;
      /* Fonts */
      --font-display: ...;
      /* Space */
      --space-1: ...;
      /* ... */
    }

    /* ===== RESET ===== */
    *, *::before, *::after { box-sizing: border-box; }
    body { margin: 0; font-family: var(--font-body); }

    /* ===== PREVIEW LAYOUT ===== */
    .section { padding: 3rem 2rem; border-bottom: 1px solid var(--color-border); }
    .section-title { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em;
                     text-transform: uppercase; color: var(--color-text-secondary);
                     margin-bottom: 1.5rem; }
  </style>
</head>
<body>

<!-- 1. 调色板 -->
<section class="section">
  <p class="section-title">Colors</p>
  <div class="color-grid">
    <!-- 每个 token 一个色块 -->
  </div>
</section>

<!-- 2. 字体 -->
<section class="section">
  <p class="section-title">Typography</p>
  <!-- h1~h4, body, caption -->
</section>

<!-- 3. 间距 -->
<section class="section">
  <p class="section-title">Spacing Scale</p>
  <!-- 色块宽度可视化 -->
</section>

<!-- 4. 圆角 & 阴影 -->
<section class="section">
  <p class="section-title">Radius & Shadow</p>
</section>

<!-- 5. 组件 -->
<section class="section">
  <p class="section-title">Components</p>
  <!-- Button, Input, Card, Badge -->
</section>

<!-- 6. Hero 示例 -->
<section class="section">
  <p class="section-title">Page Template Example</p>
  <!-- 用 token 搭的简单页面 -->
</section>

</body>
</html>
```

---

## 9. tokens.json 完整结构

```json
{
  "meta": {
    "source": "https://example.com",
    "extracted": "2025-01-01",
    "theme": "light",
    "style": "minimal SaaS",
    "confidence": {
      "color": 0.9,
      "font": 0.8,
      "space": 0.6,
      "radius": 0.9,
      "shadow": 0.7,
      "motion": 0.5,
      "layout": 0.7
    }
  },
  "color": {
    "primary": "#...",
    "primary.hover": "#...",
    "primary.foreground": "#...",
    "secondary": "#...",
    "accent": "#...",
    "bg.default": "#...",
    "bg.subtle": "#...",
    "surface": "#...",
    "text.primary": "#...",
    "text.secondary": "#...",
    "text.disabled": "#...",
    "border.default": "#...",
    "border.strong": "#...",
    "danger": "#...",
    "success": "#...",
    "warning": "#...",
    "info": "#..."
  },
  "font": {
    "family.display": "...",
    "family.body": "...",
    "family.mono": "...",
    "size.xs": "12px",
    "size.sm": "14px",
    "size.base": "16px",
    "size.lg": "18px",
    "size.xl": "20px",
    "size.2xl": "24px",
    "size.3xl": "30px",
    "size.4xl": "36px",
    "size.5xl": "48px",
    "weight.light": "300",
    "weight.regular": "400",
    "weight.medium": "500",
    "weight.semibold": "600",
    "weight.bold": "700",
    "lineHeight.tight": "1.25",
    "lineHeight.base": "1.5",
    "lineHeight.relaxed": "1.75",
    "tracking.tight": "-0.025em",
    "tracking.normal": "0",
    "tracking.wide": "0.025em"
  },
  "space": {
    "0": "0",
    "1": "4px",
    "2": "8px",
    "3": "12px",
    "4": "16px",
    "5": "20px",
    "6": "24px",
    "8": "32px",
    "10": "40px",
    "12": "48px",
    "16": "64px",
    "20": "80px",
    "24": "96px"
  },
  "radius": {
    "none": "0",
    "sm": "2px",
    "base": "4px",
    "md": "6px",
    "lg": "8px",
    "xl": "12px",
    "2xl": "16px",
    "full": "9999px"
  },
  "shadow": {
    "none": "none",
    "sm": "0 1px 2px rgba(0,0,0,0.05)",
    "base": "0 1px 3px rgba(0,0,0,0.1)",
    "md": "0 4px 6px -1px rgba(0,0,0,0.1)",
    "lg": "0 10px 15px -3px rgba(0,0,0,0.1)",
    "xl": "0 20px 25px -5px rgba(0,0,0,0.1)"
  },
  "motion": {
    "duration.fast": "150ms",
    "duration.base": "200ms",
    "duration.slow": "300ms",
    "easing.default": "ease",
    "easing.spring": "cubic-bezier(0.34, 1.56, 0.64, 1)",
    "easing.enter": "cubic-bezier(0, 0, 0.2, 1)",
    "easing.exit": "cubic-bezier(0.4, 0, 1, 1)"
  },
  "layout": {
    "maxWidth.sm": "640px",
    "maxWidth.md": "768px",
    "maxWidth.lg": "1024px",
    "maxWidth.xl": "1280px",
    "maxWidth.content": "720px",
    "grid.columns": "12",
    "grid.gutter": "24px",
    "breakpoint.sm": "640px",
    "breakpoint.md": "768px",
    "breakpoint.lg": "1024px",
    "breakpoint.xl": "1280px",
    "breakpoint.2xl": "1536px"
  }
}
```

---

## 10. 常见问题

**Q: 网站是 JS 渲染的，web_fetch 拿到的是空 body？**
A: 尝试以下备用策略：
1. 抓取 `/_next/static/css/` 下的 CSS 文件（Next.js）
2. 抓取 `/assets/` 或 `/static/` 目录
3. 尝试抓取 sitemap 找到静态子页面
4. 告知用户无法自动提取，提供手动分析清单

**Q: 如何处理渐变色？**
A: 作为独立 token 记录：
```json
"gradient.hero": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
"gradient.cta": "linear-gradient(90deg, #f093fb 0%, #f5576c 100%)"
```

**Q: 网站有 6 种按钮变体，都要记录吗？**
A: 只记录主要的 3~4 种（primary, secondary, ghost, destructive），
其余在 design.md 的"组件规律"章节用文字描述即可。

**Q: 提取到的颜色非常多（50+），怎么处理？**
A: 先聚类归纳，找出：
- 品牌主色系（通常 1~2 个色相，3~5 个深浅变体）
- 语义色（danger/success/warning/info）
- 中性色（gray scale，背景/文字/边框用）
- 其余颜色可标注为"辅助色，非核心 token"

---

## 11. 常见框架的 CSS 变量位置速查

| 框架/工具 | CSS 变量位置 | 特殊说明 |
|-----------|-------------|----------|
| Tailwind CSS | class 名称推断 | 查找 `tailwind.config` 中的 extend |
| CSS Modules | `.module.css` 文件 | 变量通常在 `:root` |
| Styled Components | JS 中的 theme 对象 | 在 `<ThemeProvider>` 中 |
| CSS-in-JS (Emotion) | `theme.ts` / `tokens.ts` | 从 data attribute 推断 |
| shadcn/ui | `globals.css` 的 `:root` | HSL 格式的 CSS 变量 |
| Radix UI | `--radix-*` 前缀变量 | |
| Ant Design | `--ant-*` 前缀 | 有完整的 token 体系 |
| Next.js | `/_next/static/css/` | 抓取编译后的 CSS 文件 |
