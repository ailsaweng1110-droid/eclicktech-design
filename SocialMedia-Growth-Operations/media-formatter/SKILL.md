---
name: media-formatter
description: 公众号排版 Skill，将已完成审阅的文章正文转换为可直接粘贴至微信公众号编辑后台的 HTML 排版版本。当用户提到"排版"、"生成HTML"、"帮我排版"、"内容写好了"、"可以排版了"等关键词，或明确表示内容撰写已完成需要输出发布版本时，触发此 Skill。本 Skill 只负责排版输出，不参与内容创作和修改，内容撰写请调用 media-content-writer Skill。
version: 1.0.0
author: 品牌公关部产品设计组
---

# 公众号排版 Skill

## Overview

接收 media-content-writer Skill 输出的已审阅文章正文，按品牌视觉规范输出可直接发布的公众号 HTML 版本。

本 Skill 不修改正文内容，只负责排版转换。如需修改内容，请返回 media-content-writer Skill 完成后再调用本 Skill。

---

## 执行流程 (Workflow)

### Step 1：接收内容

确认用户已提供以下材料，缺一则主动询问：
- 已定稿的文章正文（纯文字版）
- 选用的标题（从标题矩阵中确认用哪一个）
- 副标题（如有）
- 配图说明是否需要保留占位标注

### Step 2：读取排版规范

读取 `references/formatting-guide.md`，掌握所有组件的 HTML 代码和样式参数后再开始排版，不得凭记忆输出样式。

### Step 3：结构映射

将正文内容映射到对应的 HTML 组件：
- 文章大标题 → 一级标题组件
- 章节标题 → 二级标题组件（带品牌蓝斜体序号）
- 步骤标题 → 三级标题组件（带 STEP 胶囊标签）
- 重点词句 → 行内高亮组件
- 信息清单 / 亮点 → 蓝色信息卡组件
- 注意事项 / 踩坑 → 暖色提醒卡组件
- 引用内容 → 引用块组件
- 推荐 vs 不推荐对比 → 对比栏组件
- 数据指标 → 核心数据卡组件
- 配图占位标注 → 视频占位符样式保留

### Step 4：输出 HTML

严格按照 `references/formatting-guide.md` 的组件代码输出完整 HTML，包裹在标准容器内。不得自行发明样式，不得修改品牌色值。

### Step 5：追加标准文末模块

每篇文章结尾固定追加以下 HTML，不得遗漏：

```html
<hr style="border:none;border-top:1px solid #EAEDF2;margin:32px 0;">
<p style="font-size:13px;color:#999999;text-align:center;">
私信回复关键词【***】，即可获取：<br>
1.《Figma工程化命名与图层规范表》：让AI瞬间读懂你的设计。<br>
2.《AI动画效果演示库文件》：可视化预览所有AI原生效果。<br>
3.《三方动效库配置指令集》：包含Motion、AOS的快速接入方案。
</p>
<hr style="border:none;border-top:1px solid #EAEDF2;margin:32px 0;">
<p style="font-size:13px;color:#BBBBBB;text-align:center;">
专注于人工智能、产品设计与品牌营销的交叉融合。我们不仅分享前沿工具的实战技巧，更致力于通过设计为企业创造商业力 Designing for Business Impact。<br><br>
商务合作/出海官网定制请后台留言。
</p>
<p style="font-size:12px;color:#b2b2b2;text-align:center;font-style:italic;">
内容策划：*** | 技术撰稿：***
</p>
```

---

## 排版规范与限制 (Constraints)

1. 只排版，不改稿：不得修改正文任何文字内容，包括标点、用词、段落顺序
2. 严格遵守规范：所有样式必须来自 `references/formatting-guide.md`，不得自行添加阴影、渐变、圆角大于12px的元素
3. 三色原则：白底 #FFFFFF + 正文 #222222 + 品牌蓝 #0251FF，不引入其他颜色
4. 标签互斥：斜体蓝数字（章节序号）/ 实心胶囊（STEP）/ 空心方框（对比标签）三类禁止混用
5. 文末必须完整：标准文末模块一字不漏追加，不得简化
6. 配图占位保留：正文中的 [配图建议：XXX] 标注转换为视频占位符样式保留，提示编辑后台插图位置

---

## 输出格式规范 (Output Template)

```
### 排版说明
- 使用标题：[确认用户选定的标题]
- 组件使用：[列出本文用到的主要组件，如：二级标题×3、蓝色信息卡×2、暖色提醒卡×1]
- 配图占位：[共N处，已用占位符标注]

### 公众号 HTML 版本（可直接粘贴至编辑后台）
[完整 HTML，从 <section> 开始到署名行结束]
```

---

## References

文件：`references/formatting-guide.md`（Step 2 必须读取）

公众号完整排版参数手册，包含：
- 基础参数（字体/字号/颜色/间距）
- 标题体系（一级/二级/三级）的完整 HTML 代码
- 所有组件的完整 HTML 代码（卡片/标签/引用/对比栏/数据卡等）
- 页尾标准模块
- 完整文章 HTML 模板
