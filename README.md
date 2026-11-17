# apple-design-coach

An Apple-inspired **cross-surface software design coach** skill for AI coding agents (Cursor / Claude / Codex-compatible `SKILL.md`).

Not a Human Interface Guidelines encyclopedia. Not a compliance auditor. Not a “paint it like iOS” skin kit.

## What it does

Given a **product surface** and **requirements**, plus optional **screenshots** / **structured wireframes**, it coaches. Surfaces are specific containers, not vague device words:

- Phone: iOS or Android. “Mobile” does not default to iPhone. iPad is separate.
- Responsive website, including its narrow mobile-web layout. This is not an installed desktop app and not a browser extension.
- Browser extension popup, side panel, and options page.
- Installed desktop app: Windows, macOS, or Linux (GNOME or KDE). Windows is not a stand-in for every desktop. macOS is not the default desktop.

The skill asks only for a choice that is still missing. A stated platform is used as-is. When the user asks to see the interface, a missing visual direction is chosen before the full draft. A later screen reuses the project’s existing design notes. After a viewable draft, a short critique is applied to the draft itself. A wireframe is not renamed into a mockup.

1. Design contract (Purpose, non-goals, tradeoffs)
2. Feature placement / information architecture
3. UI structure (wireframe-level)
4. States & permissions
5. Reference advice
6. Risk & platform-translation notes

**Shared philosophy kernel (A):** [Apple HIG Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) — Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight ([WWDC26 Session 250](https://developer.apple.com/videos/play/wwdc2026/250/)).

**Surface adaptation (B):** navigation, controls, placement, keyboard or touch, and window chrome follow the target platform. Android uses Material, the web uses ordinary page structure and WCAG, Windows uses Fluent / WinUI, and Linux uses the chosen desktop guidelines. The eight principles still decide why a control is there. That is not a claim of Apple HIG compliance, and a platform checklist does not replace the principles.

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
    reference-library.md
    platform-router.md
    aesthetics.md
    visual-drafts.md
    direction-choice.md
    design-memory.md
    draft-critique.md
    source-provenance.md
  examples/
    aa-split-ios-coaching.md
    context-android-only.md
    scenario-router.md
    drafts/
```

Copying this folder is enough. Sibling skills such as `platform-android` are optional and are used only when the host already has them.

## Inputs

| Input | Role |
|-------|------|
| Surface declaration | Required (or ask once) |
| Requirements | Required — text-only is fine |
| Screenshot | Optional — reality |
| Structured wireframe / ASCII frames | Optional — intent |

If **both** screenshot and wireframe are present: align **wireframe intent first**, then use the screenshot as a **reality check**.

## References & taste vocabulary

`references/reference-library.md` lists curated, link-checked sources for shipped-product UI references (Mobbin, Page Flows, Refero, Component Gallery, Laws of UX, Vercel Web Interface Guidelines, …) and a rule for writing references: **name + technique + why (principle / UX law) + how to borrow**, never vague words like "make it premium". Curation adapted from Eian (@EianLu)'s X article on 100 design-taste websites.

`references/eight-principles.md` maps Laws of UX to the eight principles, as rationale (not a checklist).

## Example

See [`examples/aa-split-ios-coaching.md`](examples/aa-split-ios-coaching.md) — redesign of a cluttered “split the bill” iOS tool into a Purpose-first single-screen coach output.

[`examples/scenario-router.md`](examples/scenario-router.md) records how platform questions should resolve. [`examples/scenario-first3.md`](examples/scenario-first3.md) separates the expected direction, memory, and critique behavior from what this repository actually exercised. [`examples/scenario-states-handoff.md`](examples/scenario-states-handoff.md) does the same for task-sized states and the optional coding handoff. [`examples/project-memory/`](examples/project-memory/) is a sample project design note, a platform context that only points at it, and a handoff that cites that note. [`examples/drafts/`](examples/drafts/) holds offline HTML drafts for an iOS phone, an Android phone, a responsive website, an extension popup, and installed Windows, macOS, and GNOME windows, plus Android direction thumbnails, a before/after ledger screen, a bill list in several states, a larger-type check, an optional photo-denial screen, and a compact Android list that compares a rough multi-frame sheet with one finished frame. [`examples/scenario-craft.md`](examples/scenario-craft.md) says which of that comparison was actually opened in a browser. [`examples/scenario-layout.md`](examples/scenario-layout.md) separates a caption-style rule that erases an app margin from an intentional icon slot and a full-bleed divider. Those files are example designs with invented sample data. [`examples/drafts/screenshots/`](examples/drafts/screenshots/) shows those HTML files opened in a desktop browser on 2026-11-17. A browser screenshot is not a test on a phone or on Windows, macOS, or Linux. `tests/check_skill.py` is a developer check for this repository. Using the skill does not require that script or a runtime.

Source URLs, licenses, and what was actually read are in [`references/source-provenance.md`](references/source-provenance.md).

## License

MIT for original skill text and structure in this repository.

Apple Human Interface Guidelines, WWDC content, and trademarks are © Apple Inc. This project links to official sources and does **not** redistribute Apple’s HIG full text. It is unofficial and not affiliated with Apple.

## Credits

Philosophy grounded in Apple’s public Design principles / WWDC design sessions. Open-source workflow inspiration (structure only): projects such as [HIG-Driven](https://github.com/dzakwanfadhlullah/HIG-Driven).
