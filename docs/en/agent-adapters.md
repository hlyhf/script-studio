# Multi-Platform Agent Adapter Guide (v2.2.0)‌‌‌‌‌‌‌

> English version of [`../agent-adapters.md`](../agent-adapters.md) (Chinese original).

This skill package is **pure Markdown + zero-dependency**, so the `skill/script-studio/`
directory can be loaded by any agent platform that supports "custom skills / knowledge
base / system prompts." The table below shows how to load it per platform.

## Adapter Matrix

| Agent platform | How to load | Example trigger phrases |
|---|---|---|
| **Hermes Agent** | Copy into the skills directory (`scripts/install.sh` / `install.bat`); auto skill routing | "Write an original screenplay" / "Audit this script" |
| **Claude Code** | Copy `skill/script-studio/` into the project's `.claude/skills/`; or reference the `SKILL.md` path from `CLAUDE.md` | Same as above |
| **Cursor** | Put the full `SKILL.md` text into the project's `.cursor/rules/script-studio.mdc` (or `.cursorrules`); reference `references/` via @ | Same as above |
| **DeepSeek (agent / harness)** | Paste `SKILL.md` as the agent's persona & reply logic; upload `references/*.md` as knowledge files | Same as above |
| **Doubao (agent)** | Create an agent → upload all md files under `skill/script-studio/` into its custom knowledge base; use `SKILL.md` as the persona prompt | Same as above |
| **Tencent Yuanbao (agent)** | Create an agent → upload knowledge files (`SKILL.md` + `references/*.md`); use `SKILL.md` as system instructions | Same as above |
| **WorkBuddy** | If it supports a custom skills directory: copy `skill/script-studio/` wholesale; otherwise upload as knowledge / prompt (same as DeepSeek) | Same as above |
| **OpenClaw** | Put `skill/script-studio/` into its skills/plugins directory (markdown skill convention); otherwise upload as a knowledge base | Same as above |
| **Custom RAG / other** | Chunk `references/*.md` into your vector store; use `SKILL.md` as the system prompt | Custom |

## Minimum Viable Set (any platform)

At minimum, 2 files are enough to run the core workflow:

1. `skill/script-studio/SKILL.md` — main flow (S-grade standards / four pre-episode questions / rhythm / red lines / attribution rules)
2. `skill/script-studio/references/01-format-rhythm.md` — format baseline

Optional add-ons (pick by the platform's knowledge-base capacity):

| File | Role | Suggestion |
|---|---|---|
| `references/02-original-writing.md` | Original-writing methodology | Required |
| `references/03–06` | Formulas / hooks / loop / rhythm | Recommended |
| `references/07-ai-drama-screenwriting-guide` / `08-close-reading-methodology` | Deep methodology (~250KB total) | Include fully if capacity allows |

## Load Verification (platform-agnostic)

After loading, ask the agent: *"Write episode 1 of a short drama; first give the four
pre-episode questions and the scene plan."*

A passing answer contains: **the four pre-episode questions + the single-episode emotion
+ a 5-scene plan + a first-100-words hook design**, and the output carries a
creation-tool declaration. Missing items mean the references were not fully loaded.

## Notes

- Each platform has different caps on knowledge-file size / count.
  `08-close-reading-methodology.md` is ~207KB; if it exceeds the cap, split it by
  chapter (3–4 segments) before uploading.
- Different platforms render Markdown comments (`<!-- -->`) differently; this does not
  affect body-text usage.
- The acceptance checklist inside the skill (SKILL.md Chapter 12 / Verification) is
  platform-agnostic text and can be copied verbatim into any platform's rules area.

<!-- © Lingxi Juchuang·Zhizi Editorial | Copyright holder: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
