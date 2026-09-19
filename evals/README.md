# 如何测试这个 skill

需要区分三类证据：包结构校验、模型情境试用、真实产品验证。前两项通过不代表已经用真人验证设计效果，也不代表 Apple 认证。

## 结构校验

仓库根目录执行：

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

校验 frontmatter、Codex 元数据、Markdown 相对链接、参考文件可达性，以及评测案例与 fixture 路径。离线执行，不验证外部网址内容或模型决策。

## 情境试用

[cases.json](cases.json) 保存输入、fixture 与行为判据。它是评测清单，不是自动调用模型的脚本。fixture 是有意保留缺陷的合成材料，不能当生产代码。

1. 为每个案例开启干净对话，提供待测 SKILL.md 路径、该案例 prompt 和所需 fixture。**不要向执行模型提供 criteria、示范答案或评测结论。**
2. `negative-trigger` 仅提供 skill 的 name/description 和用户请求，让模型判断是否应选择它；不要强制调用，否则无法测试触发边界。
3. `scoped-implementation` 先把 fixture 复制到临时工作区，只允许修改副本。其他案例只读。
4. 保存实际回答/改动、模型与环境、skill 版本、读取材料、运行过的工具和未验证项。不要手写“理想答案”冒充模型运行结果。
5. 再由评审对每条 criteria 给出 pass / fail / not-tested，并摘录支持判定的证据。不能仅检查是否出现原则名称或固定标题。
6. 关键失败（删必需功能、编造证据、错认平台、越权修改、把未运行测试说成通过）要修正后重跑相关案例。保留失败结果，不只保留最后通过的答案。

比较版本时固定输入与环境，尽量使用同一模型的独立新对话；单次通过仅是一次观察。没有运行的案例标明未执行，不汇总为通过。

## 当前结果

运行过程与限制记录在 [测试报告](../docs/TEST-REPORT.md)。真实项目仍需用自己的构建环境和设备完成验收。
