# zMaticoo DSP 设计规范文档 v3

> **提取工具**：design-spec-extractor v4.0
> **文件**：zMaticoo-DSP（7da8NWsTXC3o0F5vHRjDfD / 模版画布 4079:61088）
> **生成日期**：2026-04-13（v3，全量 11 页面）
>
> **页面覆盖（11/11）**：注册页 / 创建商务中心 / Adset 创建 / Campaign 表格 / Report / Add Member（含 Drawer+Tag+Tooltip） / 商务中心 / Payment Management / Transactions / Add Balance（Modal）/ App Event
>
> ✅ 设计师已确认：功能色、badge dot 规则、Error 圆角、Modal、按钮尺寸
> ⚠️ 剩余 3 项低优先级推断值，见附录

---

## 一、色彩系统

### 1.1 品牌色

| Token | 色值 | 使用场景 |
|-------|------|---------|
| `--color-primary` | `#0251FF` | 链接/激活/mark/info/badge dot |
| `--color-primary-light` | `#E6F2FF` | 激活导航背景 / Admin tag 背景 |
| `--color-primary-mid` | `#2B75FF` | light/eclicktech/5（辅助蓝）|
| `--color-secondary` | `#262626` | 主操作按钮背景 / 深色文字 |
| `--color-brand-navy-deep` | `#001366` | 顶部导航栏背景 |
| `--color-brand-navy-mid` | `#001E8C` | 注册页底部色带 |
| `--color-brand-sky` | `#7AD3FF` | 注册页左侧装饰背景 |
| `--color-brand-blue` | `#0090FF` | light/bluesky/6 |
| `--color-brand-avatar-bg` | `#26367D` | 顶部导航用户头像背景 |

### 1.2 功能色（✅ 全部设计师确认）

| 类型 | Default | hover | Light 背景 | badge dot |
|------|---------|-------|-----------|-----------|
| **Error** | `#D4004A` ✅ | `#B00039` | `rgba(249,13,88,0.10)` ✅ | `#D4004A` ✅ |
| **Success** | `#00941E` ✅ | `#007A18` | `#E6F9EA` [推断] | `#00941E` ✅ |
| **Warning** | `#D95700` ✅ | `#B84900` | `#FFF3E6` [推断] | `#D95700` ✅ |
| **Info** | `#0251FF` ✅ | `#0244D6` | `#E6F2FF` ✅ | `#0251FF` ✅ |

> ✅ **badge dot 设计师确认：与功能色完全保持一致**，Approved / Active dot 使用 `#00941E`。

### 1.3 状态 dot 映射表

| 状态文字 | dot 色 | 来源 |
|---------|--------|------|
| Approved / Active | `#00941E` | ✅ |
| Rejected / Failed | `#D4004A` | ✅ |
| Under review | `#0251FF` | ✅ |

### 1.4 角色 Tag 色（商务中心成员管理）

| 角色 | 背景 | 文字色 | 样式名 |
|------|------|--------|--------|
| Admin | `#E6F2FF` | `#0251FF` | light/eclicktech/1 + light/eclicktech/6 |
| Operator | `#E6F8FF` | `#0099AD` | light/bluesky/1 + light/Cyan/7 |
| Analyst | `#F4F8E8` | `#587A00` | light/Lime/1 + light/Lime/9 |

### 1.5 中性色

**背景色**

| Token | 色值 | 使用场景 |
|-------|------|---------|
| `--color-bg-page` | `#F5F5F5` | 页面底色 |
| `--color-bg-surface` | `#FAFAFA` | 内容区/表格头/次级面板/dropdown hover |
| `--color-bg-card` | `#FFFFFF` | 卡片/表单/Modal/Drawer |
| `--color-bg-input-addon` | `#FAFAFA` | 输入框 addon 区域（货币单位）|
| `--color-bg-nav-active` | `#E6F2FF` | 激活导航项背景 |
| `--color-bg-tooltip` | `#262626` | Tooltip 背景 |
| `--color-overlay` | `rgba(38,38,38,0.32)` | Modal/Drawer 蒙层 |

**边框色**

| Token | 色值 | 使用场景 |
|-------|------|---------|
| `--color-border-default` | `#D9D9D9` | 输入框/选择器/tag 默认边框 |
| `--color-border-error` | `#D4004A` | error state 边框 / 无效 tag |
| `--color-border-warning` | `#D95700` | warning state 边框 / 警告 tag |
| `--color-border-section` | `#F0F0F0` | 分割线/表格行/section |

**文字色（五级）**

