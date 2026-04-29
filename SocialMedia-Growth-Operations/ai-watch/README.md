# ai-watch · 易点事务所 AI 观察 自动化采集

每周一早 9:00（北京时间）自动跑 RSS 采集，按 4 大栏目汇总最近 7 天的候选素材，输出 Markdown 草稿 + 推送到飞书多维表，交给 AI 编辑后发公众号。

## 目录结构

```text
ai-watch/
├── README.md                          # 本文件
├── rules.md                           # 信息检索规则（给 AI 编辑用）
├── feeds.opml                         # RSS 订阅源（按 4 栏目分组）
├── fetch.py                           # 抓取 + 过滤 + 归类 + 推飞书
├── com.eclicktech.ai-watch.plist      # macOS launchd 调度配置
├── .env.example                       # 配置模板（推 GitHub）
├── .env                               # 本地真实配置（已 gitignore）
├── .venv/                             # Python 虚拟环境（已 gitignore）
├── output/                            # 每期生成的 Markdown 草稿（已 gitignore）
│   └── YYYY-WXX.md
├── state/                             # 推送幂等状态（已 gitignore）
│   └── YYYY-WXX.json
└── logs/                              # 运行日志（已 gitignore）
```

## 完整工作链路

```text
launchd 周一 09:00 触发
  → fetch.py 拉 RSS、过滤 7 天内、按栏目归类
    → output/YYYY-WXX.md（候选素材，未筛选未翻译）
    → 同步推送到飞书多维表（每栏 Top 8 条，按来源重要性排序）
      → 你在飞书表里改"重要性 / 状态 / 备注"做筛选
        → AI 按 rules.md 翻译、点评、写 80–150 字描述
          → 你审稿
            → AI 用 media-formatter skill 输出 HTML
              → 你粘贴到公众号后台发布
```

## 首次安装步骤

仓库克隆下来之后，本机执行：

```bash
cd ~/Documents/eclicktech-design/SocialMedia-Growth-Operations/ai-watch

# 1) 建虚拟环境并安装依赖
/usr/bin/python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install feedparser

# 2) 配置环境变量
cp .env.example .env
# 用编辑器把 FEISHU_WEBHOOK_URL 填进去

# 3) 测试飞书联路
.venv/bin/python fetch.py --test-feishu
# 去飞书表看一条 [联路自检] 开头的记录是否出现

# 4) 手动跑一次完整流程
.venv/bin/python fetch.py
ls output/        # 看 Markdown 草稿
ls state/         # 看推送状态记录

# 5) 安装 launchd 调度（每周一 09:00 北京时间触发）
cp com.eclicktech.ai-watch.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist
```

> 北京时间 = 系统本地时区（macOS 默认 Asia/Shanghai），plist 里写 09:00 即为北京 09:00。

## .env 配置项

```ini
# 飞书 Base webhook（自动化 → 接收到 Webhook 时 → 复制）
FEISHU_WEBHOOK_URL=https://janzlz0n1f.feishu.cn/base/automation/webhook/event/xxxxx

# 每个栏目最多推飞书多少条候选（防止刷爆免费版自动化额度）
MAX_PER_CATEGORY=8

# 推送间隔（秒），防止触发飞书限速
PUSH_DELAY_SECONDS=0.5

# 时间窗口（天）
WINDOW_DAYS=7
```

## 飞书表字段约定

`fetch.py` 推送的 JSON payload 字段如下：

| Webhook 字段 | 飞书表列名 | 字段类型 |
|---|---|---|
| `issue` | 期数 | 文本 |
| `category` | 栏目 | 单选（4 个值） |
| `title` | 标题 | 文本 |
| `published_at` | 发布日期 | 日期（YYYY-MM-DD） |
| `summary` | 描述 | 多行文本 |
| `url` | 原文链接 | 超链接 |
| `source` | 来源 | 文本 |
| `importance` | 重要性 | 数字（1–5） |

`importance` 由 fetch.py 按来源自动评分：5=旗舰一手（OpenAI / Anthropic / Stratechery / Lenny），4=主流厂商或垂直媒体，3=其他个人/二手解读。

## 常用命令

```bash
# 立即触发一次完整流程（手动测试用）
.venv/bin/python fetch.py

# 只生成 Markdown，不推飞书
.venv/bin/python fetch.py --no-feishu

# 单独验证飞书联路
.venv/bin/python fetch.py --test-feishu

# 让 launchd 立即触发（不等周一）
launchctl start com.eclicktech.ai-watch

# 查看是否注册成功
launchctl list | grep ai-watch

# 暂停 / 恢复
launchctl unload ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist
launchctl load   ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist

# 看日志
tail -f logs/launchd.out.log
tail -f logs/$(date +%Y-%m-%d).log
```

## 修改调度时间

编辑 `com.eclicktech.ai-watch.plist`：

```xml
<key>StartCalendarInterval</key>
<dict>
  <key>Weekday</key>
  <integer>1</integer>      <!-- 0=Sun, 1=Mon, ... 6=Sat -->
  <key>Hour</key>
  <integer>9</integer>
  <key>Minute</key>
  <integer>0</integer>
</dict>
```

改完务必重新 `launchctl unload` + `launchctl load`，否则不会生效。

## 修改信息源

编辑 `feeds.opml`，按现有结构在对应栏目分组下加一行：

```xml
<outline type="rss" text="名称" title="名称"
         xmlUrl="https://example.com/feed.xml"
         htmlUrl="https://example.com/" />
```

## 修改栏目关键词与来源评分

编辑 `fetch.py` 顶部：

- `CATEGORY_KEYWORDS` — 栏目关键词
- `SOURCE_IMPORTANCE` — 来源重要性评分

## 推送幂等机制

每周首次推送会在 `state/YYYY-WXX.json` 记录已推送的 URL 列表。同一周再次运行（无论手动还是 launchd 重复触发），已推过的链接会自动跳过，**不会在飞书产生重复记录**。

## 故障排查

| 现象 | 排查 |
|---|---|
| 某栏 0 条 | 检查 `logs/YYYY-MM-DD.log` 看哪些源没抓到；OPML 里 RSS URL 可能改了 |
| 飞书 HTTP 200 但表里没记录 | 飞书自动化字段映射没配好，或自动化没启用 |
| 飞书报 4xx/5xx | webhook 地址被改 / 自动化被删 / 当月免费额度耗尽 |
| launchd 不触发 | `launchctl list \| grep ai-watch` 看 LastExitStatus；查 `logs/launchd.err.log` |
| pip 安装报权限错 | 不要用系统 pip，必须用 `.venv/bin/pip` |
| 时区不对 | 检查系统是否 Asia/Shanghai：`sudo systemsetup -gettimezone` |
