---
name: ui-acceptance-assistant
description: UI 验收助手：对照 Figma/设计图与线上官网，逐元素验收 UI 还原、响应式与交互状态，并将确认问题写入飞书多维表格或其他文档格式。用于验收官网、营销站、对比设计稿与实现、批量验收同一 Figma 文件内画板。提效助手，不替人拍板。
---

# UI 验收助手

## When To Use

Use this skill for official website acceptance when the user provides, or plans to provide:

- A production, staging, preview, or local website URL.
- A design source, preferably a Figma file/node URL; image exports are acceptable as fallback or supplements.
- A request to check UI fidelity, responsive behavior, interactions, or publish-readiness.
- A request to organize findings into Feishu Bitable.

## Required Inputs

Ask for missing items before starting:

- Website URL: production, staging, preview, or local URL.
- Design source: prefer Figma source URL with exact page/frame/node. Accept images only when Figma is unavailable.
- Interaction source: prefer Figma prototype/component variants/annotations for hover, active, focus, expanded, selected, loading, success, and error states. Accept screen recordings or written specs when design states are not modeled in Figma.
- Target pages: home page plus any key landing pages, forms, navigation paths, or conversion flows.
- Viewports: default to desktop `1440x900`, tablet `768x1024`, and mobile `390x844` unless the user specifies others.
- Feishu destination: Bitable URL/app token/table ID and write permission, or confirmation that other document formats (CSV/Markdown/JSON) are acceptable if direct write tools are unavailable.
- Acceptance mode: `static-only` for visual/static responsive acceptance, `full` for static plus interactions, or `interaction-followup` for later interaction recheck.
- Acceptance standard: if absent, use the severity rules below.

## Platform Compatibility

This skill may be called from Cursor or other agent platforms. Keep the workflow tool-agnostic:

- Treat browser automation, Figma access, screenshot capture, and Feishu writing as replaceable capabilities.
- If a capability is unavailable, ask for the missing artifact or produce the closest portable output.
- Do not depend on Cursor-only file paths, terminal state, or MCP server names in the final process.
- Prefer stable outputs: screenshots, CSV, Markdown, JSON records, and Feishu-compatible field names.
- Record what was actually verified and what was blocked by missing platform permissions or tools.

## Design Source Preference

Prefer Figma source files over image design drafts because Figma preserves dimensions, hierarchy, component structure, copy, and design tokens. Use image drafts as:

- A fallback when Figma is unavailable.
- A supplemental visual reference for exported states.
- Evidence attachments for comparing screenshots.

When a Figma URL is provided, use available Figma MCP tools to get design context, screenshots, metadata, and node-specific references before browser testing.

Accept design images (PNG/JPG exported frames or module crops) when Figma source access is unavailable. Ask for viewport width and which live page/section each image maps to.

### Figma Batch Acceptance

Two input modes:

1. **Single link**: user provides one Figma URL with `node-id` for one page/frame; accept only that board against the matching live URL.
2. **Whole file batch**: user puts all page boards (PC, mobile, interaction supplements) in one Figma file and provides the file root link. Automatically list top-level frames, map each board to live URL and Feishu `所属模块`, then accept boards in order without waiting for the user to send the next link.

Include interaction supplement boards (for example Footer hover states, contact form states) in acceptance. Treat them as interaction/state standards for the related module, not as optional notes.

## Interaction Source Preference

For hover or mouse-enter effects, prefer these sources in order:

- Figma component variants or separate frames for default/hover/active/focus states.
- Figma Prototype links showing transitions, overlays, menus, carousels, or reveal effects.
- Designer annotations that describe trigger, changed properties, duration, easing, and final state.
- Screen recording or GIF of the intended interaction.
- Written interaction spec when no visual source exists.

If no interaction source is provided, test obvious standard states and label findings as implementation-quality observations rather than design-fidelity mismatches.

## Workflow

1. Collect inputs and confirm scope.
2. Capture implementation evidence from the site at desktop, tablet, and mobile viewports using the browser or screenshot capability available on the current platform.
3. Compare implementation against the design source:
   - Layout, spacing, alignment, grid, section order.
   - Typography, font weight, line height, text wrapping, and copy.
   - Color, shadows, borders, radius, opacity, gradients, and imagery.
   - Component states: default, hover, active, focus, disabled, loading, error, success.
4. Check responsive behavior:
   - No horizontal overflow.
   - Navigation adapts correctly.
   - Images and videos keep intended crop/ratio.
   - Text remains readable and does not overlap.
   - Key CTAs remain visible and usable.
