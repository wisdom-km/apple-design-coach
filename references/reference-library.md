# 参考来源与参考写法（Reference Library）

写输出骨架的「参考建议」前加载本文件；用户给来别人产品的截图时也加载。

来源说明：清单从 Eian（@EianLu）的 X 文章《100 个提升审美的设计网站大赏》中筛出，只留与**软件 UI / 产品设计**相关的条目。每个链接在 2026-11-15 用 curl 打开过，返回 200 才收录。「付费」标记沿用原文说法。站点内容会变，引用前以当时打开的页面为准。

---

## 规则 1：真实产品优先于概念稿

原文：「画界面之前，建议先去翻翻已经上线运营的真实产品，少逛概念设计社区。真实产品能帮你把异常状态、按钮层级这些基本逻辑理顺；概念稿好看归好看，很多根本落不了地。」

教练怎么做：

- 「参考建议」里先给**已上线产品**里的模式，再给奖项或作品集里的灵感。
- 概念稿、Dribbble 式作品只能参考气质，不能用来证明某种落位可行。
- 拿参考看的是**状态和层级**：空态、错误、权限拒绝、付费墙、取消订阅，不只看首屏。

## 规则 2：参考要能叫出名字、说清手法

原文：「你如果只会跟 AI 说『帮我把网页改得大气一点、现代一点』，它给你的永远是最平庸的模板」「只有你能准确叫出名字、说清门道的东西，才是你真正长在身上的审美。」

这一点和 Emil Kowalski《Agents with Taste》（https://emilkowal.ski/ui/agents-with-taste ，已打开）一致：几乎每个「品味」决定，细看都有一个逻辑理由；能说出理由，才能把它交给 agent。

每条参考按下面格式写，缺一项就不算合格参考：

```text
参考：<产品/系统 + 具体界面或模式名>（来源：<链接>；已打开 / 还没核实）
手法：<具体做法，例如「结果数字放大并锚定在拇指区」「破坏性操作与主按钮不同形」>
为什么好：<对应哪条原则或哪条 UX 定律>
本案怎么借：<借意图，不借皮肤；非 Apple 表面换成本地惯例>
```

禁止用来替代手法描述的空词：高级、现代、大气、简约感、科技感、有质感、苹果风。

## 规则 3：没打开就不说「参考了」

- 付费库（Mobbin、Page Flows、Refero、Nicelydone、SaaSFrame）多数要登录。没打开具体页面时，只能写「建议去筛 X 标签对比」，不能编造某个产品的具体做法。
- 写某产品的具体细节，必须是本轮打开过的页面或用户提供的截图；否则标「还没核实」。

---

## 按设计问题找参考

### 功能落位、流程、状态（最常用）

