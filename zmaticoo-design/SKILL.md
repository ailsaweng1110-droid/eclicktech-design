---
name: zmaticoo-design
description: >
  向 zMaticoo DSP Figma 文件写入或修改设计页面、组件时使用此 skill。
  涵盖完整 B 端设计规范：颜色、字体、间距、圆角、阴影、组件结构。
  适用场景：新建页面、新增组件、修改 Modal/Drawer、调整表格/导航等。
  使用前提：必须已连接 Figma MCP 远程服务器，且对目标文件有编辑权限（Full seat）。
compatibility:
  tools:
    - claude-code
    - cursor
    - vscode
version: "1.0"
maintainer: "zMaticoo Design Team"
---

# zMaticoo DSP 设计规范 Skill

## 一、前置要求（每次写入前必须执行）

1. **加载 figma-use skill**：所有写入操作必须基于 `figma-use` skill，在调用 `use_figma` 前先执行 `/figma-use`。
2. **读取目标节点**：写入前用 `get_design_context` 读取目标节点，确认现有结构和位置。
3. **加载字体**：所有文字节点创建前必须执行 `await figma.loadFontAsync()`，否则报错。
4. **返回节点 ID**：每次 `use_figma` 脚本必须 `return { createdNodeIds: [...], mutatedNodeIds: [...] }`。

## 二、Figma 文件信息

```
文件 Key：    7da8NWsTXC3o0F5vHRjDfD
文件链接：    https://www.figma.com/design/7da8NWsTXC3o0F5vHRjDfD/zMaticoo-DSP
模版画布：    node-id = 4079:61088（模版，包含 11 个设计页面）
```

### 已有页面索引（模版画布内）

| node-id | 页面名称 |
|---------|---------|
| 4079:61089 | 注册-邮箱已验证-输入校验 |
| 4079:61108 | 无账号-创建商务中心 |
| 4079:61129 | Adset-Create new |
| 4079:61846 | Campaign-Subsidy Budget(USD) |
| 4087:63225 | Report-Standard Report |
| 4096:67132 | Add Member01（含 Drawer）|
| 4096:67383 | 商务中心-Payment management |
| 4096:67509 | 商务中心-Transactions |
| 4111:67455 | 商务中心-Payment management-Add balance（Modal）|
| 4111:67735 | App Event |

---

## 三、色彩系统

> 写入 Figma 时所有颜色必须转为 **0–1 范围的 RGB 对象**。

### 品牌色

| 用途 | HEX | RGB（0-1） |
|------|-----|-----------|
| 主品牌蓝（链接/激活/Primary） | `#0251FF` | `{r:0.01, g:0.318, b:1}` |
| 主品牌蓝浅色（激活导航背景/Admin tag） | `#E6F2FF` | `{r:0.902, g:0.949, b:1}` |
| 主操作按钮/深色文字 | `#262626` | `{r:0.149, g:0.149, b:0.149}` |
| 顶部导航背景 | `#001366` | `{r:0, g:0.075, b:0.4}` |
| 注册页底部色带 | `#001E8C` | `{r:0, g:0.118, b:0.549}` |
| 用户头像背景 | `#26367D` | `{r:0.149, g:0.212, b:0.49}` |

### 功能色

| 类型 | HEX | RGB（0-1） |
|------|-----|-----------|
| Error | `#D4004A` | `{r:0.831, g:0, b:0.29}` |
| Error focus ring | `rgba(249,13,88,0.10)` | `{r:0.976, g:0.051, b:0.345, a:0.1}` |
| Success | `#00941E` | `{r:0, g:0.58, b:0.118}` |
| Warning | `#D95700` | `{r:0.851, g:0.341, b:0}` |
| Info | `#0251FF` | `{r:0.01, g:0.318, b:1}` |

### 状态 Badge Dot

| 状态 | HEX | RGB（0-1） |
|------|-----|-----------|
| Approved / Active | `#00941E` | `{r:0, g:0.58, b:0.118}` |
| Rejected | `#D4004A` | `{r:0.831, g:0, b:0.29}` |
| Under review | `#0251FF` | `{r:0.01, g:0.318, b:1}` |

### 中性色

