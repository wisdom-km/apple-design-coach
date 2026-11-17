#!/usr/bin/env python3
"""Check skill docs, local links, and offline draft HTML.

This does not run Grok CLI and does not test a physical device.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required_snippets = {
    "SKILL.md": [
        "不要默认 iPhone",
        "不要默认 macOS",
        "android-phone",
        "responsive-web",
        "browser-extension",
        "windows-native",
        "macos-native",
        "linux-gnome",
        "未发现可加载的平台 Skill",
        "不是原生实现",
        "不授权去实现整个应用",
        "线框意图优先",
        "八原则必须保留",
        "平台规范清单不能代替原则判断",
        "平台清单替换哲学",
        "未选方向就出完整稿",
        "只评不改",
        "direction-choice.md",
        "design-memory.md",
        "draft-critique.md",
        "已画 / 不适用",
        "只讨论方向时不写这一段",
        "不在这里另写一套",
    ],
    "docs/approval-2026-11-17-cross-platform.md": [
        "2026-11-17 13:08 Asia/Shanghai",
        "2026-11-17 13:15 Asia/Shanghai",
        "2026-11-17 13:52 Asia/Shanghai",
        "然后对它采用平台规范是没问题的，然后就是说苹果的那个设计的哲学是要保留的。",
        "按照你的建议做就行",
        "我建议先做前三项",
        "2026-11-17 14:13 Asia/Shanghai",
        "OK，那就按照你的建议，加入这两个精简版本吧：不增加启动器脚本、服务、安装步骤和框架依赖，但该有的都要有。No job，apple design coach 里面，然后并且进行测试测试，呃，我同意之后我觉得合格了之后你再合入到那个主 分支",
        "这句回复所针对的建议",
        "解释后的批准范围",
        "本句没有给出合入许可",
    ],
    "references/platform-router.md": [
        "只做安卓",
        "安装在 Windows",
        "浏览器网站",
        "ask_again: no",
        "platform-android",
        "material-3",
        "不要默认 iPhone",
        "libadwaita",
        "visual_record:",
    ],
    "references/direction-choice.md": [
        "这是文字说明，不是已渲染的预览",
        "coach-because-user-delegated",
        "只讨论方向时，不写实现交接",
    ],
    "references/design-memory.md": [
        "visual_record: DESIGN.md",
        "未写入项目",
        "confirmed_by",
    ],
    "references/draft-critique.md": [
        "未对照成图，以下是对结构的检查",
        "原有的功能、文案和链接都留着",
        "不能只写在句子里",
        "在 HTML 里放大字号不是 iOS 动态字体",
    ],
    "examples/scenario-first3.md": [
        "不是 Grok CLI",
        "receipt-photo",
        "实际做过的",
        "没做过的",
    ],
    "examples/project-memory/DESIGN.md": [
        "receipt-photo: optional-never-required",
        "系统密表",
        "confirmed_by: user",
    ],
    "examples/scenario-states-handoff.md": [
        "NOT VERIFIED",
        "file://",
        "不是 Grok CLI",
        "receipt-photo: optional-never-required",
    ],
    "examples/project-memory/handoff.md": [
        "receipt-photo: optional-never-required",
        "DESIGN.md",
        "指定 Kotlin、Flutter、React",
        "只讨论方向时不写它",
    ],
    "examples/scenario-router.md": [
        "只做安卓",
        "安装在 Windows",
        "responsive-web",
        "browser-extension",
        "macos-native",
        "ask_again: no",
        "不要写产品代码",
        "不是 Grok CLI",
    ],
    "references/visual-drafts.md": [
        "GenerateImage",
        "结构线框",
        "不是真机测试",
    ],
    "references/source-provenance.md": [
        "https://developer.apple.com/videos/play/wwdc2026/250/",
        "https://www.w3.org/TR/WCAG22/",
        "https://m3.material.io/components/navigation-bar/guidelines",
        "https://fluent2.microsoft.design/design-principles",
        "未读正文",
        "https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md",
        "https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md",
        "https://github.com/pbakaus/impeccable",
    ],
}

for rel, snippets in required_snippets.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{rel} missing {snippet!r}")

link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for path in list(ROOT.glob("*.md")) + list((ROOT / "references").glob("*.md")) + list((ROOT / "examples").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)} broken link -> {target}")

drafts = list((ROOT / "examples" / "drafts").glob("*.html"))
if len(drafts) < 7:
    errors.append(f"expected at least 7 HTML drafts, found {len(drafts)}")

for path in drafts:
    text = path.read_text(encoding="utf-8")
    if "示例数据" not in text and "示例决定" not in text:
        errors.append(f"{path.name} does not label example data or decisions")
    if "真机" not in text:
        errors.append(f"{path.name} does not say it is not a device test")
    for bad in ("http://", "https://", "<script", "fonts.googleapis", "cdn."):
        if bad in text:
            errors.append(f"{path.name} contains external or script marker {bad}")

license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
if "MIT License" not in license_text or "Copyright (c) 2026 wisdom-km" not in license_text:
    errors.append("LICENSE no longer contains the original MIT grant")

notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
if "not affiliated with" not in notice or "WCAG 2.2" not in notice:
    errors.append("NOTICE dropped the Apple disclaimer or the WCAG citation")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if (
    "2026-11-17 13:08" in readme
    or "确认重试" in readme
    or "按照你的建议做就行" in readme
    or "我建议先做前三项" in readme
    or "2026-11-17 14:13" in readme
    or "加入这两个精简版本" in readme
    or "No job" in readme
):
    errors.append("approval record leaked into README")

after = (ROOT / "examples" / "drafts" / "android-ledger-after.html").read_text(encoding="utf-8")
before = (ROOT / "examples" / "drafts" / "android-ledger-before.html").read_text(encoding="utf-8")
directions = (ROOT / "examples" / "drafts" / "android-ledger-directions.html").read_text(encoding="utf-8")
kept = "2026年11月家庭水电燃气合缴账单（含滞纳金说明）"
for label, text in (("before", before), ("after", after)):
    if kept not in text or "保存" not in text or "删除" not in text:
        errors.append(f"{label} dropped the sample bill, save, or delete")
if "设置" not in after:
    errors.append("after draft dropped settings")
for name in ("账本纸", "系统密表", "一处重点"):
    if name not in directions:
        errors.append(f"direction thumbnails missing {name}")
if "权限页不适用" not in after:
    errors.append("simple ledger still lacks an explicit not-applicable permission note")
if "必须实现 空 / 加载 / 错误 / 权限拒绝" in (ROOT / "SKILL.md").read_text(encoding="utf-8"):
    errors.append("handoff template still forces every state including permission denial")

listing = (ROOT / "examples" / "drafts" / "android-ledger-list.html").read_text(encoding="utf-8")
scaled = (ROOT / "examples" / "drafts" / "android-ledger-list-scaled.html").read_text(encoding="utf-8")
denied = (ROOT / "examples" / "drafts" / "android-ledger-photo-denied.html").read_text(encoding="utf-8")
handoff = (ROOT / "examples" / "project-memory" / "handoff.md").read_text(encoding="utf-8")
for phrase in ("空白", "加载", "失败", "重试", "尚未核对", "不适用", kept):
    if phrase not in listing:
        errors.append(f"list draft missing {phrase}")
if "权限页" not in listing:
    errors.append("list draft does not explain why the permission screen is absent")
for phrase in ("150%", "不是动态字体", "重试", kept):
    if phrase not in scaled:
        errors.append(f"scaled draft missing {phrase}")
for phrase in ("保存这笔，不附照片", "再试一次", "不是安卓真机权限", "receipt-photo: optional-never-required"):
    if phrase not in denied:
        errors.append(f"permission draft missing {phrase}")
if re.search(r"#[0-9A-Fa-f]{3,8}", handoff):
    errors.append("handoff copied color values instead of pointing at DESIGN.md")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(drafts)} drafts, links and required phrases")
