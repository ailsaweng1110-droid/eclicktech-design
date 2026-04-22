---
name: web-design-extractor
description: >
  当你需要分析网站、逆向工程其设计、提取外观风格或编写设计指南时自动触发。
  支持三种输入：公共网站 URL、网页截图（图片文件）、界面录屏（视频文件）。
  提取视觉调性、design token、排版布局与基础组件，
  输出 tokens.json、design.md 与 preview.html 三份交付物，供 AI 喂入学习参考。
  触发关键词：分析网站设计、提取设计规范、逆向设计系统、design token、design.md、
  复制某网站风格、参考某网站设计、帮我提取 xxx 的设计规范。
version: 1.1.0
---

# Web Design Extractor

分析网站设计 → 提取 token → 输出三份交付物（tokens.json · design.md · preview.html）。

支持三种输入，提取策略不同：

| 输入类型 | 判断方式 | 数据来源 |
|---------|---------|---------|
| **URL** | 用户提供网址 | HTML/CSS 源码，精确 |
| **截图** | 用户上传图片（jpg/png/webp） | 视觉观察，颜色/字体/间距均为推测 |
| **录屏** | 用户上传视频（mp4/mov/gif） | 逐帧视觉观察，可捕捉交互态与动效 |

---

## 工作流（按序执行，不得跳步）

### STEP 1 — 判断输入类型并告知进度

根据用户提供的内容判断输入类型，输出对应提示：

**URL 输入：**
```
🔍 正在分析：{URL}
输入类型：网站 URL · 将从 HTML/CSS 源码提取
阶段 1/3：抓取页面…
```

**截图输入：**
```
🖼️ 正在分析截图：{文件名}
输入类型：静态截图 · 所有 token 将通过视觉观察推测，精度低于源码提取
阶段 1/3：解析图像…
```

**录屏输入：**
```
🎬 正在分析录屏：{文件名}
输入类型：界面录屏 · 将逐帧观察，可提取交互态与动效线索
阶段 1/3：解析视频帧…
```

---

### STEP 2 — 提取（根据输入类型选择对应策略）

提取目标：7 大类 token —— **color · font · space · radius · shadow · motion · layout**
完整字段清单见 → `TOKEN-SCHEMA.md`

---

#### 策略 A：URL 输入

用 `web_fetch` 抓取页面，从 HTML/CSS 中提取。

提取优先级：CSS 变量（`:root` / `[data-theme]`）> 内联样式 > Tailwind class 反推。
框架特定技巧见 → `REFERENCE.md`

---

#### 策略 B：截图输入

逐项视觉观察，所有值均为推测，**必须全部加 `_inferred` 备注**。

**颜色**：用吸管逻辑识别主色、背景色、文字色、边框色，记录视觉估算的 HEX 值，备注"截图视觉取色"。

**字体**：观察字形特征（衬线/无衬线/等宽）、粗细对比、字间距，推测字体族和大致字阶比例。**无法确认具体字体名时**，根据字形特征推测最相似的字体（如笔画几何、无衬线 → Futura；人文无衬线、字距宽松 → Gill Sans），并在 `_inferred` 字段备注【根据字形推测】。

**间距**：通过元素相对比例估算 padding/gap 数值，以基准单位推测 scale。

**圆角**：观察按钮、卡片、输入框的圆角程度，映射到 sm/md/lg 等语义档位。

**阴影**：观察卡片/弹层的投影深度和扩散感，推测层次档位。

**动效**：截图无法观察动效，motion 类 token 全部标注 `null`，备注"静态截图，无法提取"。

**布局**：通过内容区宽度与视口的比例估算 maxWidth，观察栅格列数。

---

#### 策略 C：录屏输入

在截图策略基础上，额外关注：

**动效提取**（录屏独有）：
- 观察 hover / focus / 点击时的过渡效果，估算 duration（快/中/慢对应 ~100ms/200ms/350ms）
- 识别缓动类型：匀速（linear）、先快后慢（ease-out）、弹性（spring）
- 记录页面切换、弹层出现、列表加载等动画模式

**交互态补充**：
- 截取 hover 态、active 态、focus 态的截图帧，补充对应颜色/阴影变化
- 记录导航 sticky 行为、滚动视差等布局交互

**多帧综合**：如录屏包含多个页面，综合所有帧的信息，优先取出现频率最高的值作为基准 token。

