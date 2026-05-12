# Brand Token Overrides

`tokens.json` remains the shared base (core).

Each brand file defines overrides under:

- `overrides.light` / `overrides.dark` — 颜色、语义色等（与主题相关）
- `overrides.layout` — **间距 / 圆角（float，单位 px）**，与 Figma **`Brand`** 集合里的 **FLOAT 变量名**一致（`space/4`、`radius/sm` 等），按品牌维护
- `overrides.typography` — **字体语义**（`font.family.*` 为 **string**，字号 / 字重 / 行高为 **float**），与 Figma **`Brand`** 里 `font/family/*`、`font/size/*` 等变量对齐

**Figma 与本地 JSON 的明暗拆分**

- **Light（默认 UI）**：Figma 集合 **`Brand`**（四品牌 Mode）↔ `dist` 中 `light.semantic` + `layout` + `typography`。
- **Dark UI**：Figma 集合 **`Brand / Dark`**（同名语义 key、四品牌 Mode）↔ `brands/*.json` 里 **`dark.semantic`**（请与 Figma 保持同步；**以 Figma 为准**时，改 Figma 后需再导出或让我协助回写 JSON）。

**中性色色相策略（Light）**

| 品牌 | 中性灰倾向 | 说明 |
| --- | --- | --- |
| eclicktech | 蓝灰 | 与主色蓝系协调 |
| yeahmobi | 黄灰 | 与主色黄系协调 |
| cyberklick | 绿灰 | 与主色绿系协调 |
| zmaticoo | 无偏色灰 | 接近 Ant 中性灰刻度，不偏蓝黄绿 |

**阴影（Elevation）**

- Figma **Effect styles**：`elevation/hover`、`elevation/dropdown`、`elevation/modal`（Ant 风格占位，可后调）。
- **「层级」**常指 z-index + 阴影一起表达的前后关系；**「阴影」**是其中可见部分。组件里可约定：悬停用 hover、菜单/下拉用 dropdown、对话框用 modal。

合并后：`dist/<brand>.tokens.json` 顶层会有 `layout` 对象（与 `light` / `dark` 并列），例如 `layout["space/4"].value`；另有 `typography["font.size.sm"].value` 等。

## 与 Figma 对齐（快照）

1. 在 Figma `design-system-2026` 中确认 **Variables**（`Brand`、`Brand / Dark`）已更新。  
2. 使用 MCP / 插件导出解析后的变量，更新 `scripts/figma-variable-snapshot.json`（路径与命名与 Figma 一致）。  
3. 运行：

```bash
cd design-tokens
node scripts/apply-figma-snapshot-to-brands.mjs
node scripts/build-brand-tokens.js
```

**说明**：若 **`Brand / Dark`** 里中性色仍为占位 `#000000`，脚本会 **保留** `brands/*.json` 里已有的 `dark.semantic` 中性色，仅覆盖品牌色与状态色等已填写的变量。占位补全后请重新导出快照并再跑上述命令。

**说明**：`tokens.json` 里仍可能保留 Ant Design 导出的 `light.borderRadius` 等字段，属于历史结构；**新规范以 `layout` + `light.semantic` 为准**。

## Semantic tokens（组件优先使用）

**组件与业务样式只应读取** `light.semantic` / `dark.semantic` 下的 **点号语义 key**（`color.brand.primary` 等），不要直接依赖色阶名（如 `blue-7`）。

合并后的路径示例：`dist/eclicktech.tokens.json` → `light.semantic["color.brand.primary"]`。

### 当前约定的 key 列表

| Key | 含义 |
| --- | --- |
| `color.brand.primary` | 品牌主色 |
| `color.brand.primary.hover` | 主色悬停 |
| `color.brand.primary.active` | 主色按下 / 激活 |
| `color.brand.primary.bg` | 主色浅底 / 选中背景 |
| `color.status.link` | 链接色 |
| `color.status.success` | 成功 |
| `color.status.warning` | 警告 |
| `color.status.error` | 错误 |
| `color.neutral.text.title` | 标题文字 |
| `color.neutral.text.primary` | 正文主文字 |
| `color.neutral.text.secondary` | 次要文字 |
| `color.neutral.text.disabled` | 禁用文字 |
| `color.neutral.border` | 边框 |
| `color.neutral.divider` | 分割线 |
| `color.neutral.bg.base` | 页面 / 区块底色 |
| `color.neutral.bg.table-header` | 表头背景 |

## Palette overrides（可选，设计系统内部）

仍可在 `overrides.light` / `dark` 下覆盖 `Daybreak Blue` 等色板分组，与 Figma 变量对齐；**业务组件不要直接引用**。

## Build

```bash
cd design-tokens
node scripts/build-brand-tokens.js
```

输出：`dist/*.tokens.json`。
