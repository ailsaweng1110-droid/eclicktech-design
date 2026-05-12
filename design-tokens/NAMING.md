# 包名与 Tag 命名规范（design-tokens）

本文档约定 **npm 包名**、**版本号** 与 **Git Tag** 的命名规则，便于设计、前端与 CI 对齐。可直接复制到飞书。

---

## 一、npm 包名（固定）


| 项         | 值                                                          |
| --------- | ---------------------------------------------------------- |
| **作用域包名** | `@eclicktech-design/tokens`                                |
| **说明**    | 与仓库根目录 `design-tokens/package.json` 中 `name` 一致；未经团队决议不改名。 |


子路径导出（研发引用时）：


| 导出路径                                   | 对应文件                               |
| -------------------------------------- | ---------------------------------- |
| `@eclicktech-design/tokens`            | 默认 → `dist/eclicktech.tokens.json` |
| `@eclicktech-design/tokens/eclicktech` | `dist/eclicktech.tokens.json`      |
| `@eclicktech-design/tokens/cyberklick` | `dist/cyberklick.tokens.json`      |
| `@eclicktech-design/tokens/yeahmobi`   | `dist/yeahmobi.tokens.json`        |
| `@eclicktech-design/tokens/zmaticoo`   | `dist/zmaticoo.tokens.json`        |


---

## 二、Git Tag 命名（发版 / Raw 锁版本）

**格式**：`tokens-v<主版本>.<次版本>.<修订号>`


| 段       | 何时递增                                | 示例              |
| ------- | ----------------------------------- | --------------- |
| **主版本** | 破坏性变更：语义 key 删除/重命名、结构大变、前端必须改代码才能接 | `tokens-v2.0.0` |
| **次版本** | 新增语义、新增品牌文件、Figma 对齐的大批色值更新         | `tokens-v1.1.0` |
| **修订号** | 小修正：个别色值、注释、文档、不影响已有 key 含义的微调      | `tokens-v1.0.1` |


**规则摘要**：

1. **前缀固定为 `tokens-v`**，与仓库内其他 Tag（若有）区分。
2. **禁止**改写已推送的 Tag；错误发版用**新版本号**纠正。
3. 每次对外宣布「前端可升级」时，**至少打一个 Tag** 指向已合并 `main` 且已包含最新 `dist/` 的提交。
4. **不要**用 `latest` 当正式环境唯一依据；生产环境 Raw URL **必须带具体 Tag**。

**Raw 示例**（将 `<TAG>` 替换为实际标签，如 `tokens-v1.0.0`）：

`https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/<TAG>/design-tokens/dist/eclicktech.tokens.json`

---

## 三、package.json 中的 version（npm 与 Tag 对齐）

1. 发 npm 包时：`package.json` 的 `version` 与 **语义化版本**一致，建议 **与 Tag 数字部分对齐**，例如 Tag `tokens-v1.2.3` ↔ `version` `1.2.3`。
2. 仅使用 **Tag + Raw**、不发 npm 时：仍建议在发版 PR 里 **顺手 bump `version`**，便于飞书公告与变更记录一致。

---

## 四、分支与日常提交（可选约定）


| 用途           | 建议名                                         |
| ------------ | ------------------------------------------- |
| 默认集成分支       | `main`                                      |
| Token 专项功能分支 | `tokens/<简述>`，例如 `tokens/add-info-semantic` |


日常小改可直接进 `main`；大改或多人并行时用分支 + PR，合并后再打 `tokens-v*`。

---

## 五、谁负责打 Tag

由团队在飞书**指定一人或角色**（例如「设计系统负责人」或「发版当周值班研发」）：合并含 `design-tokens/dist` 的提交后，按本节规则创建 Tag 并通知前端更新 Raw 或 npm 版本。

---

## 六、与 Figma 的对应关系（一句话）

**Figma Variables 为唯一事实来源**；本包内 `brands/*.json` 与 `dist/*.tokens.json` 为交付物；**Tag 表示「某时刻 Figma 已同步到 Git 的快照」**。