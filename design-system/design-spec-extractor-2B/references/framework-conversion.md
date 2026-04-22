# 框架转换规则参考

> 用户确认目标框架后读取本文件，在通用 tokens.css 基础上追加对应转换产物。
> 转换产物不替换 tokens.css，只是额外输出。

---

## A. shadcn/ui

shadcn 使用 HSL 裸值（不含 `hsl()` 包裹），变量名遵循 shadcn 约定。

**HEX → HSL 转换说明**：将提取到的 HEX 转换为 `H S% L%` 三个数值，不加 `hsl()` 包裹。
例：`#1677FF` → `213.1 100% 54.9%`

输出两个文件：

### 文件 1：`design-system/globals.css`

```css
@layer base {
  :root {
    --background:             [H S% L%];  /* ← --color-bg-page */
    --foreground:             [H S% L%];  /* ← --color-text-primary */
    --card:                   [H S% L%];  /* ← --color-bg-card */
    --card-foreground:        [H S% L%];  /* ← --color-text-primary */
    --popover:                [H S% L%];  /* ← --color-bg-modal */
    --popover-foreground:     [H S% L%];  /* ← --color-text-primary */
    --primary:                [H S% L%];  /* ← --color-primary */
    --primary-foreground:     [H S% L%];  /* ← --color-text-inverse */
    --secondary:              [H S% L%];  /* ← --color-secondary */
    --secondary-foreground:   [H S% L%];
    --muted:                  [H S% L%];  /* ← --color-bg-tag */
    --muted-foreground:       [H S% L%];  /* ← --color-text-secondary */
    --accent:                 [H S% L%];  /* ← --color-primary-light */
    --accent-foreground:      [H S% L%];
    --destructive:            [H S% L%];  /* ← --color-error */
    --destructive-foreground: [H S% L%];
    --border:                 [H S% L%];  /* ← --color-border-default */
    --input:                  [H S% L%];  /* ← --color-border-default */
    --ring:                   [H S% L%];  /* ← --color-primary-focus */
    --radius:                 [N]rem;     /* ← --radius-md 换算为 rem（÷16） */
  }
}
```

### 文件 2：`tailwind.config.js`

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        primary:   'hsl(var(--primary))',
        secondary: 'hsl(var(--secondary))',
        success:   '[#HEX]',  /* ← --color-success */
        warning:   '[#HEX]',  /* ← --color-warning */
        error:     '[#HEX]',  /* ← --color-error */
        info:      '[#HEX]',  /* ← --color-info */
      },
      borderRadius: {
        sm:  'calc(var(--radius) - 4px)',
        md:  'var(--radius)',
        lg:  'calc(var(--radius) + 4px)',
        xl:  'calc(var(--radius) + 8px)',
      },
      spacing: {
        unit: '[N]px',  /* ← --spacing-unit */
      },
      fontSize: {
        xs:   ['[N]px', { lineHeight: 'var(--line-height-tight)' }],
        sm:   ['[N]px', { lineHeight: 'var(--line-height-base)' }],
        base: ['[N]px', { lineHeight: 'var(--line-height-base)' }],
        md:   ['[N]px', { lineHeight: 'var(--line-height-base)' }],
        lg:   ['[N]px', { lineHeight: 'var(--line-height-tight)' }],
      },
    }
  }
}
```

---

## B. Tailwind CSS（无组件库）

直接输出 `tailwind.config.js`，使用 HEX 值，无需 HSL 转换。

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT:  '[#HEX]',  /* ← --color-primary */
          hover:    '[#HEX]',
          active:   '[#HEX]',
          disabled: '[#HEX]',
          light:    '[#HEX]',
        },
        success:  '[#HEX]',
        warning:  '[#HEX]',
        error:    '[#HEX]',
        info:     '[#HEX]',
        bg: {
          page:     '[#HEX]',
          card:     '[#HEX]',
          hover:    '[#HEX]',
          selected: '[#HEX]',
          disabled: '[#HEX]',
        },
        text: {
          primary:     '[#HEX]',
          secondary:   '[#HEX]',
          disabled:    '[#HEX]',
          placeholder: '[#HEX]',
        },
        border: {
          default:  '[#HEX]',
          hover:    '[#HEX]',
          focus:    '[#HEX]',
          disabled: '[#HEX]',
          error:    '[#HEX]',
        },
      },
      borderRadius: {
        sm: '[N]px',
        md: '[N]px',
        lg: '[N]px',
        xl: '[N]px',
      },
      boxShadow: {
        sm: '[完整值]',
        md: '[完整值]',
        lg: '[完整值]',
      },
      spacing: {
        /* 补充不在默认 Tailwind 里的间距值 */
      },
    }
  }
}
```

---

## C. Ant Design（React）

