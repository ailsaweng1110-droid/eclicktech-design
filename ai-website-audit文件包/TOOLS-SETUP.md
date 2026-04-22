# 工具接入指南 — 在其他模型/平台上运行本 Skill

本文档说明如何将 `web_fetch` 和 `web_search` 替换为免费 API，
使本 Skill 可以在 Claude 以外的平台（Dify、Coze、OpenAI 等）运行。

---

## 两个工具的替代方案

| Claude 原生工具 | 替代 API | 免费额度 | 是否需要注册 |
|----------------|---------|---------|------------|
| `web_fetch(url)` | Jina Reader `r.jina.ai` | 无限制（有速率限制） | 不需要 |
| `web_search(query)` | Tavily Search API | 1,000次/月 | 需要（免费，无需信用卡） |

---

## Step 1：获取 API Key

### Tavily（web_search 替代）

1. 访问 [app.tavily.com](https://app.tavily.com) → 注册账户（支持 Google/GitHub 登录）
2. 登录后，Dashboard 首页即显示你的 API Key
3. Key 格式：`tvly-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
4. 免费额度：**每月 1,000 次搜索，无需信用卡**

### Jina Reader（web_fetch 替代）

**无需注册，直接使用：**

```
读取网页：https://r.jina.ai/https://example.com
搜索网页：https://s.jina.ai/your+search+query
```

可选：注册 [jina.ai](https://jina.ai) 获取 API Key 以提高速率限制
- 无 Key：20 次/分钟
- 有免费 Key：200 次/分钟

---

## Step 2：API 调用说明

### web_fetch 替代 — Jina Reader

**读取任意网页，返回 Markdown：**

```
GET https://r.jina.ai/{目标URL}
```

**示例：**
```
GET https://r.jina.ai/https://www.eclicktech.com.cn/
```

**带 API Key（提高速率）：**
```
GET https://r.jina.ai/https://example.com
Headers:
  Authorization: Bearer jina_xxxxxxxx
```

**返回格式：** Markdown 纯文本，干净无广告，与 Claude 的 `web_fetch` 输出基本一致

---

### web_search 替代 — Tavily

**POST https://api.tavily.com/search**

```json
{
  "api_key": "tvly-你的APIKey",
  "query": "易点天下 出海营销",
  "search_depth": "basic",
  "max_results": 5,
  "include_answer": true
}
```

**返回示例：**
```json
{
  "answer": "易点天下是一家...",
  "results": [
    {
      "title": "易点天下官网",
      "url": "https://www.eclicktech.com.cn",
      "content": "...",
      "score": 0.95
    }
  ]
}
```

**参数说明：**
- `search_depth`: `"basic"`（1 credit）或 `"advanced"`（2 credits）
- `include_answer`: `true` 时返回 AI 合成的摘要答案
- `max_results`: 建议 5～10

---

## Step 3：在各平台配置工具

### Dify

1. **插件市场** → 搜索 "Tavily" → 安装 → 填入 API Key
2. **自定义工具** → 新建 → 填入以下配置：

**Jina Reader 工具配置：**
```yaml
名称: web_fetch
方法: GET
URL: https://r.jina.ai/{{url}}
参数:
  - name: url
    type: string
    description: 要读取的网页 URL
    required: true
```

---

### Coze（扣子）

1. 进入 Bot 编辑页 → 工具 → 添加插件
2. 搜索 "Tavily" 或 "Jina" 插件直接接入
3. 或使用「HTTP 请求」工具手动配置上述接口

---

### OpenAI Function Calling / 自建应用

在 system message 或 tools 配置中声明以下函数：

```json
[
  {
    "type": "function",
    "function": {
      "name": "web_fetch",
      "description": "读取指定 URL 的网页内容，返回 Markdown 格式",
      "parameters": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "要读取的网页完整 URL，如 https://example.com"
          }
        },
        "required": ["url"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "web_search",
      "description": "搜索互联网，返回相关网页摘要",
      "parameters": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "搜索关键词"
          }
        },
        "required": ["query"]
      }
    }
  }
]
```

**工具调用处理逻辑（Python 示例）：**

```python
import requests

