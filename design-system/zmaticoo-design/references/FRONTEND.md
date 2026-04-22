# zMaticoo DSP 前端代码输出规范

> 当需要同时输出设计稿 + 前端代码时加载本文件。
> 设计规范以 `SKILL.md` 为准，本文件只负责代码侧约定。

---

## 一、技术栈

```
框架：      Vite + Vue3 (Composition API + <script setup>)
语言：      TypeScript
组件库：    ant-design-vue（与 Figma 组件库风格对齐，优先使用）
状态管理：  Pinia
接口调用：  axios，统一封装，从 @/utils/request 引入
样式方案：  scoped style + Less 变量覆盖 ant-design-vue 主题
```

---

## 二、Design Token 映射（Figma → Less 变量）

> 生成代码时使用变量名，不得硬编码 HEX 值。

| 用途 | Figma HEX | Less 变量 |
|------|-----------|----------|
| 主品牌蓝 / Primary | `#0251FF` | `@primary-color` |
| Error | `#D4004A` | `@error-color` |
| Success | `#00941E` | `@success-color` |
| Warning | `#D95700` | `@warning-color` |
| 主要文字 | `#141414` | `@heading-color` |
| 正文文字 | `#262626` | `@text-color` |
| 次要文字 | `#8C8C8C` | `@text-color-secondary` |
| 占位符 | `#BFBFBF` | `@disabled-color` |
| 默认边框 | `#D9D9D9` | `@border-color-base` |
| 分割线 | `#F0F0F0` | `@border-color-split` |
| 页面底色 | `#F5F5F5` | `@layout-body-background` |
| 内容区背景 | `#FAFAFA` | `@table-header-bg` |
| 卡片/白色背景 | `#FFFFFF` | `@component-background` |
| 顶部导航背景 | `#001366` | `@layout-header-background` |
| 注册页左侧面板背景 | `#7AD3FF` | `@bluesky-3` |
| 注册页底部深蓝色带 | `#001E8C` | `@eclicktech-9` |
| Info/Alert 强调色（文字/边框） | `#003DD9` | `@eclicktech-7` |
| Info/Alert 背景色 | `#E6F2FF` | `@eclicktech-1` |

> ⚠️ 待确认：上述 Less 变量名为 ant-design-vue 默认变量，需与项目实际配置核对后更新。

---

## 三、Figma 组件 → ant-design-vue 组件对应

| Figma 组件 | ant-design-vue 组件 |
|-----------|-------------------|
| `button` | `<a-button>` |
| `input` | `<a-input>` |
| `select` | `<a-select>` |
| `table/column-based` | `<a-table>` |
| `modal/basic` | `<a-modal>` |
| `drawer` | `<a-drawer>` |
| `form` | `<a-form>` |
| `date-picker` | `<a-date-picker>` |
| `pagination` | `<a-pagination>` |
| `badge/status` | `<a-badge>` |
| `tag/default` | `<a-tag>` |
| `tabs/top` | `<a-tabs>` |
| `alert` | `<a-alert>` |
| `tooltip` | `<a-tooltip>` |
| `steps` | `<a-steps>` |
| `upload` | `<a-upload>` |

---

## 四、Vue3 组件代码模板

```vue
<template>
  <div class="page-container">
    <!-- 页面内容 -->
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { message } from 'ant-design-vue'
// import request from '@/utils/request'

// Props（如有）
// const props = defineProps<{ id: string }>()

// 响应式数据
const loading = ref(false)
const dataSource = reactive<DataItem[]>([])

// 类型定义
interface DataItem {
  id: string
  name: string
}

// 方法
const handleSubmit = async () => {
  try {
    loading.value = true
    // await request.post('/api/xxx', data)
    message.success('操作成功')
  } catch (e) {
    message.error('操作失败，请重试')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  // 初始化
})
</script>

<style scoped lang="less">
.page-container {
  padding: 24px;
  background: @layout-body-background;
}
</style>
```

---

## 五、代码生成规则

1. **组件优先**：优先使用 ant-design-vue 组件，不手写基础 UI
2. **尺寸**：按钮默认 `size="middle"`（32px），表单场景 `size="large"`（40px）
3. **样式**：颜色/间距使用 Less 变量，不硬编码
4. **类型**：接口数据定义 interface，Props 用 `defineProps<T>()`
5. **状态**：简单值用 `ref`，复杂对象用 `reactive`
6. **错误**：统一 try/catch，用 `message.error()` 提示

---

## 六、设计 + 代码同步输出流程

```
用户描述需求
    ↓
① 按 SKILL.md 第九节策略写入 Figma 设计稿
    ↓
② 基于相同规范输出 Vue3 组件代码
   · 颜色/间距/圆角 → 使用第二节 Less 变量
   · 组件 → 使用第三节对应的 ant-design-vue 组件
    ↓
前端补充：接口联调 + 业务逻辑
```
