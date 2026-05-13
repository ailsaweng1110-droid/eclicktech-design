# 网页 / 官网 GUI 长图裁剪与清理工作流

本文档服务于**官网首页 / Landing Page / Web App 全页截图**类的 GUI 外观设计专利。
当用户提及"官网"、"官网首页"、"Landing Page"、"网页 GUI 长图"、"按模块切片"时，按此文档执行。

如果是 App / 小程序 / 多页流程的 GUI（每个状态本来就是独立一屏），不需要这套裁剪逻辑，
按主 `SKILL.md` 的 Phase 1-6 走常规流程即可。

## 触发条件

满足以下任意一条即按此分支处理：

1. 用户上传**单张纵向特长截图**（高:宽 > 2:1，且高度 > 3000 px）
2. 用户文字描述提到"官网"、"主页"、"网页"、"Landing"、"H5 长页"
3. 用户上传 Figma / Sketch / XD 的整页导出图，作为 GUI 专利材料

## 第一步：源图质量校验（硬要求）

| 项目 | 最低 | 推荐 |
| --- | --- | --- |
| 宽度 | ≥ 1440 px | ≥ 1920 px |
| 整体高度 | ≥ 3000 px | ≥ 4000 px |
| 单个模块裁出后高度 | ≥ 500 px | ≥ 800 px |
| 文件格式 | PNG / 高质量 JPG | 无损 PNG |

低于最低值时**先告知用户重新提供**，不要用低清图勉强切。低清图切出来文字糊掉，
会触发 CNIPA「图面不清楚」补正通知。

来源建议：
- **Figma**：File → Export Frame → PNG @ 2x，宽度按设计稿原宽
- **Chrome DevTools**：设备模式设 1920 宽，Cmd+Shift+P → "Capture full size screenshot"
- **Firefox**：右键 → "Take a screenshot" → 整页

## 第二步：状态拆分模板

网页类 GUI 的常见状态拆分（≈ 6-10 张）：

| 编号 | 状态名 | 说明 |
| --- | --- | --- |
| 01 | 首页默认态首屏 | 首个 viewport，含顶部导航 + Hero + 主 CTA |
| 02..N | 功能介绍模块视图 | 每个核心模块一张（图文左右交替 / 上下分区） |
| N+1 | 技术方案 / 流程图模块视图 | 通常背景色切换为浅色 |
| N+2 | 客户案例 / 数据墙视图 | Logo 墙 / 数字墙 / 案例卡片 |
| 末张 | 联系表单 / 底部 CTA + Footer 视图 | 深色通栏 + 表单 + 版权 |

**判定分界点**的优先级：

1. **背景色突变**：白 → 浅蓝 → 深灰，是最可靠的分界信号
2. **大字标题位置**：每个新模块通常有一个大号居中或左对齐标题
3. **等距留白带**：模块之间有显著的纵向留白（通常 ≥ 120 px）
4. **视觉分组容器**：圆角卡片、横向分割线

## 第三步：用脚本执行

### 3.1 自动检测候选分界（首次摸索）

```bash
python scripts/crop_long_screenshot.py \
  --input  ./assets/官网长图.png \
  --auto-detect \
  --output-config ./crop-config.draft.json \
  --preview ./crop-preview.jpg
```

产物：
- `crop-config.draft.json` — 候选 segments 数组（每段一个 y0/y1 + 占位 name）
- `crop-preview.jpg` — 600px 宽预览图，红线标注每条候选分界

**自动检测必须人工 review**：
- 修正每段的 `name`（如 "首页默认态首屏"、"增长模型模块视图"）
- 微调 `y0` / `y1`（精确到 ± 20 px 即可）
- 删掉误判的分界
- 合并过细的分段

### 3.2 精确切片（最终交付前）

完成 review 后重命名 draft 为 `crop-config.json`，运行：

```bash
python scripts/crop_long_screenshot.py \
  --input  ./assets/官网长图.png \
  --segments ./crop-config.json \
  --output-dir ./dist/jpg
```

输出 `dist/jpg/变化状态图01_<名称>.jpg`、`02_*`…

### 3.3 精确定位分界（自动检测不准时）

```python
from PIL import Image
im = Image.open("源图.png").convert("RGB")
def avg(y):
    row = im.crop((0, y, im.width, y+1)).getdata()
    rs, gs, bs = zip(*row)
    n = len(rs)
    return (sum(rs)//n, sum(gs)//n, sum(bs)//n)

# 在可疑分界附近以 50 像素步长扫描，找色彩跳变
for y in range(8200, 8800, 50):
    print(y, avg(y))
```

肉眼找跳变点（如白色 255,255,255 → 浅蓝 245,248,255）。

## 第四步：截图杂质清理

整页长截图常带"瞬时 UI 噪点"，专利图必须清掉：

| 噪点类型 | 清理方式 |
| --- | --- |
| 鼠标光标（箭头/手形） | `clean_cursor_artifact.py` 同 y 高度采样替换 |
| 悬停态残影（按钮 hover、菜单下拉重叠） | 同上 |
| 截屏工具 bug 导致的重复元素 | 同上 |
| 浏览器自身 UI（滚动条、地址栏阴影） | 裁切 |
| Cookie / GDPR 横幅 | 关闭后重新截图，或大块替换 |

清理示例：

```bash
python scripts/clean_cursor_artifact.py \
  --input ./assets/原图.png \
  --target 3035,50,3110,135 \
  --sample 1800,50,1875,135 \
  --output ./assets/原图-clean.png
```

清理后再用 `--input ./assets/原图-clean.png` 喂给切片脚本。

## 第五步：合规审查清单

- [ ] 每张图都是单张状态图，不是拼接图
- [ ] 没有红色箭头、蓝色选框、说明文字、流程标题等交底标注
- [ ] 没有鼠标光标、悬停残影
- [ ] **第三方商标处理**：客户 Logo 墙含 HUAWEI / 阿里 / 腾讯等他人商标时，
      正文中**不要点名列举品牌**，仅用"客户标识墙"等中性表述
- [ ] **公开时间核验**：网页 footer 是否显示 © 年份？是否超出 6 个月新颖性宽限期？
- [ ] **品牌主体核验**：网页显示的公司名 / 商标 / 备案号是否与申请人一致？
- [ ] 切片宽高比合理（每段裁出后高度 ≥ 500 px）

## 第六步：接入主流程

切片完成后照常走 `SKILL.md` 的 Phase 3-5：

1. Phase 3 起草 `case.json` 的 `interface_states[].description`
2. Phase 4 review 单图（本流程已完成）
3. Phase 5 调 `export_gui_patent_docx.py` 输出 `02界面说明.docx` + JPG 包

## 常见错误

| 错误 | 后果 | 修复 |
| --- | --- | --- |
| 把整张长图直接喂给 Word | 单张图过长无法清晰呈现，且不符合"单张状态图"要求 | 必须切片 |
| 用低清缩略图切 | 文字糊掉，CNIPA 退回 | 要求用户重传高清源 |
| 切片包含相邻模块部分内容 | 状态边界模糊，专利图意混乱 | 用 3.3 色采样法精修分界 |
| 没清理鼠标光标 | 审查员认为图面包含临时 UI 元素 | 用 `clean_cursor_artifact.py` 清理 |
| 客户 Logo 墙点名第三方品牌 | 第三方商标进入正文描述，引发归属争议 | 用"客户标识墙"等中性表述 |