TAVILY_API_KEY = "tvly-你的Key"
JINA_API_KEY = "jina_你的Key"  # 可选

def handle_tool_call(tool_name, tool_input):
    if tool_name == "web_fetch":
        url = tool_input["url"]
        headers = {}
        if JINA_API_KEY:
            headers["Authorization"] = f"Bearer {JINA_API_KEY}"
        resp = requests.get(f"https://r.jina.ai/{url}", headers=headers)
        return resp.text

    elif tool_name == "web_search":
        query = tool_input["query"]
        resp = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "search_depth": "basic",
                "max_results": 5,
                "include_answer": True
            }
        )
        data = resp.json()
        # 格式化为文本返回给模型
        result = f"搜索答案：{data.get('answer', '')}\n\n"
        for r in data.get("results", []):
            result += f"标题：{r['title']}\n链接：{r['url']}\n摘要：{r['content'][:300]}\n\n"
        return result
```

---

## Step 4：报告生成（HTML/PDF）— 免费方案

| 功能 | Claude.ai | 其他平台 |
|------|-----------|---------|
| 网页抓取 | ✅ | ✅（Jina） |
| 搜索 | ✅ | ✅（Tavily） |
| 文字版诊断报告 | ✅ | ✅ |
| HTML 格式报告 | ✅ | ✅（见下方方案） |
| PDF 格式报告 | ✅ | ✅（见下方方案） |

---

### 方案一：浏览器打印（完全免费，无需任何配置）

**流程：** AI 输出 HTML 文本 → 保存为 `.html` 文件 → 浏览器打开 → `Ctrl+P` → 目标选"另存为 PDF"

**优点：** 零成本、无需注册、完全免费  
**缺点：** 需要手动操作，无法全自动化  
**适合：** 偶尔使用，不追求自动化的场景

---

### 方案二：WeasyPrint（完全免费，本地 Python 运行）

开源库，MIT 协议，**无使用次数限制，永久免费**。

**安装：**
```bash
pip install weasyprint

# macOS（需要先安装依赖）
brew install pango

# Ubuntu/Debian
apt install libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```

**使用：**
```python
from weasyprint import HTML

# 从 HTML 字符串生成 PDF
html_content = """..."""  # 诊断报告 HTML 内容
HTML(string=html_content).write_pdf("report.pdf")

# 从本地 HTML 文件生成 PDF
HTML(filename="report.html").write_pdf("report.pdf")
```

**中文支持：**

报告使用系统字体，需确保系统安装了中文字体：
```bash
# Ubuntu
apt install fonts-wqy-microhei fonts-noto-cjk

# macOS
# 系统自带，无需安装

# Windows
# 系统自带，无需安装
```

**优点：** 完全免费无限制，本地运行无隐私风险，支持中文  
**缺点：** 需要 Python 环境，复杂 CSS 渲染可能与 Chrome 有细微差异  
**适合：** 有 Python 环境的开发者，追求完全免费无限制

---

### 方案三：html2pdf.app API（100次/月免费）

**免费额度：** 100 credits/月，每个文件不超过 1MB  
**注册：** [html2pdf.app](https://html2pdf.app) → 免费注册获取 API Key  
**无需信用卡**

```python
import requests

API_KEY = "你的APIKey"
html_content = "..."  # 诊断报告 HTML 内容

resp = requests.post(
    "https://api.html2pdf.app/v1/generate",
    json={
        "html": html_content,
        "apiKey": API_KEY,
        "format": "A4",
        "margin": "14mm 16mm 14mm 16mm"
    }
)

with open("report.pdf", "wb") as f:
    f.write(resp.content)
```

**优点：** 无需本地安装，基于 Chromium 渲染质量好  
**缺点：** 每月 100 次限制  
**适合：** 偶尔使用，不想安装 Python 库

---

### 方案四：PDFShift（50次/月免费）

**免费额度：** 50 credits/月（每个文件不超过 5MB）  
**注册：** [pdfshift.io](https://pdfshift.io) → 免费注册，无需信用卡

```python
import requests, base64

API_KEY = "你的APIKey"
html_content = "..."

credentials = base64.b64encode(f"api:{API_KEY}".encode()).decode()