5. Check interactions unless the mode is `static-only`:
   - Header navigation, anchors, buttons, cards, tabs, accordions, carousels, menus, forms, modals, and external links.
   - Hover/mouse-enter states for nav items, buttons, cards, image tiles, dropdown triggers, tooltips, and interactive text links.
   - Form validation, submit behavior, loading states, success/error messaging, and duplicate-submit prevention.
   - Keyboard focus order for primary interactive elements.
6. Check technical signals when the platform exposes them:
   - Browser console errors and failed network requests.
   - Basic SEO tags: title, description, canonical, Open Graph, favicon, heading structure.
   - Basic accessibility: alt text for meaningful images, labels for inputs, focus visibility, contrast risks.
   - Basic performance risks: oversized assets, slow hero media, layout shift, obvious blocking resources.
7. Record findings with reproducible evidence.
8. Complete the user-specific acceptance self-check below before writing or updating any finding.
9. Write results into Feishu Bitable when a supported Feishu API/MCP/tool is available. If unavailable, create an import-ready CSV/Markdown/JSON table and clearly state what is needed to push it into Feishu.

## User-Specific Acceptance Self-Check

Before every website acceptance run, and again before writing findings into Feishu, self-check every item in this section one by one. These are strict user requirements learned from prior acceptance work, and every future acceptance task for this user must verify that the work follows them.

If the user later states any new acceptance requirement, caution, table rule, evidence rule, or reporting preference, immediately add it to this Markdown skill file before continuing the acceptance work. Do not rely on memory or chat history alone. Before every delivery, self-check against the latest version of this file and confirm that the output follows the user's requirements. For every future reply about website acceptance, explicitly tell the user whether the required pixel-level visual workflow was followed for that response.

### Scope And Order

- Perform pixel-level scanning to identify differences between the live implementation and the design. Every visible piece of page content must be checked one by one; do not stop at module-level comparison.
- Check the full requested page, not only the first visible section. For a homepage, go from top to bottom by module: navigation, hero, data/statistics, product/solution sections, video/media sections, logo matrices, awards/recognition, case studies, news, contact form, footer, and any other visible module in page order.
- Check elements inside each module one by one: text, icon, logo, image, card, button, form field, divider, progress line, background, spacing, radius, color, opacity, shadow, and state shown by default.
- For initial acceptance, write findings in Feishu by page module order from top to bottom; within the same module, write issues from top to bottom as they appear on the page.
- For non-initial or supplemental acceptance, append newly discovered issues to the end of the corresponding module/group list so the user can immediately see which issues are newly found.
- Keep findings in the Feishu table ordered by module from top to bottom. Do not interleave issues from different modules.
- Do not add broad or vague findings such as "the whole page differs" or "many places are inconsistent". Every record must name the exact element, the current problem, and the expected design result.
- Do not re-add issues that the user deleted from the Feishu table. If a deleted issue appears again, only mention it after re-verifying and asking whether it should be restored.

### Evidence And Accuracy

