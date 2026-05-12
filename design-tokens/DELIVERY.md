# 设计系统 Token 交付说明（Figma + JSON）

> 本文档与仓库结构一致，可全文复制到飞书；维护时以 GitHub `design-tokens` 为准更新本节。

---

## 1. 目标

建立多品牌（eclicktech / cyberklick / yeahmobi / zmaticoo）可切换的设计 Token，支撑中后台与营销相关界面；研发侧同时对接 **Ant Design** 与 **Shadcn**（映射约定见 `MAPPING.md`，**实现代码**放在各前端或主题包仓库）。

---

## 2. 单一事实来源（SoT）

- **设计侧以 Figma Variables 为准**：颜色、间距、圆角、字体等由设计师在 Figma 内维护。  
- **研发数值交付物以仓库内 `design-tokens/dist/<品牌>.tokens.json` 为准**：由 `tokens.json` + `brands/<品牌>.json` 构建生成。  
- **Figma 与 JSON 冲突时，以 Figma 为准**，再更新 `brands` / 快照并重新 `build`（见 `brands/README.md`「与 Figma 对齐」）。

---

## 3. Figma 结构（`design-system-2026`）

- **`Brand`（Light）**  
  - **Mode**：eclicktech、cyberklick、yeahmobi、zmaticoo。  
  - **内容**：语义色（`color/...`）、间距/圆角（`space/*`、`radius/*`）、字体（`font/...`）、功能色占位（如 `color/status/info`）等。  
  - **中性色策略（Light）**：eclicktech 偏蓝灰；yeahmobi 偏黄灰；cyberklick 偏绿灰；zmaticoo 无偏色灰。  

- **`Brand / Dark`（Dark）**  
  - **Mode**：与 `Brand` 相同的四个品牌。  
  - **内容**：与 `Brand` **同名的颜色语义变量**，取值为 Dark 场景。若中性色在 Figma 中仍为占位（如纯黑），同步脚本会保留 JSON 中已有暗色中性值，直至 Figma 定稿后再覆盖。  

- **阴影（Elevation）**  
  - Effect styles：`elevation/hover`、`elevation/dropdown`、`elevation/modal`（可按 Ant 习惯微调）。  

- **「README for AI」页面**  
  - 供 AI 按固定顺序读取变量与规范；人类协作仍以 Variables + 本仓库为准。  

---

## 4. 仓库目录（当前约定）

仓库：**[eclicktech-design](https://github.com/ailsaweng1110-droid/eclicktech-design)**（`main` 分支）。**Token 包在仓库根目录下的 `design-tokens/`，与 `design-system/` 并列**（不再放在 `Web Design Extractor` 子路径内）。

```
eclicktech-design/
├── design-tokens/                      # ★ 多品牌 Token 包（主工作目录）
│   ├── README.md                       # 取用方式、构建命令
│   ├── DELIVERY.md                     # 本文件：飞书可同步的交付说明
│   ├── CONTRIBUTING.md                 # 设计协作与发版约定
│   ├── NAMING.md                       # npm 包名、Git Tag、version 命名
│   ├── MAPPING.md                      # 语义 Token → AntD / Shadcn 映射骨架（规范）
│   ├── tokens.json                     # 全品牌共用底座
│   ├── brands/
│   │   ├── README.md                   # 语义 key、Figma 对齐步骤
│   │   ├── eclicktech.json
│   │   ├── cyberklick.json
│   │   ├── yeahmobi.json
│   │   └── zmaticoo.json
│   ├── dist/                           # ★ 给前端的合并结果（按品牌）
│   │   ├── eclicktech.tokens.json
│   │   ├── cyberklick.tokens.json
│   │   ├── yeahmobi.tokens.json
│   │   └── zmaticoo.tokens.json
│   └── scripts/
│       ├── build-brand-tokens.js       # 生成 dist
│       ├── figma-variable-snapshot.json # 从 Figma 导出后的数值快照（可替换更新）
│       └── apply-figma-snapshot-to-brands.mjs # 快照 → 写回 brands/*.json
├── .github/
│   └── workflows/
│       └── design-tokens.yml           # 变更 design-tokens 时 CI 执行 build 校验
└── design-system/                      # Figma Skill、Web Design Extractor 等（与 design-tokens 独立）
    ├── README.md
    └── Web Design Extractor/
        └── …
```

**本地已删除的 `Documents/token` 仅作历史说明**：请勿再使用；**唯一维护路径为上述 `eclicktech-design/design-tokens`**。

---

## 5. 使用约定

- **组件与业务样式优先读语义**：`light.semantic` / `dark.semantic` 下的点号 key（与 Figma 语义一致）；**间距/圆角**读 `layout`；**字体**读 `typography`。  
- **不要**直接依赖色阶名（如 `blue-7`）作为对外组件 API（色阶仅供设计系统内部或与 Figma 色板对齐）。  

---

## 6. 与 Ant Design / Shadcn

- **`dist` 只提供数值与语义结构**，不内置框架主题。  
- **`MAPPING.md`**：约定「语义 key → Ant Design `theme.token` / Shadcn CSS 变量」的对照；随语义增减更新该表。  
- **落地代码**：在各**前端仓库**或 **`@scope/theme` 包**中实现（读取 `dist` + 按映射生成 `ConfigProvider` / `globals.css` 等）。  

---

## 7. 变更与发版流程

1. 设计师在 **Figma** 更新 Variables（必要时更新 Effect styles）。  
2. 更新 `scripts/figma-variable-snapshot.json`（或由工具从 Figma 再导出），在 `design-tokens` 目录执行：  
   `npm run sync:figma`（或先 `npm run apply:figma-snapshot` 再 `npm run build`）。  
3. **Commit + Push** 至 `main`；对外冻结版本时按 [NAMING.md](./NAMING.md) 打 **`tokens-v*`** Tag。  
4. 前端使用 **带 Tag 的 Raw URL** 或 npm 包引用对应版本。  
5. **飞书发版表**（可选）：记录 Tag、变更摘要、对齐 Figma 说明、发布人（见 CONTRIBUTING）。  

---

## 8. 无障碍

- 主色、功能色、中性色在 Light / Dark 下需满足目标对比度（建议正文与关键控件至少 **AA**，重要场景倾向 **AAA**）。  
- 设计师用对比度工具全量检查；研发在页面级抽检。  

---

## 9. 已知占位与后续

- `info` / `info-bg`、三档 elevation、**Brand / Dark 中性色**等若在 Figma 中仍为占位，以定稿后再次同步快照为准。  
- **AntD + Shadcn 自动生成脚本**可在映射稳定后由研发补充。  

---

## 10. 前端 Raw 链接模板（替换 `<TAG>`）

`https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/<TAG>/design-tokens/dist/eclicktech.tokens.json`

其余品牌将文件名替换为 `cyberklick.tokens.json`、`yeahmobi.tokens.json`、`zmaticoo.tokens.json` 即可。