| Token | 色值 | 使用场景 |
|-------|------|---------|
| `--color-text-primary` | `#141414` | 主要文字：标题/表格内容 |
| `--color-text-body` | `#262626` | 正文/输入内容 |
| `--color-text-secondary` | `#8C8C8C` | 次要/ID/导航分组标签/dropdown 描述 |
| `--color-text-placeholder` | `#BFBFBF` | 占位符 |
| `--color-text-inverse` | `#FFFFFF` | 深色背景反色 / Tooltip 文字 |
| `--color-text-link` | `#0251FF` | 链接文字（带下划线）|
| `--color-text-nav-active` | `#0251FF` | 激活导航文字 |

---

## 二、字体系统

**字体族**：`Montserrat`（全站英文），`Noto Sans JP`（日文回退）

| Token | 字号 | 字重 | 行高 | 使用场景 |
|-------|------|------|------|---------|
| `--font-size-xs` | 12px | 500 Medium | 20px | 导航分组标签 / 表格次级文字 / Tag 文字 / 副说明 |
| `--font-size-sm` | 14px | 400/500/600 | 22px | 主要正文 / 表单 / 表格 / Tooltip / 32px 按钮 |
| `--font-size-base` | 16px | 500/600 | 24px | 40px 按钮 / Modal&Drawer 标题 / 导航 |
| `--font-size-md` | 20px | 500/600 | 28px | 卡片标题（Payment management）|
| `--font-size-lg` | 24px | 600 | 32px | 页面主标题 |
| `--font-size-xl` | 40px | 700 | 1.2 | 品牌 hero 大字 |

---

## 三、间距系统

**基础单位**：4px

| 层级 | 值 | 典型场景 |
|------|----|---------|
| xs | 4px | icon 与文字间距 / tag icon-text gap |
| sm | 8px | form label-input / btn gap / table action divider gap |
| md | 16px | 表单项间距 / Modal 内边距 / nav item px |
| lg | 24px | 内容区 padding / Modal header px / Drawer body padding |
| xl | 32px | |
| 5xl | 64px | 顶部导航高度 |

**组件内边距（精确值）**

| 组件 | 规格 |
|------|------|
| 输入框（标准 40px） | `px-12px / py-9px` |
| 输入框（紧凑 32px，Modal/Drawer内） | `px-12px / py-5px` |
| 大按钮 40px | `px-13px / py-8px`，16px Medium |
| 中按钮 32px（含图标/primary/ghost-icon） | `px-13px / py-5px`，14px Medium |
| 中按钮 32px（ghost 无图标） | `px-17px / py-5px`，14px Medium |
| 按钮内 icon-文字 gap | `8px` |
| 角色 Tag | `px-8px / py-1px`，12px Medium |
| 可关闭 Tag | `px-6px / py-1px`，12px Medium |
| Tooltip | `px-8px / py-6px`，14px |
| 表格单元格（双行 55px） | `px-16px / pt-16px / pb-19px` |
| 表格单元格（单行 47px） | `px-16px / pt-12px / pb-13px` |
| 表格头 | `px-16px / pt-12px / pb-13px` |
| Modal header | `px-24px / py-16px` |
| Modal content | `px-24px / pt-16px / pb-24px` |
| Modal footer | `px-16px / py-12px` |
| Drawer header | `px-24px / py-16px` |
| Drawer body | `p-24px` |
| Drawer footer | `px-24px / py-16px` |
| 导航项 | `px-16px`，高 40px |
| 导航分组标签 | `px-16px / py-4px` |

---

## 四、圆角系统

| Token | 值 | 使用组件 |
|-------|----|---------| 
| `--radius-xs` | 2px | ✅ **Modal / Drawer / Tooltip / Tag / Dropdown / Popconfirm / pagination** |
| `--radius-sm` | **4px** | ✅ **主圆角**：按钮 / 输入框（error state 已确认统一）/ tag-closable |
| `--radius-md` | 8px | ✅ 内容子卡片 / 用户头像 / dropdown item icon |
| `--radius-lg` | 12px | ✅ 主内容区容器 |
| `--radius-nav-active` | 20px | ✅ 导航激活项 pill |
| `--radius-panel` | 24px | ✅ 注册页侧面板 |
| `--radius-badge` | 100px | ✅ 状态 badge dot |

---

## 五、阴影系统

