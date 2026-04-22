# 规范解构维度参考

> 提取时读取本文件，按以下 8 个维度逐一扫描设计稿。
> Token 必要性等级：`[必要]` 缺失阻塞输出 / `[推荐]` 缺失标注待补充 / `[可选]` 有对应页面才提取

---

## 1. 色彩系统

### 品牌色（来源：登录页、导航、任意含主操作的页面）

| Token | 等级 | 使用场景 |
|-------|------|---------|
| Primary 默认 | 必要 | 主按钮、激活状态、链接 |
| Primary Hover | 必要 | 主按钮悬停 |
| Primary Active | 必要 | 主按钮点击 |
| Primary Disabled | 必要 | 主按钮禁用，不可用中性色代替 |
| Primary Focus | 推荐 | 键盘焦点环 |
| Primary Light | 推荐 | 选中行、激活背景浅底色 |
| Secondary | 推荐 | 次级操作色 |

### 功能色（来源：任意含状态反馈的页面）

必须逐一识别，禁止遗漏。每种功能色提取三个变体：

| 功能色 | 默认 | Hover | Light（背景用） | 等级 |
|--------|------|-------|----------------|------|
| Success | # | # | # | 必要（默认）/ 推荐（Hover/Light） |
| Warning | # | # | # | 必要（默认）/ 推荐（Hover/Light） |
| Error / Danger | # | # | # | 必要（默认）/ 推荐（Hover/Light） |
| Info | # | # | # | 必要（默认）/ 推荐（Hover/Light） |

### 中性色 · 背景（来源见各行说明）

| Token | 等级 | 来源页面 |
|-------|------|---------|
| bg-page | 必要 | 登录页 |
| bg-card | 必要 | 任意含卡片页面 |
| bg-sidebar | 必要 | 主导航 / 侧边栏 |
| bg-topbar | 必要 | 主导航 / 顶部导航 |
| bg-hover | 必要 | 数据列表页（行 hover） |
| bg-selected | 必要 | 数据列表页（选中行） |
| bg-disabled | 必要 | 表单页（禁用输入框） |
| bg-modal | 推荐 | 弹窗 / Modal |
| bg-tag | 推荐 | 任意含标签的页面 |
| bg-code | 可选 | 含代码展示的页面 |

### 中性色 · 边框（来源：表单页为主）

| Token | 等级 | 状态说明 |
|-------|------|---------|
| border-default | 必要 | 默认边框 |
| border-hover | 必要 | 悬停 |
| border-focus | 必要 | 聚焦（来源：表单页） |
| border-disabled | 必要 | 禁用（来源：表单页） |
| border-error | 必要 | 错误校验（来源：表单页） |
| border-readonly | 推荐 | 只读（来源：详情页） |

### 中性色 · 文字

| Token | 等级 | 使用场景 |
|-------|------|---------|
| text-primary | 必要 | 主要文字 |
| text-secondary | 必要 | 次要文字 |
| text-disabled | 必要 | 禁用文字 |
| text-placeholder | 必要 | 占位符（来源：表单页） |
| text-inverse | 推荐 | 深色背景上的反色文字 |
| text-link | 推荐 | 链接色（有时独立于 primary） |

### 中性色 · 其他

| Token | 等级 | 说明 |
|-------|------|------|
| divider | 必要 | 分割线 |
| overlay | 推荐 | 弹窗蒙层（来源：弹窗页面） |

### 图表色板（来源：Dashboard / 数据概览页，可选页面）

提取 `--color-chart-1` 到 N，以及 `--color-chart-positive`（正向）和 `--color-chart-negative`（负向）。
全部为 `[可选]`，无 Dashboard 页面时整组跳过。

---

## 2. 文字排版系统（来源：任意页面）

**字体家族**

| Token | 等级 | 说明 |
|-------|------|------|
| font-family-base | 必要 | 中英文主字体 |
| font-family-mono | 可选 | 等宽字体（代码/数字） |
| font-family-data | 可选 | 数据大字专用（来源：Dashboard） |

最小字号限制：B 端不低于 12px。

**字号层级**

