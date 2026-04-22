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
version: "2.0"
maintainer: "zMaticoo Design Team"
---

# zMaticoo DSP 设计规范 Skill

## 一、前置要求（每次写入前必须执行）

1. **加载 figma-use skill**：所有写入操作必须基于 `figma-use` skill，在调用 `use_figma` 前先执行 `/figma-use`。
2. **读取目标节点**：写入前用 `get_design_context` 读取目标节点，确认现有结构和位置。
3. **加载字体**：所有文字节点创建前必须执行 `await figma.loadFontAsync()`，否则报错。
4. **返回节点 ID**：每次 `use_figma` 脚本必须 `return { createdNodeIds: [...], mutatedNodeIds: [...] }`。

---

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

```js
// 写入前必须加载
await figma.loadFontAsync({ family: 'Montserrat', style: 'Regular' });   // 400
await figma.loadFontAsync({ family: 'Montserrat', style: 'Medium' });    // 500
await figma.loadFontAsync({ family: 'Montserrat', style: 'SemiBold' }); // 600
await figma.loadFontAsync({ family: 'Montserrat', style: 'Bold' });     // 700
```

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
| 表格单元格（55px 双行）| px: 16px | pt: 16px, pb: 19px |
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
| sm | **4px** | 按钮、输入框（含 error state）、下拉选择器 |
| md | **8px** | 内容子卡片、用户头像、dropdown item icon |
| lg | **12px** | 主内容区容器 |
| nav-active | **20px** | 导航激活项 pill |
| panel | **24px** | 注册页右侧面板 |
| badge | **100px** | 状态 badge dot（完整圆形）|

---

## 七、阴影系统

```js
// Modal / Drawer / Dropdown 弹层阴影
effects: [
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.12}, offset:{x:0,y:3}, radius:6, spread:-4 },
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.08}, offset:{x:0,y:6}, radius:16, spread:0 },
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.05}, offset:{x:0,y:9}, radius:28, spread:8 }
]

// Tooltip 阴影
effects: [
  { type: 'DROP_SHADOW', color: {r:0,g:0,b:0,a:0.15}, offset:{x:0,y:2}, radius:8, spread:0 }
]

// Error focus ring
effects: [
  { type: 'DROP_SHADOW', color: {r:0.976,g:0.051,b:0.345,a:0.10}, offset:{x:0,y:0}, radius:0, spread:2 }
]
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

## 九、组件复用策略（重要）

**每次写入前，必须按以下优先级决定如何获取组件，不得跳过步骤直接手写。**

```
优先级 1：使用文件内已有组件（search_design_system + importComponentByKeyAsync）
优先级 2：引入开源组件库（需与用户确认）
优先级 3：AI 直接手写组件（兜底）→ 参考 ./references/COMPONENTS.md
```

### 优先级 1：使用文件内已有组件（首选）

```js
const comp = await figma.importComponentByKeyAsync('组件的 key');
const instance = comp.createInstance();
instance.resize(160, 32);
instance.setProperties({ 'size': 'medium', 'type': 'primary' });
parentFrame.appendChild(instance);
return { createdNodeIds: [instance.id] };
```

> 搜索关键词尽量简短：`button` / `input` / `radio` / `tag`

**文件已确认组件（87 个，均可通过 search_design_system 找到）：**

#### 📊 表格系列（9 个）
| 组件名 | 说明 |
|--------|------|
| `table-cell/text` | 表格文本单元格 |
| `table-cell/status` | 表格状态单元格（含 badge）|
| `components/table-column/text` | 表格文本列 |
| `table-header/default` | 表格列头 |
| `components/table-column/check-box` | 表格 checkbox 列 |
| `table/column-based` | 列式表格容器 |
| `components/table-column/status` | 表格状态列 |
| `components/table-column/switch` | 表格开关列 |
| `components/table-cell/checkbox` | 表格 checkbox 单元格 |

#### 🔘 按钮 & 操作（5 个）
| 组件名 | Node ID | 说明 |
|--------|---------|------|
| `button` | 3863:38186 | 按钮（多尺寸/多变体）|
| `button-group` | 3863:39264 | 按钮组 |
| `components/dropdown/menu-item` | — | 下拉菜单项 |
| `dropdown-trigger` | — | 下拉触发器 |
| `dropdown-menu` | — | 下拉菜单 |

#### 📝 表单系列（24 个）
| 组件名 | Node ID | 说明 |
|--------|---------|------|
| `vertical-form-item/input` | — | 垂直表单项-输入框 |
| `checkbox` | — | 复选框 |
| `vertical-form-item/radio` | — | 垂直表单项-单选 |
| `vertical-form-item/select` | — | 垂直表单项-选择器 |
| `input` | 85:1655 | 文本输入框 |
| `search-box` | 142:3014 | 搜索框 |
| `select` | 3863:40846 | 下拉选择器 |
| `date-picker` | — | 日期选择器 |
| `form-item/input` | — | 表单项-输入框 |
| `components/radio` | — | 单选框 |
| `vertical-form-item/textarea` | — | 垂直表单项-多行文本 |
| `vertical-form-item/radio-button-group` | — | 垂直表单项-单选按钮组 |
| `form` | 3930:104894 | 表单容器 |
| `form-item/radio-button` | — | 表单项-单选按钮 |
| `form-item/upload` | — | 表单项-上传 |
| `form-item/select` | — | 表单项-选择器 |
| `form-item/button` | — | 表单项-按钮 |
| `form-item/upload-files` | — | 表单项-上传文件列表 |
| `vertical-form-item/date-picker` | — | 垂直表单项-日期选择 |
| `vertical-form-item/switch` | — | 垂直表单项-开关 |
| `time-picker` | — | 时间选择器 |
| `vertical-form-item/checkbox` | — | 垂直表单项-复选框 |
| `form-item/textarea` | — | 表单项-多行文本 |
| `password` | 690:9533 | 密码输入框 |

#### 🗂 导航 & Tab（7 个）
| 组件名 | 说明 |
|--------|------|
| `menu` | 顶部导航菜单 |
| `components/tab-vertical` | 垂直 Tab 子项 |
| `tabs/card` | Card 式 Tab |
| `tabs/left` | 垂直 Tab（左侧步骤）|
| `inline-menu-item/1st-level` | 侧边导航菜单项 |
| `tabs/top` | 水平 Tab |
| `select（导航顶部）` | 顶部导航内选择器 |

#### 🪟 弹层（6 个）
| 组件名 | 说明 |
|--------|------|
| `drawer` | Drawer 侧边抽屉 |
| `modal/basic` | Modal 弹窗 |
| `alert` | 警告提示 |
| `popconfirm` | 气泡确认框 |
| `tooltip` | 文字提示 |
| `modal/Delete` | 删除确认 Modal |

#### 🏷 标签 & 状态（6 个）
| 组件名 | Node ID | 说明 |
|--------|---------|------|
| `badge/status` | 3930:105552 | 状态 Badge |
| `tag/default` | — | 标签 |
| `statistic` | — | 统计数字 |
| `badge/dot` | 115:2688 | dot badge |
| `tag/closable/small` | — | 可关闭小标签 |
| `tag/ec` | — | 角色标签（Admin/Operator）|

#### 📄 分页 & 步骤（4 个）
| 组件名 | Node ID | 说明 |
|--------|---------|------|
| `pagination` | 3863:41543 | 分页 |
| `steps` | 3863:42705 | 步骤条 |
| `components/steps-item-icon` | — | 步骤图标 |
| `scrollbar` | — | 滚动条 |

#### 📤 上传（4 个）
| 组件名 | 说明 |
|--------|------|
| `upload-picture-list-item` | 图片上传列表项 |
| `upload-picture-card` | 图片上传卡片 |
| `upload` | 上传 |
| `upload-picture` | 图片上传 |

#### 🔧 通用（11 个）
| 组件名 | Node ID | 说明 |
|--------|---------|------|
| `divider` | 85:7621 | 分割线 |
| `icon-wrapper` | 1:451 | 图标容器 |
| `text/title` | — | 标题文本 |
| `grid` | — | 栅格 |
| `progress-scrubber/basic` | — | 进度条控件 |
| `text/text` | — | 正文文本 |
| `list` | — | 列表 |
| `progress` | — | 进度条 |
| `empty/customize` | — | 空状态 |
| `components/header` | — | 页面头部 |
| `components/footer` | — | 页面底部 |

### 优先级 2：引入开源组件库（未在文件中找到时）

暂停写入，询问用户：
```
在 zMaticoo DSP 文件中未找到「xxx」组件。
A. Ant Design（antd）— 推荐，与文件风格最接近
B. Semi Design
C. 跳过，由 AI 按设计规范手写
```

### 优先级 3：AI 手写组件（兜底）

手写时读取 `./references/COMPONENTS.md` 获取各组件的精确规范值。

### 决策流程

```
需要某个组件
    ↓