| 来源 | 何时翻 | 看什么 | 备注 |
|------|--------|--------|------|
| [Mobbin](https://mobbin.com/) | 要画某类页面（订阅页、空状态、引导） | 按功能标签把多个上线 App 并排对比 | iOS / Android / Web；付费，免费号可看一部分 |
| [Page Flows](https://pageflows.com/) | 梳理整条流程（注册、付费、取消） | 带点击轨迹的真实操作录屏 | 付费 |
| [Refero](https://refero.design/) | 找具体组件和页面类型（表格筛选、面包屑、价格表） | 标签细，适合查某个组件 | Web + iOS；付费 |
| [Nicelydone](https://nicelydone.club/) | ToB、后台、复杂表单、数据看板 | 高密度界面的层级 | 付费 |
| [SaaSFrame](https://www.saasframe.io/) | SaaS 的登录、设置、弹窗 | 按页面类型分好类 | 付费 |
| [Growth.Design](https://growth.design/) | 想知道某一步为什么让人放心或让人流失 | 用连环画拆解真实产品体验 | 免费 |
| [Game UI Database](https://www.gameuidatabase.com/) | 信息量极大、要排层级（HUD、背包、设置） | 按 UI 功能分类的游戏截图 | 免费 |

平台权威来源、许可和「本轮有没有读到正文」记在 `source-provenance.md`。官方网页不是因为能打开就属于 MIT。下面的表保留 2026-11-15 的用法；本轮没有把每一条付费库重开一遍。

### 平台惯例与组件（Familiarity 依据）

| 来源 | 何时翻 | 备注 |
|------|--------|------|
| [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) | Apple 表面的控件、导航、权限问题 | 本 skill 的 A 层来源 |
| [Apple Design Awards](https://developer.apple.com/design/awards/) | 找 Apple 平台上公认做得好的 App | 按类别列获奖与入围（Delight and Fun、Inclusivity、Innovation、Interaction 等，已打开）；原文说每个获奖 App 附评语，还没逐条核实 |
| [Material Design 3](https://m3.material.io/) | 学一套设计系统怎么定色阶、字号层级、状态 | 不做 Android 也可读；不要把 M3 外观搬到 Apple 表面 |
| [The Component Gallery](https://component.gallery/) | 同一个组件（开关、警告横幅）各家怎么做 | 多套设计系统并排，查漏补缺 |
| [Figma Community](https://www.figma.com/community) | 想看设计系统源文件的结构 | 看 Auto Layout、变量命名 |

### 理由与原则（写「为什么好」时用）

| 来源 | 用途 |
|------|------|
| [Laws of UX](https://lawsofux.com/) | 给落位和简化找心理学依据；映射见 `eight-principles.md`「UX 定律作理由」 |
| [Rauno Freiberg — Invisible Details of Interaction Design](https://rauno.me/craft/interaction-design) | Craft：手势、滚动、菜单防误触这些「看不见的细节」 |
| [Emil Kowalski — You Don't Need Animations](https://emilkowal.ski/ui/you-dont-need-animations) | Craft / Delight：每个动效先问目的；什么时候不该加动效 |
| [Practical Typography](https://practicaltypography.com/) | 正文行长、行高、字距的底线 |

### 实现交接与自查（交给写码 agent 时用）

| 来源 | 用途 | 备注 |
|------|------|------|
| [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines) | Web、浏览器扩展 UI 写完后的逐条自查 | 页面提供 AGENTS.md 和 `web-design-guidelines` skill；条目如「移动端输入框字号 ≥16px，防 iOS Safari 自动放大」「不要 `transition: all`」（已打开核实） |
| [Impeccable](https://impeccable.style/) | 识别「AI 味」默认套路 | 首页示例含 card 套 card、状态 chip 堆砌、所有元素一样重、字段过多、空泛 CTA（已打开）；原文说有 62 项检查，还没核实 |
| [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) / [Refero Styles](https://styles.refero.design/) | 品牌风格的 DESIGN.md 合集 | 只在 Web 产品、且用户明确要某品牌风格时用；Apple / Windows 表面不要拿来替代平台惯例 |
| [Radix Colors](https://www.radix-ui.com/colors) / [Utopia](https://utopia.fyi/) | 需要数值时引用的体系（12 级色阶、按比例的字号阶梯） | 用来避免「伪精确」：数值必须有体系来源 |

### 动效与细节灵感（Craft，克制使用）

| 来源 | 看什么 |
|------|--------|
| [60fps](https://60fps.design/) | 真实 App 的高帧率交互片段 |
| [Spotted in Prod](https://www.spottedinprod.com/) | 已上线 iOS App 的小细节 |

---

## 用户贴来别人产品的截图

这类截图既不是「现实」（不是本产品现状），也不是「意图」（不是本产品线框）。按 **外部参考** 处理，规则见 `input-visuals.md`：

1. 先复述「我看到的是……」，说出 1–3 个可命名的手法；
2. 每个手法对上原则；
3. 只借意图，按本产品的表面翻译；不照抄布局、品牌色、插画。

---

## 不收录（及原因）

- 广告、电影、3D、MV、动画类奖项和片库（D&AD、ShotDeck、ArtStation 等）：与软件 UI 落位无关。
- 实验性网页奖项与怪网站（FWA、Hoverstat.es）：常与 Familiarity、Simplicity 冲突，只适合找视觉灵感，不适合作落位依据。
- Awwwards / CSS Design Awards / 落地页图库：偏营销网页，本 skill 无「营销网页」表面；需要时交给 hallmark / ui-ux-pro-max。
- WebGL / Shader / GSAP 演示库：属实现层，不属教练层。
- Pinterest：原文自己提醒信息流混入大量粗糙 AI 生成图。
- Realtime Colors：2026-11-15 打开返回 402（DEPLOYMENT_DISABLED），暂不收录。
- Siteinspire：curl 被安全检查页拦截（429），还没核实，暂不收录。
