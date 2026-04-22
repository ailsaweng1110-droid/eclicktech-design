# 下载报告生成规范

> 本文件被 report-template.md 引用，定义如何在 Step 9 之后生成可下载的 PDF/HTML 报告。

---

## 核心规则

**Claude 沙箱环境中，所有 JS 触发下载（Blob URL / data URI）均被阻止。**
唯一可靠方案：用 `bash_tool` 生成文件 → 调用 `present_files` 提供下载链接。

---

## 生成流程

### Step 1：准备 HTML 内容

报告 HTML 已在 show_widget 中渲染。用 Python 写入到 `/home/claude/report_final.html`：
- 所有颜色必须硬编码为 hex（不得使用 `var(--color-*)` CSS 变量，离线打开后变量失效）
- 所有 h2 标题不加 emoji 前缀（使用纯文字）
- 表格/卡片内的状态符号使用内联 SVG 图标（不用 emoji，wkhtmltopdf 不支持彩色 emoji）
- 边框统一使用 hex（rgba() 在 wkhtmltopdf 中支持不稳定）

### Step 2：生成 PDF（推荐，使用 wkhtmltopdf）

```bash
# 先添加 PDF 专用 CSS
python3 << 'PYEOF'
html = open('/home/claude/report_final.html').read()
print_css = """
@page { size: A4; margin: 14mm 16mm 14mm 16mm; }
html, body { background: #FFFFFF !important; }
.page { max-width: 100%; padding: 0; }
body { font-family: "Noto Sans CJK SC", "WenQuanYi Micro Hei", sans-serif; }
* { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
h2, h3 { page-break-after: avoid; }
.sug, .card, .gw, .fc, .stbl { page-break-inside: avoid; }
.pb, .fs { max-height: none !important; overflow: visible !important; }
"""
html_pdf = html.replace('</style>', print_css + '</style>')
open('/home/claude/report_for_pdf.html', 'w').write(html_pdf)
PYEOF

# 生成 PDF
wkhtmltopdf \
  --page-size A4 --margin-top 14mm --margin-bottom 14mm \
  --margin-left 16mm --margin-right 16mm \
  --encoding utf-8 --no-stop-slow-scripts \
  --enable-local-file-access --quiet \
  /home/claude/report_for_pdf.html \
  /mnt/user-data/outputs/[域名]_AI诊断报告_v2.5.pdf
```

### Step 3：输出 HTML 并 present_files

```bash
cp /home/claude/report_final.html /mnt/user-data/outputs/[域名]_AI诊断报告_v2.5.html
```

然后调用 `present_files`，同时提供 PDF 和 HTML 两个文件。

---

## 颜色硬编码对照表

| 用途 | Hex 值 |
|------|--------|
| 页面背景 | `#F9F9F7` |
| 白色卡片（card）| `#FFFFFF` |
| 次级面板（secondary）| `#F5F5F2` |
| 三级面板（tertiary）| `#EFEEEA` |
| 主文字 | `#1C1C1A` |
| 次文字 | `#4A4A46` |
| 辅文字 | `#79786E` |
| 边框（通用）| `rgba(28,28,26,.14)` → 在白背景上 ≈ `#DEDEDC` |
| h2 分割线 | `#DDDCD8` |
| info 背景/边框 | `#E6F1FB` / `#B5D4F4` |
| danger 背景/边框 | `#FCEBEB` / `#F7C1C1` |
| warning 背景/边框 | `#FAEEDA` / `#FAC775` |
| success 背景/边框 | `#EAF3DE` / `#C0DD97` |
| info 文字 | `#185FA5` |
| danger 文字 | `#A32D2D` |
| warning 文字 | `#854F0B` |
| success 文字 | `#3B6D11` |

---

## SVG 图标参考（替代 emoji）

```html
<!-- ✅ 验证通过/一致 -->
<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#3B6D11" stroke-width="1.5" style="display:inline;vertical-align:middle">
  <path d="M4 8l3 3 5-5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>

<!-- ⚠ 警告/出入 -->
<svg width="12" height="12" viewBox="0 0 16 16" style="display:inline;vertical-align:middle">
  <path d="M8 2L14 13H2L8 2z" fill="#FAEEDA" stroke="#854F0B" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M8 6v4M8 12v.5" stroke="#854F0B" stroke-width="1.5" stroke-linecap="round"/>
</svg>

<!-- ❌ 错误/矛盾 -->
<svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="#A32D2D" stroke-width="1.5" style="display:inline;vertical-align:middle">
  <path d="M4 4l8 8M12 4l-8 8" stroke-linecap="round"/>
</svg>

<!-- 🔒 锁定/未抓取 -->
<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#79786E" stroke-width="1.5" style="display:inline;vertical-align:middle">
  <rect x="3" y="7" width="10" height="7" rx="1.5"/>
  <path d="M5 7V5a3 3 0 016 0v2" stroke-linecap="round"/>
</svg>

<!-- ⬜ N/A -->
<svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="#79786E" stroke-width="1.5" style="display:inline;vertical-align:middle">
  <rect x="2" y="2" width="12" height="12" rx="2"/>
</svg>

<!-- 〜 推断 -->
<svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="#854F0B" stroke-width="1.5" style="display:inline;vertical-align:middle">
  <path d="M3 8c1-3 3-3 4 0s3 3 4 0" stroke-linecap="round"/>
</svg>
```

---

## wkhtmltopdf 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| Emoji 变空白/方块 | Qt WebKit 不支持彩色 emoji | 所有 emoji 改为内联 SVG 图标 |
| 边框消失 | `rgba()` 支持不稳定 | 改为 hex 颜色 |
| 中文乱码 | 字体顺序错误 | `font-family: "Noto Sans CJK SC", sans-serif`（CJK 在前） |
| 背景色不打印 | 默认不打印背景 | 加 `-webkit-print-color-adjust: exact` |
| 滚动容器内容截断 | `max-height` + `overflow` 限制 | PDF CSS 中设 `max-height: none; overflow: visible` |
