# 来源核对（2026-11-17）

本轮独立打开过下列页面。表里的「用在哪」是本仓库采用的决定，不是把原文搬进来。

官方文档页面不等于可以自由改写或再分发。代码仓库的许可证只覆盖该仓库里的代码。没有逐字复制手册、色板、图标或组件实现。

W3C 文档许可（2023）允许在保留链接、原版权声明和文档状态的前提下复制片段；**不授予**把 W3C 文档改写成衍生作品的一般权利（实现规格的软件及其配套说明除外，且须带指定声明）。因此 WCAG 只保留数字和准则号，并在下面附上许可要求的出处。

Apple HIG 页面标明 © 2026 Apple Inc. All rights reserved。只链接和转述，不复制条文。

---

## 已读并采用

| 来源 | URL | 平台 | 用在哪 | 官方 / 社区 | 许可与复用 | 核对 |
|------|-----|------|--------|-------------|------------|------|
| Apple HIG Design principles | https://developer.apple.com/design/human-interface-guidelines/design-principles | Apple 各平台 | 八原则仍是 A 层。Markdown 版写明 2026-06-08 重新列入；HTML 版需要 JavaScript，改读同路径 `.md` | 官方 | 版权所有。不复制正文 | 2026-11-17 读完 Markdown |
| WWDC26 Session 250 | https://developer.apple.com/videos/play/wwdc2026/250/ | Apple | 章节顺序与八原则名称一致：Purpose、Agency、Responsibility、Familiarity、Flexibility、Simplicity、Craft、Delight。原则之间没有必胜公式 | 官方 | 视频与页面 © Apple。不转载讲稿 | 2026-11-17 读到章节与讲稿文本 |
| Apple HIG Buttons | https://developer.apple.com/design/human-interface-guidelines/buttons | iOS 等 | 按钮热区一般至少 44×44 pt（visionOS 60×60 pt）。用在触控目标，不外推成网页像素 | 官方 | 版权所有。只引用这一测量 | 2026-11-17 读 `.md` |
| Apple HIG Accessibility | https://developer.apple.com/design/human-interface-guidelines/accessibility | Apple | 控件与自定义字号的默认/最小表；有边框约 12 pt、无边框约 24 pt 的间距经验 | 官方 | 同上 | 2026-11-17 读 `.md` |
| Material 3 导航栏指南 | https://m3.material.io/components/navigation-bar/guidelines | Android 手机/平板 | 底栏用于 3–5 个同级目的地；单任务不用底栏；少于 3 个改用 tabs；紧凑与中等窗口可用，扩展窗口改导航轨；不要用在桌面 | 官方 | 站点正文许可未发现为开源。只摘要这条落位 | 2026-11-17 WebFetch 读到正文。curl 看到的 HTML 外壳不含正文 |
| Material 3 导航轨概述 | https://m3.material.io/components/navigation-rail/overview | Android 大窗口 | 未把该页当成已读。导航轨的使用条件来自上面的导航栏指南 | 官方 | 同上 | **未读正文**（页面要求 JavaScript，外壳无内容） |
| Android Accessibility Help，触控目标 | https://support.google.com/accessibility/android/answer/7101858?hl=en | Android | 可交互元素至少约 48×48 dp，目标可以大于视觉尺寸 | 官方 | Google 帮助页。只引用尺寸 | 2026-11-17 打开 |
| Jetpack Compose 无障碍默认值 | https://developer.android.com/develop/ui/compose/accessibility/api-defaults | Android | Material 组件在可交互时把目标补到至少 48 dp | 官方 | Android 开发者文档。只引用行为 | 2026-11-17 打开 |
| Fluent 2 Design principles | https://fluent2.microsoft.design/design-principles | Windows / Microsoft | 四条原则名称用来提醒：跟随所在平台、少干扰、包容、Microsoft 自己的识别性。不把 Fluent 皮肤搬到 Apple 或网页上冒充原生 | 官方 | 站点许可未当作 MIT。代码许可见下栏，不覆盖这篇网页 | 2026-11-17 读到四条原则 |
| Fluent 2 Accessibility | https://fluent2.microsoft.design/accessibility | Windows / Web 上的 Fluent | 对比度要求指向 WCAG AA；键盘焦点要看得见。Windows 稿不另造点击像素 | 官方 | 同上 | 2026-11-17 由检索工具提取正文；同日 curl 返回 200 |
| Windows 应用设计总览 | https://learn.microsoft.com/en-us/windows/apps/design/ | Windows 原生 | 窗口应用要清晰、可访问、响应窗口、与 Fluent 一致。标题栏、命令、导航分属不同指南 | 官方 | Microsoft Learn。只摘要方向 | 2026-11-17 打开。`.../signature-experiences/design-principles` 实际打开的是这一总览，**不是**一篇独立原则文，故不把它当原则出处 |
| Windows Navigation basics | https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics | Windows | 导航保持一致、简单、清楚；层级深过两级时给面包屑 | 官方 | 同上 | 2026-11-17 检索工具读到正文；curl 200 |
| NavigationView | https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/navigationview | Windows | 顶级目的地大约不超过 5 个且同等重要时可用顶栏；大约 5–10 个时用左侧 | 官方 | 同上 | 2026-11-17 检索工具读到正文 |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | 网页，也作其他平台的无障碍下限参照 | 见文末版权块。AA 目标 2.5.8、AAA 目标 2.5.5、对比 1.4.3 | 官方 | W3C Document License 2023。不改写规范全文 | WebFetch 读到 2024-12-12 Recommendation。本环境 curl 对 `www.w3.org` 返回 403，以 WebFetch 正文为准 |
| W3C Document License 2023 | https://www.w3.org/copyright/document-license/ | 许可本身 | 决定「只引用数字并附链接与版权，不派生整份规范」 | 官方 | 该页说明自身的复制条件 | 2026-11-17 curl 200，读到许可条款 |
| GNOME HIG 原则 | https://developer.gnome.org/hig/principles.html | Linux 上的 GNOME | 常用操作放近，少打断；破坏性操作优先可撤销。与 Apple「先确认」的张力要写出来 | 官方（GNOME 项目） | 原则页上看不到内容许可证。不复制段落 | 2026-11-17 读到 Design for People / Make it Simple / Reduce User Effort / Be Considerate |
| KDE HIG：何为 KDE 应用 | https://develop.kde.org/hig/kde_app_design/ | Linux 上的 KDE | 「默认简单，需要时强大」。专家快捷键不能是唯一入口 | 官方（KDE） | 内容许可证本轮未打开 | 2026-11-17 检索工具读到正文；curl 200 |
| KDE：默认简单 | https://develop.kde.org/hig/simple_by_default/ | KDE | 主路径默认可见；不要用汉堡菜单藏起唯一入口 | 官方 | 同上 | 2026-11-17 检索工具读到正文；curl 200 |
| Chrome 扩展界面目录 | https://developer.chrome.com/docs/extensions/develop/ui | 浏览器扩展 | 弹窗、侧栏、选项页、徽章是扩展自己的界面，不是整站 | 官方 | Google 开发者文档。只采用这个分类 | 2026-11-17 读到目录 |
| MDN Responsive web design | https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design | 普通网页 | 同一页面按视口重排；窄屏 mobile web 不是另一套原生应用。断点按内容何时变坏，而不是按某一台手机 | 社区 / 浏览器文档 | 正文许可证页本轮未单开。只摘要定义并链接 | 2026-11-17 WebFetch 读到定义与 mobile-first 说明 |
| Flutter adaptive and responsive | https://docs.flutter.dev/ui/adaptive-responsive | 跨平台框架 | 响应是塞进空间；适配是换布局和输入方式。框架不是「一个皮肤打所有系统」的理由 | 官方 | 文档不是 BSD 代码许可的自动覆盖。只采用这一区分 | 2026-11-17 读到定义段 |
| Vercel Web Interface Guidelines 仓库 | https://github.com/vercel-labs/web-interface-guidelines | 网页 / 扩展的实现自查 | 交接给写网页的人时作自查清单。不替代平台 HIG，也不提供本仓库的视觉皮肤 | 社区 | 仓库 LICENSE 为 MIT，Copyright (c) 2025 Vercel Labs。本轮读了许可证开头，**没有**重读每一条指南 | 仓库 2026-11-17 读 LICENSE；页面 https://vercel.com/design/guidelines 同日 curl 200 |
| Radix Colors 仓库 | https://github.com/radix-ui/colors | 网页需要一套有来源的色阶时 | 可以作为数值出处。示例草稿没用它的色值 | 社区 | MIT。本轮未复制色板 | 2026-11-17 API 显示 MIT；站点 https://www.radix-ui.com/colors curl 200 |
| microsoft/fluentui | https://github.com/microsoft/fluentui | Windows / Web 组件实现 | 不把组件代码抄进 skill。网站原则与组件库分开引用 | 社区实现，微软维护 | 仓库 `LICENSE` 文件开头为 MIT，Copyright (c) Microsoft Corporation。API 的 SPDX 字段曾是 NOASSERTION，以 LICENSE 文件为准 | 2026-11-17 读 LICENSE 开头；pushed 2026-11-16 |
| material-components/material-web | https://github.com/material-components/material-web | Web 上的 Material 组件 | 不抄组件。Android 落位以 Material 指南和 Android 文档为准 | 社区实现，Google 维护 | Apache-2.0。不覆盖 m3.material.io 上的文章 | 2026-11-17 API；pushed 2026-11-16 |
| material-components-android | https://github.com/material-components/material-components-android | Android 组件 | 仓库说明为维护模式。不要求安装它才能使用本 skill | 同上 | Apache-2.0 | 2026-11-17 API；pushed 2026-10-16 |

