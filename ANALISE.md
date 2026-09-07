# Análise — o que mudou no prompt de sistema do Fable 5.1

Data da análise: 2026-09-05 (feita para o curso `fable51-system`; copiada para cá como referência do projeto). Base: extração pública do runtime do Claude.ai para o Fable 5.1 (275.723 chars), prompt central oficial publicado pela Anthropic, Field Guide (comparação Fable 5 × 5.1 congelada em 2026-09-02).

## O que os arquivos são

| Arquivo (em `doc/`, local) | O que é | Confiabilidade |
|---|---|---|
| `Claude-Fable-5.1.md` | Runtime montado do Claude.ai (prompt central + memória + busca + artefatos + roteamento + schemas de ferramentas) | Extração **não oficial**. A Anthropic publica só o prompt central. |
| `Fable-5-1-System-Prompt-Field-Guide.pdf` (EN, Mark Kashef) e `…-PT-BR.pdf` | Comparação Fable 5 vs Fable 5.1 no mesmo commit, mesmo método de contagem | Reproduzível, mas compara dois dumps não autenticados |
| Benchmarks citados | Anthropic: ciência com agentes 24,7→52,6; negócios 17,1→31,4; código 70,5→73,4 | Oficial, escolhido pela Anthropic |

## Os três números

- Prompt: **17.501 → 40.046 palavras (2,3x)**.
- **+28 ferramentas** (18 mantidas, 46 total, zero removidas) — contagem do Field Guide.
- **75% do crescimento** = memória (+8.639 palavras) + schemas de ferramentas (+8.328).

No dump atual, `memory_filesystem` sozinho ocupa 836 das 2.196 linhas (38%). Ver [INDICE-DO-DUMP.md](INDICE-DO-DUMP.md).

## As 28 adições, por função

| Grupo | Qtd | Ferramentas | O que muda para o usuário |
|---|---|---|---|
| Memória | 6 | memory_list / read / write / append / str_replace / delete | Claude mantém arquivos (perfil, preferências, projetos, pessoas). Lê antes de escrever, edita pontualmente, apaga com checagem de versão. |
| Conversas passadas | 3 | conversation_search, recent_chats, read_conversation | Reabre a conversa original, não só o resumo. Dispara por pistas linguísticas ("meu projeto", "o que você sugeriu"). |
| Respostas visuais | 13 | chart, comparison_card, quiz, step_card, itinerary, translation, visualize:show_widget… | Resposta vira interface (gráfico, quiz, comparação) em vez de texto longo. |
| Plugins + skills | 4 | search_plugins, search_skills, suggest_plugin_install, suggest_skills | Claude procura uma capacidade faltante e sugere (máx. 1 cartão por conversa). |
| Pesquisa | 1 | suggest_research | Oferece pesquisa profunda multifonte e espera decisão. |
| Controle | 1 | end_conversation | Botão de parada estreito, só segurança, com confirmação. |

## Regras de comportamento que apareceram (além das ferramentas)

- **Memória com limite rígido:** nunca armazena saúde, religião, orientação, dados de pagamento etc. Fato guardado só entra na resposta se **mudar a substância**; "decorar" com memória é tratado como vigilância.
- **Rotina de visual em 4 passos:** precisa de visual? → MCP conectado serve? → pediu arquivo? → só então Visualizer inline.
- **Tom:** curto, sem "genuinamente/honestamente", formatação mínima, sem bullets ao recusar, sem formatação em conversa pessoal.
- **Skills obrigatórias antes de gerar arquivo:** ler o SKILL.md relevante é passo mandatório.
- **Anti-cópia:** máx. 1 citação curta (<15 palavras) por fonte em buscas.

## O paradoxo

Fable 5.1 **pontua mais alto** e o **sistema ao redor cresceu muito**. Nenhuma fonte prova que um causou o outro. O Field Guide pede: **julgue o modelo e o produto separadamente.**

## Onde o material é fraco

- Não diz nada sobre **preço** nem sobre **API** (isso vem da tabela oficial e do guia de custo; ver `fichas/03-custo-e-esforco.md`).
- Disponibilidade das 46 ferramentas **varia por superfície, plano e conta**.
- Dump congelado em 2026-09-02; o produto muda depois.

## Relação com a geração de set/2026

O guia oficial de prompting do Fable 5/5.1 diz que instruções escritas para modelos anteriores "são prescritivas demais e podem degradar a qualidade". O prompt de sistema capturado mostra o porquê: tom, formatação, honestidade e "pense passo a passo" **já estão no prompt de sistema ou são proibidos nele**. Repetir isso no seu prompt é ruído. O que sobra para você escrever é o que o modelo não tem: leitor, finalidade, restrição real, quando usar cada capacidade e o que conta como pronto. Tratamento completo dessa virada no Dia 4 do curso [Arquitetura de Intenção](https://inematds.github.io/arquitetura-de-intencao/dia-4.html).
