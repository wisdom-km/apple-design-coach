# apple-design-coach

An Apple-inspired **cross-surface software design coach** skill for AI coding agents (Cursor / Claude / Codex-compatible `SKILL.md`).

Not a Human Interface Guidelines encyclopedia. Not a compliance auditor. Not a “paint it like iOS” skin kit.

## What it does

Given a **product surface** (iOS, iPadOS, macOS, Windows, browser extension, …), **requirements**, and optional **screenshots** / **structured wireframes**, it coaches:

1. Design contract (Purpose, non-goals, tradeoffs)
2. Feature placement / information architecture
3. UI structure (wireframe-level)
4. States & permissions
5. Reference advice
6. Risk & platform-translation notes

**Shared philosophy kernel (A):** [Apple HIG Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) — Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight ([WWDC26 Session 250](https://developer.apple.com/videos/play/wwdc2026/250/)).

**Surface adaptation (B):** same intent, host-platform conventions. On Windows / extensions: **borrow the spirit only — never claim Apple HIG compliance.**

## Install

Copy this folder into your agent skills directory, or point your agent at `SKILL.md`.

Typical layout:

```text
apple-design-coach/
  SKILL.md
  references/
    eight-principles.md
    surfaces.md
    placement-playbook.md
    input-visuals.md
  examples/
    aa-split-ios-coaching.md
```

## Inputs

| Input | Role |
|-------|------|
| Surface declaration | Required (or ask once) |
| Requirements | Required — text-only is fine |
| Screenshot | Optional — reality |
| Structured wireframe / ASCII frames | Optional — intent |

If **both** screenshot and wireframe are present: align **wireframe intent first**, then use the screenshot as a **reality check**.

## Example

See [`examples/aa-split-ios-coaching.md`](examples/aa-split-ios-coaching.md) — redesign of a cluttered “split the bill” iOS tool into a Purpose-first single-screen coach output.

## License

MIT for original skill text and structure in this repository.

Apple Human Interface Guidelines, WWDC content, and trademarks are © Apple Inc. This project links to official sources and does **not** redistribute Apple’s HIG full text. It is unofficial and not affiliated with Apple.

## Credits

Philosophy grounded in Apple’s public Design principles / WWDC design sessions. Open-source workflow inspiration (structure only): projects such as [HIG-Driven](https://github.com/dzakwanfadhlullah/HIG-Driven).