- Do not rely on visual memory or screenshot impressions alone. Verify with source evidence: Figma design context/screenshot/metadata plus live DOM, computed style, asset source, or current screenshot.
- Do not treat the browser/webview's transparent or dark surrounding background as the page UI background. For background-color findings, verify the actual page/container element's computed `background-color` (for example `html`, `body`, `main`, or the module wrapper such as `.resource`) and confirm the live screenshot shows the same color. If the screenshot shows white but the surrounding browser area is black, that is not a UI restoration defect.
- If computed background is transparent (`rgba(0,0,0,0)`) but the visible module area is white in the live screenshot, do not report a black-background issue. Only report background-color differences when both the screenshot and the target element's computed style clearly show a wrong color.
- If Figma source files cannot be read through Figma MCP, Figma API, or Dev Mode, do not pretend that source data was read. Tell the user exactly what is unavailable and ask them to provide Figma screenshots, exported Frame images, or enable Figma access.
- Every Feishu issue must have a relevant screenshot or evidence attachment unless the user explicitly says not to include one. If using screenshots, ensure the captured area is the exact module and not a stale or wrong scroll position.
- Problem screenshots must mark the exact problem location accurately. Do not randomly or loosely draw boxes around nearby areas.
- Red boxes or annotations must precisely frame the actual problem element. If accurate box placement is uncertain, use clean side-by-side design-vs-live screenshots instead of inaccurate markings.
- Each issue screenshot must only mark the element described by that one issue. Do not reuse a screenshot with multiple unrelated red boxes for separate records; create separate evidence images for logo, icon, button, text, shadow, or layout issues when they are separate findings.
- For text/copy issues, verify the live text from DOM rather than reading only from screenshots.
- For style issues, compare against the correct design width and viewport. For this project, desktop PC checks should use the design-native 1920px width unless the user specifies another viewport.
- Do not report exact pixel values without screenshot diff data, DOM/CSS measurements, Figma parameters, or another clear measurement basis. If exact measurement is unavailable, use approximate wording such as "约 8-12px" or "视觉上偏大/偏小", and mark "需 DevTools 或截图工具确认".
- Do not report "consistent", "correct", "same", "no issue", or "all good" in a problem row. Acceptance findings are only for differences.
- Before writing any finding to Feishu, first prepare an element checklist and evidence source for that finding. A finding is not allowed into Feishu unless it has Figma source/screenshot evidence plus live DOM/CSS, asset, screenshot, or aligned visual evidence.
- For compound elements such as search boxes, buttons, cards, dropdowns, and form controls, verify every sub-element separately before concluding: container, border, radius, background, placeholder/text, icon graphic, icon size, icon stroke/fill, spacing, divider, and state. Do not treat checking the container as checking the whole component.
- All visual findings must pass an evidence gate before writing: generate or inspect a single-issue screenshot, confirm the red box only marks the exact element, then write the record. If the screenshot is inaccurate or the difference is only an impression, do not write it.
- After writing each Feishu record, immediately read it back and verify the problem description, module, size, issue type, optimization checkbox, acceptance result, order, and attachment. If the user points out a false positive, delete the wrong record in the same turn and explain the cause briefly.

#### High-Risk Double Verification

- For high-risk findings, require dual evidence before writing to Feishu: aligned design-vs-live visual evidence plus DOM/CSS, SVG, or asset-source verification. Single-source impressions are not enough.
- High-risk categories:
  - `背景色`: target element computed `background-color` plus live screenshot of the same module area.
  - `hover/交互态`: default-state evidence and hover-state evidence for the same component.
  - `图标`: Figma icon asset or node screenshot plus live SVG/path, size, stroke/fill, and position evidence.
  - `文字样式`: Figma text parameters plus live computed `font-size`, `font-weight`, `line-height`, `color`, and truncation/wrapping behavior.
- If the two evidence sources disagree, do not write the finding. Re-check viewport, element selector, state, and screenshot crop first.

### Description Style

- Write for frontend engineers. Keep descriptions concise and actionable: "what is wrong now" + "what the design expects".
- Keep issue descriptions as short as possible. Do not write verbose official-sounding wording, process explanations, apologies, background, or low-value filler. Prefer one concise sentence when it can fully explain the problem and expected result.
- Put all explanation in `问题描述`; do not split the useful explanation into `备注说明`.
- Do not include long acceptance commentary, reasoning history, or unrelated context in Feishu records.
- If only one property is wrong, describe only that property. Do not mention properties that are already consistent.
- If multiple issues are in the same small component, group them only when it helps the frontend fix the same component. Split unrelated differences into separate records.

### Feishu Field Rules

- For newly reported acceptance findings, keep `UI验收是否通过` empty by default. Do not set it to `待验收` or any other value unless the user explicitly asks.
- If `前端是否完成优化` is not checked, keep `UI验收是否通过` empty. Only fill `UI验收是否通过` after the frontend has completed optimization and the issue has been rechecked.
- Keep `备注说明` empty unless the table schema requires it for non-issue metadata. User-facing problem details belong in `问题描述`.
- Remove empty records and meaningless records.
- Do not restore columns that the user has deleted or hidden from the Feishu view. If a technical helper field is needed for sorting, keep it hidden from user-facing views.
- Do not overwrite or rewrite problem descriptions that the user has manually modified. Treat user-edited descriptions as authoritative.
- If a newly verified issue relates to a user-edited record, create a new row directly below or near that issue instead of merging the new finding into the user's edited description.
- Use stable existing records only when the record was created by the agent and has not been manually edited by the user. Do not create duplicates for the same confirmed problem unless preserving the user's edited wording requires a separate row.

#### 所属模块 Grouping Rules

