# design-spec-extractor-2B · 输出示例

> 以下为一个虚构的 B 端 SaaS 产品「DataFlow 数据平台」的完整提取输出示例。
> 输入源：Figma MCP 直连，已分析页面：登录页、主导航、列表页、表单页、详情页。

---

## 示例一：design.md

```markdown
# DataFlow 数据平台 设计规范

> 提取自：Figma MCP（DataFlow-Design/Main）· 生成时间：2026-04-16 · 工具：design-spec-extractor-2B v4.1
> ⚠️ 本规范含推断内容（标注 [推断]），建议补充 Dashboard 页面后校验图表色板

## 概述

- 产品类型：B 端数据平台
- 目标设备：桌面端，最小宽度 1280px
- 布局模式：左侧边栏 + 顶部导航
- 设计密度：标准密度（High Information Density）
- 组件库：待确认（建议 shadcn/ui 或 Ant Design）

## 色彩系统

### 品牌色

| Token | 值 | 使用场景 |
|-------|----|---------|
| `--color-primary` | `#1677FF` | 主按钮、激活状态、链接 |
| `--color-primary-hover` | `#4096FF` | 主按钮悬停 |
| `--color-primary-active` | `#0958D9` | 主按钮点击 |
| `--color-primary-disabled` | `#91CAFF` | 主按钮禁用 |
| `--color-primary-focus` | `#BAD4FF` | 键盘焦点环 |
| `--color-primary-light` | `#E8F4FF` | 选中行、激活背景 |
| `--color-secondary` | `#6B7280` | 次级操作 |

### 功能色

| Token | Default | Hover | Light |
|-------|---------|-------|-------|
| Success | `#52C41A` | `#73D13D` | `#F6FFED` |
| Warning | `#FAAD14` | `#FFC53D` | `#FFFBE6` |
| Error | `#FF4D4F` | `#FF7875` | `#FFF2F0` |
| Info | `#1677FF` | `#4096FF` | `#E8F4FF` |

### 中性色 · 背景

| Token | 值 | 使用场景 |
|-------|----|---------|
| `--color-bg-page` | `#F5F7FA` | 整体页面底色 |
| `--color-bg-card` | `#FFFFFF` | 卡片、面板 |
| `--color-bg-sidebar` | `#001529` | 侧边栏背景 |
| `--color-bg-topbar` | `#FFFFFF` | 顶部导航 |
| `--color-bg-hover` | `#F0F4FF` | 列表行悬停 |
| `--color-bg-selected` | `#E8F4FF` | 选中行 |
| `--color-bg-disabled` | `#F5F5F5` | 禁用区域 |
| `--color-bg-tag` | `#F0F0F0` | 标签背景 |

### 中性色 · 边框 / 文字 / 其他

（略，见 tokens.css）

### 图表色板

> ⚠️ **[待补充]** — 缺少 Dashboard 页面，图表色板无法提取

## 文字排版

- 中文主字体：`PingFang SC, HarmonyOS Sans, sans-serif`
- 英文/数字字体：同上（未单独配置）
- 最小字号：12px

| 层级 | 字号 | 字重 | 行高 | 使用场景 |
|------|------|------|------|---------|
| 页面标题 H1 | 20px | 500 | 28px | 页面大标题 |
| 模块标题 H2 | 16px | 500 | 24px | 卡片标题 |
| 正文 Body | 14px | 400 | 22px | 表格内容 |
| 辅助文字 Caption | 12px | 400 | 20px | 时间戳、提示 |
| 按钮文字 | 14px | 500 | — | 各类按钮 |
| 表格表头 | 14px | 500 | 22px | Table Header |

## 间距系统

- 基础步进单位：`8px`
- `--spacing-xs: 4px` / `--spacing-sm: 8px` / `--spacing-md: 16px`
- `--spacing-lg: 24px` / `--spacing-xl: 32px` / `--spacing-2xl: 48px`

