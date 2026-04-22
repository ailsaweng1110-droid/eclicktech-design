# zmaticoo-design

zMaticoo DSP 设计规范 Skill，用于在 Claude Code 中通过 Figma MCP 向 zMaticoo DSP Figma 文件写入设计页面和组件。

---

## 文件结构

```
zmaticoo-design/
├── README.md              本文档
├── SKILL.md               Skill 主文件，包含完整设计规范和写入规则
├── install.sh             一键安装脚本
└── references/
    ├── DESIGN_SPEC.md     完整设计规范文档（颜色/字体/间距/组件）
    └── tokens.css         Design Token CSS 变量
```

---

## 前置条件

使用前确认以下条件已满足：

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Figma 账号为 **Full seat**（Dev seat 无法写入已有文件）
- 对目标 Figma 文件有**编辑权限**
- 已在 Claude Code 中安装 Figma Plugin：

```bash
claude plugin install figma@claude-plugins-official
```

---

## 安装

### 方式一：一键安装（推荐）

在终端执行以下命令，skill 会自动安装到全局目录 `~/.claude/skills/`：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/main/zmaticoo-design/install.sh)
```

### 方式二：手动安装

```bash
# 创建目录
mkdir -p ~/.claude/skills/zmaticoo-design/references

# 下载文件
curl -fsSL https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/main/zmaticoo-design/SKILL.md \
  -o ~/.claude/skills/zmaticoo-design/SKILL.md

curl -fsSL https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/main/zmaticoo-design/references/DESIGN_SPEC.md \
  -o ~/.claude/skills/zmaticoo-design/references/DESIGN_SPEC.md

curl -fsSL https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/main/zmaticoo-design/references/tokens.css \
  -o ~/.claude/skills/zmaticoo-design/references/tokens.css
```

---

## 使用方式

### 第一步：启动 Claude Code

```bash
cd 你的项目目录
claude
```

### 第二步：验证 Figma MCP 已连接

```
/mcp
```

看到 `✔ figma  connected` 即可。

### 第三步：调用 skill

```
/figma-use /zmaticoo-design

在 https://www.figma.com/design/7da8NWsTXC3o0F5vHRjDfD/zMaticoo-DSP
模版画布里新建一个「用户详情页」，包含顶部导航、侧边菜单、主内容区。
```

> `/figma-use` 是 Figma 官方写入 skill，必须在 `/zmaticoo-design` 前加载。

---

## 使用示例

**新建页面**
```
/figma-use /zmaticoo-design
在模版画布里新建一个 Campaign 列表页，包含顶部导航、表格、分页组件。
```

**修改已有节点**
```
/figma-use /zmaticoo-design
找到 node-id 4112:68305（Add balance Modal），
在 Account 行下方插入 Fund type 单选字段，选项为 Cash（默认）和 Coupon。
```

**查询规范**
```
/zmaticoo-design
Modal 组件的 footer 内边距和按钮排列规范是什么？
```

---

## 规范更新

设计规范有变更时：

1. 在此 repo 中更新对应文件（`SKILL.md` / `DESIGN_SPEC.md` / `tokens.css`）
2. 提交并推送到 GitHub
3. 通知团队成员执行更新命令：

```bash
update-zmaticoo-skill
```

> `update-zmaticoo-skill` 命令在首次执行 `install.sh` 时自动注册，无需额外配置。

---

## 设计规范概览

| 维度 | 核心值 |
|------|--------|
| 主品牌色 | `#0251FF` |
| 主按钮/深色 | `#262626` |
| 导航背景 | `#001366` |
| 字体 | Montserrat |
| 主圆角 | 4px（按钮/输入框）|
| Modal 圆角 | 2px |
| Modal 宽度 | 640px |
| Drawer 宽度 | 800px |
| 表格行高 | 55px（双行）/ 47px（单行）|
| 按钮尺寸 | 40px / 32px / 24px |

完整规范见 [DESIGN_SPEC.md](./references/DESIGN_SPEC.md)，Design Token 见 [tokens.css](./references/tokens.css)。

---

## 常见问题

**Q：执行 `/zmaticoo-design` 提示找不到 skill？**

确认 Claude Code 是在包含 `.claude/` 目录的项目里启动的，或 skill 已安装到全局 `~/.claude/skills/`。

**Q：写入 Figma 时提示权限不足？**

确认 Figma 账号是 Full seat，且对目标文件有编辑权限。Dev seat 只能在 Drafts 中写入。

**Q：字体写入报错？**

`use_figma` 脚本中所有文字节点创建前必须先执行 `await figma.loadFontAsync()`，Claude Code 在加载本 skill 后会自动处理。

**Q：写入后样式不符合规范？**

在 prompt 中明确说明"遵循 zMaticoo DSP 设计规范"，并提供目标节点的 Figma 链接，让 Claude Code 先读取周边节点作为参考。
