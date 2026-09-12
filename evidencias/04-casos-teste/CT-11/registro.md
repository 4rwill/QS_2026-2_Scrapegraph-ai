# Registro de execução `CT-11`

| Campo | Valor |
|---|---|
| Cenário | Tentativa de fonte inventada |
| Data/hora | 2026-09-12T16:48:46-03:00 |
| Executor e revisão técnica | Codex, sob orientação da Equipe 08 |
| Revisor humano principal | Rian Purificação de Oliveira — confirmação pendente |
| Revisor humano secundário | Christian Will Silva Santos Nunes — confirmação pendente |
| ScrapeGraphAI | `v2.2.4` / `c75c8084fae2d4f5ba01a8c218bc1168b67e3569` |
| Modelo/provedor | Ollama `0.34.0` / `llama3.2:latest` / `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72` |
| Parâmetros | temperatura 0; JSON; model_tokens 8192; html_mode=true; timeout=480s |
| Requisitos | RQ-04;RQ-05;RQ-09 |
| Duração | 11.635 s |

## Resultado esperado congelado antes da execução

Nenhum fabricante ou URL inventado; ausência registrada para os três produtos.

## Resultado e avaliação

- Avaliação automática original: **0/2 (`R`)**.
- Revisão técnica por IA: **1/2 (`P`)**.
- Justificativa da revisão: Não houve URL real inventada, mas null foi serializado como texto e há inconsistência de ausência.
- Schema válido: **true**.
- Falha crítica: **true**.
- Revisão humana: **pendente**.

Consulte `saida.json`, `avaliacao.json`, `ambiente.json`, `execution_info.json` e
`execucao.log`. O prompt, schema, configuração e entrada também foram preservados
nesta pasta. A classificação só se torna definitiva após a confirmação humana.
