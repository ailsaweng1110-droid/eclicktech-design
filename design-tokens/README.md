# design-tokens

多品牌设计 Token 包，与 Figma Variables 对齐；**消费入口为 `dist/*.tokens.json`**。


| 路径                              | 说明                                       |
| ------------------------------- | ---------------------------------------- |
| `tokens.json`                   | 全品牌共用底座                                  |
| `brands/<brand>.json`           | 各品牌覆盖（light / dark 语义、layout、typography） |
| `scripts/build-brand-tokens.js` | 合并生成 `dist`                              |
| `dist/<brand>.tokens.json`      | **给前端的交付文件**                             |


## 前端取用

**方式一：GitHub Raw（按 Tag 锁版本，推荐）**

将 `<TAG>` 换成发布标签（如 `tokens-v0.1.0`）：

`https://raw.githubusercontent.com/ailsaweng1110-droid/eclicktech-design/<TAG>/design-tokens/dist/eclicktech.tokens.json`

其余品牌：文件名改为 `cyberklick.tokens.json`、`yeahmobi.tokens.json`、`zmaticoo.tokens.json`。

**方式二：npm（需研发配置 registry 与发包权限后）**

```bash
npm install @eclicktech-design/tokens@0.1.0
```

```js
import eclicktech from "@eclicktech-design/tokens/eclicktech";
```

## 构建

```bash
cd design-tokens
npm run build
```

## 设计协作

见 [CONTRIBUTING.md](./CONTRIBUTING.md)。**包名 / Tag / 版本约定**见 [NAMING.md](./NAMING.md)。品牌与 Figma 语义见 [brands/README.md](./brands/README.md)。**Ant Design / Shadcn 映射表（骨架）**见 [MAPPING.md](./MAPPING.md)。

## Tag vs npm（给团队看的结论）

- **只打 Tag、用 Raw URL**：零 npm 配置，适合先跑起来；版本 = Git tag。  
- **发 npm 包**：适合多仓库、多产品统一 `npm install` 升级；需要 registry 与发包流程。  
- 当前规模（4 品牌 × 多产品 × 3 设计师）可先 **Tag + Raw**，稳定后再上 npm。