resp = requests.post(
    "https://api.pdfshift.io/v3/convert/pdf",
    headers={"Authorization": f"Basic {credentials}"},
    json={
        "source": html_content,
        "format": "A4",
        "margin": {"top": "14mm", "right": "16mm", "bottom": "14mm", "left": "16mm"}
    }
)

with open("report.pdf", "wb") as f:
    f.write(resp.content)
```

---

### 方案对比总结

| 方案 | 费用 | 次数限制 | 中文支持 | 自动化 | 推荐场景 |
|------|------|---------|---------|-------|---------|
| 浏览器打印 | 完全免费 | 无限制 | ✅ | ❌ 手动 | 偶尔用，不在乎操作 |
| WeasyPrint | 完全免费 | 无限制 | ✅（需装字体）| ✅ | 有 Python 环境的开发者 |
| html2pdf.app | 免费100次/月 | 100次 | ✅ | ✅ | 低频使用 |
| PDFShift | 免费50次/月 | 50次 | ✅ | ✅ | 低频使用 |

**推荐优先级：**
1. 个人用 → **浏览器打印**（零成本零配置）
2. 开发集成 → **WeasyPrint**（免费无限制）
3. 无 Python 环境 → **html2pdf.app**（100次/月够用）

---

## 费用估算

按每次诊断 6 次网络请求 + 1 次 PDF 生成计算：

| 工具 | 每次诊断用量 | 免费额度 | 可支持诊断次数 |
|------|------------|---------|--------------|
| Jina Reader | 4 次 fetch | 实际无限制 | 无限制 |
| Tavily Search | 2 次搜索 | 1,000次/月 | **500次诊断/月** |
| PDF 生成（WeasyPrint） | 本地运行 | 完全免费 | 无限制 |
| PDF 生成（html2pdf.app） | 1 次生成 | 100次/月 | 100次/月 |

**最省钱组合（完全免费）：**  
Jina Reader（无需Key）+ Tavily（免费1000次）+ WeasyPrint（本地免费）= **0元/月，无限制**

**最省事组合（无需安装任何东西）：**  
Jina Reader + Tavily + 浏览器打印 = 仅需注册 Tavily 一个账号

---

## 完整示例：在 Python 中运行 Skill

```python
import anthropic
import requests

client = anthropic.Anthropic(api_key="your-claude-api-key")
TAVILY_KEY = "tvly-你的Key"

def web_fetch(url):
    resp = requests.get(f"https://r.jina.ai/{url}", timeout=30)
    return resp.text[:8000]  # 限制长度

def web_search(query):
    resp = requests.post("https://api.tavily.com/search", json={
        "api_key": TAVILY_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 5,
        "include_answer": True
    })
    data = resp.json()
    result = data.get("answer", "") + "\n\n"
    for r in data.get("results", [])[:3]:
        result += f"[{r['title']}]({r['url']})\n{r['content'][:200]}\n\n"
    return result

# 读取 SKILL.md 作为 system prompt
with open("SKILL.md") as f:
    skill_content = f.read()

tools = [
    {"type": "function", "function": {
        "name": "web_fetch",
        "description": "读取网页内容返回 Markdown",
        "parameters": {"type": "object", "properties": {
            "url": {"type": "string"}}, "required": ["url"]}
    }},
    {"type": "function", "function": {
        "name": "web_search",
        "description": "搜索互联网",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string"}}, "required": ["query"]}
    }}
]

messages = [{"role": "user", "content": "/ai-website-audit https://www.example.com"}]

while True:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=skill_content,
        tools=tools,
        messages=messages
    )
    
    if resp.stop_reason == "end_turn":
        print(resp.content[0].text)
        break
    
    # 处理工具调用
    tool_results = []
    for block in resp.content:
        if block.type == "tool_use":
            if block.name == "web_fetch":
                result = web_fetch(block.input["url"])
            elif block.name == "web_search":
                result = web_search(block.input["query"])
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result
            })
    
    messages.append({"role": "assistant", "content": resp.content})
    messages.append({"role": "user", "content": tool_results})
```

---

*ai-website-audit Skill v3.1 · tools-setup.md*
