# Custo e esforço — Fable 5.x

Origem: Trilha 3 do curso `fable51-system` (tabela oficial de preços + guia de otimização de custo da Anthropic; números de rodadas com Fable 5, salvo indicação). O prompt de sistema **não fala de preço**; esta ficha existe para preencher essa lacuna.

## Premissa honesta

Por token, o Fable 5.x é **mais caro**, não mais barato.

| Modelo | Entrada ($/1M) | Saída ($/1M) | Em relação ao Fable |
|---|---|---|---|
| Fable 5.1 / Fable 5 | 10,00 | 50,00 | referência |
| Opus 5 | 5,00 | 25,00 | metade |
| Sonnet 5 | 2,00 | 10,00 | um quinto |
| Haiku 4.5 | 1,00 | 5,00 | um décimo |

A economia só existe medida em **custo por tarefa concluída**: menos turnos, menos re-explicação, menos retrabalho, esforço calibrado. Um modelo barato que precisa de duas tentativas custou o dobro da tabela.

## Esforço (o primeiro botão antes de trocar de modelo)

| Nível | Quando faz sentido | Efeito típico |
|---|---|---|
| low | Subagentes, tarefas simples, alto volume, latência importa | Menos chamadas de ferramenta, menos preâmbulo, confirmações curtas |
| medium | Passo de economia onde a qualidade se mantém | Em pesquisa, igualou o padrão a 70–85% do custo |
| high (padrão) | Trabalho sensível a inteligência | Equilíbrio entre qualidade e eficiência |
| xhigh | Código e agentes de longo horizonte | Mais uso de ferramentas, mais profundidade |
| max | Quando acertar importa mais que custar | Só depois de medir que há ganho acima de xhigh |

Na Fable 5.1: padrão `high` no Claude Code e `medium` no chat; em `medium` rende o que a Fable 5 rendia em `high`. Re-teste a escala a cada geração — o mesmo nome de nível não significa a mesma quantidade de pensamento entre modelos.

## Rode barato, refaça só o que falhou

Vale quando existe um checador (teste, validador de formato):

| Política | Taxa de acerto | Custo por tarefa |
|---|---|---|
| Tudo no padrão | 91,7% | $1,39 |
| Tudo em low, refazer falhas no padrão | ~93% | ~$0,70 |
| Tudo em medium, refazer falhas no padrão | ~94% | ~$0,95 |

## Onde o mais barato ganha (e onde não)

| Situação | Medição publicada | Decisão |
|---|---|---|
| Código onde ambos acertam quase tudo | Opus 5: 91,7% · Fable 5: 91,3% · custo do Opus ≈ 60% | Desça para o Opus 5 |
| Perguntas de conhecimento em alto volume | Haiku 4.5: 63% de acerto a 1/10 do custo do Opus 5 (92%) | Haiku, se você consegue checar a saída e o erro é barato |
| Loop longo com agentes | Modelos pequenos perdem na cauda de tarefas difíceis | Não desça; a economia se perde em falhas |
| Pesquisa profunda | Fable 5 em low venceu Sonnet 5 por 10% menos | Fable em esforço baixo |

Compare modelos na **décima parte mais difícil** do seu trabalho: na tarefa típica todos parecem iguais e o barato parece melhor; a conta é decidida pelas tarefas que o barato erra (numa rodada de 20 problemas, 2 carregaram 43% do gasto).

## Alavancas do 5.1 na API (ordem: cache → esforço → orçamento → modelo, uma por vez, medindo)

- Leitura de cache a $0,25/MTok (a 5.1 baixou o preço de leitura de cache; é isso que faz trabalho agêntico longo custar até 45% menos).
- Troca de esforço por mensagem sem resetar o cache.
- Orçamento de tarefa (task budget): −18% de custo por −2,7 pts; −47% por −4,4 pts.
- Batch a 50%. Fallbacks do lado do servidor.
- Prova mínima: `cache_read_input_tokens` nos logs diferente de zero.