search_design_system 搜索
    ↓
找到 → importComponentByKeyAsync → createInstance ✅
未找到 → 询问用户选择开源库
         ↓
    选 A/B → 引入组件库实例 ✅
    选 C   → 参考 COMPONENTS.md 手写 ✅
```

---

## 十、写入流程

```
1. 执行 /figma-use（加载官方写入 skill）
2. 执行 /zmaticoo-design（加载本设计规范 skill）
3. get_design_context 读取目标节点，确认现有结构
4. 按第九节组件复用策略，决定每个组件的获取方式
5. 编写 use_figma JavaScript，执行写入
   → 写入规范参考 ./references/FIGMA_API.md
6. 验证返回的 node ID，必要时再次 get_design_context 确认结果
7. 如有异常，读取 error message，修正后重试（不要盲目重试）
```

---

## 十一、常见错误处理

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `font not loaded` | 忘记 loadFontAsync | 在脚本最前面加载所有用到的字体 |
| `figma is not defined` | 文件权限不足 | 确认有 Full seat 且对文件有编辑权限 |
| `Cannot read properties of null` | node ID 不存在 | 先用 get_metadata 确认节点 ID |
| `insertChild` 报错 | 父节点不是 Frame | 确认目标节点类型为 FRAME |
| 写入后尺寸不对 | Auto Layout 未设置 | 检查 layoutMode 和 Sizing Mode |
| `importComponentByKeyAsync` 失败 | key 不正确或无访问权限 | 重新用 search_design_system 确认 key |

---

## 十二、参考文件

- 组件手写规范：`./references/COMPONENTS.md`（手写组件时按需读取）
- Figma 写入 API：`./references/FIGMA_API.md`（写入代码参考）
- 前端代码输出：`./FRONTEND.md`（需要同步输出 Vue3 代码时加载）
- Figma Plugin API：https://developers.figma.com/docs/plugins/api/global-objects/
