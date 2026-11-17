# 成稿完成度走查

日期：2026-11-17。对照 `references/aesthetics.md`、`references/visual-drafts.md`、`references/draft-critique.md`。

## 实际做过

在隔离环境里用桌面 Chrome 以 `file://` 打开下面这些本地 HTML，并截图：

- 改进前的多框说明书：[android-ledger-craft-before.html](drafts/android-ledger-craft-before.html)，截图 [android-ledger-craft-before.png](drafts/screenshots/android-ledger-craft-before.png)
- 改进后的一帧主界面：[android-ledger-craft.html](drafts/android-ledger-craft.html)，主屏 [android-ledger-craft.png](drafts/screenshots/android-ledger-craft.png)，状态在后面 [android-ledger-craft-states.png](drafts/screenshots/android-ledger-craft-states.png)
- 窄窗口和 150% 字号：[android-ledger-craft-narrow.html](drafts/android-ledger-craft-narrow.html)，截图 [android-ledger-craft-narrow.png](drafts/screenshots/android-ledger-craft-narrow.png)

`python3 tests/check_skill.py` 只检查文档句子和 HTML 没有外链。它不是审美验收。

这些 HTML 是仓库里的示例，由编写示例的人画出来，用来说明规则。它们不是一次 Grok CLI 会话生成的终稿。

## 看得见的前后差

同一套示例数据，仍是 Android、仍是系统密表：

- 改进前：说明和四只粗黑框在内容前面；顶栏「搜索 / 更多」和标题同一字重；长标题和金额挤在一起；空白和加载是高屏里的一句字；加载用了绿色的「请稍候」。
- 改进后：打开先是一帧「本月」；结余是唯一的大字；金额列等宽右齐；长标题在行里最多两行，全文在后面的详情；顶栏是图标；空白和失败展开「更多」里的分类和货币；加载是骨架，没有能点的主色按钮。

没有改成大卡片、大留白或玻璃渐变。

## 没有做过（NOT VERIFIED）

没有跑 Grok CLI。这些检查不是 Grok CLI 测试。不能把手写示例当成技能已经让模型画出合格成稿的证明。

没有 Windows 上的真实会话，没有安卓真机。截图是桌面 Chrome 打开 HTML。
