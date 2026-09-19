# 技能选择试验：无关代码修复

## 实际决定

不选择 `apple-design-coach`。请求是 Python CSV 导出函数的时区转换 bug 修复，明确不涉及界面、用户流程或设计评审；技能描述明确排除无关代码评审。

## 给用户的简短回复

请提供 CSV 导出函数的代码，以及能复现问题的输入、实际输出和预期输出（注明源时区和目标时区）。拿到后我会定位并修复时区转换 bug，再验证相关案例。

## 实际读取的元数据

来源：`SKILL.md (tested working copy)`

只将第二个 `---` 分隔符之前的 YAML `name` 和 `description` 字段及其续行传入模型上下文。未读取正文、引用文件、案例、报告或其他输出。第一次提取仅返回两个字段的首行；第二次提取包含 description 的全部续行。读取的字段原文如下：

```yaml
name: apple-design-coach
description: >-
  Improve an existing product's UI and UX, review screens or user flows, or plan
  a new feature using Apple design principles. Ground recommendations in project
  code, requirements, screenshots, or wireframes; prioritize fixes and explain
  how to validate them. Adapt to iOS, iPadOS, macOS, Windows, web, and browser
  extensions. Use for Apple-inspired design coaching, not unrelated code review
  or automatic HIG certification.
```