| 用途 | HEX | RGB（0-1） |
|------|-----|-----------|
| 页面底色 | `#F5F5F5` | `{r:0.961, g:0.961, b:0.961}` |
| 内容区/表格头背景 | `#FAFAFA` | `{r:0.98, g:0.98, b:0.98}` |
| 卡片/Modal/表单白色背景 | `#FFFFFF` | `{r:1, g:1, b:1}` |
| 输入框 addon 背景 | `#FAFAFA` | `{r:0.98, g:0.98, b:0.98}` |
| Modal/Drawer 蒙层 | `rgba(38,38,38,0.32)` | `{r:0.149, g:0.149, b:0.149, a:0.32}` |
| Tooltip 背景 | `#262626` | `{r:0.149, g:0.149, b:0.149}` |
| 激活导航背景 | `#E6F2FF` | `{r:0.902, g:0.949, b:1}` |

### 边框色

| 用途 | HEX | RGB（0-1） |
|------|-----|-----------|
| 默认边框（输入框/选择器/tag） | `#D9D9D9` | `{r:0.851, g:0.851, b:0.851}` |
| 分割线/表格行/section | `#F0F0F0` | `{r:0.941, g:0.941, b:0.941}` |
| Error state 边框 | `#D4004A` | `{r:0.831, g:0, b:0.29}` |
| Warning state 边框 | `#D95700` | `{r:0.851, g:0.341, b:0}` |

### 文字色

| 层级 | HEX | RGB（0-1） |
|------|-----|-----------|
| 主要（标题/表格内容） | `#141414` | `{r:0.078, g:0.078, b:0.078}` |
| 正文/输入内容 | `#262626` | `{r:0.149, g:0.149, b:0.149}` |
| 次要（副标题/ID/导航分组） | `#8C8C8C` | `{r:0.549, g:0.549, b:0.549}` |
| 占位符 | `#BFBFBF` | `{r:0.749, g:0.749, b:0.749}` |
| 反色（深色背景上） | `#FFFFFF` | `{r:1, g:1, b:1}` |
| 链接/激活导航 | `#0251FF` | `{r:0.01, g:0.318, b:1}` |
| Error 提示文字 | `#D4004A` | `{r:0.831, g:0, b:0.29}` |

### 角色 Tag 色

| 角色 | 背景 HEX | 文字 HEX |
|------|---------|---------|
| Admin | `#E6F2FF` | `#0251FF` |
| Operator | `#E6F8FF` | `#0099AD` |
| Analyst | `#F4F8E8` | `#587A00` |

---

## 四、字体系统

### 字体族

```js
// 写入前必须加载
await figma.loadFontAsync({ family: 'Montserrat', style: 'Regular' });   // 400
await figma.loadFontAsync({ family: 'Montserrat', style: 'Medium' });    // 500
await figma.loadFontAsync({ family: 'Montserrat', style: 'SemiBold' }); // 600
await figma.loadFontAsync({ family: 'Montserrat', style: 'Bold' });     // 700
```

### 字号与行高

| Token | 字号 | 字重 | 行高 | 主要用途 |
|-------|------|------|------|---------|
| xs | 12px | Medium 500 | 20px | 导航分组标签、表格次级文字、Tag 文字 |
| sm | 14px | 400/500/600 | 22px | 主要正文、表单、表格、32px 按钮 |
| base | 16px | 500/600 | 24px | 40px 按钮、Modal/Drawer 标题、导航 |
| md | 20px | 500/600 | 28px | 卡片标题 |
| lg | 24px | 600 | 32px | 页面主标题 |
| xl | 40px | 700 | 1.2 | 品牌 hero 大字 |

---

## 五、间距系统

**基础单位：4px**

| 名称 | 值 | 典型用途 |
|------|----|---------|
| xs | 4px | icon 与文字间距 |
| sm | 8px | form label-input 间距、按钮 gap |
| md | 16px | 表单项间距、Modal 内边距 |
| lg | 24px | 内容区 padding、Modal header px |
| xl | 32px | 段落间距 |
| 2xl | 40px | 区块间距 |
| 5xl | 64px | 顶部导航高度 |

### 组件内边距速查