- `所属模块` groups findings by first-level page, language, and device type. Use the naming pattern `{一级页面}-{语言}-{端}`.
- PC and mobile must be in separate groups. Do not mix PC and mobile findings in the same `所属模块`.
- If the site has multiple languages, each language must be in a separate group. Do not mix Chinese and English findings in the same `所属模块`.
- Example: homepage with Chinese and English, checked on both PC and mobile, has 4 groups: `首页-中文-PC`, `首页-英文-PC`, `首页-中文-移动`, `首页-英文-移动`.
- Secondary pages use the same rule with their first-level page name. Example: `资源中心-中文-PC`, `资源中心-英文-移动`.
- Cross-page global components (header, footer, contact form reused across pages) go into `全局-PC` or `全局-移动` when the user has defined those groups; otherwise use the first-level page group where the issue was found.
- `尺寸` is a separate field: use `PC端`, `移动端`, or `双端`. Do not put device info only in `所属模块` and leave `尺寸` empty.
- Before writing, read `+field-list` and confirm the target group option already exists in `所属模块`. If a required group is missing, tell the user instead of inventing a mismatched name.

#### 问题类型 Tag Rules

- Every finding must choose the correct `问题类型` from the table's existing options. Do not leave it empty and do not use a generic catch-all when a specific tag fits.
- Choose by the actual defect, not by page or module:
  - `基础视觉还原`: layout, spacing, typography, color, border, radius, shadow, icon shape, image crop, background, and other default-state visual mismatches.
  - `交互还原`: hover/active/focus/expanded/click states, missing or wrong interaction feedback, cursor behavior, dropdown/menu/tab state changes.
  - `动效还原`: transition timing, easing, duration, motion path, entrance/exit animation differences.
  - `动画还原`: looping/continuous animation, marquee, auto-play animation, progress animation differences.
  - `适配兼容`: responsive layout breakage, overflow, wrong rendering on a target viewport/device, breakpoint-specific issues.
  - `切图模糊`: blurry logo/icon/image caused by low-resolution asset, wrong scale, or over-enlarged source.
  - `页面性能`: slow load, oversized asset, obvious layout shift, blocking media, or other performance-related delivery issues.
  - `内容更新`: wrong or missing copy/content that the user explicitly wants matched to launch content or design copy.
  - `效果优化`: polish-level visual refinement that is real but lower priority than a core restoration defect.
  - `二次优化`: follow-up polish after an earlier fix round; use only when the user or table workflow indicates recheck/polish rather than first-pass restoration.
  - `其余视觉还原`: visual differences that do not fit the categories above but are still visual restoration issues.
  - `其他`: only when none of the above tags apply; avoid overusing this.
- If one record contains multiple defect types, split into separate records when the tags differ. Example: a wrong icon shape is `基础视觉还原`; missing hover shadow on the same card is a separate `交互还原` record.

#### 需人工复核 Rules

- `需人工复核` is a checkbox field. Default is unchecked for every record.
- Check `需人工复核` only when the issue is real but the evidence is not strong enough for a fully confirmed write-up, and a designer or frontend engineer should manually confirm it.
- Check it only in these cases:
  - Visual difference is suspected, but screenshot diff and DOM/CSS evidence do not fully agree.
  - Hover/active/focus state cannot be captured reliably, yet the design includes a hand-cursor hover reference or an interaction source.
  - Figma/live alignment is blocked by animation, carousel timing, sticky behavior, lazy loading, or a mismatched capture state.
  - Figma source, live DOM/CSS, or screenshot evidence is incomplete for that specific element, but the module still needs human eyes.
  - Measurement is approximate only, such as "visually偏大/偏小", and exact px values still need DevTools or design-tool confirmation.
- Do not check `需人工复核` when:
  - The issue is fully confirmed by dual evidence and a precise single-issue screenshot.
  - The issue is a normal, certain restoration defect.
  - The issue is actually uncertain; in that case do not write the record at all unless the user explicitly wants suspected items logged.
- Do not use `需人工复核` as a substitute for weak acceptance work. Prefer re-checking first; only use it after re-checking still leaves uncertainty.
- In delivery summaries, mention the `需人工复核` field only when at least one record in that run was checked. If no record needs it, do not mention this field in the user-facing output.

### Visual And Asset Checks

