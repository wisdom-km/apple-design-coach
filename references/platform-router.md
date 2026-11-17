# 平台路由（只问还没决定的事）

在写设计合同之前使用。目标是把「表面」定下来，并且下一次会话还能用。

本文件不依赖某家 agent 的专有工具。Grok CLI、Cursor、以及其他只能收发明文的宿主都能执行。

---

## 先读已经有的决定

按这个顺序找，找到就用，不要再问同一件事：

1. 用户这一句里已经说清的平台、容器、范围。
2. 项目里的 `.apple-design-coach/context.md`（若存在）。
3. 同一会话里前面已经确认过的合同。

只有会改变落位的缺口才提问。一次只问一个缺口。产品的主任务、用户或约束还没说时，问那个，不要顺便追问技术栈。

设计咨询本身不需要选定框架。用户没提 Flutter、React Native、网页技术时，不要问。用户已经提了框架时，把它记成实现约束，界面仍按目标操作系统的习惯设计。

---

## 问法

宿主若提供结构化选择题（按钮、表单、choice），用它问这一题。宿主没有这种界面时，用编号纯文本，例如：

```text
还缺一个会改变布局的选择：
1. iOS
2. Android
3. 两者都要，先做其中一个
```

不要为了提问去依赖某个必须存在的插件或工具名。没有该界面就用编号。

---

## 决策表

| 用户已经说的 | 怎么定 | 还要不要问 |
|--------------|--------|------------|
| 手机、移动端、phone、mobile，但没说系统 | 不定平台 | 问：iOS、Android，还是两者。不要默认 iPhone |
| iPhone、iOS 手机 | `ios-phone` | 不问 Android。不自动扩到 iPad |
| iPad、平板，且上下文是 Apple | `ipados` | 不问手机系统。不把它做成放大的 iPhone |
| 只说 iOS，产品明显会因手机/平板改导航 | 不定 | 问：iPhone 还是 iPad。单屏小工具可先按 iPhone 做，并写明不含 iPad |
| Android、安卓，或只做安卓 | `android-phone` | 不问 iOS，不扩到桌面 |
| 手机 + Android，没说「只做」 | `android-phone` | 不问 iOS |
| 两者都要 / iOS 和 Android | 多目标 | 若没说先做哪个，问主目标。然后分别落位 |
| 桌面、电脑、desktop，没说容器 | 不定 | 问：浏览器网站，还是安装的桌面应用。不要默认 macOS，也不要默认 Windows |
| 安装的桌面应用，但没说系统 | 不定 | 问：Windows、macOS，还是 Linux |
| Windows 桌面应用、安装在 Windows | `windows-native` | 不再问是不是网站，不再问系统 |
| macOS、Mac 应用 | `macos-native` | 不再问是不是网站。这不是「所有桌面」 |
| Linux 桌面，没说桌面环境 | 不定 | 问：GNOME、KDE，还是项目已经在用的工具包（例如 libadwaita 或 Kirigami）。不要套 Windows 壳 |
| 网站、网页、web app、响应式 | `responsive-web` | 不问扩展。窄屏是同一网站的 mobile web，不是原生 App |
| 浏览器，但没说网站还是扩展 | 不定 | 问：普通网页，还是浏览器扩展 |
| 扩展、插件、browser extension | `browser-extension` | 不问网站的整页信息架构 |
| 多平台列表 | 选一个主目标 | 主目标写完整方案；其余只写差表。不要复制同一套 chrome |
| 范围是只做手机 | 停在手机 | 不要为了「完整」补桌面、网站或扩展 |
| 上下文文件里已经有同一决定，用户没改口 | 沿用 | 不问 |

明确说法优先于模糊说法。同一句里若有冲突，问哪一句算数，不要自行取平均。

---

## 容器不要混

| 容器 | 是什么 | 不是什么 |
|------|--------|----------|
| `ios-phone` / `android-phone` | 安装在手机上的原生应用，或明确按该系统习惯设计的界面 | 桌面网站的窄窗口 |
| `ipados` | 平板上的 Apple 界面：分栏、指针、多任务 | 放大的 iPhone |
| `responsive-web` | 浏览器标签页里的网站。宽窗口和窄窗口是同一产品的两种视口 | 原生桌面应用，也不是扩展弹窗 |
| `browser-extension` | 弹出页、侧栏、选项页、内容脚本。会话短，依附当前网页 | 把整个网站塞进弹窗 |
| `windows-native` | 有自己的标题栏、命令和窗口的 Windows 应用 | 所有桌面，也不是浏览器里的网站 |
| `macos-native` | 使用菜单栏、窗口和工具栏的 Mac 应用 | 网站，也不是 Windows |
| `linux-gnome` / `linux-kde` | 按该桌面环境习惯设计的安装应用 | 把 Windows NavigationView 或 macOS 菜单栏叫做 Linux |

跨平台框架（Flutter、React Native 等）只说明代码可以共用。导航、窗口 chrome、主按钮和指针/触控仍按上面的目标容器分开。Flutter 文档把「适应空间」和「按平台选择可用的布局与输入」分开；这里采用这个区分：一套皮肤打所有系统不算适配。

路由只决定容器。决定了之后，八原则仍然必须用来判断；Android 的导航和控件看 Material，Windows 看 Fluent / WinUI，Linux 看已经选定的桌面环境，网页看页面结构与 WCAG。这些规范选择 B 层，不替换 A 层，也不写成「符合 Apple HIG」。

---

## 可选 Skill：发现了才加载

独立安装本仓库就必须能工作。不要把「先装齐所有平台 Skill」当成门禁。

只有宿主已经列出、或技能目录里确实能读到的 Skill，才可以加载。候选名字仅作对照，不是安装清单：

| 表面 | 可能有用的名字 |
|------|----------------|
| iOS / iPadOS | `platform-ios` |
| Android | `platform-android`、`material-3` |
| 响应式 Web | `platform-web` |
| macOS | `platform-macos` |
| Windows | `platform-windows` |
| 本仓库自带 | 下面的 references。它们不是外部 Skill |

宿主没有技能清单，或清单里没有这些名字：写一句「未发现可加载的平台 Skill，使用本仓库 references」。然后继续。不要声称已经加载。不要中途要求用户先去安装。

加载了某一个时，写明名字和原因（例如「Android 落位，且技能目录里有 material-3」）。外部 Skill 与本仓库冲突时，官方平台习惯优先于把界面做成另一种系统的皮肤；把冲突写进风险备注。

---

## 写入项目，供下次使用

在项目目录里、且这次允许写文件时，把已经定下的内容写入 `.apple-design-coach/context.md`。用户改了决定就更新，并在回复里说明改了哪一条。

不能写文件时：把同一段内容放进回复，并写「未写入项目」。不要假装已经保存。

模板：

```markdown
# apple-design-coach context

- primary_surface:
- also_surfaces:
- container:
- os:
- scope:
- framework:
- primary_task:
- user:
- constraints:
- ask_again: no
- visual_record:
- decisions:
- updated:
```

`ask_again: no` 表示平台已经定了。下次只要用户没有改口，就不要再问平台。

`visual_record` 只写项目里那份设计文档的路径，例如 `DESIGN.md`。色、字和密度以那份文件为准，不在这里再抄一遍。写法见 `design-memory.md`。

这个文件可以提交到用户自己的产品仓库。不要把私人数据写进去。本 skill 仓库里的 `examples/context-android-only.md` 只是格式示例。
