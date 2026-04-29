# SocialMedia-Growth-Operations

自媒体增长运营 Skill 套件，覆盖「素材采集 -> 内容撰写 -> 公众号排版」三阶段工作流。

## 目录结构

```text
SocialMedia-Growth-Operations/
├── README.md
├── ai-watch/
│   ├── README.md
│   ├── rules.md                       # 信息检索规则（给 AI 编辑用）
│   ├── feeds.opml                     # RSS 订阅源
│   ├── fetch.py                       # 自动采集脚本
│   └── com.eclicktech.ai-watch.plist  # 每周一 09:00 launchd 调度
├── media-content-writer/
│   ├── README.md
│   ├── SKILL.md
│   └── references/
│       └── case-library.md
└── media-formatter/
    ├── README.md
    ├── SKILL.md
    └── references/
        └── formatting-guide.md
```

## 三段式工作链路

### 0) ai-watch（采集前置，自动）

- 目标：每周一早 9 点（北京时间）从 RSS 源自动拉近 7 天素材
- 输出：`ai-watch/output/YYYY-WXX.md` 候选 Markdown
- 入口文档：`ai-watch/README.md`
- 检索规范：`ai-watch/rules.md`

### 1) media-content-writer

- 目标：把候选素材或人工选题转成可审阅文章草稿
- 输出：标题矩阵、公众号正文、可选小红书/LinkedIn 版本、配图建议
- 入口文档：`media-content-writer/SKILL.md`
- 参考资料：`media-content-writer/references/case-library.md`

详情见：`media-content-writer/README.md`

### 2) media-formatter

- 目标：把定稿正文转换为可直接粘贴到微信公众号后台的 HTML
- 输出：排版说明 + 完整 HTML（内联样式）
- 入口文档：`media-formatter/SKILL.md`
- 参考资料：`media-formatter/references/formatting-guide.md`

详情见：`media-formatter/README.md`

## 标准使用流程

1. `ai-watch` 自动跑出候选素材 Markdown
2. 在 `media-content-writer` 完成选题分析、出稿和多轮修改
3. 确认标题与正文定稿
4. 将定稿内容交给 `media-formatter` 进行 HTML 排版
5. 粘贴到公众号编辑器并补充图片后发布

## 维护说明

- 更新采集规则：改 `ai-watch/rules.md`
- 更新订阅源：改 `ai-watch/feeds.opml`
- 更新写作策略/栏目：改 `media-content-writer/SKILL.md`
- 更新案例参考：改 `media-content-writer/references/case-library.md`
- 更新排版规范：改 `media-formatter/references/formatting-guide.md`
- 调整排版执行逻辑：改 `media-formatter/SKILL.md`

---

维护团队：品牌公关部产品设计组
