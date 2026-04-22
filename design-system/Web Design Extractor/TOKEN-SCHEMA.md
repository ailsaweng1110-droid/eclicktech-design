# Token Schema — 字段清单参考

生成 `tokens.json` 时按此结构填写。所有字段均为目标值，无法从源码读取时合理推测并加 `_inferred` 备注字段。颜色字段无法确认时保留 `null`。

---

## color

```
color.primary           主品牌色，CTA 按钮
color.primary.hover     主色悬停态
color.primary.foreground  主色上的文字色（通常白色）
color.secondary         辅助品牌色
color.accent            强调/高亮色
color.bg.default        页面主背景
color.bg.subtle         区块底色、次级背景
color.surface           卡片/浮层表面色
color.text.primary      主文字
color.text.secondary    次文字、说明
color.text.disabled     禁用态文字
color.border            默认边框
color.border.strong     强调边框
color.danger            错误/删除
color.success           成功/完成
color.warning           警告/注意
color.info              信息提示
```

提取规则：优先读 `:root` 或 `[data-theme]` 中的 CSS 变量；其次内联样式；最后 Tailwind class 反推。记录 HEX/RGB/HSL 中最完整的格式。

---

## font

```
font.family.display     标题字体
font.family.body        正文字体
font.family.mono        代码字体
font.size.xs            最小号
font.size.sm
font.size.base          正文基准（通常 16px）
font.size.lg
font.size.xl
font.size.2xl
font.size.3xl
font.size.4xl
font.weight.regular     400
font.weight.medium      500
font.weight.semibold    600
font.weight.bold        700
font.lineHeight.tight   标题行高（~1.2）
font.lineHeight.base    正文行高（~1.5）
font.lineHeight.loose   长文行高（~1.8）
font.tracking.tight     标题字距
font.tracking.wide      标签字距
```

---

## space

基准通常为 4px 或 8px，从组件 padding/gap 归纳。

```
space.0  = 0
space.1  最小单位
space.2
space.3
space.4
space.6
space.8
space.10
space.12
space.16
space.20
space.24
```

---

## radius

```
radius.none   = 0
radius.sm     微圆角
radius.base   默认（按钮/输入框）
radius.md
radius.lg     卡片
radius.xl     大卡片/弹窗
radius.full   = 9999px（胶囊）
```

---

## shadow

```
shadow.sm     微阴影（表格行 hover）
shadow.base   卡片默认
shadow.md     卡片 hover / 下拉菜单
shadow.lg     弹窗 / 侧边栏
shadow.xl     全屏遮罩层
```

---

## motion

```
motion.duration.fast    hover/focus 颜色变化（~100ms）
motion.duration.base    位移/展开（~200ms）
motion.duration.slow    页面级动画（~350ms）
motion.easing.default
motion.easing.spring    弹性反弹
motion.easing.enter     快进慢出
motion.easing.exit      快出
```

---

## layout

```
layout.maxWidth.sm
layout.maxWidth.md
layout.maxWidth.lg
layout.maxWidth.xl
layout.maxWidth.content  正文最大宽度（~720px）
layout.grid.columns      通常 12
layout.grid.gutter
layout.breakpoint.sm
layout.breakpoint.md
layout.breakpoint.lg
layout.breakpoint.xl
layout.breakpoint.2xl
```