| 组件 | 水平 | 垂直 |
|------|------|------|
| 输入框（标准 40px 高） | px: 12px | py: 9px |
| 输入框（紧凑 32px 高，Modal 内）| px: 12px | py: 5px |
| 大按钮 40px | px: 13px | py: 8px |
| 中按钮 32px Primary | px: 13px | py: 5px |
| 中按钮 32px Ghost（无图标）| px: 17px | py: 5px |
| 角色 Tag | px: 8px | py: 1px |
| 可关闭 Tag | px: 6px | py: 1px |
| Tooltip | px: 8px | py: 6px |
| 表格单元格（55px 双行行）| px: 16px | pt: 16px, pb: 19px |
| 表格单元格（47px 单行）| px: 16px | pt: 12px, pb: 13px |
| 表格头 | px: 16px | pt: 12px, pb: 13px |
| Modal header | px: 24px | py: 16px |
| Modal content | px: 24px | pt: 16px, pb: 24px |
| Modal footer | px: 16px | py: 12px |
| Drawer header | px: 24px | py: 16px |
| Drawer body | p: 24px | — |
| Drawer footer | px: 24px | py: 16px |
| 导航项 | px: 16px | — |
| 导航分组标签 | px: 16px | py: 4px |

---

## 六、圆角系统

| Token | 值 | 使用组件 |
|-------|----|---------| 
| xs | **2px** | Modal、Drawer、Tooltip、Tag、Dropdown、Popconfirm、pagination item |
| sm | **4px** | 按钮、输入框（含 error state）、下拉选择器（主圆角）|
| md | **8px** | 内容子卡片、用户头像、dropdown item icon |
| lg | **12px** | 主内容区容器 |
| nav-active | **20px** | 导航激活项 pill（Border Radius 20px）|
| panel | **24px** | 注册页右侧面板 |
| badge | **100px** | 状态 badge dot（完整圆形）|

---

## 七、阴影系统

```js
// Modal / Drawer / Dropdown 弹层阴影（drop-shadow/0.12+0.8+0.5）
effects: [
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.12}, offset:{x:0,y:3}, radius:6, spread:-4 },
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.08}, offset:{x:0,y:6}, radius:16, spread:0 },
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.05}, offset:{x:0,y:9}, radius:28, spread:8 }
]

// Tooltip 阴影（drop-shadow/0.15）
effects: [
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.15}, offset:{x:0,y:2}, radius:8, spread:0 }
]

// Error focus ring
effects: [
  { type: 'DROP_SHADOW', color: {r:0.976,g:0.051,b:0.345,a:0.10}, offset:{x:0,y:0}, radius:0, spread:2 }
]

// 分割线（用 strokes 实现，Figma inner shadow 等价）
// Modal header 底线：strokeBottom #F0F0F0, weight 1
// Modal footer 顶线：strokeTop #F0F0F0, weight 1
```

---

## 八、布局系统

| 属性 | 值 |
|------|----|
| 页面最大宽度 | 1440px |
| 顶部导航高度 | 64px |
| 内容区 padding | 24px |
| 主内容区圆角 | 12px |
| 主内容区背景 | `#FAFAFA`，边框 `#F0F0F0` |
| 商务中心左侧导航宽度 | 224px |
| Adset 步骤导航宽度 | 226px |
| Modal 标准宽度 | 640px |
| Drawer 标准宽度 | 800px |

---

## 九、组件规范详解

### 9.1 按钮（四尺寸）

```js
// 大按钮 40px（Primary Dark）
{
  height: 40, paddingH: 13, paddingV: 8,
  fontSize: 16, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],  // #262626
  strokes: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],
  cornerRadius: 4
}

// 中按钮 32px Primary
{
  height: 32, paddingH: 13, paddingV: 5,
  fontSize: 14, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],
  cornerRadius: 4
}

// 中按钮 32px Ghost/Secondary
{
  height: 32, paddingH: 17, paddingV: 5,  // 含图标时 paddingH: 13
  fontSize: 14, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],              // white
  strokes: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],
  cornerRadius: 4
}

// 小按钮 24px（表格 inline）
{ height: 24, fontSize: 14, cornerRadius: 4 }

// 按钮内 icon-文字间距：8px
// 按钮内 icon 尺寸：14x14px
```

### 9.2 输入框（Input）

