# 平台路由走查

日期：2026-11-17。这是对照 `SKILL.md` 与 `references/platform-router.md` 写的预期行为，用来人工核对和做文档断言。

它不是 Grok CLI 的真实运行记录，也没有在 iPhone、Android、Windows、macOS 或 Linux 真机上测试。

| # | 用户原话里的平台信息 | 预期 | 不应出现 |
|---|----------------------|------|----------|
| 1 | 「做个手机应用，算餐后 AA」 | 问 iOS、Android，还是两者。编号或宿主选择题 | 直接按 iPhone 出方案 |
| 2 | 「只做安卓」 | 主表面 `android-phone`，不再问 iOS | 再问要不要做 iPhone；补桌面 |
| 3 | 「iPhone 上的 AA」 | `ios-phone`。结构见 `aa-split-ios-coaching.md` | 扩成 iPad 或 Android |
| 4 | 「做个桌面版」 | 先问：浏览器网站，还是安装的桌面应用 | 默认 macOS；把 Windows 当全部桌面 |
| 5 | 「安装在 Windows 上的桌面应用」 | `windows-native`。标题栏、命令栏、NavigationView | 再问是不是网站；再问系统 |
| 6a | 「一个看书清单网站，手机浏览器也要能用」 | `responsive-web`。窄屏是同一网站 | 做成扩展弹窗或原生 App |
| 6b | 「浏览器扩展，保存当前页」 | `browser-extension`。弹窗一件事 | 把整站塞进弹窗 |
| 7 | 「macOS 应用」 | `macos-native`。菜单栏在窗口之外 | 画成网页或 Windows 标题栏 |
| 8 | 「iOS 和 Android 都要，先做 Android」 | 主目标 Android；iOS 只写差表 | 两套都用底栏皮肤，或再问先做哪个 |
| 9 | 项目里已有 `context.md`，`ask_again: no`，用户只说「把主按钮文案改成复制」 | 沿用原表面，只改文案 | 再问平台 |
| 10 | 要 Android 方案，但技能目录里没有 `platform-android` / `material-3`；也没有图像工具 | 写明未发现这些 Skill，改用本仓库 references。没有图像工具就不声称出了图 | 假装已经加载；要求先装齐才能继续 |
| 11 | 「给我一张能看的稿，不要写产品代码」 | 合同和落位之后给独立 HTML 草稿或回复里的 HTML。不创建产品工程 | 只给提示词或 ASCII 并称之为视觉稿；开始实现应用 |

多目标没有「先做哪个」时，只多问这一题。设计任务不问框架，除非落位真的依赖一个已经在项目里的工具包（例如已经使用 libadwaita）。

上下文文件的格式示例：[`context-android-only.md`](context-android-only.md)。写入位置是目标项目的 `.apple-design-coach/context.md`，不是本 skill 的 README。
