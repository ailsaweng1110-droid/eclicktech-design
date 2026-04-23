# Web Design Extractor

> 分析网站设计 → 提取 Design Token → 输出三份可直接使用的交付物

---

## 简介

**Web Design Extractor** 是一个 AI 驱动的设计规范提取工具，能够从网站 URL、截图或录屏中自动逆向提取 Design Token，生成标准化的设计文档和预览页面，供团队复用或喂入 AI 工具参考。

触发关键词：分析网站设计 · 提取设计规范 · 逆向设计系统 · design token · 复制某网站风格 · 帮我提取 xxx 的设计规范

---

## 支持的输入类型

| 输入类型 | 判断方式 | 数据来源 | 精度 |
|---------|---------|---------|------|
| **URL** | 用户提供网址 | HTML/CSS 源码直接解析 | 高 |
| **截图** | 上传图片（JPG / PNG / WebP） | 视觉观察，颜色 / 字体 / 间距为推测值 | 中 |
| **录屏** | 上传视频（MP4 / MOV / GIF） | 逐帧视觉分析，可捕捉交互态与动效 | 中（含动效） |

---

## 提取的 Token 类别

提取目标涵盖 **7 大类** Design Token：

| Token 类别 | 说明 |
|-----------|------|
| `color` | 主色、背景色、文字色、语义色（danger / success / warning / info）等 |
| `font` | 字体族、字阶（xs → 4xl）、字重、行高、字间距 |
| `space` | 基准单位（4px / 8px），间距 scale（space.0 → space.24） |
| `radius` | 无圆角 → 全圆角，语义档位（none / sm / md / lg / full） |
| `shadow` | 五级阴影（sm → 2xl），从微投影到强浮层 |
| `motion` | 过渡时长档位、缓动函数（ease / spring / enter / exit） |
| `layout` | 最大宽度、栅格列数、间距、响应式断点 |

完整字段定义见 → [`TOKEN-SCHEMA.md`](./TOKEN-SCHEMA.md)

---

## 输出交付物

每次提取完成后生成三份文件：

### 1. `{site-name}-tokens.json`
严格 JSON 格式，包含全部 7 类 token + meta 信息（来源 / 提取日期 / 主题 / 风格 / 精度说明）。
- 支持双主题：`color.light.*` / `color.dark.*` 分组输出
- 无法确认的推测值统一加 `_inferred` 字段备注依据

### 2. `{site-name}-design.md`
人类可读的设计规范文档，按以下章节组织：
品牌概览 · 视觉调性 · 颜色系统 · 字体系统 · 间距系统 · 形态语言 · 动效规范 · 布局规范 · 组件规律 · 设计原则 · AI 使用说明

AI 使用说明模板见 → [`AI-USAGE-TEMPLATE.md`](./AI-USAGE-TEMPLATE.md)

### 3. `{site-name}-preview.html`
单文件自包含预览页，无外部依赖，直接浏览器打开。内容包括：
- 调色板色块展示
- 字阶与字体展示
- 间距可视化
- 组件示例：Button / Input / Card / Badge / Navigation
- Hero Section 模板

支持亮/暗主题切换（`data-theme` 属性驱动，右上角切换按钮）。

---

## 工作流程

```
用户输入（URL / 截图 / 录屏）
       ↓
STEP 1：识别输入类型，输出进度提示
       ↓
STEP 2：按对应策略提取 7 类 token
  ├── URL     → 解析 CSS 变量 > 内联样式 > Tailwind 反推
  ├── 截图    → 视觉观察推测，所有值加 _inferred 备注
  └── 录屏    → 截图策略 + 动效帧分析（duration / easing）
       ↓
STEP 3：生成三份交付物
  ├── tokens.json
  ├── design.md
  └── preview.html
```

提取框架特定技巧（shadcn/ui、Tailwind、暗色模式等）见 → [`REFERENCE.md`](./REFERENCE.md)

---

## 质量标准

- 7 类 token 必须全部覆盖，不得缺项
- 截图 / 录屏输入的所有推测值必须附 `_inferred` 备注，说明推测依据
- `preview.html` 中所有样式值通过 CSS 变量引用，可直接复制使用
- URL 无法访问时，自动降级尝试直接抓取 CSS 文件；完全失败时提示用户切换为截图输入

---

## 文件结构

```
Web Design Extractor/
├── README.md              # 本文件，项目总览
├── SKILL.md               # AI Skill 定义，含完整工作流与输出规范
├── REFERENCE.md           # 技术参考：CSS 解析规则、框架适配、常见问题
├── TOKEN-SCHEMA.md        # Token 字段清单，生成 tokens.json 时对照使用
├── AI-USAGE-TEMPLATE.md   # AI 使用说明模板，附入 design.md 末尾
└── examples/              # 示例输出文件
```

---

## 推荐配合使用的 AI 工具

Claude · Cursor · GitHub Copilot · v0.dev · Lovable

将生成的 `design.md` 或 `tokens.json` 喂入以上工具，可快速生成与品牌视觉一致的 UI 代码，无需手动查阅设计稿。
