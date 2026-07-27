# 桌面 → 移动端转换代码模式（Tailwind）

每个模式给出「桌面原样」与「适配后」。适配后代码采用移动优先：默认样式即手机，`md:`/`lg:` 叠加大屏。**注意：桌面（≥1024px）渲染结果不得改变——为移动端改基准值时用 `lg:` 锁定原桌面值。**

## 页面容器

```html
<!-- 桌面原样：固定大留白 -->
<div class="max-w-screen-xl mx-auto px-24">...</div>

<!-- 适配后（桌面仍是 px-8 级别留白，此处按规范统一为 lg:px-8） -->
<div class="mx-auto w-full max-w-screen-xl px-4 md:px-6 lg:px-8">...</div>
```

## 多列网格 → 单列（桌面列数不变）

```html
<!-- 桌面原样 -->
<div class="grid grid-cols-3 gap-8">...</div>

<!-- 适配后：桌面仍 3 列 -->
<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3 lg:gap-8">...</div>
```

## 横排两栏（图文）→ 竖排堆叠

```html
<!-- 桌面原样 -->
<section class="flex items-center gap-12">
  <div class="w-1/2">文字</div>
  <div class="w-1/2"><img ... /></div>
</section>

<!-- 适配后：手机文字在上、图在下；桌面仍横排 -->
<section class="flex flex-col gap-6 md:flex-row md:items-center md:gap-12">
  <div class="w-full md:w-1/2">文字</div>
  <div class="w-full md:w-1/2"><img class="w-full h-auto" ... /></div>
</section>
```

## 标题字号（全站统一）

```html
<!-- H1：全站所有 H1 用同一组类 -->
<h1 class="text-3xl font-bold leading-tight text-balance md:text-5xl lg:text-6xl">标题</h1>

<!-- H2：全站所有 H2 用同一组类 -->
<h2 class="text-2xl font-bold leading-tight md:text-3xl lg:text-4xl">标题</h2>

<!-- 正文：全站统一 -->
<p class="text-base leading-relaxed text-pretty lg:text-lg">正文</p>
```

不要逐页给标题设不同尺寸；如需变体，在设计系统里定义命名变体后复用。

## 区块间距

```html
<!-- 桌面原样 -->
<section class="py-32">...</section>

<!-- 适配后：桌面仍大间距 -->
<section class="py-12 md:py-16 lg:py-24">...</section>
```

## 图片：保持原比例等比缩小

```html
<!-- 正确：按容器宽度等比缩小，比例不变、不裁切、不拉伸 -->
<img src="hero.jpg" class="w-full h-auto" />

<!-- 响应式图源：手机加载小图，比例仍不变 -->
<img src="hero-800.jpg"
     srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1600.jpg 1600w"
     sizes="(max-width: 768px) 100vw, 50vw"
     class="w-full h-auto" />

<!-- 避免：固定高度 + object-cover 会裁切/改变观感，非必要不用 -->
<!-- <img class="w-full h-[600px] object-cover" /> -->
```

## 整幅媒体：移动端满宽出血（标题用实时文本）

```html
<!-- 文字用带边距的容器；整图容器不加侧边距，边到边出血 -->
<section class="py-12 md:py-16">
  <div class="mx-auto w-full max-w-screen-xl px-4 md:px-6">
    <span class="inline-flex w-fit self-start rounded-full px-3 py-1.5 ...">INDUSTRIAL</span>
    <h2 class="mt-4 ...">Where North Powers Real-World Automation</h2>
  </div>
  <div class="mx-auto mt-6 w-full max-w-[1920px]">
    <img src="/map-mobile.png" alt="..." class="h-auto w-full" />
  </div>
</section>
```

## 「文字烤进图片」的区块：移动端拆成 实时文字 + 无文字图

```html
<!-- 桌面：带文字大图，全宽 -->
<!-- 移动：无文字纯图 + HTML 实时标题（避免图内文字太小/重复） -->
<img src="/banner-mobile.png"  alt="..." class="h-auto w-full lg:hidden" />
<img src="/banner-desktop.jpg" alt="..." class="hidden h-auto w-full lg:block" />
```

## 整段合成图 ≠ 单栏插画（裁切 / 按节点导出）

```html
<!-- 错误：把左右栏都烤进的 section 截图塞进右栏 → 文案重复、比例错 -->
<!-- <img src="/section-full-1920x900.png" /> -->

<!-- 正确：只用插画节点导出（或裁右半），左栏 HTML 实时文案 -->
<section class="grid lg:grid-cols-2">
  <div class="...">标题 / 列表 / CTA（HTML）</div>
  <img src="/panel-illustration-only.png" alt="" class="h-auto w-full" />
</section>
```

## Logo 条 / 跑马灯：外框 + 字形双缩

