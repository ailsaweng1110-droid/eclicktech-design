# UI 验收助手 Skill

官网 UI 验收助手，用于对照 **Figma / 设计图** 与 **线上页面**，逐元素走查 UI 还原、响应式与交互状态，并将确认问题写入 **飞书多维表格** 或其他文档格式。

定位：**提效助手，不替人拍板**。负责走查、对照、留证、录入；美学终审与发布决策仍由人完成。

## 能做什么

- 单页验收：每次提供一个 Figma 画板链接
- 整文件批量验收：所有待验画板放在一个 Figma 文件里，自动按顺序逐个验收
- 多端视口：PC / 平板 / 移动端
- 交互补充画板：Footer、表单等 hover / 点击态一并验收
- 动态内容边界：新闻、案例、客户 logo 等 CMS 模块默认只验样式，不因内容/顺序与设计静态稿不同而报问题（除非指令明确要求对内容验收）
- 飞书交付：一项目一表，结构可复用团队验收模板

## 安装（Cursor）

```bash
git clone https://github.com/ailsaweng1110-droid/eclicktech-design.git
cp -r eclicktech-design/ui-acceptance-assistant ~/.cursor/skills/ui-acceptance-assistant
```

重启 Cursor 或新开 Agent 会话后，Skill 会在你提到「验收官网」「UI 验收」「对比 Figma」等场景时自动加载。

也可复制到项目级目录：

```bash
mkdir -p .cursor/skills
cp -r ui-acceptance-assistant .cursor/skills/ui-acceptance-assistant
```

## 依赖能力

| 能力 | 用途 | 不可用时的降级 |
|------|------|----------------|
| Figma MCP / API | 读取设计稿结构、截图 | 使用设计稿导出图 |
| 浏览器自动化 | 打开线上页、截图、读 DOM | Playwright / 手动截图 |
| 飞书 `lark-cli` | 写入多维表格 | 输出 CSV / Markdown / JSON |

## 使用前准备

1. **设计稿**：优先 Figma；也支持 PNG / JPG 导出图
2. **画板规范**：一页一板，命名含页面名 + 语言 + 端类型（如 `EC-首页-M端-中文`）
3. **官网 URL**：可访问的测试/预发/正式地址
4. **飞书表**：每个项目单独一张验收表；新项目按团队模板新建
5. **授权**：Figma 可读、飞书 Base 可写、`lark-cli auth login` 已完成

## 目录结构

```
ui-acceptance-assistant/
├── SKILL.md          # Skill 主文件（Agent 读取）
├── README.md         # 安装与使用说明
└── assets/           # 说明用示意图
    ├── ui-acceptance-workflow.png
    └── ui-acceptance-compare-sample.png
```

## 飞书字段约定（摘要）

- `问题描述`：给前端看的「现在是什么 + 设计要什么」
- `所属模块`：`{一级页面}-{语言}-{端}`
- `UI验收是否通过`：默认留空
- `需人工复核`：仅证据不足时勾选
- `问题截图`：一图一问题，红框准确

完整规则见 `SKILL.md`。

## 参考项目

本 Skill 在真实官网 UI 验收项目中投入使用，可与「EC 官网 UI 验收走查」飞书表结构对齐使用。

## 许可与维护

团队内部使用。规则变更请直接修改 `SKILL.md` 并提交 PR，避免只记在对话里。