- Mandatory minimum-unit comparison: every component must be decomposed into the smallest visible elements before acceptance. This includes, but is not limited to, container shape, border/stroke, stroke width, radius, fill/background, shadow, icon shape, icon stroke/fill, image crop, text layer, spacing, size, and position. Never conclude a component is restored by checking only the overall component or parent container.
- For every component, build a sub-element checklist before judging. Do not rely on one component example such as a search box to represent all component types. First apply the universal checklist below, then apply the matching component-type checklist for every component found on the page.
- Universal checklist for any component: container shape, border/stroke, stroke width, radius, fill/background, shadow, size, position, spacing to neighbors, alignment, default state, hover/active/focus state when applicable, and every visible child layer inside the component.
- Component-type checklists:
  - Navigation/header: logo graphic, menu text, menu spacing, active item, language switcher, CTA button, divider/underline, sticky behavior if shown, hover state per menu item.
  - Tabs: container, bottom border/divider, inactive text style, active text style, active indicator line, tab spacing, hover state, nearby actions such as search or filters.
  - Button: container, height, padding, radius, background, border, shadow, text style, every embedded icon, icon-to-text spacing, disabled/loading state if shown, hover/active state.
  - Input/search/select/textarea: container, border, radius, background, label, required marker, placeholder/value text, helper/error text, leading/trailing icon, clear button, dropdown arrow, focus state, error state.
  - Card: container, border, radius, shadow, cover image crop/radius, tag/badge, title, subtitle/body, metadata/date, footer actions, every visible icon, internal spacing, default state, hover state.
  - Tag/badge: container, border, radius, padding, text style, icon if present, spacing to nearby content.
  - Typography block: title, subtitle, body, number/stat, unit, label, date, link text; check each text layer's font, size, weight, color, line height, letter spacing, truncation, and alignment separately.
  - Image/logo/media: asset graphic, natural size vs displayed size, crop, radius, mask/overlay, play button, video cover, blur/sharpness, alt/label if visible.
  - Icon: graphic shape, stroke/fill, color, size, position, spacing, container if any, default vs hover color/state.
  - Divider/progress/arrow/decoration: shape, color, thickness, length, opacity, position, repeat/scale for patterned backgrounds.
  - Dropdown/modal/popover: trigger, panel container, item text, selected state, divider, shadow, arrow, open/close state, hover item state.
  - Table/list/pagination: row height, cell padding, header style, border/divider, hover row state, active sort/filter state, page button, current page style.
  - Footer: logo, link columns, social icons one by one, legal text, filing icon, back-to-top button, hover states.
  - Carousel/slider: frame, arrow buttons, dots/progress, active slide state, autoplay indicator if shown, slide spacing and crop.
- For every component type, inventory every visible icon inside that component, not only the main text or container. Check each icon separately: graphic shape, stroke/fill, size, color, position, spacing to nearby text, and state differences between default and hover. Do not assume a fixed icon role; verify every icon that appears in that component.
- Logo checks must be done one by one. Verify the actual logo graphic, not only the text label, count, or layout. Check brand marks such as Google, Apple Ads, Meta, 巨量引擎, TikTok/Kwai/AppLovin, customer logos, footer platform logos, and any logo matrix items.
- For image/logo/icon grids, compare category order, item count, each icon graphic, repeated assets, placeholder assets, incorrect assets, missing assets, and visible labels.
- Detect repeated or placeholder assets by checking live image source URLs and duplicate counts, not only by visual inspection.
- Include blurry or low-resolution image cuts as findings when an image/logo/icon is visibly enlarged beyond its source resolution or does not meet the expected crispness. Prefer source natural size vs displayed size/DPR evidence.
- Check videos and image covers against the design material, including overlay masks, opacity, play states shown by default, and whether wrong placeholder covers are used.
- Check decorative graphics, dividers, progress indicators, arrows, buttons, form icons, public security icons, and footer/link icons against the design.
- Small decorative markers before titles, labels, tabs, statistics, or section captions must be checked as separate visual elements. Verify their shape, color, size, radius, position, and alignment; do not ignore them while only checking nearby text.
- Footer "follow us" social icons must be checked one by one against the design: official account, video account, LinkedIn, Weibo, and any other platform icon. Do not only check the text label, hover QR code, or link target.
- Do not treat a component-level screenshot as sufficient for graphic acceptance. Break each visual component into sub-elements and check every visible graphic layer: background image, mask, overlay, icon shape, icon fill, icon stroke, icon container, opacity, blur, shadow, radius, border, crop, and alignment.
- For CTA/play buttons and other compound controls, separately verify the outer container, translucent/blur background, inner circle/square, icon shape, icon color, icon size, border/stroke, spacing, and centering. Do not mark the button as checked by only comparing the text.
- For buttons that contain brand logos or product logos, separately verify the button container style and the embedded logo asset. Check logo graphic fidelity, sharpness, natural size vs displayed size, crop, alignment, and whether the logo is blurred or replaced by a low-resolution asset.
- For hover cards, compare the hover state by sub-element: card shadow/background/border, embedded logo graphic, text style, arrow button container, arrow icon shape, arrow icon size, and arrow icon position. Do not mark the card hover as checked by only checking whether the card is clickable or whether any one effect exists.
- For transition backgrounds, decorative strips, blue patterned backgrounds, repeated textures, and section divider graphics, compare the exact pattern/texture, repeat behavior, scale, crop, opacity, and visible position against Figma. Do not ignore them as "background decoration".
- When a module contains any image, SVG, icon, background, or decoration, create an element inventory before judging: list the Figma visual elements and the live visual elements, then tick off each item one by one. Missing, extra, replaced, repeated, or visually different items must be recorded.
- For pixel-level visual self-check, use this sequence whenever tools allow it: export/capture the Figma module, capture the live module at the same viewport, align/crop to the same visual region, generate a diff image, inspect the red/yellow diff areas, then map each diff area back to a named element before writing a finding.
- If exact alignment is not possible because the live module is animated, sticky, carousel-driven, or captured at a different state, state that the diff is only an auxiliary visual check. Only then may the related record use `需人工复核`.
- This pixel-level visual workflow is mandatory for future website acceptance work. Do not skip it for visual findings. If any step cannot be completed, state exactly which step was blocked and do not call the result pixel-level acceptance for that area.

