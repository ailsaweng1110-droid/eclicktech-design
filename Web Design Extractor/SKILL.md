---
name: web-design-extractor
description: >
  当你需要分析网站、逆向工程其设计、提取外观风格或编写设计指南时自动触发。
  输入公共网站 URL，提取视觉调性、design token、排版布局与基础组件，
  输出 tokens.json、design.md 与 preview.html 三份交付物，供 AI 喂入学习参考。
  触发关键词：分析网站设计、提取设计规范、逆向设计系统、design token、design.md、
  复制某网站风格、参考某网站设计、帮我提取 xxx 的设计规范。
version: 1.0.0
---

# Web Design Extractor

抓取公共网站 → 提取设计 token → 输出三份交付物（tokens.json · design.md · preview.html）。

---

## 工作流（按序执行，不得跳步）

### STEP 1 — 告知进度

```
🔍 正在分析：{URL}
阶段 1/3：抓取页面信息…
```

### STEP 2 — 抓取与提取

用 `web_fetch` 抓取页面，从 HTML/CSS 中提取 7 大类 token：

**color · font · space · radius · shadow · motion · layout**

各类的完整字段清单见 → `TOKEN-SCHEMA.md`

提取优先级：CSS 变量（`:root` / `[data-theme]`）> 内联样式 > Tailwind class 反推。
框架特定技巧（shadcn、Tailwind、Ant Design 等）见 → `REFERENCE.md`

同时记录：
- 品牌调性：行业、受众、视觉风格、情绪关键词（3~5 个）
- 组件特征：Button / Input / Card / Nav / Badge 的 padding、radius、hover 规律

### STEP 3 — 生成三份交付物

#### A · tokens.json

严格 JSON，7 大 token 类别 + meta（source / extracted / theme / style）。

无法从源码读取的值：**合理推测填写**，并以 `字段名_inferred` 备注推测依据。
颜色值无法确认时保留 `null`，不得推测。

```json
"motion.duration.base": "200ms",
"motion.duration.base_inferred": "依据按钮 transition 观察值估算"
```

#### B · design.md

按以下章节输出（跟随用户语言）：
品牌概览 · 视觉调性 · 颜色系统 · 字体系统 · 间距系统 · 形态语言 · 动效规范 · 布局规范 · 组件规律 · 设计原则 · AI 使用说明

AI 使用说明的标准模板见 → `AI-USAGE-TEMPLATE.md`

#### C · preview.html

单文件，内嵌全部 CSS，无外部依赖，可直接浏览器打开。包含：
调色板色块 · 字阶展示 · 间距可视化 · Button / Input / Card / Badge / Nav 组件示例 · Hero section 模板。
所有样式值必须通过 CSS 变量引用（`:root { --color-primary: … }`）。

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

**无法访问时降级**：
1. 告知具体原因（403 / JS 渲染 / 空内容）
2. 尝试直接抓 CSS 文件（`/styles.css`、`/_next/static/css/`、`/app.css`）
3. 完全无法访问则生成空白模板，注明"需手动填写"

**质量底线**：7 类 token 必须全部覆盖；颜色值禁止凭空捏造；CSS 变量可直接复制使用。