```html
<!-- 错误：手机仍接近桌面卡尺寸 -->
<!-- <div class="flex h-24 min-w-[232px] ..."><img class="h-8 w-[148px]" /></div> -->

<!-- 正确：外框与字形都按断点缩小，lg 锁回稿面 -->
<div class="overflow-hidden">
  <div class="flex w-max gap-2 md:gap-3 lg:gap-4 animate-[marquee_28s_linear_infinite]">
    <div class="flex h-14 w-[128px] shrink-0 items-center justify-center rounded-lg border
                md:h-20 md:w-[180px] lg:h-24 lg:w-[232px] lg:rounded-xl">
      <img src="/partner.svg" alt=""
           class="h-5 w-[82px] md:h-7 md:w-[110px] lg:h-[38px] lg:w-[148px]" />
    </div>
    <!-- 其余 logo 同构；行内复制两份做无缝跑马灯 -->
  </div>
</div>
```

## 多层品牌标：叠放 + 阅读顺序

```html
<!-- 对照截图：彩色 X 两片叠同一槽，再 OO、再 M —— 不要按文件名横排 -->
<a href="/" class="inline-flex items-center gap-1" aria-label="Brand">
  <span class="relative inline-flex size-5 shrink-0 lg:size-6">
    <img src="/mark-blue.svg" alt="" class="absolute inset-0 size-full" />
    <img src="/mark-green.svg" alt="" class="absolute inset-0 size-full" />
  </span>
  <img src="/letters-oo.svg" alt="" class="h-5 w-[37px] lg:h-6 lg:w-[44px]" />
  <img src="/letter-m.svg" alt="" class="h-5 w-[30px] lg:h-6 lg:w-[36px]" />
</a>
```

## 1920 绝对定位 → 流式两栏（避免 1440 重叠）

```html
<!-- 错误：lg 起 absolute 左图 + 定宽右文，1440 会撞 -->
<!-- <div class="relative">
  <img class="absolute left-0 w-[440px]" />
  <div class="ml-auto max-w-[960px]">...</div>
</div> -->

<!-- 正确：flex 流式；文案 min-w-0 防撑破 -->
<div class="flex flex-col gap-10 lg:flex-row lg:items-start lg:gap-10 xl:gap-16">
  <img src="/globe.png" alt="" class="mx-auto w-full max-w-md shrink-0 lg:mx-0 lg:max-w-[min(40%,420px)]" />
  <div class="min-w-0 flex-1">...</div>
</div>
```

## 桌面半展开双态 → 手机 tab（桌面不加手机 tab）

```html
<!-- 手机：分段器；切换时换 title + points -->
<div class="flex gap-2 self-start rounded-full bg-white/15 p-1 lg:hidden">
  <button class="min-h-11 rounded-full px-4 ...">Advertiser</button>
  <button class="min-h-11 rounded-full px-4 ...">Publisher</button>
</div>

<!-- 桌面：稿面形态——当前态全文 + 下方可点的另一态标题 -->
<button type="button" class="hidden border-t pt-8 text-left text-white/50 lg:block"
        onclick="switchTab()">For Publisher-Traffic Monetization</button>
```

## 轮播箭头必须能滚 / 能切

```html
<div ref={scrollerRef} class="flex gap-6 overflow-x-auto scroll-smooth">...</div>
<button type="button" class="inline-flex h-12 w-[90px] ..."
        onclick="scrollerRef.scrollBy({ left: -664, behavior: 'smooth' })">
  ←
</button>
<button type="button" class="inline-flex h-12 w-[90px] ..."
        onclick="scrollerRef.scrollBy({ left: 664, behavior: 'smooth' })">
  →
</button>
<!-- 禁止：两枚 <span> 装饰箭头无 onClick / 无 scroll -->
```

## 按钮组

```html
<!-- 桌面原样 -->
<div class="flex gap-4">
  <a class="px-6 py-2 ...">主 CTA</a>
  <a class="px-6 py-2 ...">次要</a>
</div>

<!-- 适配后：手机全宽竖排，触控区 ≥44px；桌面仍横排 -->
<div class="flex flex-col gap-3 md:flex-row">
  <a class="w-full md:w-auto min-h-11 inline-flex items-center justify-center px-6 ...">主 CTA</a>
  <a class="w-full md:w-auto min-h-11 inline-flex items-center justify-center px-6 ...">次要</a>
</div>
```

## 行内/次级按钮：自适应宽度，别撑满

```html
<!-- 「查看更多 / 播放视频」这类短操作：自适应宽度靠左，不要 w-full -->
<!-- 在 flex 列里必须 self-start，否则被 align-items:stretch 拉满 -->
<div class="flex flex-col gap-4">
  <a class="inline-flex min-h-11 items-center gap-2 self-start rounded-full px-6 ...">
    查看更多
  </a>
</div>
```

