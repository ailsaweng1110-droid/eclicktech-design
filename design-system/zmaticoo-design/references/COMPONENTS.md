# zMaticoo DSP 组件手写规范

> 仅在 search_design_system 未找到组件、且用户选择手写时使用本文件。
> 正常情况优先通过 importComponentByKeyAsync 复用现有组件。

---

## Button 按钮

```js
// 大按钮 40px（Primary Dark）
{ height: 40, paddingH: 13, paddingV: 8, fontSize: 16, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}],
  strokes: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}], cornerRadius: 4 }

// 中按钮 32px Primary
{ height: 32, paddingH: 13, paddingV: 5, fontSize: 14, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}], cornerRadius: 4 }

// 中按钮 32px Ghost
{ height: 32, paddingH: 17, paddingV: 5,  // 含图标时 paddingH: 13
  fontSize: 14, fontStyle: 'Medium',
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  strokes: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}], cornerRadius: 4 }

// 小按钮 24px（表格 inline）
{ height: 24, fontSize: 14, cornerRadius: 4 }

// icon 与文字间距：8px，icon 尺寸：14x14px
```

---

## Input 输入框

```js
// 标准输入框（40px）
{ height: 40, paddingLeft: 12, paddingRight: 12, paddingTop: 9, paddingBottom: 9,
  fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],
  strokeWeight: 1, cornerRadius: 4, fontSize: 14, fontStyle: 'Regular' }

// Error state
{ strokes: [{type:'SOLID', color:{r:0.831,g:0,b:0.29}}], cornerRadius: 4
  // + error focus ring shadow }

// Addon（货币单位等）
{ fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],
  paddingLeft: 12, paddingRight: 13, fontSize: 14, fontStyle: 'Regular' }
```

---

## Modal

```js
// 容器
{ width: 640, fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  cornerRadius: 2, layoutMode: 'VERTICAL',
  effects: [ /* 三层 drop-shadow，见 SKILL.md 七节 */ ] }

// Header（底线 #F0F0F0）
{ paddingLeft: 24, paddingRight: 24, paddingTop: 16, paddingBottom: 16
  // 标题：16px SemiBold #141414，关闭图标：16x16px 右侧 }

// Content
{ paddingLeft: 24, paddingRight: 24, paddingTop: 16, paddingBottom: 24,
  itemSpacing: 16, layoutMode: 'VERTICAL' }

// Footer（顶线 #F0F0F0，右对齐）
{ paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 12,
  primaryAxisAlignItems: 'MAX', itemSpacing: 8 }
```

---

## Drawer

```js
// 容器
{ width: 800, fills: [{type:'SOLID', color:{r:1,g:1,b:1}}],
  layoutMode: 'VERTICAL', effects: [ /* 同 Modal 阴影 */ ] }

// Header（px-24 py-16，关闭图标左侧，标题 16px SemiBold）
// Body（p-24，gap-24）
// Footer（px-24 py-16，border-top #F0F0F0，右对齐，gap-12）
```

---

## Table 表格

```js
// 表格头
{ fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],
  paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 13,
  fontSize: 14, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}] }

// 数据行 双行（55px）
{ height: 55, paddingLeft: 16, paddingRight: 16, paddingTop: 16, paddingBottom: 19
  // 主文字：14px Regular #141414，次文字：12px Medium #8C8C8C }

// 数据行 单行（47px）
{ paddingLeft: 16, paddingRight: 16, paddingTop: 12, paddingBottom: 13,
  fontSize: 14, fontStyle: 'Regular',
  fills_text: [{type:'SOLID', color:{r:0.078,g:0.078,b:0.078}}] }

// 操作链接：14px Regular #141414，textDecoration: 'UNDERLINE'，间距 8px
```

---

## 侧边导航

```js
// 容器：224px（商务中心）/ 226px（Adset）
// 分组标签：12px Medium #8C8C8C，px-16 py-4
// 导航项：height 40px，px-16，icon 16x16，gap 8px

// 激活态
{ fills: [{type:'SOLID', color:{r:0.902,g:0.949,b:1}}],
  cornerRadius: 20, fontSize: 14, fontStyle: 'SemiBold',
  fills_text: [{type:'SOLID', color:{r:0.01,g:0.318,b:1}}] }

// 非激活态
{ fills: [], fontSize: 14, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}] }
```

---

## Tag 标签

```js
// 角色 Tag（Admin）
{ fills: [{type:'SOLID', color:{r:0.902,g:0.949,b:1}}], cornerRadius: 2,
  paddingLeft: 8, paddingRight: 8, paddingTop: 1, paddingBottom: 1,
  fontSize: 12, fontStyle: 'Medium',
  fills_text: [{type:'SOLID', color:{r:0.01,g:0.318,b:1}}] }

// 可关闭 Tag
{ fills: [{type:'SOLID', color:{r:0.98,g:0.98,b:0.98}}],
  strokes: [{type:'SOLID', color:{r:0.851,g:0.851,b:0.851}}],
  cornerRadius: 2, paddingLeft: 6, paddingRight: 6, paddingTop: 1, paddingBottom: 1,
  fontSize: 12, fontStyle: 'Medium' }
// Error 态：strokes → #D4004A；Warning 态：strokes → #D95700
```

---

## Tooltip

```js
{ fills: [{type:'SOLID', color:{r:0.149,g:0.149,b:0.149}}], cornerRadius: 2,
  paddingLeft: 8, paddingRight: 8, paddingTop: 6, paddingBottom: 6,
  effects: [ /* drop-shadow/0.15 */ ],
  fontSize: 14, fontStyle: 'Regular',
  fills_text: [{type:'SOLID', color:{r:1,g:1,b:1}}] }
// 箭头：8x8 旋转 45° 正方形，同色背景
```

---

## Badge Dot

```js
{ width: 6, height: 6, cornerRadius: 100,
  // Active/Approved → #00941E
  // Rejected → #D4004A
  // Under review → #0251FF
  // 与文字间距：8px }
```
