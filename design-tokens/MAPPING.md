# Token 映射表（设计 → 工程）

**状态**：骨架文档。数值以 Figma Variables 与 `dist/*.tokens.json` 为准；下列 **Ant Design / Shadcn 列**由研发在接库时填实，或后续用脚本从本表生成主题代码。

---

## 1. 命名桥接（Figma ↔ JSON）


| Figma Variable 路径（示例） | `dist` 内路径（示例）                                |
| --------------------- | --------------------------------------------- |
| `color/brand/primary` | `light.semantic["color.brand.primary"].value` |
| `color/status/info`   | `light.semantic["color.status.info"].value`   |
| `space/4`             | `layout["space/4"].value`                     |
| `radius/sm`           | `layout["radius/sm"].value`                   |


规则：**Figma 用 `/`，合并后语义色用 `.`；layout / typography 的 key 与 Figma 一致（含 `/`）。**

---

## 2. 语义色 → Ant Design 5 `theme.token`（待填）

在 `ConfigProvider` / `theme={{ token: { ... } }}` 中赋值时对照。下列为常见对应关系起点，**以你们最终 AntD 定制为准**。


| `light.semantic` key（`dist`）    | Ant Design `token` 键（建议）                 | 备注                 |
| ------------------------------- | ---------------------------------------- | ------------------ |
| `color.brand.primary`           | `colorPrimary`                           |                    |
| `color.brand.primary.hover`     | `colorPrimaryHover`                      |                    |
| `color.brand.primary.active`    | `colorPrimaryActive`                     |                    |
| `color.brand.primary.bg`        | `colorPrimaryBg` / `controlItemBgActive` | 择一或拆细              |
| `color.status.link`             | `colorLink`                              |                    |
| `color.status.success`          | `colorSuccess`                           |                    |
| `color.status.warning`          | `colorWarning`                           |                    |
| `color.status.error`            | `colorError`                             |                    |
| `color.status.info`             | `colorInfo`                              |                    |
| `color.status.info.bg`          | 自定义扩展或 `colorInfoBg`（若启用算法衍生）            | AntD 5 默认以算法为主，需约定 |
| `color.neutral.text.title`      | `colorTextHeading`                       |                    |
| `color.neutral.text.primary`    | `colorText`                              |                    |
| `color.neutral.text.secondary`  | `colorTextSecondary`                     |                    |
| `color.neutral.text.disabled`   | `colorTextDisabled`                      |                    |
| `color.neutral.border`          | `colorBorder`                            |                    |
| `color.neutral.divider`         | `colorSplit`                             |                    |
| `color.neutral.bg.base`         | `colorBgLayout` / `colorBgContainer`     | 按使用场景拆             |
| `color.neutral.bg.table-header` | `colorFillAlter` 或自定义                    |                    |


**Dark**：在 `algorithm: theme.darkAlgorithm` 下同样映射 `dark.semantic.*`，或单独 `theme.dark` 对象；与 Figma `**Brand / Dark`** 对齐后在此表加一列「Dark 说明」。

---

## 3. 语义色 → Shadcn / CSS 变量（待填）

Shadcn 习惯在 `:root` / `.dark` 下维护 `--background`、`--primary` 等。**下列为逻辑对应，变量名以项目 `globals.css` 为准。**


| `light.semantic` key         | Shadcn 语义（示例变量名）         | 备注              |
| ---------------------------- | ------------------------ | --------------- |
| `color.neutral.bg.base`      | `--background`           |                 |
| `color.neutral.text.primary` | `--foreground`           |                 |
| `color.brand.primary`        | `--primary`              |                 |
| （主色上的对比文字）                   | `--primary-foreground`   | 需对比度推导或单独 token |
| `color.neutral.border`       | `--border`               |                 |
| `color.status.error`         | `--destructive`          | 若对齐 danger      |
| `color.status.link`          | 常用 `--ring` 或单独 `--link` | 团队自定            |


**Layout / radius**：可映射到 Tailwind 扩展 `theme.extend.spacing` / `borderRadius`，或统一为 CSS 变量 `--radius`、`--space-`*。

---

## 4. 与「仅写基础 token」的关系

- **已完成**：语义结构 + 品牌 JSON + `dist` = **单一数值源**。  
- **仍缺**：上表 **AntD / Shadcn 列的定稿**（人工表即可，不必一开始就上脚本）；有表之后，再写 **生成脚本** 才不易返工。

---

## 5. 维护约定

1. 改 Figma → 更新 `brands` / `dist` → **再检查本表**是否需增删行。
2. 新增语义 key 时：**先**在 `brands/README.md` 登记含义，**再**在本表补两行（AntD + Shadcn）。
3. 本文件可拆为 `mapping/antd.md` + `mapping/shadcn.md`；当前先单文件便于飞书导出。