## 标签胶囊 / badge：收缩包裹文字

```html
<!-- 陷阱：inline-flex 的小标签在 flex 列里会被拉成整行满宽 -->
<!-- 修复：加 w-fit / self-start，按内容收缩靠左 -->
<div class="flex flex-col gap-4">
  <span class="inline-flex w-fit self-start rounded-full px-3 py-1.5 text-sm ...">OUR MISSION</span>
  <h2 class="...">区块标题</h2>
</div>
```

## 导航栏 → 汉堡菜单（桌面导航不变）

```html
<header class="flex items-center justify-between px-4 py-3 md:px-8">
  <a class="font-bold">Logo</a>

  <!-- 桌面链接：保持原样 -->
  <nav class="hidden md:flex md:items-center md:gap-8">
    <a href="#">首页</a><a href="#">产品</a><a href="#">关于</a>
    <a class="min-h-11 inline-flex items-center px-4 ...">联系我们</a>
  </nav>

  <!-- 移动端汉堡 icon，点击展开，触控区 ≥44px -->
  <button class="md:hidden inline-flex h-11 w-11 items-center justify-center"
          aria-label="打开菜单" aria-expanded="false">☰</button>
</header>

<!-- 移动端抽屉：默认隐藏，点击后显示；每项 ≥44px 高 -->
<div class="fixed inset-0 z-50 hidden bg-white p-6 md:hidden" data-mobile-menu>
  <nav class="flex flex-col gap-2">
    <a href="#" class="flex min-h-11 items-center border-b">首页</a>
    <a href="#" class="flex min-h-11 items-center border-b">产品</a>
    <a href="#" class="flex min-h-11 items-center border-b">关于</a>
  </nav>
</div>
```

此导航应作为**全站共享组件**，每页复用同一份；React/Next 里用 `useState` 控制抽屉开关。

## 表格 → 移动端卡片 / 横向滚动

```html
<!-- 方案 A：横向滚动兜底 -->
<div class="overflow-x-auto">
  <table class="min-w-[640px] w-full">...</table>
</div>

<!-- 方案 B（更佳）：手机隐藏表格、显示卡片堆叠 -->
<table class="hidden md:table w-full">...</table>
<div class="grid gap-3 md:hidden">
  <div class="rounded border p-4"><span class="font-medium">列名：</span>值</div>
</div>
```

## 页脚：移动端「分组名在左 / 链接在右」两列行式

```html
<!-- 桌面多列（lg:grid-cols-6）；移动端每组一行，标签左、链接右 -->
<div class="grid grid-cols-1 gap-4 lg:grid-cols-6 lg:gap-8">
  <!-- 每个分组：移动 flex-row(左右两列)，桌面 lg:flex-col(标签在上) -->
  <div class="flex flex-row gap-4 lg:flex-col lg:gap-8">
    <p class="w-1/2 shrink-0 text-sm text-muted lg:w-auto">Products</p>
    <ul class="flex w-1/2 flex-col gap-1 lg:w-auto">
      <li><a class="inline-flex min-h-11 items-center ...">Wave</a></li>
      <li><a class="inline-flex min-h-11 items-center ...">North</a></li>
    </ul>
  </div>
  <!-- 其余分组同构 -->
</div>

<!-- 底部：移动端 Logo+CTA 同一行；社媒/条款/版权居中 -->
<div class="flex flex-row items-center justify-between gap-4">
  <a><img src="/logo.svg" class="h-6 w-auto lg:h-10" /></a>
  <a class="inline-flex min-h-11 shrink-0 items-center rounded-full px-6 ...">Talk to Our Team</a>
</div>
<div class="flex flex-col items-center gap-4 lg:flex-row lg:justify-between">
  <div class="flex items-center justify-center gap-2"><!-- 社媒 icon --></div>
  <div class="flex flex-col items-center gap-1 lg:flex-row lg:gap-3">
    <div class="flex items-center gap-3 lg:contents"><a>Terms</a><a>Privacy</a></div>
    <p class="text-center">© 2026 …</p>
  </div>
</div>
```

## 公共组件（导航/页脚）复用

```jsx
// 抽成共享组件，每页导入同一份，保证全站移动端适配一致
// components/SiteHeader.tsx, components/SiteFooter.tsx
export default function Page() {
  return (
    <>
      <SiteHeader />
      <main>...</main>
      <SiteFooter />
    </>
  );
}
```

## hover 交互的触摸替代

```html
<!-- 桌面 hover 显示的下拉，改为点击切换，保证触摸端可用 -->
<div class="group relative">
  <button aria-expanded="false" class="min-h-11">菜单</button>
  <!-- 用 JS 切换 hidden，而非仅依赖 group-hover -->
  <div class="hidden group-hover:md:block ...">...</div>
</div>
```
