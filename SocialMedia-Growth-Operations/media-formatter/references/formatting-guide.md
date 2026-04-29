# 公众号排版规范

> 本规范用于易点设计 UED 团队公众号文章排版，所有 AI 生成的内容稿件最终输出 HTML 时，须严格遵循以下样式规则，确保可直接复制粘贴至微信公众号编辑后台发布。

---

## 一、整体页面规则

| 项目 | 规则 |
|---|---|
| 页边距 | 左右各 10px |
| 全文背景 | 纯白 #FFFFFF |
| 字体族 | 系统默认（-apple-system, "PingFang SC", "Microsoft YaHei", sans-serif） |

---

## 二、文字层级规范

### 1. 一级标题

用于文章主体的章节划分，如「一、品牌级视觉搭建能力」。

- **字号**：20px
- **颜色**：#222222
- **字重**：Bold（加粗）
- **对齐**：左对齐
- **上下间距**：上 24px / 下 12px
- **标题下方分割线**：高度 2px，颜色 #F4F4F4，宽度 100%

**HTML 示例：**

```html
<h2 style="font-size:20px;color:#222222;font-weight:bold;margin:24px 0 12px 0;">一、品牌级视觉搭建能力</h2>
<div style="height:2px;background-color:#F4F4F4;width:100%;margin-bottom:16px;"></div>
```

---

### 2. 正文

用于所有段落内容、说明文字。

- **字号**：15px
- **颜色**：#3F3F3F
- **行间距（line-height）**：2
- **字间距（letter-spacing）**：1px
- **段落间距**：上下 12px
- **对齐**：左对齐
- **页边距**：左右 10px

**HTML 示例：**

```html
<p style="font-size:15px;color:#3F3F3F;line-height:2;letter-spacing:1px;margin:12px 10px;">
  这里是正文内容，保持自然流畅的语言风格，避免过长段落，建议每段控制在 1–3 行内。
</p>
```

---

### 3. 重点高亮

正文中需要强调的关键词、核心观点、产品名、数据等。

- **样式**：加粗 + 颜色高亮
- **颜色**：#0052FF
- **字号**：与正文一致（15px）
- **使用克制**：每段建议高亮不超过 1–2 处，避免视觉过载

**HTML 示例：**

```html
<p style="font-size:15px;color:#3F3F3F;line-height:2;letter-spacing:1px;margin:12px 10px;">
  最近两天,系统检测了一下 ChatGPT Image2 的<strong style="color:#0052FF;">生图能力</strong>。
</p>
```

---

## 三、辅助元素

### 1. 引导句 / 小结句

每个章节末尾的高亮小结，用于强调本节核心结论。

- 句首加 emoji（如 👍 💡 🎯）
- 整句使用主题色 #0052FF
- 字号 15px，加粗

**HTML 示例：**

```html
<p style="font-size:15px;color:#0052FF;font-weight:bold;line-height:2;letter-spacing:1px;margin:12px 10px;">
  👍 这已经是「初级品牌设计师」的能力！
</p>
```

---

### 2. 列表

用于并列要点说明。

- **项目符号**：圆点 •
- **单行字号**：15px / 颜色 #3F3F3F
- **行间距**：2
- **缩进**：左侧 20px

**HTML 示例：**

```html
<ul style="font-size:15px;color:#3F3F3F;line-height:2;letter-spacing:1px;padding-left:20px;margin:12px 10px;">
  <li>Logo + VI 延展</li>
  <li>包装设计</li>
  <li>品牌色彩体系</li>
  <li>电商视觉统一</li>
</ul>
```

---

### 3. 数字总结列表

用于文末的总结收尾段落。

- 使用「1. 2. 3.」阿拉伯数字格式
- 字号 15px，颜色 #3F3F3F
- 关键词加粗 + #0052FF 高亮

**HTML 示例：**

```html
<p style="font-size:15px;color:#3F3F3F;line-height:2;letter-spacing:1px;margin:12px 10px;">
  1. ChatGPT Image 2 已经超越「AI 画图工具」，更像一个：<strong style="color:#0052FF;">品牌视觉生产引擎</strong>。
</p>
```

---

## 四、图片规范

- 图片**全宽铺满**容器，左右不留白
- 同模块多图采用**等高拼接**，图与图之间间距 0 或极小
- 图片**置于对应文字说明之后**
- 建议宽度 ≥ 750px，避免模糊

**HTML 示例：**

```html
<p style="margin:16px 0;text-align:center;">
  <img src="图片地址" style="width:100%;display:block;" />
</p>
```

---

## 五、文章结构模板

```
[文章主标题]
  ↓
[作者署名 / 分类标签 / 日期]（小字、灰色）
  ↓
[引子段落 — 1–2 段，建立背景]
  ↓
[一级标题 一、xxxx] + 分割线
  ↓
[正文 + 图片 + 小结句]
  ↓
[一级标题 二、xxxx] + 分割线
  ↓
[正文 + 图片 + 小结句]
  ↓
... （依此类推）
  ↓
[文末数字列表总结 1. 2. 3.]
  ↓
[文末固定区：阅读量 / 留言 / 引导链接]
```

---

## 六、AI 生成排版的关键约束

在调用此规范进行 HTML 排版时，必须满足：

1. **所有样式使用 inline style 内联写法**，不使用 `<style>` 标签或 class 类名（公众号编辑器会过滤）。
2. **不使用 `<section>` 嵌套**，统一用 `<p>` `<h2>` `<div>` `<ul>` 等基础标签。
3. **颜色值统一大写十六进制**：#222222、#3F3F3F、#0052FF、#F4F4F4。
4. **每段正文左右各 10px 外边距**，与页面边距规则一致。
5. **不使用阴影、圆角、渐变等装饰效果**，保持极简克制。
6. **输出内容可直接整段复制至公众号编辑后台**，无需二次手动调整。

---

## 七、快速取色卡

| 用途 | 色值 |
|---|---|
| 一级标题 | `#222222` |
| 正文 | `#3F3F3F` |
| 重点高亮 / 主题色 | `#0052FF` |
| 分割线 / 浅色背景 | `#F4F4F4` |
| 页面背景 | `#FFFFFF` |
