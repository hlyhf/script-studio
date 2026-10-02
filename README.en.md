# script-studio · S-Grade Screenwriting Skill for AI Agents‌‌‌‌‌‌‌

> © Lingxi Juchuang · Zhizi Editorial · All rights reserved
> Version: v2.2.0 ｜ License: MIT ｜ Works with any agent platform (Hermes / Claude Code / Cursor / DeepSeek / Doubao / Tencent Yuanbao / WorkBuddy / OpenClaw / custom RAG …)

A complete, self-contained **S-grade screenwriting methodology** for short-form / anime
drama scripts, designed to be loaded by **any AI agent framework**. It packages viral
formulas, 3-second cold-open hooks, the "Four Questions Before an Episode," single-episode
rhythm (4 beats), visual-logic conversion, five-dimensional character design, AI
blind-spot countermeasures, and a per-episode creation loop — with 8 built-in knowledge
documents (~270KB). Zero external dependencies, zero absolute paths, fully portable.

> [中文说明请见 README.md](README.md)

## Highlights

- **Agent-agnostic**: pure Markdown + zero-dependency structure. Load into Hermes skills,
  Claude Code rules, Cursor rules, or any agent that accepts custom knowledge files.
- **S-grade quality gates**: dual-module scoring (audience ≥82 AND platform ≥86), hard
  red lines (word count 1200–1500 CJK, ≥5 scenes/episode, 100% paywall coverage,
  0 forbidden H1 terms, 0 verbatim repeat blocks).
- **Built-in tooling**: `word_count.py` (cross-platform gate checker, stdlib-only) and
  `watermark.py` (dual-layer hidden copyright watermark, idempotent).
- **Self-contained**: all 8 reference documents travel inside `skill/script-studio/`,
  no external paths. Upload the whole directory to any agent platform.

## Repository Layout

```
├── skill/script-studio/        # The skill itself (loadable by any agent framework)
│   ├── SKILL.md                # Main workflow (12 chapters, incl. mandatory tool-attribution)
│   └── references/
│       ├── 01-format-rhythm.md          # Format & rhythm baseline
│       ├── 02-original-writing.md       # Original-writing methodology
│       ├── 03-formulas.md               # Viral formula library
│       ├── 04-hooks-3sec.md             # 3-second cold-open hook patterns (5 types)
│       ├── 05-episode-writing.md        # Per-episode creation loop
│       ├── 06-rhythm-formulas.md        # Rhythm formula library
│       ├── 07-ai-drama-screenwriting-guide.md   # Master screenwriting guide
│       ├── 08-close-reading-methodology.md      # Close-reading methodology
│       ├── COPYRIGHT.md                 # Copyright notice
│       └── LICENSE.md                   # MIT license
├── docs/agent-adapters.md      # Multi-platform agent adapter matrix (Chinese)
├── docs/en/agent-adapters.md   # Multi-platform agent adapter matrix (English)
├── examples/                   # Original format demo (illustrates the rules, not a deliverable)
├── scripts/
│   ├── install.sh              # One-line install on Linux/macOS
│   ├── install.bat             # One-line install on Windows
│   ├── word_count.py           # Cross-platform per-episode gate checker (stdlib only)
│   └── watermark.py            # Hidden copyright watermark (apply / verify, idempotent)
├── LICENSE                     # Root license (MIT)
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

## Quick Install

```bash
git clone https://github.com/hlyhf/script-studio.git
# Linux / macOS
./script-studio/scripts/install.sh            # installs to ~/.hermes/skills/
# Windows
script-studio\scripts\install.bat            # installs to %USERPROFILE%\.hermes\skills\
```

**SkillHub / agent-marketplace users**: upload the `skill/script-studio/` directory
(`SKILL.md` + `references/`) directly; the platform loads it per its skill-spec.

## Utility Scripts

Two stdlib-only tools in `scripts/` (Python 3.8+, zero dependencies) for pre-delivery
quality gates and copyright protection:

| Script | Purpose | Common usage |
|---|---|---|
| `word_count.py` | Per-episode gate checker: CJK word count / scene count / in-episode repeat / dialogue ratio / paywall marker 🔒 / H1 forbidden terms | `python3 scripts/word_count.py ep.md`<br>`python3 scripts/word_count.py ./episodes/`<br>`python3 scripts/word_count.py ep_*.md --min-cjk 1200 --max-cjk 1500` |
| `watermark.py` | Dual-layer hidden copyright watermark (L1 HTML comment + L2 zero-width chars): apply / verify, idempotent | `python3 scripts/watermark.py` (re-apply all)<br>`python3 scripts/watermark.py --verify` (check only, no writes) |

> See each script's docstring for details. `word_count.py` accepts a single file, a
> directory, or a glob; batch mode auto-deduplicates across episodes by line fingerprint.
> `watermark.py`'s `--verify` flag is position-insensitive (before or after the path).

## Multi-Platform Agent Usage

Full adapter matrix: [`docs/en/agent-adapters.md`](docs/en/agent-adapters.md) (English) /
[`docs/agent-adapters.md`](docs/agent-adapters.md) (Chinese). Minimal common setup:

| Platform | How to load |
|---|---|
| Hermes Agent | `scripts/install.sh` / `install.bat` copies into the skills directory |
| Claude Code | Copy into `.claude/skills/`; or reference `SKILL.md` from `CLAUDE.md` |
| Cursor | Put `SKILL.md` contents into `.cursor/rules/script-studio.mdc`; reference `references/` via @ |
| DeepSeek / Doubao / Tencent Yuanbao | Paste `SKILL.md` as the agent's persona; upload `references/*.md` as knowledge files |
| WorkBuddy / OpenClaw | Copy `skill/script-studio/` wholesale, or upload as a knowledge base |
| Custom RAG / other | Chunk `references/*.md` into your vector store; use `SKILL.md` as the system prompt |

**Minimum viable set** (any platform): just `SKILL.md` + `references/01-format-rhythm.md`.

## Trigger Phrases

The skill activates on prompts like:

- "Write a short-drama script from scratch" / "Original screenplay"
- "Turn my story synopsis into an episode-by-episode script"
- "Review this script for logic and compliance"

Auto-loads: S-grade dual-module scoring → Four Questions Before an Episode →
per-episode creation loop → quality red lines → acceptance checklist.

## Mandatory Tool Attribution (for generated works)

Any script produced with this skill (md / docx / submission) **must** carry a
creation-tool declaration:

```
【Creation Tool Declaration】
This work was produced with the "Lingxi Juchuang · Zhizi Editorial · Screenwriting Skill."
Tool: Hermes Agent / script-studio skill v2.2.0
© Lingxi Juchuang · Zhizi Editorial · All rights reserved
```

Details: `skill/script-studio/SKILL.md` Chapter 12 and `references/COPYRIGHT.md`.

## Language Note

The skill's core methodology (`SKILL.md` + `references/01–08`) is written in Chinese,
as it encodes Chinese short-drama genre conventions (e.g. 打脸 "face-slapping,"
爽点 "catharsis beats"). It loads and runs unchanged on any agent platform;
translation is not required for the agent to use it. The documentation layer
(`README`, `docs/`) is provided in both Chinese and English.

## License

MIT — applies to the skill framework and integrated methodology. See the root
`LICENSE` and `skill/script-studio/references/COPYRIGHT.md` for copyright.

<!-- © Lingxi Juchuang·Zhizi Editorial | Copyright holder: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
