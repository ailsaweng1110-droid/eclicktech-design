# 下载报告生成规范

> 本文件被 report-template.md 引用，定义如何在 Step 9 之后生成可下载的 PDF/HTML 报告。

---

## 按平台分支执行

### 方案 A：Claude.ai（有 bash_tool）

**在 Claude.ai 平台**：沙箱环境中所有 JS 触发下载（Blob URL / data URI）均被阻止。**此方案唯一可靠做法**：用 `bash_tool` 生成文件 → 调用 `present_files` 提供下载链接。

#### 流程
1. 将报告 HTML 写入 `/home/claude/report_final.html`
2. 添加 PDF 专用 CSS，写入 `/home/claude/report_final_pdf.html`
3. 使用 wkhtmltopdf 转 PDF
4. 同时复制两个文件到 `/mnt/user-data/outputs/`
5. 调用 `present_files`（Claude.ai 专有工具），同时提供 HTML 和 PDF 两个文件

---

### 方案 B：其他平台（无 bash_tool）

**无法服务器端生成 PDF，改为"纯 HTML 输出 + 引导用户本地转换"。**

#### 流程
1. 将完整 HTML（含所有 inline CSS）输出到对话中，用 ```html 代码块包裹
2. 告知用户以下三个步骤：
   - 复制代码块内容
   - 保存为 `{网站名}_AI诊断报告.html` 文件
   - 浏览器打开后按 Ctrl+P，目标选"另存为 PDF"即可得到 PDF 版本
3. llms.txt 和 ai-page.md 同样用 ```text 代码块输出，告知用户复制保存

**可选增强**：若平台接入了 PDFShift / html2pdf.app 等第三方 PDF API，可在本地代码中直接调用生成 PDF 并返回下载链接（详见 TOOLS-SETUP.md）。

---

## 两个平台共用的 HTML 生成规范

无论在哪个平台，生成的 HTML 都必须遵循：

- 所有颜色硬编码为 hex（不得使用 `var(--color-*)` CSS 变量，离线打开后变量失效）
- 所有 h2 标题不加 emoji 前缀（使用纯文字）
- 表格/卡片内的状态符号使用内联 SVG 图标（不用 emoji，wkhtmltopdf 不支持彩色 emoji）
- 边框统一使用 hex（rgba() 在 wkhtmltopdf 中支持不稳定）
- 使用系统字体栈（-apple-system, "Noto Sans CJK SC" 等），不依赖外部字体

---

## PDF 生成命令（仅方案 A 使用）

```bash
wkhtmltopdf --page-size A4 --margin-top 14mm --margin-bottom 14mm \
  --margin-left 16mm --margin-right 16mm \
  --encoding utf-8 --no-stop-slow-scripts --enable-local-file-access --quiet \
  /home/claude/report_final_pdf.html \
  /mnt/user-data/outputs/{网站名}_AI诊断报告.pdf
```

PDF 专用 CSS 重点：
- `@page { size: A4; margin: 14mm 16mm; }`
- `*{-webkit-print-color-adjust:exact!important}`
- `.file-dl,button{display:none!important}` 隐藏按钮
- flex 属性加 !important 防被打印 CSS 重置
