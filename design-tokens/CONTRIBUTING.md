# 设计 Token 协作说明

## 角色

- **单一事实来源**：Figma Variables（`Brand` / `Brand / Dark` 等约定集合）。  
- **本仓库 JSON**：与 Figma 同步的中间层；改 Figma 后由指定人或 AI 辅助回写 `brands/*.json`，再 `npm run build` 更新 `dist`。

## 3 位设计师分工建议

任选一种，团队定稿后写在飞书：

1. **按品牌 owner**：每人主责 1～2 个品牌的 Figma Mode + 对应 `brands/<brand>.json`（减少互相覆盖）。
2. **按职能**：颜色一人、版式字体一人、审核合并一人（适合 Figma 结构已很统一时）。
3. **按产品线**：若某产品强绑定某品牌，由该产品主设维护该品牌在 Figma 的变更，**合并 PR 前**由 DS 负责人做一致性检查。

## 提交流程（简版）

1. Figma 改完 → 飞书说明「变更摘要 + 影响品牌」。
2. 更新 `brands`（及必要时 `tokens.json`）→ 本地 `npm run build`。
3. 提交时 **同时包含** `brands` 与 `**dist`**（除非团队已约定 CI 只生成 dist）。
4. 合并 `main` 后，对本次可交付版本 **打 Tag**（如 `tokens-v0.2.0`），前端用 Raw 链接指向该 Tag。

## 不要做的事

- 不要只改 `dist` 不回写 `brands`（下次构建会丢）。  
- 不要在业务仓库里手改一份分叉的 JSON 当主源。