### Typography And Layout Checks

- Text must be checked by layer, not only by module. For repeated cards or badges, separately compare brand/name text, subtitle/qualification text, date/year text, labels, numbers, units, and button text.
- Compare font family, font size, weight, color, line height, letter spacing, alignment, truncation, and wrapping.
- For statistics or numbers, compare the number, unit, label, font, color, and letter spacing separately.
- For forms, check each label, required asterisk, placeholder, input/select/textarea shape, default button state, agreement text, and link color.
- For hover/interaction issues, only record them as design-fidelity findings when the interaction source is provided or the default state visibly exposes the issue. Otherwise mark them as interaction follow-up observations.
- In Figma or design screenshots, a hand cursor/pointer annotation means the annotated component is shown in its hover state. That frame is the hover reference even if the nearby text does not explicitly say "hover".
- When a design shows a hand cursor on a component, acceptance must check both states for that component: the default state and the hover state. Do not inspect only the hover frame or only the default implementation.
- For components with a hand-cursor hover reference, compare default and hover separately by sub-element: container, shadow, border, background, text, and every visible icon inside the component.

### Data-Driven Content

- Be careful with data-driven modules such as news lists, carousels, dates, and CMS-managed content. Do not mark content order/date/title as a UI restoration defect unless the instruction explicitly requires content acceptance.
- For pages whose content is dynamically configured by the backend/CMS, do not treat different text content, image content, dates, or item order as defects by default. The acceptance requirement is that styles must match the design exactly: layout, grid, spacing, card/container shape, border, radius, shadow, tag style, typography, icon graphics, button style, hover state, pagination/load-more style, and responsive behavior. Only treat content/order mismatches as defects when the instruction explicitly requires content acceptance.
- For backend/CMS-driven pages, still compare every component at minimum visible-unit granularity. Content can differ, but the component style and state must be checked one by one against Figma.
- If data-driven content differs but structure and style match, explain it in the final summary only; do not re-add it to the issue table if the user has removed it.
- If content differences affect visible UI assets or confirmed launch content, state the exact mismatch and expected content.

## Efficiency Without Quality Loss

Use these rules to improve acceptance speed and reduce token consumption without lowering acceptance quality. Efficiency comes from narrower scope, batched evidence collection, evidence sufficiency, local reuse, and lean delivery. It does not come from skipping minimum-unit checks, dual verification, or hover/default-state rules.

### Scope First

- Lock scope before any browser or Figma work: first-level page, language, device type, viewport, target module, and whether the page is CMS-driven.
- If the user only requests one page or one module, do not expand into unrelated pages or modules unless explicitly asked.
- For shared components already recorded in Feishu and not yet fixed, do not repeat a full deep audit and duplicate record. Reference the existing record in the delivery summary instead.
- State uncovered scope explicitly in the final delivery. Do not imply full-site acceptance when only one module was checked.

### Evidence Sufficiency