---

## WCAG 引用所需的出处

本仓库提到 WCAG 2.2 的目标尺寸和对比度时，依据的是：

- 文档：Web Content Accessibility Guidelines (WCAG) 2.2，W3C Recommendation，12 December 2024
- URL：https://www.w3.org/TR/WCAG22/
- Copyright © 2024 World Wide Web Consortium. https://www.w3.org/copyright/document-license-2023/

采用的决定（不是规范全文）：网页草稿的指针目标至少满足 2.5.8 的 24×24 CSS 像素这一档，并记得它有例外；重要操作可以按 2.5.5 的 44×44 CSS 像素来留余量。正文对比按 1.4.3 的 4.5:1（大号文字 3:1）来检查。这些数字不改写成「HIG 规定网页必须如此」。

---

## 方向、记忆和评审（2026-11-17 另读）

这三份公开技能只提供做法，不安装、不运行它们的脚本，也不把手册抄进本仓库。星标不是采用理由。本轮没有证明任何外部技能会在真实会话里照做。

| 来源 | URL | 采用的做法 | 许可 | 核对 |
|------|-----|------------|------|------|
| Anthropic frontend-design | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md | 先写短的视觉计划，对照任务看是不是通用默认脸，再做完整稿，然后自查。大胆集中在一处 | 该技能目录下的 `LICENSE.txt` 为 Apache-2.0。仓库 API 的 SPDX 为空，不能把整个 anthropics/skills 仓库都说成同一许可证 | 2026-11-17 读到 Process 与 Restraint 两节 |
| Hallmark | https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md | 用户已经点名方向就直接做；否则先给出少数几个不同方向，看过再做完整页面 | 仓库 MIT，Copyright (c) 2026 Hallmark contributors | 2026-11-17 读到 Direction 一节。不运行它的 `theme.mjs` |
| Impeccable | https://github.com/pbakaus/impeccable | 用项目自己的 `DESIGN.md` 记住视觉；评审之后，精修留下原有功能与文案，重做才换外观 | Apache-2.0 | 2026-11-17 读 README 的命令表和 `skill/SKILL.src.md` 里关于精修与重做的一句。未逐条打开它宣称的规则文件，也不使用它的启动器 |

## 本轮未当成已读

- Material 导航轨概述页的正文（见上表）。
- GNOME HIG 与 KDE HIG 的内容许可证文本。
- `reference-library.md` 里 2026-11-15 已收录的付费库与文章，本轮没有逐条重开。那里的「已打开」只代表那天的记录。
- Windows 最小点击尺寸：没找到可引用的官方像素，所以不编。
- 任何未出现在本表、且本轮没有打开的产品截图。引用时标「还没核实」。
