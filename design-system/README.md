
# design-system Skills

基于 Figma MCP 的设计工作流技能包，包含三个协同工作的 Skill：

| Skill | 作用 | 方向 |
|-------|------|------|
| `design-spec-extractor-2B` | 从 Figma 截图或链接中**提取** B 端设计规范 | 设计稿 → 规范文档 |
| `web-design-extractor` | 抓取公共网站，**逆向提取**其设计 Token | 网站 URL → Token 文件 |
| `zmaticoo-design` | 将设计内容**写入** zMaticoo DSP Figma 文件 | AI 指令 → Figma 画布 |

三个 Skill 构成完整闭环：先用提取类 Skill 建立规范文档，再用 `zmaticoo-design` 携带规范向 Figma 写入新内容，确保每次输出都与现有设计系统保持一致。

---

## 目录结构

> 说明：多品牌设计 Token 包在**仓库根目录** [`../design-tokens`](../design-tokens/README.md)，与本 `design-system/` 目录并列。

```
design-system/
├── README.md                                    本文档
├── design-spec-extractor-2B/
│   ├── SKILL.md                                 B 端设计规范提取器（v4.1）
│   └── references/
│       ├── extraction-dimensions.md             提取维度说明
│       ├── framework-conversion.md              框架转换指南
│       └── raw-json-schema.md                   原始 JSON 数据结构
├── Web Design Extractor/
│   ├── SKILL.md                                 网站设计逆向提取器（v1.0）
│   ├── REFERENCE.md                             CSS 解析与提取技术参考
│   ├── TOKEN-SCHEMA.md                          Token 结构说明
│   ├── AI-USAGE-TEMPLATE.md                     AI 使用模板
│   └── examples/
│       ├── example-stripe-design.md             Stripe 设计示例
│       ├── example-stripe-preview.html          Stripe 预览页面
│       └── example-stripe-tokens.json           Stripe Token 示例
└── zmaticoo-design/
    ├── README.md                                zmaticoo-design 单独说明
    ├── SKILL.md                                 zMaticoo DSP 写入规范 Skill（v1.0）
    ├── install.sh                               一键安装脚本
    └── references/
        ├── DESIGN_SPEC.md                       完整设计规范文档
        └── tokens.css                           Design Token CSS 变量
```

---

## Skill 1：design-spec-extractor-2B

### 是什么

一个专为 B 端产品设计的**设计规范自动提取器**（v4.1）。输入 Figma 链接或截图，输出结构化的设计规范文档和可直接使用的 CSS Token 文件。

### 能做什么

- 通过 Figma MCP 直连读取设计文件，精度达到 1px / 1 色值
- 自动检测页面覆盖率，缺少关键页面时主动提醒补充
- 检测设计稿内部的规范不一致（如同一组件多种圆角值），上报并请求确认
- 输出 8 个维度的完整规范：颜色 / 字体 / 间距 / 圆角 / 边框 / 阴影 / 布局 / 适配规则
- 生成可直接注入 Claude Code / Cursor / v0 的 `:root` CSS Variables

### 适用场景

- 新项目启动，需要快速建立设计规范文档
- 设计稿更新后，同步规范文档
- 开发需要精确的 Token 数值时
- 设计评审前，自动生成规范一致性报告

### 使用方式

在 Claude Code 对话中直接触发，支持截图或 Figma 链接：

```
# 输入 Figma 链接
/design-spec-extractor-2B https://www.figma.com/design/xxxxxx/项目名?node-id=0-1

# 或上传截图后说
请提取这个设计稿的规范

# 或直接说
帮我总结这个 Figma 文件的色彩规范和字体规范
```

### 输出产物

| 文件 | 说明 |
|------|------|
| `raw.json` | 原始数据记录，含所有发现值和冲突检测 |
| `DESIGN_SPEC.md` | 结构化设计规范文档（8 个维度）|
| `tokens.css` | 通用 CSS Variables，可转换为任意框架格式 |

### 支持框架转换

提取完成后可按需转换：shadcn/ui · Tailwind CSS · Ant Design · Element Plus · Naive UI

---

## Skill 2：web-design-extractor

### 是什么

一个**网站设计逆向提取器**（v1.0）。输入公共网站 URL，自动抓取并分析其视觉设计，提取 Design Token、排版布局与基础组件风格，供 AI 喂入学习参考或复刻使用。

### 能做什么

- 抓取公共网站 HTML/CSS，提取 7 大类 Design Token
- 支持 CSS 变量、Tailwind class、内联样式等多种提取方式
- 识别 shadcn/ui、Tailwind、Ant Design 等主流设计框架的 token 模式
- 输出三份交付物，可直接供 AI 开发工具使用

### 适用场景

- 参考某网站的设计风格进行仿写
- 逆向分析竞品设计系统
- 快速复制某品牌的视觉调性
- 为新项目建立设计基准参考

### 使用方式

```
# 分析目标网站
分析 https://stripe.com 的设计风格

# 或直接触发
提取 xxx 网站的设计规范
帮我逆向分析这个网站的 design token
```

### 输出产物

| 文件 | 说明 |
|------|------|
| `tokens.json` | 结构化 Design Token，含颜色/字体/间距等 7 大类 |
| `design.md` | 设计规范文档，包含视觉调性和组件分析 |
| `preview.html` | 可视化预览页面，展示提取的 Token 效果 |

