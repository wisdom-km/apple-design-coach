# 排版关系走查

日期：2026-11-17。对照 `references/aesthetics.md` 的六步和 `references/draft-critique.md` 的最多 5 条。

## 预期

- 说明容器里更具体的 `p` 规则清掉应用段落的横 margin，应识别为宿主污染。打开文件时的第一帧如果在该规则外面，不把它说成同样错了。
- 图标槽比正文更靠左、分隔线满宽，是刻意的，不应判成必须同一左线。
- 长中文保留全文，完整金额在窄宽时可以换到下一行。密表不换成海报大数字。
- 修复先动容器和级联，不用 `!important` 或多处负 margin 补洞。

## 实际做过

`python3 tests/check_skill.py` 用选择器优先级比较了 `.notes p` 和 `.balance`，并检查两份本地 HTML 里的句子：

- 反例：[layout-host-pollution.html](drafts/layout-host-pollution.html)
- 正例：[layout-intentional.html](drafts/layout-intentional.html)

没有用浏览器把这两份再截图。没有跑 Grok CLI。这些检查不是 Grok CLI 测试，也不是真机。

## 给下一次真实会话的短复测

用新的消费者包开一次新会话，让它在已选的 Android「系统密表」上交出一帧，并在同一文件里放一个状态。然后只看三件事：结余和大数字的前缘是否与列表正文相同；这个状态若包在说明容器里，前缘有没有被说明样式改掉；窄宽时金额是否仍完整。三件都要指到画面上的位置。这一份仓库里的反例不能代替那次会话。

## 没做过（NOT VERIFIED）

没有 Windows 上的真实会话，没有安卓真机。方法写进参考不等于新的 CLI 已经排出合格画面。
