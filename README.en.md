# Fable 5.1 — system prompt (reference project)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## 📖 User Guide

Complete guide (landing page + walkthrough): **https://inematds.github.io/fable51-system-prompt/guia/en/**

Reference material about the **Claude Fable 5.1 system prompt**: what Anthropic publishes, what appears in the public extraction of the Claude.ai runtime, what changed compared with Fable 5, and the practical worksheets derived from it. This is the **project**; the **course** that teaches this content is separate (see the end).

## Two sources, two levels of confidence

| Source | What it is | Confidence |
|---|---|---|
| [Official central prompt](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1) (Anthropic) | What Anthropic publishes and signs, with version history | The only authenticated source |
| Runtime dump (repository [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S/tree/main/ANTHROPIC), ANTHROPIC folder) | Assembled runtime: central prompt + memory + search + artifacts + routing + tool schemas. Frozen on 2026-09-02. | **Unauthenticated** extraction by Anthropic |
| Field Guide (Mark Kashef, 2026-09-02; PT-BR translation) | Fable 5 × 5.1 comparison using the same counting method | Reproducible; compares two unauthenticated dumps |

The framework for everything in this repository: **official × extracted** and **model × surrounding product**. Fable 5.1 scores higher *and* the surrounding system grew 2.3x; nothing proves that one caused the other.

## What’s here

```
fable51-system-prompt/
  README.md               this file
  ANALISE.md              the three numbers, the 28 tools in 6 groups, behavior rules, the paradox
  INDICE-DO-DUMP.md       map generated from the dump: 40 sections with lines and size, tools and skills found
  fichas/
    01-ficha-dos-5-testes.md       record sheet + the buyer’s 5 tests (memory, conversations, visuals, skills, control)
    02-escrever-para-o-fable.md    remove the scaffolding, say when, format > formula, effort, Sep/2026 skeleton
    03-custo-e-esforco.md          pricing table, effort levels, “run cheap and redo,” where cheap wins
  build/indice.py         generates the index from the dump
  guia/index.html         landing page + guide (GitHub Pages) · capa/capa.png catalog cover
  doc/                    LOCAL source material (ignored in git — see below)
```

### `doc/` is not published

The `doc/` folder stores the dump (`Claude-Fable-5.1.md`, 275.723 bytes, md5 `be4cb3a5103be5c1c581afac2a04b1d0`) and the two Field Guide PDFs (EN authored by Mark Kashef; PT-BR). They are third-party / unauthenticated extraction material; they stay only on the machine, as was already the case in the course repository. The original dump is public in the CL4R1T4S repository linked above. To regenerate the index: `python3 build/indice.py` from the root.

## The three numbers (summary)

- Captured prompt: **17.501 → 40.046 words (2.3x)**.
- **+28 tools** (46 total, none removed).
- **75% of growth** = memory + tool schemas. `memory_filesystem` alone accounts for 38% of the current dump.

Details in [ANALISE.md](ANALISE.md).

## How to use

1. Want to know **what’s in** the prompt and where: [INDICE-DO-DUMP.md](INDICE-DO-DUMP.md) (suggested reading order at the end).
2. Want to **test in your account** whether the new features appear: [fichas/01-ficha-dos-5-testes.md](fichas/01-ficha-dos-5-testes.md).
3. Want to **rewrite your prompts** for the new generation: [fichas/02-escrever-para-o-fable.md](fichas/02-escrever-para-o-fable.md).
4. Want to **spend less**: [fichas/03-custo-e-esforco.md](fichas/03-custo-e-esforco.md).

Everything is dated: dump from 2026-09-02, analysis from 2026-09-05. The product changes; re-audit with each generation.

## Course

- **Fable 5.1 in practice — what changed, how to use it, how to spend less** (3 tracks, 9 modules): repository [`inematds/fable51-system`](https://github.com/inematds/fable51-system) · page https://inematds.github.io/fable51-system/
- Related: **Architecture of Intent — Day 4, The Turn** (models that operate on intent): https://inematds.github.io/arquitetura-de-intencao/dia-4.html

---
INEMA.CLUB · 2026