```js
// 标准输入框（高 40px）
{
  height: 40,
  paddingLeft: 12, paddingRight: 12, paddingTop: 9, paddingBottom: 9,
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],  // #D9D9D9
  strokeWeight: 1, cornerRadius: 4,
  fontSize: 14, fontStyle: 'Regular'
}

// Error state（圆角统一为 4px，不是 2px）
{
  strokes: [{type:'SOLID', color:{r:0.831,g:0,b:0.29}}],  // #D4004A
  cornerRadius: 4,
  // 同时添加 error focus ring shadow
}

// 输入框 Addon（货币单位 USD 等）
{
  fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],  // #FAFAFA
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],
  paddingLeft: 12, paddingRight: 13, fontSize: 14, fontStyle: 'Regular'
}
```

### 9.3 Modal

```js
// Modal 容器
{
  width: 640,
  // height: AUTO（由内容决定）
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  cornerRadius: 2,
  effects: [ /* drop-shadow/0.12+0.8+0.5，见第七节 */ ],
  layoutMode: 'VERTICAL'
}

// Header（px-24 py-16，底部分割线）
{
  paddingLeft: 24, paddingRight: 24, paddingTop: 16, paddingBottom: 16,
  // 底线：描边 bottom #F0F0F0 weight 1
  // 标题：16px SemiBold #141414
  // 关闭图标：16x16px，右侧
}

// Content（px-24 pt-16 pb-24，gap-16）
{
  paddingLeft: 24, paddingRight: 24, paddingTop: 16, paddingBottom: 24,
  itemSpacing: 16, layoutMode: 'VERTICAL'
}

// Footer（px-16 py-12，顶部分割线，右对齐，button-group gap 8px）
{
  paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 12,
  primaryAxisAlignItems: 'MAX',  // justify-end
  itemSpacing: 8,
  // 顶线：描边 top #F0F0F0 weight 1
}
```

### 9.4 Drawer

```js
// Drawer 容器（右侧滑入）
{
  width: 800, height: 900,  // 全屏高
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  effects: [ /* 同 Modal 阴影 */ ],
  layoutMode: 'VERTICAL'
}

// Header（px-24 py-16，关闭图标在左侧，标题 16px SemiBold）
// Body（p-24，gap-24）
// Footer（px-24 py-16，border-top #F0F0F0，右对齐，gap-12）
```

### 9.5 表格（Table）

```js
// 表格头
{
  fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],     // #FAFAFA
  paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 13,
  // 底线 #F0F0F0
  fontSize: 14, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}]  // #262626
}

// 数据行（双行，55px 高）
{
  height: 55,
  paddingLeft: 16, paddingRight: 16, paddingTop: 16, paddingBottom: 19,
  // 底线 #F0F0F0
  // 主文字：14px Regular #141414
  // 次文字（ID 等）：12px Medium #8C8C8C
}

// 数据行（单行，47px 高）
{
  paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 13,
  fontSize: 14, fontStyle: 'Regular',
  fills_text: [{type:'SOLID', color:{r:0.078,g:0.078,b:0.078}}]  // #141414
}

// 操作列链接
// 14px Regular #141414 + textDecoration: 'UNDERLINE'
// 操作间用 12px 高分割线（#F0F0F0），gap 8px
```

### 9.6 侧边导航

```js
// 导航容器宽度：224px（商务中心）/ 226px（Adset）
// 导航分组标签：12px Medium #8C8C8C，px-16 py-4
// 导航项高度：40px，px-16，gap-icon-text: 8px，icon: 16x16

// 激活态
{
  fills: [{type:'SOLID', color:{r:0.902,g:0.949,b:1}}],  // #E6F2FF
  cornerRadius: 20,  // pill 圆角
  fontSize: 14, fontStyle: 'SemiBold',
  fills_text: [{type:'SOLID', color:{r:0.01,g:0.318,b:1}}]  // #0251FF
}

// 非激活态
{
  fills: [],  // 透明
  fontSize: 14, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}]  // #262626
}
```

### 9.7 Tag（标签）

```js
// 角色 Tag（不可关闭，Admin 为例）
{
  fills: [{type:'SOLID', color:{r:0.902,g:0.949,b:1}}],   // #E6F2FF
  cornerRadius: 2,
  paddingLeft: 8, paddingRight: 8, paddingTop: 1, paddingBottom: 1,
  fontSize: 12, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.01,g:0.318,b:1}}]  // #0251FF
}

// 可关闭 Tag（正常态）
{
  fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],  // #FAFAFA
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],  // #D9D9D9
  cornerRadius: 2,
  paddingLeft: 6, paddingRight: 6, paddingTop: 1, paddingBottom: 1,
  fontSize: 12, fontStyle: 'Medium'
}
// Error 态：strokes 改为 #D4004A
// Warning 态：strokes 改为 #D95700
```