| Token | 等级 | 使用场景 |
|-------|------|---------|
| font-size-xs | 必要 | 辅助文字、时间戳 |
| font-size-sm | 必要 | 次要正文、标签 |
| font-size-base | 必要 | 主要正文、表格内容 |
| font-size-md | 必要 | 模块标题、表格表头 |
| font-size-lg | 必要 | 页面标题 |
| font-size-xl | 可选 | 数据大字（来源：Dashboard） |
| font-size-2xl | 可选 | 超大数据展示（来源：Dashboard） |

**字重与行高**

| Token | 等级 |
|-------|------|
| font-weight-regular (400) | 必要 |
| font-weight-medium (500) | 必要 |
| font-weight-bold (600) | 推荐 |
| line-height-base | 必要 |
| line-height-tight | 推荐 |
| line-height-loose | 推荐 |

---

## 3. 圆角系统

逐组件记录，识别是否存在步进规律（如 2/4/6/8px）。
⚠️ B 端约束：> 12px 为异常值，标注「待确认」。

| 组件 | 对应 Token | 等级 |
|------|-----------|------|
| 标签 Tag / Badge | radius-xs | 推荐 |
| Tooltip / Popover | radius-sm | 推荐 |
| 按钮 / 输入框 | radius-md | 必要 |
| 卡片 / 面板 | radius-lg | 必要 |
| 弹窗 Modal | radius-xl | 推荐（来源：弹窗页面） |
| 圆形元素（头像等） | radius-full (9999px) | 推荐 |

---

## 4. 边框系统

```
边框粗细：[N]px（B 端通常为 1px）
边框样式：实线 / 虚线 / 无（用背景色区分）

表格边框规则：
  横向边框：是 / 否
  纵向边框：是 / 否
  外边框：是 / 否

分割线：
  颜色：# → 对应 --color-divider
  粗细：[N]px
  样式：实线 / 虚线
```

---

## 5. 间距系统

**基础步进单位**：识别是 4px 还是 8px（所有间距值均应为整数倍）

**组件内间距 Padding（来源：表单页 / 列表页）**

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

**组件间间距 Gap（来源：表单页 / 列表页）**

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

**页面级间距（来源：主导航页面）**

```
页面内容区水平 Padding → --layout-content-padding-x
页面内容区顶部 Padding → --layout-content-padding-y
面包屑区域高度 → --layout-breadcrumb-height
```

---

## 6. 阴影系统

逐层级提取，记录完整 CSS box-shadow 值：

| 层级 | Token | 等级 | 使用场景 |
|------|-------|------|---------|
| 无阴影 | shadow-none | 必要 | 普通卡片、表格行 |
| 轻阴影 | shadow-sm | 推荐 | 卡片 Hover、固定表头 |
| 中阴影 | shadow-md | 推荐 | 下拉菜单、Tooltip |
| 重阴影 | shadow-lg | 推荐 | Modal、Drawer（来源：弹窗页面） |
| 内阴影 | shadow-inset | 可选 | 输入框内阴影 |

B 端阴影特征：颜色浅、偏移小，常见格式：`0 2px 8px rgba(0,0,0,0.12)`

---

## 7. 排版布局系统（来源：主导航 / 侧边栏页面）

**整体框架结构**

```
布局模式：左侧边栏 + 顶部导航 / 纯顶部导航 / 混合
侧边栏展开宽度 → --layout-sidebar-width      [必要]
侧边栏收起宽度 → --layout-sidebar-collapsed   [推荐]
顶部导航高度   → --layout-topbar-height       [必要]
内容区最大宽度：[N]px 或 无限制
面包屑：有 / 无
```

**栅格系统**

```
列数：12 / 24 / 其他
Gutter（列间距）：[N]px
响应式断点：有 / 无
```

**表单规范（来源：表单页）**

```
标签对齐方式：顶部对齐 / 左对齐 / 右对齐
标签宽度：[N]px 或 自适应
必填标记位置：标签前 * / 标签后 *
校验提示位置：输入框下方 / 右侧
单行表单列数：1 / 2 / 3
```

**表格规范（来源：数据列表页）**

```
行高-标准密度 → --layout-table-row-height      [必要]
行高-紧凑密度 → --layout-table-row-height-sm   [推荐]
斑马纹：有 / 无（奇偶行背景色）
固定列：操作列固定右侧 / 不固定
操作项间距：[N]px
空状态高度：[N]px
分页位置：右下角 / 居中
```

---

## 8. 适配规则

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