## 圆角 · 阴影

| Token | 值 | 组件 |
|-------|----|------|
| `--radius-sm` | 4px | 标签、Tooltip |
| `--radius-md` | 6px | 按钮、输入框 |
| `--radius-lg` | 8px | 卡片、面板 |
| `--radius-xl` | [推断] 12px | 弹窗（置信度：中）|

## 布局规范

- 侧边栏展开宽度：`240px`
- 侧边栏收起宽度：`64px`
- 顶部导航高度：`56px`
- 内容区水平内边距：`24px`
- 表格行高（标准）：`48px`
- 表格行高（紧凑）：`40px`

## 动效

- `--duration-fast: 100ms` / `--duration-base: 200ms` / `--duration-slow: 300ms`
- `--easing-standard: cubic-bezier(0.4, 0, 0.2, 1)`

## 待补充项汇总

| Token | 原因 |
|-------|------|
| `--color-chart-1~5` | 缺少 Dashboard 页面 |
| `--color-chart-positive/negative` | 缺少 Dashboard 页面 |
| `--font-size-xl/2xl` | 缺少数据大字使用场景 |
| `--radius-xl` | 弹窗页面未提供，当前为推断值 |
| `--color-overlay` | 弹窗页面未提供 |
```

---

## 示例二：tokens.json（节选）

```json
{
  "color": {
    "primary": {
      "$value": "#1677FF",
      "$type": "color",
      "$description": "主按钮、激活状态、链接 [必要]"
    },
    "primary-hover": {
      "$value": "#4096FF",
      "$type": "color",
      "$description": "主按钮悬停 [必要]"
    },
    "primary-disabled": {
      "$value": "#91CAFF",
      "$type": "color",
      "$description": "主按钮禁用 [必要]"
    },
    "success": {
      "$value": "#52C41A",
      "$type": "color",
      "$description": "成功状态 [必要]"
    },
    "warning": {
      "$value": "#FAAD14",
      "$type": "color",
      "$description": "警告状态 [必要]"
    },
    "error": {
      "$value": "#FF4D4F",
      "$type": "color",
      "$description": "错误状态 [必要]"
    },
    "bg-page": {
      "$value": "#F5F7FA",
      "$type": "color",
      "$description": "整体页面底色 [必要]"
    },
    "bg-sidebar": {
      "$value": "#001529",
      "$type": "color",
      "$description": "侧边栏背景 [必要]"
    },
    "bg-hover": {
      "$value": "#F0F4FF",
      "$type": "color",
      "$description": "列表行悬停背景 [必要]"
    },
    "text-primary": {
      "$value": "#1F2937",
      "$type": "color",
      "$description": "主要文字 [必要]"
    },
    "text-secondary": {
      "$value": "#6B7280",
      "$type": "color",
      "$description": "次要文字 [必要]"
    },
    "text-disabled": {
      "$value": "#9CA3AF",
      "$type": "color",
      "$description": "禁用文字 [必要]"
    },
    "chart-1": {
      "$value": null,
      "$type": "color",
      "$description": "[待补充] 缺少 Dashboard 页面，图表色板无法提取"
    }
  },
  "spacing": {
    "unit": { "$value": "8px", "$type": "dimension", "$description": "基础步进单位" },
    "xs":   { "$value": "4px",  "$type": "dimension" },
    "sm":   { "$value": "8px",  "$type": "dimension" },
    "md":   { "$value": "16px", "$type": "dimension" },
    "lg":   { "$value": "24px", "$type": "dimension" },
    "xl":   { "$value": "32px", "$type": "dimension" },
    "2xl":  { "$value": "48px", "$type": "dimension" }
  },
  "radius": {
    "sm": { "$value": "4px",  "$type": "dimension" },
    "md": { "$value": "6px",  "$type": "dimension" },
    "lg": { "$value": "8px",  "$type": "dimension" },
    "xl": { "$value": "12px", "$type": "dimension", "$description": "[推断·置信度:中] 弹窗圆角，弹窗页面未提供" }
  },
  "shadow": {
    "sm": { "$value": "0 1px 4px rgba(0,0,0,0.08)",  "$type": "shadow" },
    "md": { "$value": "0 2px 8px rgba(0,0,0,0.12)",  "$type": "shadow" },
    "lg": { "$value": "0 4px 16px rgba(0,0,0,0.16)", "$type": "shadow" }
  },
  "font": {
    "family-base": { "$value": "PingFang SC, HarmonyOS Sans, sans-serif", "$type": "fontFamily" },
    "size-xs":   { "$value": "12px", "$type": "dimension" },
    "size-sm":   { "$value": "12px", "$type": "dimension" },
    "size-base": { "$value": "14px", "$type": "dimension" },
    "size-md":   { "$value": "16px", "$type": "dimension" },
    "size-lg":   { "$value": "20px", "$type": "dimension" }
  },
  "layout": {
    "sidebar-width":       { "$value": "240px", "$type": "dimension" },
    "sidebar-collapsed":   { "$value": "64px",  "$type": "dimension" },
    "topbar-height":       { "$value": "56px",  "$type": "dimension" },
    "table-row-height":    { "$value": "48px",  "$type": "dimension" },
    "table-row-height-sm": { "$value": "40px",  "$type": "dimension" }
  }
}
```

---

## 示例三：preview.html（结构说明）

> 完整 HTML 文件为单文件，内联所有样式，可直接双击在浏览器中打开。
> 以下展示页面各区块的核心 HTML 结构，供参考。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>DataFlow 设计规范预览</title>
  <style>
    /* 所有 Token 以 CSS Variables 形式内联 */
    :root {
      --color-primary: #1677FF;
      --color-primary-hover: #4096FF;
      --color-bg-page: #F5F7FA;
      --color-bg-card: #FFFFFF;
      --color-bg-sidebar: #001529;
      --color-text-primary: #1F2937;
      --color-text-secondary: #6B7280;
      --color-success: #52C41A;
      --color-warning: #FAAD14;
      --color-error: #FF4D4F;
      --spacing-md: 16px;
      --radius-md: 6px;
      --shadow-md: 0 2px 8px rgba(0,0,0,0.12);
      /* ... 所有 Token */
    }
    body { background: var(--color-bg-page); font-family: PingFang SC, sans-serif;
           color: var(--color-text-primary); padding: 32px; }
    .section { background: var(--color-bg-card); border-radius: var(--radius-lg);
               padding: 24px; margin-bottom: 24px; box-shadow: var(--shadow-sm); }
    .section-title { font-size: 16px; font-weight: 500; margin-bottom: 16px;
                     border-bottom: 1px solid #f0f0f0; padding-bottom: 8px; }
    /* 色板 */
    .swatch-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
    .swatch { width: 80px; text-align: center; }
    .swatch-block { height: 48px; border-radius: var(--radius-md); margin-bottom: 4px; }
    .swatch-label { font-size: 11px; color: var(--color-text-secondary); }
    /* 待补充高亮 */
    .pending { border: 2px dashed #FF4D4F; border-radius: var(--radius-md);
               padding: 12px; background: #FFF2F0; }
    .pending-icon { color: #FF4D4F; margin-right: 6px; }
  </style>
</head>
<body>

  <!-- Header -->
  <div style="margin-bottom:32px">
    <h1 style="font-size:24px;font-weight:500">DataFlow 数据平台 · 设计规范预览</h1>
    <p style="color:var(--color-text-secondary);font-size:13px">
      提取自 Figma MCP · 2026-04-16 · design-spec-extractor-2B v4.1
    </p>
    <button onclick="copyTokens()"
      style="background:var(--color-primary);color:#fff;border:none;
             padding:8px 16px;border-radius:var(--radius-md);cursor:pointer">
      复制 tokens.css
    </button>
  </div>

  <!-- 品牌色 -->
  <div class="section">
    <div class="section-title">品牌色</div>
    <div class="swatch-row">
      <div class="swatch">
        <div class="swatch-block" style="background:var(--color-primary)"></div>
        <div class="swatch-label">primary<br>#1677FF</div>
      </div>
      <div class="swatch">
        <div class="swatch-block" style="background:var(--color-primary-hover)"></div>
        <div class="swatch-label">hover<br>#4096FF</div>
      </div>
      <!-- ... 其余状态色块 -->
    </div>
  </div>

  <!-- 功能色 -->
  <div class="section">
    <div class="section-title">功能色</div>
    <!-- Success / Warning / Error / Info 各三色展示 -->
  </div>

  <!-- 文字排版 -->
  <div class="section">
    <div class="section-title">文字排版</div>
    <p style="font-size:20px;font-weight:500;margin:8px 0">
      H1 页面标题 20px / 500
    </p>
    <p style="font-size:16px;font-weight:500;margin:8px 0">
      H2 模块标题 16px / 500
    </p>
    <p style="font-size:14px;font-weight:400;margin:8px 0">
      正文 Body 14px / 400 — 一二三四五六七八九十
    </p>
    <p style="font-size:12px;color:var(--color-text-secondary);margin:8px 0">
      辅助文字 Caption 12px / 400
    </p>
  </div>

  <!-- 间距预览 -->
  <div class="section">
    <div class="section-title">间距（基础单位 8px）</div>
    <!-- 各 spacing 变量对应色块宽度 -->
  </div>

  <!-- 阴影预览 -->
  <div class="section">
    <div class="section-title">阴影</div>
    <div style="display:flex;gap:24px">
      <div style="width:120px;height:80px;border-radius:var(--radius-md);
                  box-shadow:var(--shadow-sm);background:var(--color-bg-card);
                  display:flex;align-items:center;justify-content:center;font-size:12px">
        shadow-sm
      </div>
      <div style="width:120px;height:80px;border-radius:var(--radius-md);
                  box-shadow:var(--shadow-md);background:var(--color-bg-card);
                  display:flex;align-items:center;justify-content:center;font-size:12px">
        shadow-md
      </div>
    </div>
  </div>

  <!-- 待补充项汇总 -->
  <div class="section">
    <div class="section-title" style="color:#FF4D4F">⚠ 待补充项（4 项）</div>
    <div class="pending" style="margin-bottom:8px">
      <span class="pending-icon">!</span>
      <strong>--color-chart-1~5</strong> — 缺少 Dashboard 页面，图表色板无法提取
    </div>
    <div class="pending" style="margin-bottom:8px">
      <span class="pending-icon">!</span>
      <strong>--color-overlay</strong> — 缺少弹窗页面
    </div>
    <!-- ... 其余待补充项 -->
  </div>

  <script>
    function copyTokens() {
      const tokens = `/* DataFlow Design Tokens */\n:root {\n  --color-primary: #1677FF;\n  /* ... */\n}`;
      navigator.clipboard.writeText(tokens);
      alert('tokens.css 已复制到剪贴板');
    }
  </script>
</body>
</html>
```

---

## 输出文件结构总览

```
your-project/
├── .design-spec-extractor/
│   └── raw.json                  ← 过程文件，原始数据，供回溯
└── design-system/
    ├── tokens.css                ← 通用 CSS Variables，框架无关
    ├── tokens.json               ← W3C Design Token 格式，供工具消费
    ├── design.md                 ← 人类可读的设计规范文档
    └── preview.html              ← 可视化预览，双击即开
    （以下按需生成）
    ├── globals.css               ← shadcn/ui 框架专属
    ├── tailwind.config.js        ← Tailwind / shadcn 专属
    ├── theme.ts                  ← Ant Design 专属
    ├── el-variables.css          ← Element Plus 专属
    └── themeOverrides.ts         ← Naive UI 专属
```
