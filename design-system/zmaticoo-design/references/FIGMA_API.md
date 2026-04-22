# Figma API 写入规范参考

> use_figma 脚本编写时的代码模板和常用 API 速查。

---

## 基础写入模板

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

return { createdNodeIds: [frame.id] };

// ❌ 禁止使用
// figma.notify()           → 报错
// figma.closePlugin()      → 不需要
// getPluginData()          → 不支持，用 getSharedPluginData()
// (async () => { ... })()  → 不要包裹
```

---

## 插入到已有节点

```js
const targetNode = await figma.getNodeByIdAsync('4112:68309');
targetNode.insertChild(1, newFrame);  // index=1 → 第二个子节点
return { createdNodeIds: [newFrame.id], mutatedNodeIds: [targetNode.id] };
```

---

## Auto Layout 关键属性

```js
frame.layoutMode = 'VERTICAL';            // 或 'HORIZONTAL'
frame.primaryAxisSizingMode = 'AUTO';     // 主轴自动撑开
frame.counterAxisSizingMode = 'FIXED';   // 或 'AUTO'
frame.counterAxisAlignItems = 'CENTER';  // 交叉轴对齐
frame.primaryAxisAlignItems = 'MAX';     // justify-end（footer 右对齐）
frame.itemSpacing = 8;                   // gap
```

---

## 常用 API 速查

```js
// 创建节点
figma.createFrame()
figma.createText()
figma.createRectangle()
figma.createLine()

// 引入并实例化组件
const comp = await figma.importComponentByKeyAsync('key');
const instance = comp.createInstance();

// 获取节点
await figma.getNodeByIdAsync('node-id')

// 文字设置（必须先 loadFont）
textNode.fontName = { family: 'Montserrat', style: 'Medium' };
textNode.fontSize = 14;
textNode.lineHeight = { value: 22, unit: 'PIXELS' };
textNode.characters = '文字内容';

// 颜色设置
node.fills = [{ type: 'SOLID', color: { r: 0.01, g: 0.318, b: 1 } }];
node.strokes = [{ type: 'SOLID', color: { r: 0.851, g: 0.851, b: 0.851 } }];
node.strokeWeight = 1;

// 阴影
node.effects = [
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.12},
    offset:{x:0,y:3}, radius:6, spread:-4, visible: true, blendMode: 'NORMAL' }
];
```