### 9.8 Tooltip

```js
{
  fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],  // #262626
  cornerRadius: 2,
  paddingLeft: 8, paddingRight: 8, paddingTop: 6, paddingBottom: 6,
  effects: [ /* drop-shadow/0.15 */ ],
  fontSize: 14, fontStyle: 'Regular',
  fills_text: [{type:'SOLID', color:{r:1,g:1,b:1}}]  // white
  // 箭头：8x8 旋转45度正方形，同色背景
}
```

### 9.9 状态 Badge Dot

```js
{
  width: 6, height: 6,
  cornerRadius: 100,  // 完整圆形
  // Approved/Active：fills #00941E
  // Rejected：fills #D4004A
  // Under review：fills #0251FF
  // 与文字间距：8px
}
```

---

## 十、use_figma 写入规范

### 代码模板

```js
// ✅ 正确写法（不要包裹 async IIFE，平台自动处理）
await figma.loadFontAsync({ family: 'Montserrat', style: 'Medium' });
await figma.loadFontAsync({ family: 'Montserrat', style: 'Regular' });

const frame = figma.createFrame();
frame.name = 'my-component';
frame.layoutMode = 'VERTICAL';
frame.primaryAxisSizingMode = 'AUTO';
frame.counterAxisSizingMode = 'FIXED';
frame.resize(640, 10);
frame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
frame.cornerRadius = 2;
frame.itemSpacing = 16;
frame.paddingLeft = 24;
frame.paddingRight = 24;
frame.paddingTop = 16;
frame.paddingBottom = 24;
frame.clipsContent = false;

// 必须返回 node ID
return { createdNodeIds: [frame.id] };

// ❌ 禁止使用
// figma.notify()          → 会报错
// figma.closePlugin()     → 不需要
// getPluginData()         → 不支持，用 getSharedPluginData()
// (async () => { ... })() → 不要包裹，平台自动处理
```

### 插入到已有节点

```js
// 获取目标节点
const targetNode = await figma.getNodeByIdAsync('4112:68309');

// 插入到指定位置（index=1 表示第二个子节点）
targetNode.insertChild(1, newFrame);

return { createdNodeIds: [newFrame.id], mutatedNodeIds: [targetNode.id] };
```

### Auto Layout 关键属性

```js
frame.layoutMode = 'VERTICAL';           // 或 'HORIZONTAL'
frame.primaryAxisSizingMode = 'AUTO';    // 主轴自动撑开
frame.counterAxisSizingMode = 'FIXED';  // 或 'AUTO'
frame.counterAxisAlignItems = 'CENTER'; // 交叉轴对齐
frame.primaryAxisAlignItems = 'MAX';    // justify-end（footer 右对齐）
frame.itemSpacing = 8;                  // gap
```

---

## 十一、写入流程

```
1. 执行 /figma-use（加载官方写入 skill）
2. 执行 /zmaticoo-design（加载本设计规范 skill）
3. get_design_context 读取目标节点，确认现有结构
4. 根据第九节组件规范，编写 use_figma JavaScript
5. 执行 use_figma，传入 skillNames: "zmaticoo-design,figma-use"
6. 验证返回的 node ID，必要时再次 get_design_context 确认结果
7. 如有异常，读取 error message，修正后重试（不要盲目重试）
```

---

## 十二、常见错误处理

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `font not loaded` | 忘记 loadFontAsync | 在脚本最前面加载所有用到的字体 |
| `figma is not defined` | 文件权限不足 | 确认有 Full seat 且对文件有编辑权限 |
| `Cannot read properties of null` | node ID 不存在 | 先用 get_metadata 确认节点 ID |
| `insertChild` 报错 | 父节点不是 Frame | 确认目标节点类型为 FRAME |
| 写入后尺寸不对 | Auto Layout 未设置 | 检查 layoutMode 和 Sizing Mode |

---

## 十三、参考文件

- 完整设计规范：`./references/DESIGN_SPEC.md`
- Design Token CSS：`./references/tokens.css`
- Figma Plugin API 文档：https://developers.figma.com/docs/plugins/api/global-objects/
- Figma MCP 写入文档：https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/
