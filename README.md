# Fable 5.1 — prompt de sistema (projeto de referência)

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/fable51-system-prompt/guia/**

Material de referência sobre o **prompt de sistema do Claude Fable 5.1**: o que a Anthropic publica, o que aparece na extração pública do runtime do Claude.ai, o que mudou em relação ao Fable 5, e as fichas práticas derivadas disso. É o **projeto**; o **curso** que ensina esse conteúdo vive separado (ver o fim).

## Duas fontes, dois pesos

| Fonte | O que é | Confiança |
|---|---|---|
| [Prompt central oficial](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1) (Anthropic) | O que a Anthropic publica e assina, com histórico de versões | Única fonte autenticada |
| Dump do runtime (repositório [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S/tree/main/ANTHROPIC), pasta ANTHROPIC) | Runtime montado: prompt central + memória + busca + artefatos + roteamento + schemas de ferramentas. Congelado em 2026-09-02. | Extração **não autenticada** pela Anthropic |
| Field Guide (Mark Kashef, 2026-09-02; tradução PT-BR) | Comparação Fable 5 × 5.1 no mesmo método de contagem | Reproduzível; compara dois dumps não autenticados |

Moldura para tudo neste repositório: **oficial × extraído** e **modelo × produto ao redor**. O Fable 5.1 pontua mais alto *e* o sistema ao redor cresceu 2,3x; nada prova que um causou o outro.

## O que tem aqui

```
fable51-system-prompt/
  README.md               este arquivo
  ANALISE.md              os três números, as 28 ferramentas em 6 grupos, regras de comportamento, o paradoxo
  INDICE-DO-DUMP.md       mapa gerado do dump: 40 seções com linhas e tamanho, ferramentas e skills encontradas
  fichas/
    01-ficha-dos-5-testes.md       ficha de registro + os 5 testes do comprador (memória, conversas, visuais, skills, controle)
    02-escrever-para-o-fable.md    tirar o andaime, dizer o quando, formato > fórmula, esforço, esqueleto set/2026
    03-custo-e-esforco.md          tabela de preços, níveis de esforço, "rode barato e refaça", onde o barato ganha
  build/indice.py         gera o índice a partir do dump
  guia/index.html         landing + guia (GitHub Pages) · capa/capa.png capa do catálogo
  doc/                    material-fonte LOCAL (ignorado no git — ver abaixo)
```

### `doc/` não é publicado

A pasta `doc/` guarda o dump (`Claude-Fable-5.1.md`, 275.723 bytes, md5 `be4cb3a5103be5c1c581afac2a04b1d0`) e os dois PDFs do Field Guide (EN de autoria de Mark Kashef; PT-BR). São material de terceiros / extração não autenticada; ficam só na máquina, como já era no repositório do curso. O dump original está público no repositório CL4R1T4S linkado acima. Para regenerar o índice: `python3 build/indice.py` na raiz.

## Os três números (resumo)

- Prompt capturado: **17.501 → 40.046 palavras (2,3x)**.
- **+28 ferramentas** (46 no total, nenhuma removida).
- **75% do crescimento** = memória + schemas de ferramentas. Só `memory_filesystem` ocupa 38% do dump atual.

Detalhe em [ANALISE.md](ANALISE.md).

## Como usar

1. Quer saber **o que existe** no prompt e onde: [INDICE-DO-DUMP.md](INDICE-DO-DUMP.md) (ordem de leitura sugerida no fim).
2. Quer **testar na sua conta** se as novidades aparecem: [fichas/01-ficha-dos-5-testes.md](fichas/01-ficha-dos-5-testes.md).
3. Quer **reescrever seus prompts** para a nova geração: [fichas/02-escrever-para-o-fable.md](fichas/02-escrever-para-o-fable.md).
4. Quer **gastar menos**: [fichas/03-custo-e-esforco.md](fichas/03-custo-e-esforco.md).

Tudo datado: dump de 2026-09-02, análise de 2026-09-05. O produto muda; reaudite a cada geração.

## Curso

- **Fable 5.1 na prática — o que mudou, como usar, como gastar menos** (3 trilhas, 9 módulos): repositório [`inematds/fable51-system`](https://github.com/inematds/fable51-system) · página https://inematds.github.io/fable51-system/
- Relacionado: **Arquitetura de Intenção — Dia 4, A Virada** (modelos que operam na intenção): https://inematds.github.io/arquitetura-de-intencao/dia-4.html

---
INEMA.CLUB · 2026