- Use the minimum evidence set that can still support a confirmed finding. Do not run the full diff workflow for every issue by default.
- Suggested minimum evidence by defect type:
  - Icon graphic mismatch: Figma icon asset or node screenshot plus live SVG/path, size, stroke/fill, and position.
  - Typography mismatch: Figma text parameters plus live computed `font-size`, `font-weight`, `line-height`, `color`, and truncation/wrapping.
  - Hover/interaction mismatch: default-state and hover-state local screenshots plus relevant computed style such as `box-shadow`, `border`, or `color`.
  - Layout/spacing mismatch: aligned cropped comparison plus key element rects or spacing measurements.
- Generate a diff image only when DOM/CSS cannot confirm the issue but visual suspicion remains. If DOM/CSS already proves the defect, skip diff generation.
- For high-risk categories (`背景色`, `hover/交互态`, `图标`, `文字样式`), still follow the dual-evidence rule. Efficiency does not waive high-risk double verification.

### Batched Collection

- Prefer one batched DOM/CSS/SVG extraction per module instead of one tool call per element.
- Export structured JSON locally for tabs, cards, buttons, icons, and text layers. Keep only fields needed for comparison: selector, bounding rect, key computed styles, and SVG `outerHTML`.
- Do not paste large CDP JSON dumps into chat. Read the saved file locally during comparison.
- Use local module screenshots by default. Avoid `fullPage` screenshots unless the issue requires below-the-fold or full-page context.
- Take issue evidence screenshots only for confirmed or high-risk suspected findings, and crop tightly to the exact element.

### Figma Reuse

- For each Figma node, call `get_design_context` and `get_screenshot` once, then reuse the exported screenshot, parameters, and asset URLs locally.
- For sibling pages that share the same shell, such as resource-center tabs sharing tab bar and search box, reuse shell evidence once and only incrementally audit the page-specific content area.
- Do not re-fetch the same Figma node during the same acceptance run unless the node or viewport changed.

### Tiered Walkthrough

- Keep minimum-unit comparison mandatory, but prioritize effort by risk:
  1. Structure and interaction: layout, spacing, hover/default dual-state, tabs, buttons, cards.
  2. Icons and text layers: the most common miss areas.
  3. Responsive checks: only when mobile/tablet is in scope.
- For repeated identical components with the same DOM structure and class pattern, fully deep-audit the first instance, then verify the remaining instances are structurally identical and style-equivalent. If a difference appears in a later instance, audit that instance fully.
- Do not sample away unique graphics, unique icons, or hand-cursor hover components. Those always require full checks.

### Feishu Write Efficiency

- Read `+field-list` once per acceptance run before writing.
- Batch write records when possible. Keep batches within the platform limit of 200 records.
- Re-read records after write only for high-risk findings or `需人工复核` findings. Do not re-read every normal confirmed record unless the write failed.
- Merge only when it does not reduce fix clarity: same root cause, same tag, same component pattern across multiple instances may be one record with wording such as "全部小卡". Do not merge different defect types or different component fixes into one row.

### Lean Delivery

- Keep chat output short: conclusion, new record IDs, uncovered scope, and any `需人工复核` items.
- Do not paste element inventories, DOM dumps, crop coordinates, or full evidence images into chat unless the user explicitly asks.
- Attach evidence images to Feishu, not to the chat response.
- If no record needs `需人工复核`, do not mention that field in the delivery.
- If a suspected issue remains uncertain after re-check, prefer not writing it. Do not create low-confidence rows just to show effort.

### Per-Run Budget Guidelines

Use these soft budgets to avoid unnecessary token use while keeping quality gates intact:

- Figma calls: about 2 per node (`get_design_context` + `get_screenshot`), unless scope changes.
- Live full-page screenshots: 1 per page/module unless more are required by the issue.
- Issue evidence images: 1 per confirmed finding.
- Batched CDP extraction scripts: about 3 per module (collect, hover/forced-state check, targeted re-collect if needed).
- Feishu `field-list`: 1 per run.
- Post-write verification: required for high-risk and `需人工复核` records only.

### Do Not Cut For Speed

- Do not skip minimum-unit decomposition.
- Do not inspect only the parent container and ignore child icons, text layers, or decorations.
- Do not treat browser/webview black surroundings as page UI background.
- Do not inspect only hover or only default when the design includes a hand-cursor hover reference.
- Do not write Feishu records without evidence gates.
- Do not duplicate existing unfixed records for shared components.
- Do not use `需人工复核` to excuse weak verification when re-checking is still possible.

## Static-Only Acceptance

When the user asks to validate static styles first:

