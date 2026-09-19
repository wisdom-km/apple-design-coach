# 官方来源与核实边界

按需查与当前建议相关的页面，不要批量抓取整部指南。链接是检索入口；做具体规范/API/版本结论时须阅读对应内容。无法访问正文时说明未核实，不能把 JavaScript 提示页当作已读规范。

| 主题 | 官方入口 | 使用范围 |
|------|----------|----------|
| 八项原则 | [WWDC26 Session 250](https://developer.apple.com/videos/play/wwdc2026/250/)；[HIG Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) | 判断与取舍；本仓库的教练问题是转述/方法 |
| 导航与动作 | [HIG Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | 顶级目的地、状态保留；不把执行动作当导航 |
| 可访问性 | [HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)；[Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | 感知、操作、动态字号；具体阈值需确认平台和单位 |
| 材质 | [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | 导航/控件层、背景可读性与辅助功能设置 |
| Windows 导航 | [Microsoft Navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics) | 原生 Windows 导航，不能要求 web 改成 WinUI |
| 扩展弹窗 | [Chrome Add a popup](https://developer.chrome.com/docs/extensions/develop/ui/add-popup) | 失去焦点会关闭；长任务需考虑持久状态和合适容器 |
| Web 表单 | [W3C WAI User notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) | 清晰反馈、错误关联、辅助技术可感知；不是整站合规认证 |

2026-09-19 核实记录：WWDC26 视频页的标题、八章节和文字稿可读，八原则出处成立；HIG Design principles 的直接网页抓取只返回 JavaScript 提示，未据此声称读到正文。其余主题通过官方页面可检索正文核对上述有限范围；不代表本文件覆盖全部规范或未来版本。后续使用遇到新系统/API时重新核实。

报告把依据分清：

- **官方指导**：链接到支持该结论的具体主题，不用首页为所有断言背书。
- **项目事实**：给文件/界面证据与版本。
- **教练判断**：说明为何适合本案、代价与验证方式，不能包装成 Apple 强制要求。
