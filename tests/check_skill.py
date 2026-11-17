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
    ],
}

for rel, snippets in required_snippets.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{rel} missing {snippet!r}")

link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for path in list((ROOT).glob("*.md")) + list((ROOT / "references").glob("*.md")) + list((ROOT / "examples").glob("*.md")):
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
if "2026-11-17 13:08" in readme or "确认重试" in readme:
    errors.append("approval record leaked into README")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(drafts)} drafts, links and required phrases")