- Check default visual state only: layout, spacing, typography, colors, images, icons, copy, section order, and responsive default rendering.
- Check responsive static rendering across agreed viewports.
- Do not mark missing hover/active/focus/expanded states as defects unless they visibly affect the default page.
- Add `交互待补充` to the status or notes for components that require later interaction-state acceptance.
- Keep issue IDs stable so later interaction findings can be added without renumbering static findings.

## Feishu Integration

### One Website, One Bitable Table

- Each official website acceptance project must use its own Feishu Bitable table. Do not write a new website's findings into an existing website's acceptance table.
- When the user asks to accept a different website, create a new Bitable table first, using the current eclicktech acceptance table as the schema/template reference.
- The new table should replicate the same field structure, grouping logic, tag options, and workflow fields used in this acceptance run, including at minimum:
  - `问题描述`
  - `所属模块`
  - `尺寸`
  - `问题类型`
  - `优先级`
  - `问题截图`
  - `提出时间`
  - `区块顺序`
  - `前端是否完成优化`
  - `UI验收是否通过`
  - `需人工复核`
  - `备注说明`
- Rebuild `所属模块` group options for the new website's information architecture. Do not copy the old website's page groups into the new table.
- Reuse the same grouping naming rule: `{一级页面}-{语言}-{端}`.
- Before writing findings for a new website, confirm the new Base/table exists, field definitions are in place, and write permission is available. Tell the user the new table link or identifiers after creation.
- Continue using the old website's table only when doing follow-up, recheck, or supplemental acceptance for that same website.

To write directly into Feishu Bitable, require one of these connection methods:

- Feishu CLI (`lark-cli`) installed, configured, and authenticated with Base/Bitable write permissions.
- Feishu MCP/tool connection with permission to create/update Bitable records.
- Feishu OpenAPI credentials: app ID, app secret or access token, Bitable app token, table ID, and field IDs if the table already exists.
- A user-provided Bitable table link plus an authenticated platform session that exposes write tools.

Prefer Feishu CLI when available because it works across agent platforms and can directly create or update Bitable records from structured findings. Before using it, verify:

- `lark-cli --version` succeeds.
- `lark-cli auth status` reports an authenticated account.
- The requested Bitable/table is accessible with write permission.

If direct writing is unavailable:

- Generate Feishu-compatible CSV with the schema below.
- Generate JSON records using the same field names for later API import.
- State exactly which credential, permission, or tool is missing.

## Severity Rules

Use these levels consistently:

- `P0 阻塞`: Site or core conversion path is unusable; severe broken layout on a target device; form cannot submit; release should stop.
- `P1 高`: Major UI mismatch, broken primary interaction, obvious responsive issue, console/runtime error affecting users.
- `P2 中`: Noticeable visual deviation, secondary interaction defect, copy mismatch, minor accessibility or SEO issue.
- `P3 低`: Polish issue, small spacing/color variance, non-critical hover/state detail, minor improvement.

## Feishu Bitable Schema

Use or create these fields:

- `编号`: stable issue ID, such as `WEB-001`.
- `页面`: page name or route.
- `设备/视口`: desktop/tablet/mobile and viewport size.
- `模块`: header, hero, form, footer, pricing, FAQ, etc.
- `问题类型`: UI还原/响应式/交互/控制台/SEO/可访问性/性能/内容.
- `严重级别`: P0/P1/P2/P3.
- `问题描述`: concise user-visible problem.
- `设计稿预期`: expected behavior or appearance from the design.
- `实际表现`: observed implementation behavior.
- `复现步骤`: numbered steps or direct URL plus action.
- `证据`: screenshot/video/link/log excerpt.
- `建议修复`: practical fix guidance.
- `状态`: 待修复/修复中/待复验/已通过/暂不处理.
- `负责人`: leave blank if unknown.
- `验收时间`: current date.

## Reporting Rules

- Lead with acceptance conclusion: `通过`, `有条件通过`, or `不通过`.
- Summarize counts by severity and issue type.
- Do not rely on memory for visual comparison; use screenshots and design context.
- Be specific enough that an engineer or designer can reproduce every finding.
- Avoid vague feedback such as "looks off"; name the module, viewport, expected value/visual, and actual deviation.
- If direct Feishu writing is blocked by missing authentication, missing MCP, or missing table permissions, report the blocker and provide the import-ready table content.

## Final Response

Keep the final response concise:

- State whether the Feishu Bitable was updated or an import-ready report was prepared.
- Include the acceptance conclusion and the top risks.
- Mention any pages, viewports, or design states that could not be verified.
