# apple-design-coach

用 Apple 设计原则改善**现有项目的界面和体验**。这是给 AI 编程助手使用的设计教练 skill：读取项目，理解用户任务，找到具体问题，解释取舍，给出能实施、可验收的建议。

支持 iOS、iPadOS、macOS、Windows、web 和浏览器扩展。保留现有技术栈、品牌和必要功能，按宿主平台调整交互。

## 可以怎样用

在支持 skills 的工具中安装后，打开目标项目并输入：

```text
请使用 $apple-design-coach 先理解当前项目的用户、主任务和技术栈。
检查主要页面，给出最值得先改的 3 个体验问题。
每项说明：证据位置、用户影响、具体改法、如何验收。
先给建议，不改代码；保留已有业务功能和品牌。
```

有了建议，继续要求落地：

```text
请使用 $apple-design-coach 修复刚才确认的保存失败体验问题。
复用现有组件和样式，保留输入，提供清晰的错误与恢复路径。
完成当前环境能执行的检查，明确哪些还没有验证。
```

没有代码也能开始：给出目标平台、用户任务和问题描述；截图、线框均可选。如果问题很小，可以只问“这个操作应该放哪里”，无需填写完整产品表。

## 输出是什么

| 场景 | 输出 |
|------|------|
| 已有项目诊断 | 项目理解；有证据的优先问题；具体改法与验收 |
| 只问一个问题或要三个建议 | 按请求范围直接回答，不强制长报告 |
| 新功能或整体改版 | 设计合同 → 功能落位 → UI 结构 → 状态与权限 → 参考建议 → 风险与验证 |
| 授权修改代码 | 实际改动、保留的约束、运行结果及未验证项 |

例如，发现保存逻辑在请求成功前清空表单时，建议会关联实际组件，解释失败时如何丢失输入，提出成功后再清空与可访问错误反馈，并给出模拟失败后的验收步骤。不会仅给“更简洁、更高级”的形容词。

## 安装

这是普通的 `SKILL.md` 文件夹，没有运行时依赖，也不需要 API key。

1. 克隆本仓库或下载源码。
2. 将 `SKILL.md`、`agents/`、`references/`、`LICENSE`、`NOTICE` 保持结构，放到工具配置的 skills 目录下的 `apple-design-coach/` 文件夹。Codex 用户级目录可用 `~/.codex/skills/apple-design-coach/`。
3. 按工具要求刷新技能发现；在目标项目中调用 `$apple-design-coach`。其他工具的目录和调用语法以其实际配置为准。

暂不安装也可以：在目标项目的对话中明确要求“读取这份仓库的 SKILL.md，并按它评估当前项目”，提供本地完整路径。直接读文件不等于已经注册到工具的自动发现列表。

可构建精简安装包：

```sh
python -m pip install -r requirements-dev.txt
python scripts/build_skill.py
```

生成 `dist/apple-design-coach.zip`，包含一个 `apple-design-coach/` 顶层目录。开发测试需要 Python 3.10+ 与 PyYAML；**使用 skill 不需要 Python**。打包前会执行结构校验，不会把开发用例、结果或虚拟环境带入安装包。

## 设计依据与边界

保留项目原有的两层设计：共享原则 + 平台适配。

- 共享原则：Purpose、Agency、Responsibility、Familiarity、Flexibility、Simplicity、Craft、Delight，见 [Apple WWDC26 官方课程](https://developer.apple.com/videos/play/wwdc2026/250/) 和 [HIG Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)。
- 平台适配：同一任务按输入方式、窗口模型和平台惯例调整；React 网页在 Windows 浏览器运行仍是 web。
- 证据：区分用户描述、代码观察、截图线索与设计推断；不会凭截图宣布读屏、对比度或离线行为通过。
- 范围：必要功能不能因为“减法”被直接删除；可撤销删除不机械加确认框；不把所有页面都变成 Liquid Glass。
- 视觉冲突：默认先理解线框意图，再检查截图；用户声明的最新目标优先，废弃草图不能覆盖当前要求。

这不是 Apple 官方工具或合规认证器。教练问题、优先级与验证流程是本仓库的方法，不是 Apple 强制条款。具体平台/API/版本结论按需查询官方资料，见 [来源索引与核实记录](references/sources.md)。

## 测试与示例

```sh
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

- [评测方法与案例](evals/README.md)：覆盖项目读取、聚焦建议、扩展生命周期、信息不足、旧线框、材质/版本、多平台、触发边界及代码修复。
- [本次测试报告](docs/TEST-REPORT.md)：实际运行结果、原始输出与验证限制。
- [餐后 AA 完整设计示例](examples/aa-split-ios-coaching.md)：示范答案，不能当作独立测试通过证据。

GitHub Actions 会检查元数据、引用完整性、评测配置、校验器与安装包；不会自动证明建议质量。情境试用和真实产品验收需分别执行。

## 目录

```text
SKILL.md                 核心入口与模式选择
agents/openai.yaml       Codex 展示信息与默认调用提示
references/              按任务读取的原则、项目诊断、平台与验证参考
examples/                完整设计包示范
evals/                   行为案例、合成项目、实际试用结果
scripts/                 离线结构校验与打包
tests/                   校验器和打包回归测试
docs/TEST-REPORT.md       本次测试证据与局限
```

## License

Original skill text and structure: MIT. Apple HIG, WWDC materials and trademarks belong to Apple Inc. This unofficial project links to official sources and does not redistribute the full HIG. It is not affiliated with or endorsed by Apple.

Workflow inspiration (structure only): [HIG-Driven](https://github.com/dzakwanfadhlullah/HIG-Driven).
