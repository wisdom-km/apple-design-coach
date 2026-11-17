# 状态与交接走查

日期：2026-11-17。对照 `SKILL.md` 的状态段、实现交接模板，以及 `references/draft-critique.md`。

`tests/check_skill.py` 是仓库的开发检查。使用这个 skill 不需要运行它，也不需要安装运行时。

## 实际做过

在隔离环境里用桌面 Chrome 以 `file://` 打开下面这些本地 HTML，并截图：

- 宽窗口下的四种列表状态：[android-ledger-list.html](drafts/android-ledger-list.html)
- 窄窗口下的同一文件（先看到长中文标题）
- 150% 字号的失败态：[android-ledger-list-scaled.html](drafts/android-ledger-list-scaled.html)
- 可选照片被拒绝：[android-ledger-photo-denied.html](drafts/android-ledger-photo-denied.html)

`python3 tests/check_skill.py` 检查句子、本地链接，以及草稿 HTML 里没有 `http`、`https` 或脚本。页面用 `file://` 打开。同一次打开写下的 Chrome netlog 里仍有 `accounts.google.com` 等主机，那是浏览器进程自己的连接，草稿 HTML 里没有这些地址。所以「页面没有外链」成立；「整个浏览器进程零网络」不成立。没有另放代理去拦截那些连接。

交接样例 [project-memory/handoff.md](project-memory/handoff.md) 指向 [project-memory/DESIGN.md](project-memory/DESIGN.md)，并保留 `receipt-photo: optional-never-required`。交接里没有新的色值。

## 静态断言，不是代理会话

下面几条由文件里的句子和 HTML 结构支撑。它们不是一次真实 AI 会话的记录。

| 情况 | 文件里的预期 | 这次的证据 |
|------|----------------|------------|
| 记账主屏不需要权限 | 不画权限流程 | `android-ledger-after.html` 写明权限页不适用 |
| 列表会读失败 | 空白、加载、失败和重试出现在稿上 | 列表 HTML 里有这四块 |
| 用户点了附照片 | 拒绝后仍能保存，并能再试 | 照片页有这两个动作 |
| 只讨论方向 | 不写交接 | `direction-choice.md` 写了这一句 |
| 用户要交接 | 平台、设计记录、状态、交互、验收都在，不指定技术栈 | `handoff.md` |
| 已有设计记录 | 引用 DESIGN.md，不另写色板，保留自定义字段 | 交接没有色值；DESIGN.md 的 receipt-photo 仍在 |
| 没有提供的数字 | 保持未知或标成示例 | 删除的确认方式仍是 Unknown；金额标成示例数据 |

## 没有做过（NOT VERIFIED）

没有跑 Grok CLI。这些检查不是 Grok CLI 测试，也没有别的新鲜 AI 会话成绩单。因此不能把上面的 Markdown 样例当成模型已经照做的证明。这些行为在真实会话里是否发生，标为 NOT VERIFIED。

没有真机。HTML 截图不是 iOS 动态字体，也不是安卓系统权限弹窗。没有在用户的电脑上写文件。没有合入。