| Token | 值 | 使用场景 |
|-------|----|---------|
| `--shadow-popup` | `0px 3px 6px -4px rgba(0,0,0,0.12), 0px 6px 16px 0px rgba(0,0,0,0.08), 0px 9px 28px 8px rgba(0,0,0,0.05)` | ✅ **Modal / Drawer / Dropdown / Popconfirm**，Figma：drop-shadow/0.12+0.8+0.5 |
| `--shadow-tooltip` | `0px 2px 8px rgba(0,0,0,0.15)` | ✅ Tooltip，Figma：drop-shadow/0.15 |
| `--shadow-error-ring` | `0px 0px 0px 2px rgba(249,13,88,0.10)` | ✅ error + focus ring |
| `--shadow-border-top` | `inset 0px 1px 0px 0px #F0F0F0` | ✅ Modal footer / Drawer footer 顶部边线 |
| `--shadow-border-bottom` | `inset 0px -1px 0px 0px #F0F0F0` | ✅ Modal header / Drawer header 底部边线 |
| `--shadow-sm/md/lg` | — | [推断] 待补充卡片 hover 状态 |

---

## 六、布局系统

| 属性 | 值 |
|------|----|
| 页面最大宽度 | 1440px |
| 顶部导航高度 | 64px |
| 内容区 padding | 24px |
| 主内容区圆角 | 12px |
| 主内容区背景 | `#FAFAFA`（border `#F0F0F0`）|
| 左侧导航宽度 | 224px（商务中心）/ 226px（Adset）|
| Modal 宽度 | 640px |
| Drawer 宽度 | 800px |

---

## 七、组件规范

### 7.1 按钮（四尺寸体系 ✅）

| 尺寸 | 高度 | 内边距 | 字体 | 使用场景 |
|------|------|--------|------|---------|
| **XL 大** | 40px | `13px 8px` | 16px Medium | 注册/"Continue"/"Complete"等主 CTA |
| **MD 中-Primary** | 32px | `13px 5px` | 14px Medium | Modal Confirm / 表格操作区 |
| **MD 中-Ghost** | 32px | `17px 5px`（无图标）/ `13px 5px`（含图标）| 14px Medium | Modal Cancel / Export 等次级操作 |
| **SM 小** | 24px | `4px 8px` [推断] | 14px | 表格行内 inline 操作按钮 |
| **Link** | auto(inline) | `2px H` | 14px Medium `#0251FF` | 行内链接/"Sign in"等 |

**按钮变体**

| 变体 | 背景 | 边框 | 文字 | 圆角 |
|------|------|------|------|------|
| Primary（深色） | `#262626` | `#262626` | `#FFFFFF` | 4px |
| Ghost/Secondary | `#FFFFFF` | `#262626` | `#262626` | 4px |
| Link/Text | 透明 | 无 | `#0251FF` | 4px |

> 按钮内图标尺寸：14×14px，icon-文字 gap：8px

### 7.2 Modal

| 属性 | 值 |
|------|----|
| 宽度 | 640px |
| 圆角 | 2px |
| 背景 | `#FFFFFF` |
| 阴影 | `--shadow-popup` |
| 蒙层 | `rgba(38,38,38,0.32)` |
| Header | `px-24px py-16px`，标题 16px SemiBold，关闭图标右侧 16×16px |
| Header 底线 | `--shadow-border-bottom`（inset）|
| Content | `px-24px pt-16px pb-24px`，gap 16px |
| Footer | `px-16px py-12px`，justify-end，button-group gap 8px |
| Footer 顶线 | `--shadow-border-top`（inset）|

### 7.3 Drawer（侧边弹出层）

| 属性 | 值 |
|------|----|
| 宽度 | 800px |
| 高度 | 全屏（900px）|
| 位置 | 右侧滑入 |
| 圆角 | 无（全屏高度）|
| 背景 | `#FFFFFF` |
| 阴影 | `--shadow-popup`（同 Modal）|
| 蒙层 | `rgba(38,38,38,0.32)` |
| Header | `px-24px py-16px`，关闭图标**左侧** 16×16px，标题 16px SemiBold |
| Header 底线 | `--shadow-border-bottom`（inset）|
| Body | `p-24px`，gap 24px |
| Footer | `px-24px py-16px`，border-top `#F0F0F0`，justify-end，gap 12px |

### 7.4 Tag（标签）

**角色 Tag（不可关闭）**

| 角色 | 背景 | 文字色 | 圆角 | 内边距 | 字体 |
|------|------|--------|------|--------|------|
| Admin | `#E6F2FF` | `#0251FF` | 2px | `px-8px py-1px` | 12px Medium |
| Operator | `#E6F8FF` | `#0099AD` | 2px | `px-8px py-1px` | 12px Medium |
| Analyst | `#F4F8E8` | `#587A00` | 2px | `px-8px py-1px` | 12px Medium |