---

### STEP 3 — 生成三份交付物

#### A · tokens.json

严格 JSON，7 大 token 类别 + meta（source / extracted / theme / style / **input\_type**）。

无法从源码读取的值：**合理推测填写**，以 `字段名_inferred` 备注推测依据。
颜色值（URL 输入）无法确认时保留 `null`，不得推测；截图/录屏输入的颜色允许视觉估算但必须备注。

```json
"meta": {
  "source": "截图文件名 或 URL",
  "input_type": "url | screenshot | screenrecording",
  "extracted": "YYYY-MM-DD",
  "theme": "light | dark | both",
  "style": "品牌风格关键词",
  "accuracy_note": "截图输入，所有 token 为视觉推测，建议结合源码验证"
},

"color.primary": "#3b82f6",
"color.primary_inferred": "截图视觉取色，按钮主色区域采样",

"motion.duration.base": null,
"motion.duration.base_inferred": "静态截图，无法提取"
```

**双主题（theme: "both"）时的颜色结构**：颜色 token 拆分为 `color.light.*` 和 `color.dark.*` 两组，非颜色 token（font/space/radius/shadow/motion/layout）保持单组不变。

```json
"color": {
  "light": {
    "primary": "#635bff",
    "bg.default": "#ffffff",
    "text.primary": "#0a2540"
  },
  "dark": {
    "primary": "#7c75ff",
    "bg.default": "#0a0a0a",
    "text.primary": "#f0f0f0"
  }
}
```

#### B · design.md

按以下章节输出（跟随用户语言）：
品牌概览 · 视觉调性 · 颜色系统 · 字体系统 · 间距系统 · 形态语言 · 动效规范 · 布局规范 · 组件规律 · 设计原则 · AI 使用说明

截图/录屏输入时，在文档开头加入精度声明：
```
> ⚠️ 本文档基于[截图/录屏]视觉分析生成，token 值为推测估算。
> 建议在获取源码后对照 TOKEN-SCHEMA.md 逐项校验。
```

AI 使用说明标准模板见 → `AI-USAGE-TEMPLATE.md`

#### C · preview.html

单文件，内嵌全部 CSS，无外部依赖，可直接浏览器打开。包含：
调色板色块 · 字阶展示 · 间距可视化 · Button / Input / Card / Badge / Nav 组件示例 · Hero section 模板。
所有样式值必须通过 CSS 变量引用（`:root { --color-primary: … }`）。

**双主题支持（theme: "both" 时必须实现）**：

在页面右上角固定显示切换按钮（Light / Dark），点击时切换 `<html>` 的 `data-theme` 属性，CSS 变量随之切换。默认展示 light 主题。

```css
/* 亮色（默认） */
:root, [data-theme="light"] {
  --color-primary: #635bff;
  --color-bg-default: #ffffff;
  --color-text-primary: #0a2540;
}
/* 暗色 */
[data-theme="dark"] {
  --color-primary: #7c75ff;
  --color-bg-default: #0a0a0a;
  --color-text-primary: #f0f0f0;
}
```

```js
// 切换逻辑
btn.addEventListener('click', () => {
  const html = document.documentElement;
  html.dataset.theme = html.dataset.theme === 'dark' ? 'light' : 'dark';
  btn.textContent = html.dataset.theme === 'dark' ? '☀️ Light' : '🌙 Dark';
});
```

调色板区块同步展示两套颜色对比（亮/暗各一行），其余组件随主题实时切换。

---

## 输出规范

**文件命名**：`{site-name}-tokens.json` · `{site-name}-design.md` · `{site-name}-preview.html`

**每步完成后汇报**：
```
✅ 颜色系统提取完成（17 个 token）
✅ 字体系统提取完成（基准 16px，8 阶 scale）
⚠️  动效系统：值已推测，见 _inferred 备注
📦 正在生成 3 份交付物…
```

**URL 无法访问时降级**：
1. 告知具体原因（403 / JS 渲染 / 空内容）
2. 尝试直接抓 CSS 文件（`/styles.css`、`/_next/static/css/`、`/app.css`）
3. 完全无法访问则询问用户是否提供截图作为替代输入

**质量底线**：7 类 token 必须全部覆盖；截图/录屏输入的推测值必须有 `_inferred` 备注；CSS 变量可直接复制使用。