输出 `design-system/theme.ts`，格式为 antd `theme.token` 覆盖对象：

```ts
import type { ThemeConfig } from 'antd'

export const theme: ThemeConfig = {
  token: {
    /* Brand */
    colorPrimary:         '[#HEX]',  /* ← --color-primary */
    colorPrimaryHover:    '[#HEX]',
    colorPrimaryActive:   '[#HEX]',

    /* Functional */
    colorSuccess:         '[#HEX]',
    colorWarning:         '[#HEX]',
    colorError:           '[#HEX]',
    colorInfo:            '[#HEX]',

    /* Text */
    colorText:            '[#HEX]',  /* ← --color-text-primary */
    colorTextSecondary:   '[#HEX]',
    colorTextDisabled:    '[#HEX]',
    colorTextPlaceholder: '[#HEX]',

    /* Background */
    colorBgContainer:     '[#HEX]',  /* ← --color-bg-card */
    colorBgLayout:        '[#HEX]',  /* ← --color-bg-page */

    /* Border */
    colorBorder:          '[#HEX]',
    colorBorderSecondary: '[#HEX]',

    /* Typography */
    fontFamily:           '[字体栈]',
    fontSize:             [N],       /* base 字号，数字不带 px */
    lineHeight:           [N],

    /* Radius */
    borderRadius:         [N],       /* md 圆角，数字不带 px */
    borderRadiusSM:       [N],
    borderRadiusLG:       [N],

    /* Spacing */
    padding:              [N],
    paddingSM:            [N],
    paddingLG:            [N],
    margin:               [N],
    marginSM:             [N],
    marginLG:             [N],
  }
}
```

---

## D. Element Plus（Vue）

输出 `design-system/el-variables.css`，覆盖 Element Plus CSS 变量：

```css
:root {
  /* Brand */
  --el-color-primary:           [#HEX];
  --el-color-primary-light-3:   [#HEX];  /* ← --color-primary-hover */
  --el-color-primary-dark-2:    [#HEX];  /* ← --color-primary-active */

  /* Functional */
  --el-color-success:           [#HEX];
  --el-color-warning:           [#HEX];
  --el-color-danger:            [#HEX];  /* ← --color-error */
  --el-color-info:              [#HEX];

  /* Text */
  --el-text-color-primary:      [#HEX];
  --el-text-color-regular:      [#HEX];  /* ← --color-text-secondary */
  --el-text-color-secondary:    [#HEX];
  --el-text-color-placeholder:  [#HEX];
  --el-text-color-disabled:     [#HEX];

  /* Background */
  --el-bg-color:                [#HEX];  /* ← --color-bg-card */
  --el-bg-color-page:           [#HEX];
  --el-bg-color-overlay:        [#HEX];  /* ← --color-bg-modal */

  /* Border */
  --el-border-color:            [#HEX];
  --el-border-color-light:      [#HEX];
  --el-border-color-lighter:    [#HEX];
  --el-border-color-extra-light:[#HEX];

  /* Typography */
  --el-font-size-base:          [N]px;
  --el-font-size-small:         [N]px;
  --el-font-size-large:         [N]px;

  /* Radius */
  --el-border-radius-base:      [N]px;
  --el-border-radius-small:     [N]px;
  --el-border-radius-large:     [N]px;

  /* Shadow */
  --el-box-shadow:              [完整值];
  --el-box-shadow-light:        [完整值];
}
```

---

## E. Naive UI（Vue）

输出 `design-system/themeOverrides.ts`：

```ts
import type { GlobalThemeOverrides } from 'naive-ui'

export const themeOverrides: GlobalThemeOverrides = {
  common: {
    primaryColor:         '[#HEX]',
    primaryColorHover:    '[#HEX]',
    primaryColorPressed:  '[#HEX]',  /* ← --color-primary-active */
    primaryColorSuppl:    '[#HEX]',

    successColor:         '[#HEX]',
    warningColor:         '[#HEX]',
    errorColor:           '[#HEX]',
    infoColor:            '[#HEX]',

    textColor1:           '[#HEX]',  /* ← --color-text-primary */
    textColor2:           '[#HEX]',  /* ← --color-text-secondary */
    textColor3:           '[#HEX]',  /* ← --color-text-disabled */
    placeholderColor:     '[#HEX]',

    bodyColor:            '[#HEX]',  /* ← --color-bg-page */
    cardColor:            '[#HEX]',  /* ← --color-bg-card */
    modalColor:           '[#HEX]',  /* ← --color-bg-modal */

    borderColor:          '[#HEX]',
    dividerColor:         '[#HEX]',

    fontFamily:           '[字体栈]',
    fontSize:             '[N]px',
    borderRadius:         '[N]px',
  }
}
```