---

## Skill 3：zmaticoo-design

### 是什么

zMaticoo DSP 产品的**专属设计写入 Skill**（v1.0）。携带完整设计规范，通过 Figma MCP 的 `use_figma` 工具，直接向 Figma 画布写入符合规范的页面和组件。

### 能做什么

- 新建页面（导航、侧边栏、主内容区完整结构）
- 新增或修改组件（Modal、Drawer、表格、表单、Tag、Tooltip 等）
- 所有写入内容自动遵循 zMaticoo DSP 设计规范（颜色 / 字体 / 间距 / 圆角均精确匹配）
- 写入前自动读取周边节点作为参考，确保与现有页面风格一致

### 适用场景

- 新功能页面的初稿搭建
- 在已有页面中新增字段或组件
- 批量修改某类组件的样式
- 快速复制已有页面结构并调整内容

### 安装

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/main/design-system/zmaticoo-design/install.sh)
```

### 使用方式

```bash
# 启动 Claude Code
claude

# 验证 Figma MCP 已连接
/mcp

# 加载 skill 并描述需求
/figma-use /zmaticoo-design

在 https://www.figma.com/design/7da8NWsTXC3o0F5vHRjDfD/zMaticoo-DSP
模版画布里新建一个「用户详情页」，包含顶部导航、侧边菜单、主内容区卡片。
```

### 前置条件

- 已安装 Claude Code
- Figma 账号为 **Full seat**（Dev seat 无法写入已有文件）
- 对目标 Figma 文件有编辑权限
- 已执行 `claude plugin install figma@claude-plugins-official`

---

## 三个 Skill 的协作流程

```
  ┌─────────────────────────────────────────────────┐
  │              设计素材来源                         │
  │   Figma 设计文件  /  公共网站 URL                 │
  └───────────────┬─────────────────┬───────────────┘
                  │                 │
   ╔══════════════▼══╗         ╔════▼════════════════╗
   ║ design-spec-    ║         ║  web-design-        ║
   ║ extractor-2B    ║         ║  extractor          ║
   ║ Figma → 规范    ║         ║ 网站 URL → Token     ║
   ╚══════════════╤══╝         ╚════╤════════════════╝
                  │                 │
         ┌────────▼─────────────────▼────────┐
         │  DESIGN_SPEC.md / tokens.css       │
         │  tokens.json / design.md           │
         └────────────────┬──────────────────┘
                          │ 写入 references/
         ╔════════════════▼════════════════╗
         ║         zmaticoo-design         ║  ← Claude Code
         ║      携带规范 → 写入画布          ║
         ╚════════════════╤════════════════╝
                          │
         ┌────────────────▼────────────────┐
         │      Figma 画布（新页面/组件）     │
         └─────────────────────────────────┘
```

**典型工作流：**

1. 设计稿有更新 → 运行 `design-spec-extractor-2B` 重新提取规范
2. 将新生成的 `DESIGN_SPEC.md` 和 `tokens.css` 更新到 `references/` 目录
3. 团队成员执行 `update-zmaticoo-skill` 拉取最新规范
4. 在 Claude Code 中用 `/figma-use /zmaticoo-design` 按最新规范写入新内容

---

## 规范更新

设计规范变更时：

```bash
# 1. 重新提取规范（Figma 链接或截图）
/design-spec-extractor-2B https://www.figma.com/design/7da8NWsTXC3o0F5vHRjDfD/zMaticoo-DSP

# 2. 下载新的 DESIGN_SPEC.md 和 tokens.css，替换 references/ 目录下的文件

# 3. 推送到 GitHub
git add . && git commit -m "chore: 更新设计规范" && git push

# 4. 通知团队成员执行
update-zmaticoo-skill
```

---

## 常见问题

**Q：三个 Skill 分别在什么场景下用？**

- `design-spec-extractor-2B`：有 Figma 设计文件或截图，需要提取结构化规范文档时使用。
- `web-design-extractor`：需要参考某个公开网站的视觉风格，或逆向分析竞品设计时使用。
- `zmaticoo-design`：在 Claude Code 中，需要向 zMaticoo DSP Figma 文件写入新页面或组件时使用。

**Q：design-spec-extractor-2B 提取的规范精度如何？**

通过 Figma MCP 直连时精度最高，可达 1px / 1 色值。通过截图时依赖视觉识别，颜色和间距存在轻微估算误差。

**Q：zmaticoo-design 写入后样式不符合预期？**

在 prompt 中提供目标节点的 Figma 链接，让 Claude Code 先读取周边现有节点作为参考，写入结果会更准确。

**Q：web-design-extractor 能分析需要登录的网站吗？**

不能，只支持公开可访问的网站。需要登录鉴权的页面无法直接抓取。

**Q：design-spec-extractor-2B 可以用于其他产品吗？**

可以，它是通用的 B 端规范提取器，任何 B 端产品的 Figma 文件都可以使用。`zmaticoo-design` 是 zMaticoo DSP 专用的写入 Skill，其他产品需要单独建立对应的写入 Skill。

---

## 相关链接

- [zMaticoo DSP Figma 文件](https://www.figma.com/design/7da8NWsTXC3o0F5vHRjDfD/zMaticoo-DSP)
- [Figma MCP 官方文档](https://developers.figma.com/docs/figma-mcp-server/)
- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)
- [Figma Write to Canvas 文档](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)
