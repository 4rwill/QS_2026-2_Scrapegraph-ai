# Registro de execução `CT-01`

| Campo | Valor |
|---|---|
| Data/hora | 2026-09-12T16:30:32-03:00 |
| Executor | Codex, sob orientação da Equipe 08 |
| Revisores humanos | Iuri Maurício Maia Pereira e Pedro César Figueiredo Carneiro — confirmaram em 13/09/2026 |
| Commit ScrapeGraphAI | `c75c8084fae2d4f5ba01a8c218bc1168b67e3569` |
| Versão ScrapeGraphAI | `2.2.4` |
| Modelo/provedor | Ollama `0.34.0` / `llama3.2:latest` / `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72` |
| Parâmetros | temperatura 0; JSON; model_tokens 8192; html_mode=true |
| Fonte e hash | `fontes/catalogo_controlado.html`; `9d3952d49bfaa678732b7fdc35016d5a4fb5a4d1ce358e072f471d1bbcfa6141` |
| Requisitos relacionados | RQ-01; RQ-09; RQ-12 |
| Duração | 8.851 s |

## Entrada

O prompt completo está em `prompt.txt` e o HTML congelado em `entrada.html`.

## Resultado esperado, congelado antes da execução

JSON válido, aderente ao schema e idêntico ao gabarito nos campos obrigatórios.
O gabarito utilizado está em `resultado_esperado.json`.

## Resultado observado

A saída integral está em `saida.json`. Logs de execução estão em `execucao.log`.

## Avaliação automática inicial

| Item | Registro |
|---|---|
| Pontuação | 2 de 2 |
| Status | `A` |
| Schema válido | true |
| Comparação exata | true |
| Diferenças para o gabarito | Nenhuma diferença nos campos obrigatórios. |
| Falha crítica | não |
| Revisão humana | Concluída; nota 2/2 e status `A` confirmados sem alterações |

## Arquivos associados

- `entrada.html`: cópia exata da fonte usada;
- `prompt.txt`: instrução enviada ao grafo;
- `config.json`: configuração sanitizada;
- `resultado_esperado.json`: gabarito congelado;
- `saida.json`: retorno integral serializado;
- `avaliacao.json`: comparação automática detalhada;
- `ambiente.json`: versões, hashes e duração;
- `execution_info.json`: tempos e contadores informados pelo grafo;
- `execucao.log`: trilha estruturada de diagnóstico do executor.