**Tag/Closable（可关闭，多值输入）**

| 状态 | 背景 | 边框 | 文字色 | 圆角 | 内边距 |
|------|------|------|--------|------|--------|
| Normal | `#FAFAFA` | `#D9D9D9` | `#262626` | 2px | `px-6px py-1px` |
| Error（无效值）| `#FAFAFA` | `#D4004A` | `#262626` | 2px | `px-6px py-1px` |
| Warning（警告）| `#FAFAFA` | `#D95700` | `#262626` | 2px | `px-6px py-1px` |

### 7.5 Tooltip

| 属性 | 值 |
|------|----|
| 背景 | `#262626`（Tooltip/.85）|
| 文字 | `#FFFFFF`，14px Regular/Medium |
| 圆角 | 2px |
| 内边距 | `px-8px py-6px` |
| 阴影 | `0px 2px 8px rgba(0,0,0,0.15)` |
| 箭头 | 8px 正方形旋转 45°，bg `#262626`，border-radius 2px |

### 7.6 Dropdown Menu

| 属性 | 值 |
|------|----|
| 背景 | `#FFFFFF` |
| 圆角 | 2px |
| 阴影 | `--shadow-popup` |
| 外边距（y）| `py-4px` |
| 普通 item | `px-16px py-12px`，bg 透明 |
| Hover item | bg `#FAFAFA` |
| Active item | bg `#E6F2FF` |
| Icon 容器 | 40×40px，bg white，border `#F0F0F0`，radius 4px |

### 7.7 表格（Table）

| 元素 | 规格 |
|------|------|
| 表头 | bg `#FAFAFA`，`pt-12px pb-13px px-16px`，border-bottom `#F0F0F0`，14px Medium `#262626` |
| 数据行（双行，55px）| `pt-16px pb-19px px-16px`，主文字 14px Regular `#141414`，次文字 12px Medium `#8C8C8C` |
| 数据行（单行，47px）| `pt-12px pb-13px px-16px`，14px Regular `#141414` |
| 操作列 | 链接文字 14px Regular `#141414` + 下划线，分隔用 `#F0F0F0` divider（高 12px）|
| 行分割线 | `#F0F0F0` |
| Checkbox / Switch | 左侧固定列 |

### 7.8 侧边导航（Inline Menu）

| 属性 | 值 |
|------|----|
| 宽度 | 224px |
| 分组标签 | 12px Medium `#8C8C8C`，`px-16px py-4px` |
| 导航项高度 | 40px，`px-16px` |
| 图标 | 16×16px，与文字 gap 8px |
| **激活态** | bg `#E6F2FF`，文字 `#0251FF` SemiBold，radius 20px（pill）|
| 非激活态 | bg 透明，文字 `#262626` Medium |

### 7.9 状态 Badge（badge/dot）

| 规格 | 值 |
|------|----|
| dot 尺寸 | 6×6px |
| dot 圆角 | 100px（完整圆形）|
| 与文字间距 | 8px |
| 文字 | 14px Regular `#141414` |

---

## 附录

### 已解决问题汇总

| 问题 | 解决方案 |
|------|---------|
| Error state 圆角 2px vs 4px | ✅ 统一为 4px |
| 功能色未确认 | ✅ S=#00941E / W=#D95700 / I=#0251FF |
| badge dot 规则 | ✅ 与功能色完全一致，Approved / Active = `#00941E` |
| Modal 规范 | ✅ 完整提取 |
| 按钮尺寸 | ✅ 四尺寸：40px / 32px-Primary / 32px-Ghost / 24px |
| Drawer 规范 | ✅ 完整提取（Add Member 页）|
| Tag 规范 | ✅ 角色 tag + 可关闭 tag |
| Tooltip 规范 | ✅ 完整提取 |
| 页面覆盖率 | ✅ 11/11 |

### 仍为推断值（低优先级）

| 维度 | 值 | 建议 |
|------|----|----|
| border-hover/focus 色 | `#0251FF`（推断）| 补充输入框 hover/focus 交互态稿 |
| success-light / warning-light | `#E6F9EA` / `#FFF3E6`（推断）| 补充 Toast/通知组件稿 |
| shadow-sm / shadow-md | 推断 | 补充卡片 hover 效果稿 |

---

*生成工具：design-spec-extractor v4.0 | 需要转换为 shadcn/Tailwind/AntD 等框架格式，请告知。*
