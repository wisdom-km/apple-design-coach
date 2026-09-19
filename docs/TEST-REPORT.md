# 测试报告：项目设计教练

日期：2026-09-19。基线提交：`bcb0b4c`。本次范围：保留八原则和跨平台设计方向，增强现有项目诊断、建议质量、授权修复与验证。

## 基线检查

原仓库包含一个入口、四份参考和一个手写示例，没有独立评测清单、校验脚本或 CI。原版在一次聚焦网页咨询中给出了有用建议，不能据此声称原版不会指导设计。

静态检查发现的改进点：缺少项目读取/代码定位流程；固定六段输出与小问题不匹配；缺少 web 独立表面；部分导航数量/步骤限制写成通用规则；线框未画的功能误被当成非目标；删除确认缺少恢复风险判断；AA 示例小费金额不一致（328 的 10% 为 32.80，原示例写 36）。

## 自动化检查

环境：Windows PowerShell；Python 3.14.2；PyYAML 6.0.3；Node v24.13.0。Python 依赖仅安装到本项目 `.venv`。CI 配置使用 Python 3.12；本报告记录本地结果，不能据此宣称远端 CI 已通过。

| 检查 | 结果 | 能证明什么 |
|------|------|------------|
| `python scripts/validate_skill.py` | PASS | frontmatter、展示元数据、本地链接、参考可达性、9 个案例的结构/fixture |
| `python -m unittest discover -s tests -v` | 12/12 PASS | 能识别缺失引用、越界路径、错误元数据、重复案例和无效 fixture；安装包可独立解压校验 |
| skill-creator 的 `quick_validate.py` | PASS | 技能入口通过其基础结构检查 |
| 保存处理函数模拟 | 修复副本 PASS；原始副本预期 FAIL | 真正执行提取的保存函数，检查等待、失败、重试、成功、重复提交与同步异常 |

原始副本的失败断言是 `Keep draft while saving`：输入 `128.50 / 餐饮` 在请求完成前变成空字符串。相同脚本在修复副本中通过。不是只对理想答案中的关键词打勾。

保存模拟脚本另有 JSX 属性和入口的静态检查；这些静态检查不能证明浏览器/读屏行为。复现修复后的有限验证：

```sh
node evals/results/2026-09-19/implementation/check-save.cjs
```

复现失败对照时，将该脚本复制到临时目录中的 `ledger-web` 原始 fixture 副本后执行；不要改动原 fixture 来使测试通过。

## 情境试用与人工复核

模型：本次会话的 GPT-6 系列代理，沿用父任务模型设置，没有指定覆盖或固定随机种子。执行代理未获得判据、期望答案或父任务结论；原版由单独代理执行一次，改进版分为项目组、边界组、实施组与干净的触发测试。

**9 个案例的 39 条判据，本轮人工复核均满足。** 这是主代理对实际输出的定性检查，不是自动模型打分、独立人类评价或 39 个软件单元测试。逐条证据见 [assessment.json](../evals/results/2026-09-19/assessment.json)。

| 案例 | 本轮观察 | 实际输出 |
|------|----------|----------|
| 三个网页建议 | 保留必要功能，识别 web，只给三条，不把未知数据丢失说成事实 | [focused-web](../evals/results/2026-09-19/focused-web.md) |
| 读取真实文件 | 定位 await 前清空 draft、catch 未恢复；建议关联源码；不谎称启动 | [repo-review](../evals/results/2026-09-19/repo-review.md) |
| 扩展生命周期 | 识别 popup 关闭与 DOM 草稿冲突，建议持久化与适合长任务的容器 | [extension-lifecycle](../evals/results/2026-09-19/extension-lifecycle.md) |
| 信息不足 | 询问平台与主任务，未默认 iPhone 或编造截图 | [unknown-platform](../evals/results/2026-09-19/unknown-platform.md) |
| 废弃线框 | 保留当前分栏，不让旧五 Tab 覆盖明确要求；区别文字与图像 | [old-wireframe](../evals/results/2026-09-19/old-wireframe.md) |
| 材质与版本 | 保留 iOS 17 和品牌，正文不全玻璃化，列出辅助功能与版本验证 | [ios-materials](../evals/results/2026-09-19/ios-materials.md) |
| 原生多平台 | 保留批量能力，区分手机触控和 Mac 菜单/键盘 | [native-multiplatform](../evals/results/2026-09-19/native-multiplatform.md) |
| 无关代码任务 | 仅凭元数据，拒绝误用设计教练处理 Python 时区 bug | [negative-trigger-clean](../evals/results/2026-09-19/negative-trigger-clean.md) |
| 授权实施 | 只改隔离副本，失败保留输入、动态反馈语义；实际模拟并诚实报告限制 | [scoped-implementation](../evals/results/2026-09-19/scoped-implementation.md) |

原版的 [同一聚焦案例输出](../evals/results/2026-09-19/baseline-focused-web.md) 也表现良好。此次不声称所有表现均优于原版，或给出无统计依据的提升百分比；新增价值主要在明确项目工作流、安装/校验资源以及覆盖更广的测试材料。

实施产物：[修改后的组件](../evals/results/2026-09-19/implementation/src/BillForm.tsx)、[实际模拟脚本](../evals/results/2026-09-19/implementation/check-save.cjs)。这些文件是测试证据，不进入 skill 安装包。

## 试验限制与未覆盖项

1. 项目组三例共享代理上下文；边界组四例也共享上下文，并非每例一个全新会话。即使未提供判据，仍可能存在上下文迁移。正式回归应按 [评测流程](../evals/README.md) 逐例隔离、多轮运行。
2. 首次负触发试验误读取了标题和两段正文，已保留 [受污染记录](../evals/results/2026-09-19/negative-trigger-contaminated.md) 和 [执行元数据](../evals/results/2026-09-19/trial-boundaries-metadata.md)。该次不计入通过；另开新代理，仅提取元数据后重跑，结果见表。
3. 没有真实截图输入；旧线框案例只有文字与 ASCII 结构。没有验证图像识别、像素测量、实机读屏、SwiftUI 编译、真实 React 渲染或扩展安装。
4. 实施 fixture 明确缺少完整运行依赖。保存模拟用实际源码函数和替代状态 setter；不能证明 React 生命周期、焦点恢复、后端幂等性或真实屏幕阅读器播报。
5. GitHub Actions 仅自动执行结构、校验器测试与打包，不会自动调用模型做情境试用，也不代表真实用户的任务完成率。
6. 试用后仅整理链接/换行和澄清一处参考示例标题（将未知恢复能力明确标为待确认）；未把这一文字澄清当成额外行为测试通过。

留存回答只将机器本地链接转换为仓库相对链接，并规范化换行；保留原始建议内容。安装包不含这些评测上下文，避免使用时加载示范答案。
