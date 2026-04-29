# ai-watch · 易点事务所 AI 观察 自动化采集

每周一早 9:00（北京时间）自动跑 RSS 采集，按 4 大栏目汇总最近 7 天的候选素材，输出 Markdown 草稿，交给 AI 编辑后发公众号。

## 目录结构

```text
ai-watch/
├── README.md                          # 本文件
├── rules.md                           # 信息检索规则（给 AI 编辑用）
├── feeds.opml                         # RSS 订阅源（按 4 栏目分组）
├── fetch.py                           # 抓取 + 过滤 + 归类脚本
├── com.eclicktech.ai-watch.plist      # macOS launchd 调度配置
├── .venv/                             # Python 虚拟环境（已 gitignore）
├── output/                            # 每期生成的 Markdown 草稿（已 gitignore）
│   └── YYYY-WXX.md
└── logs/                              # 运行日志（已 gitignore）
```

## 完整工作链路

```text
launchd 周一 09:00 触发
  → fetch.py 拉 RSS、过滤 7 天内、按栏目归类
    → output/YYYY-WXX.md（候选素材，未筛选未翻译）
      → 你打开看一眼，丢给 AI 编辑
        → AI 按 rules.md 翻译、点评、排序、写 80–150 字描述
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

# 2) 手动跑一次确认能输出
.venv/bin/python fetch.py
ls output/

# 3) 安装 launchd 调度（每周一 09:00 北京时间触发）
cp com.eclicktech.ai-watch.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist
```

> 北京时间 = 系统本地时区（macOS 默认 Asia/Shanghai），plist 里写 09:00 即为北京 09:00。

## 常用命令

```bash
# 查看下一次运行计划
launchctl list | grep ai-watch

# 立即触发一次（不等周一）
launchctl start com.eclicktech.ai-watch

# 暂停 / 重新启用
launchctl unload ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist
launchctl load   ~/Library/LaunchAgents/com.eclicktech.ai-watch.plist

# 看日志
tail -f logs/launchd.out.log
tail -f logs/$(date +%Y-%m-%d).log
```

## 修改调度时间

编辑 `com.eclicktech.ai-watch.plist`，改 `StartCalendarInterval` 这段：

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

## 修改栏目关键词

编辑 `fetch.py` 顶部的 `CATEGORY_KEYWORDS` 字典即可。

## 故障排查

| 现象 | 排查 |
|---|---|
| 某栏 0 条 | 检查 `logs/YYYY-MM-DD.log` 看哪些源没抓到；OPML 里 RSS URL 可能改了 |
| launchd 不触发 | `launchctl list | grep ai-watch` 看 LastExitStatus；查 `logs/launchd.err.log` |
| pip 安装报权限错 | 不要用系统 pip，必须用 `.venv/bin/pip` |
| 时区不对 | 检查系统是否 Asia/Shanghai：`sudo systemsetup -gettimezone` |
