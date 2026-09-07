# Índice do dump — runtime do Claude.ai para o Fable 5.1

Arquivo: `doc/Claude-Fable-5.1.md` (local, não publicado) · 275,723 bytes · 2,196 linhas · 40.046 palavras (contagem por espaço, bate com o Field Guide) · md5 `be4cb3a5103be5c1c581afac2a04b1d0`

Fonte: extração pública não autenticada (repositório CL4R1T4S, pasta ANTHROPIC), congelada em 2026-09-02. A Anthropic publica apenas o **prompt central**; tudo abaixo de `memory_filesystem` em diante é a camada de produto que aparece só no dump.

Este índice é gerado por script (`build/indice.py`) e traz só metadados: nome da seção, linhas e tamanho. Não reproduz o conteúdo.

## Seções de nível superior (tags no início de linha)

| # | Seção | Linhas | Tamanho | Grupo |
|---|---|---|---|---|
| 1 | `product_information` | 2–24 | 23 linhas | prompt central |
| 2 | `refusal_handling` | 25–79 | 55 linhas | prompt central |
| 3 | `legal_and_financial_advice` | 80–82 | 3 linhas | prompt central |
| 4 | `tone_and_formatting` | 83–115 | 33 linhas | prompt central |
| 5 | `reply_after_tool_calls` | 116–118 | 3 linhas | prompt central |
| 6 | `user_wellbeing` | 119–151 | 33 linhas | prompt central |
| 7 | `anthropic_reminders` | 152–158 | 7 linhas | prompt central |
| 8 | `evenhandedness` | 159–171 | 13 linhas | prompt central |
| 9 | `responding_to_mistakes_and_criticism` | 172–176 | 5 linhas | prompt central |
| 10 | `knowledge_cutoff` | 177–184 | 8 linhas | prompt central |
| 11 | `tone_preference` | 186–188 | 3 linhas | prompt central |
| 12 | `memory_filesystem` | 189–1024 | 836 linhas | memória |
| 13 | `end_conversation_tool_info` | 1027–1052 | 26 linhas | controle |
| 14 | `persistent_storage_for_artifacts` | 1054–1126 | 73 linhas | artefatos |
| 15 | `mcp_app_suggestions` | 1127–1174 | 48 linhas | plugins/conectores |
| 16 | `suggest_catalog_plugins_and_skills` | 1176–1193 | 18 linhas | plugins/skills |
| 17 | `past_chats_tools` | 1195–1224 | 30 linhas | conversas passadas |
| 18 | `computer_use` | 1226–1367 | 142 linhas | arquivos/computador |
| 19 | `request_evaluation_checklist` | 1368–1392 | 25 linhas | artefatos/visuais |
| 20 | `when_to_use_visualizer_for_inline_visuals` | 1394–1419 | 26 linhas | respostas visuais |
| 21 | `visualizer_examples` | 1421–1439 | 19 linhas | respostas visuais |
| 22 | `search_instructions` | 1441–1678 | 238 linhas | busca |
| 23 | `using_image_search_tool` | 1679–1745 | 67 linhas | busca |
| 24 | `functions` | 1761–1808 | 48 linhas | schemas de ferramentas |
| 25 | `profile` | 1817–1819 | 3 linhas | memória (estado) |
| 26 | `memory_listing` | 1820–1823 | 4 linhas | memória (estado) |
| 27 | `anthropic_api_in_artifacts` | 1824–2024 | 201 linhas | artefatos |
| 28 | `skill` | 2044–2054 | 11 linhas | skills |
| 29 | `skill` | 2056–2066 | 11 linhas | skills |
| 30 | `skill` | 2068–2078 | 11 linhas | skills |
| 31 | `skill` | 2080–2090 | 11 linhas | skills |
| 32 | `skill` | 2092–2102 | 11 linhas | skills |
| 33 | `skill` | 2104–2114 | 11 linhas | skills |
| 34 | `skill` | 2116–2126 | 11 linhas | skills |
| 35 | `skill` | 2128–2138 | 11 linhas | skills |
| 36 | `skill` | 2140–2150 | 11 linhas | skills |
| 37 | `skill` | 2152–2162 | 11 linhas | skills |
| 38 | `skill` | 2164–2174 | 11 linhas | skills |
| 39 | `network_configuration` | 2178–2184 | 7 linhas | ambiente |
| 40 | `filesystem_configuration` | 2186–2195 | 10 linhas | ambiente |

## Definições de ferramenta encontradas por `"name":` (31)

Contagem do script; o Field Guide chega a 46 porque também conta widgets visuais e ferramentas descritas fora de schema JSON.

`bash_tool`, `conversation_search`, `create_file`, `end_conversation`, `fetch_sports_data`, `image_search`, `memory_append`, `memory_delete`, `memory_list`, `memory_read`, `memory_str_replace`, `memory_write`, `places_search`, `present_files`, `read_conversation`, `recent_chats`, `recommend_claude_apps`, `search_mcp_registry`, `search_plugins`, `search_skills`, `str_replace`, `suggest_connectors`, `suggest_plugin_install`, `suggest_research`, `suggest_skills`, `view`, `visualize:read_me`, `visualize:show_widget`, `weather_fetch`, `web_fetch`, `web_search`

## Skills listadas no bloco `<skill>` (11)

`docx`, `pdf`, `pptx`, `xlsx`, `product-self-knowledge`, `frontend-design`, `file-reading`, `pdf-reading`, `import-memory`, `morning`, `skill-creator`

## Ordem de leitura sugerida

1. `tone_and_formatting` + `reply_after_tool_calls` (83–118): as regras de tom que explicam por que micro-instruções de estilo hoje atrapalham.
2. `memory_filesystem` (189–1024): 38% do arquivo. Limites do que nunca é armazenado, quando a memória entra na resposta, frases proibidas.
3. `past_chats_tools` (1195–1224): pistas linguísticas que disparam busca em conversas antigas.
4. `request_evaluation_checklist` + `when_to_use_visualizer_for_inline_visuals` (1368–1419): a rotina de 4 passos antes de um visual.
5. `search_instructions` (1441–1678): quando buscar, anti-cópia (1 citação curta por fonte).
6. `functions` (1761–1808) e os blocos `<skill>` (2044–2174): o que existe como ferramenta e o que é lido antes de gerar arquivo.
