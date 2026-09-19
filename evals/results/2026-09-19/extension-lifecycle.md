**C｜项目诊断：阅读笔记扩展的草稿恢复**

用户需要一边手写长笔记，一边切换标签页查证，再回来续写；保留手动写作是核心约束。[README](../../fixtures/reading-extension/README.md#L3) 明确这是 Chrome Manifest V3 扩展，草稿只存在 popup 的 DOM 状态中。

1. **最高优先级：让草稿独立于弹窗保存，并在再次打开时恢复。** [manifest.json](../../fixtures/reading-extension/manifest.json#L5) 将编辑入口注册成 popup；[popup.html](../../fixtures/reading-extension/popup.html#L7) 只有文本框，没有保存与读取脚本。[Chrome 官方说明](https://developer.chrome.com/docs/extensions/develop/ui/add-popup) 明确，点击弹窗外部后 popup 会关闭，不能保持打开。这与用户反馈吻合，支持“草稿随弹窗关闭而失去”的判断，但本次未实际加载扩展复现。建议编辑过程中持续保存草稿，重新打开先恢复已有文本，不等到关闭时才尝试写入；可采用扩展本地存储，所需 storage 权限及异步写入行为见 [Chrome Storage 文档](https://developer.chrome.com/docs/extensions/reference/api/storage)。界面区分“正在保存”“草稿已保存”“保存失败”，完成写入后才声称已保存；失败保留当前文字，并提供重试、复制文本的出口。验收：输入中文和长段落后立即切换标签、关闭重开弹窗、重启浏览器，逐项比对恢复文本；模拟写入失败，确认不出现虚假成功提示。自动保存解决可靠性，用户仍自行写作、修改和删除。

2. **第二优先级：为跨标签查证提供持续编辑的位置，保持同一份笔记。** 现有 [提示文案](../../fixtures/reading-extension/popup.html#L8) 鼓励切换标签后回来，却没有提供稳定的编辑空间。建议 popup 保留快速记笔记及“继续编辑”入口，把长文写作打开到扩展独立标签页；也可选 Chrome 侧栏，但项目尚未声明最低 Chrome 版本，需先核实目标版本和所需配置。[Side Panel 官方文档](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) 提供相应能力说明。两种编辑入口应读取同一份持久草稿，明确正在编辑哪篇笔记；切换到查证页面时，不自动把原笔记改归新网页或用空稿覆盖它。新增编辑容器有实现成本，第一项持久化仍是前提，单纯加大弹窗不能消除关闭行为。验收：在文章 A 写笔记，切到文章 B 查证，再回来继续，原文与笔记身份保持不变；从 popup 和持续编辑页面先后打开时，不相互覆盖更新的内容。

这两项借用 Apple 的 Agency 与 Flexibility：保护用户劳动，也适应真实的查证流程，具体排序和方案是本次设计判断。[原则出处](https://developer.apple.com/videos/play/wwdc2026/250/)

本方案借用 Apple 设计原则，不作 HIG 合规认证；控件与导航遵循实际宿主平台和项目设计系统。本次已读取 README、manifest.json、popup.html 并核对 Chrome 官方文档；未安装或加载扩展，未实测保存、切换标签和恢复，未修改代码。以上验收全部待执行。
