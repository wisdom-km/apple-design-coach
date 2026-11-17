# 前三项走查

日期：2026-11-17。对照 `direction-choice.md`、`design-memory.md`、`draft-critique.md`。

**实际做过的：** 在这台隔离环境里写了示例 HTML，并用桌面 Chrome 打开方向小样、评审前和评审后三张页面。`python3 tests/check_skill.py` 检查文档句子和本地链接。

**没做过的：** 没有跑 Grok CLI。这些检查不是 Grok CLI 测试。没有在用户的电脑上写文件，没有真机，也没有证明模型下次会照做。下表的「预期」是技能文本要求的行为，不是一次真实会话的记录。

| # | 情况 | 预期 | 这次有没有用样例演出来 |
|---|------|------|------------------------|
| 1 | 方向含糊，只要手机记账草稿 | 先给 2–3 个不同方向，不出完整稿 | 有。`drafts/android-ledger-directions.html` 是三张小样，不是三个成品 |
| 2 | 已经说 Android，或设计记录里方向已确认 | 不问平台，也不再问方向 | 预期写在 `project-memory/context.md`。没有另开一次代理会话去验证 |
| 3 | 已有 `DESIGN.md`，用户要设置页 | 沿用原风格和自定义字段，只加设置页 | 样例保留 `receipt-photo: optional-never-required`。没有生成第二份被覆盖的文件 |
| 4 | 再次进入同一项目 | 同一套视觉 | 同上，只是文件里的约定 |
| 5 | 用户明确要换品牌 | 先问，记下之后再改 | 写在 context 示例的最后一句。没有演一次对话 |
| 6 | 不知道项目根 | 不写文件 | 只写在 `design-memory.md`。这次没有对一个模糊目录做写入试验 |
| 7 | 用户说「你定方向」 | 代选并写理由，`confirmed_by` 不是 user | 写在方向文件里。样例本身标的是尚未选定 |
| 8 | 稿子主按钮和删除同形、长标题被截断 | 评审后改稿，功能还在 | 有。`android-ledger-before.html` 与 `android-ledger-after.html` |

八原则仍然先于平台控件。三张 Android 小样都没有换成 iOS 底栏。
