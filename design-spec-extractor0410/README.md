# design-spec-extractor

> B 端设计规范提取 Skill · v4.0

从设计稿截图或 Figma 链接中，自动提取完整的 B 端设计规范，并生成可直接注入 Claude / Cursor / v0 的 Design Token 代码块。

---

## 这个 Skill 能做什么

上传设计稿后，它会做三件事：

1. **检查完整性** — 对照内置的页面清单，判断设计稿是否覆盖了提取规范所需的关键页面，缺失时主动追问
2. **系统性提取** — 按 8 个维度扫描设计稿，输出结构化的规范文档，所有结果有具体数值，不允许模糊描述
3. **生成 Token** — 输出可直接粘贴进 AI 开发工具的 Design Token 代码块，减少设计到代码的翻译损耗

---

## 适用场景

专为 **B 端产品**设计，包括：

- 后台管理系统（Admin Panel）
- 数据平台 / BI 工具
- 企业级 SaaS 产品
- 内部运营工具
- 工业控制台 / 监控平台

> 遇到 SaaS 营销官网等灰色地带，Skill 会主动询问确认，不会自动触发。

---

## 安装方式

### 方式一：客户端安装（推荐，无需命令行）

适合不熟悉终端操作的设计师，在 AI 工具的图形界面里完成安装。

**Claude Code 桌面 App**
1. 打开 Claude Code App
2. 顶部菜单 → `Plugins` → `Discover`
3. 搜索 `design-spec-extractor`，点击 `Install`
4. 安装完成后在对话框输入 `/` 可见所有已安装 Skill

**Cursor**
1. 打开 Cursor → 左侧边栏点击 `Extensions`（插件图标）
2. 搜索 `design-spec-extractor`
3. 点击 `Install`，重启 Cursor 生效

**Windsurf**
1. 打开 Windsurf → 顶部菜单 `View` → `Extensions`
2. 搜索 `design-spec-extractor`，点击安装
3. 重启后自动生效

---

### 方式二：命令行安装（一行命令）

```bash
# Claude Code（推荐，自动检测工具并放到正确目录）
npx skills add design-spec-extractor

# 或手动指定工具
npx skills add design-spec-extractor --target cursor
npx skills add design-spec-extractor --target windsurf
```

---

### 方式三：手动安装（离线 / 私有化部署）

下载文件后，将 `design-spec-extractor/` 文件夹复制到对应目录：

```
# Claude Code（项目级，仅当前项目生效）
your-project/.claude/skills/design-spec-extractor/SKILL.md

# Claude Code（全局，所有项目生效）
~/.claude/skills/design-spec-extractor/SKILL.md

# Cursor
your-project/.cursor/skills/design-spec-extractor/SKILL.md

# Windsurf
your-project/.windsurf/skills/design-spec-extractor/SKILL.md
```

> 💡 推荐使用**全局安装路径**（`~/.claude/`），这样无论在哪个项目里都能直接使用，不需要每次重复安装。

---

安装完成后无需任何配置，上传设计稿并说"帮我提取设计规范"即可触发。

---

## 触发关键词

以下任意词语均可触发此 Skill：

`设计规范` `设计系统` `提取规范` `总结规范` `色彩规范` `字体规范` `组件规范` `Design Token` `设计稿` + `规范`

---

## 使用流程

### 第一步：上传设计稿

支持以下输入方式：
- 截图（PNG / JPG）
- Figma 分享链接
- 多张截图组合

### 第二步：选择处理方式（如设计稿不完整）

Skill 检测到缺失页面时，会暂停并给出三个选项：

| 选项 | 说明 | 适用情况 |
|------|------|---------|
| A. 补充设计稿 | 等你补充后再提取，结果最准确 | 有条件补充时优先选此项 |
| B. 跳过缺失 | 只提取已有页面的确认内容，缺失维度标注「待补充」 | 设计稿暂不完整，只需部分规范 |
| C. 推断性提取 | 基于现有页面的设计语言合理推断缺失内容，结果带「[推断]」标注和置信度 | 赶时间，需要完整框架但能接受部分估算 |

### 第三步：选择目标框架

Skill 会询问你的开发框架，以生成对应格式的变量：

| 选项 | 框架 |
|------|------|
| 1 | React + shadcn/ui |
| 2 | React + Tailwind CSS |
| 3 | React + Ant Design |
| 4 | Vue + Element Plus |
| 5 | Vue + Naive UI |
| 6 | 原生 CSS / CSS Variables |
| 7 | 其他 |

### 第四步：获取输出

输出包含两部分：

**① 结构化规范文档**（共 8 个维度）

```
颜色规范     — 品牌色、功能色、中性色，含全交互状态
文字规范     — 字体家族、字号层级、字重、行高
圆角规范     — 逐组件记录，识别步进规律
边框规范     — 粗细、样式、各状态色值
间距规范     — 基础单位、组件内/间距、页面级间距
阴影规范     — 各层级完整 CSS 值
排版布局     — 整体结构、栅格、表单、表格规范
适配规则     — 断点、最小宽度、移动端策略
```

**② Design Token 注入代码块**

```text
### 🛠️ UI Framework Context
### 🎨 Design Tokens（:root CSS Variables）
### 📐 Layout Heuristics
### 🎯 Execution Task
```

直接复制粘贴到 Claude / Cursor / v0 的对话框，作为新需求的上下文前缀使用。

---

## 推断性提取说明

选择选项 C 时，推断遵循以下规则：

- **必须有依据**：例如"根据登录页主按钮圆角 6px，推断输入框圆角同为 6px"
- **禁止无中生有**：无法推断的维度仍标注「待补充」，不填默认值
- **置信度三级**：
  - 高 — 同类组件直接参考
  - 中 — 跨组件类比
  - 低 — 跨页面泛化
- **文档顶部注明**：含推断内容的文档会在顶部加注"本规范含推断内容，建议补充设计稿后校验"

---

## shadcn/ui 特别说明

选择 React + shadcn/ui 框架时，CSS Variables 输出格式为 **HSL 裸值**（shadcn 的标准格式）：

```css
/* ✅ 正确：shadcn 格式 */
--primary: 221.2 83.2% 53.3%;

/* ❌ 错误：普通 CSS 格式 */
--primary: hsl(221.2, 83.2%, 53.3%);
--primary: #1677ff;
```

同时提示你同步更新 `tailwind.config.js` 中的颜色映射。

---

## 约束说明

Skill 内置以下硬性约束，不会因任何 prompt 绕过：

- 未在设计稿中出现的颜色，不会用框架默认值填充
- 所有输出必须有具体数值，不允许"浅蓝色"、"适中字号"等描述
- 圆角超过 12px 的值会被标注为「待确认」（B 端约束）
- 功能色 4 个（Success / Warning / Error / Info）必须全部提取，不允许遗漏
- 交互状态（Hover / Focus / Disabled / Error / Read-only）必须逐一覆盖

---

## 文件结构

```
design-spec-extractor/
├── README.md     — 本文档
└── SKILL.md      — Skill 主体（安装到 AI 工具后自动读取）
```

---

## 版本记录

| 版本 | 更新内容 |
|------|---------|
| v4.0 | 合并两版本；补全圆角/边框/阴影/适配 4 个维度；加入追问三选项（含推断性提取）；加入 shadcn/ui 支持；加入 Claude 注入工具；加入 B 端场景判断标准 |
| v3.1 | 加入 System Prompt Injection 输出格式；加入框架锁定；加入状态感知色彩 |
| v1.0 | 初版，基础 8 维度提取 |
