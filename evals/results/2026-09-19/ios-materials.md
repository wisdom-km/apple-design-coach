建议以连续、舒适阅读为主任务，保留现有品牌和 iOS 17 支持，把新材质集中用在工具栏等操作区域。

- **正文卡片与背景保持稳定。** 沿用品牌配色、排版和已有阅读主题，以不透明背景或克制的标准材质区分内容层。Apple 明确把 Liquid Glass 定位于导航和控件层，不建议用于正文内容层；全页玻璃会削弱这层区分。[Apple Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- **工具栏分系统版本渐进适配。** Liquid Glass 从 iOS 26 引入；最低部署版本仍保持 iOS 17。先用当前 SDK 构建，检查已有系统工具栏和按钮在支持系统上的默认外观，再决定是否需要定制。自定义新材质调用必须按其实际 API 可用版本分支，iOS 17 保留现有工具栏和背景方案，所有阅读、搜索与书签功能相同。当前没有项目配置，不能认定现有自绘背景或组件已经兼容。[Apple 发布说明](https://www.apple.com/newsroom/2025/09/new-versions-of-apples-software-platforms-are-available-today/) · [Liquid Glass 采用指南](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)
- **滚动时保持正文位置稳定。** 不建议让段落随滚动大幅缩放、旋转或视差位移；将动效用于打开阅读设置、保存书签等明确反馈，避免等待动画才能继续阅读。自定义动效读取 `accessibilityReduceMotion`，开启时取消大幅位移和缩放；自定义半透明背景依据 `accessibilityReduceTransparency` 切换为不透明。品牌通过颜色、内容和语气保留，不靠叠加玻璃强化。[Apple Motion](https://developer.apple.com/design/human-interface-guidelines/motion) · [减少动态效果](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion) · [降低透明度](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency)

实施后分别在 iOS 17 和拟支持的新系统上检查：长文连续滚动、阅读位置恢复、亮暗主题、动态大字号、减少动态效果、降低透明度、VoiceOver 和滚动性能。验收标准是正文可读、操作可达、品牌可辨认，关闭效果不损失功能。本次只核对了官方指导与版本引入信息，未读代码、编译或运行；具体新材质 API 的可用性声明仍须在实施时核对，不能据此声称已通过设备验证。
