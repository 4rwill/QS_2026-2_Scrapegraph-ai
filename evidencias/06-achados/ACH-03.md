# ACH-03 — Mensagem não acionável fora do domínio

| Campo | Registro |
|---|---|
| Severidade | Média |
| Requisitos | RQ-03; RQ-11 |
| Caso | CT-04 |
| Evidência primária | `../04-casos-teste/CT-04/saida.json` e `avaliacao.json` |
| Revisão humana | Pendente |

O fluxo evitou inventar previsão do tempo, porém respondeu apenas `NA`. A string
é válida no schema, mas não explica que a fonte contém somente um catálogo nem
orienta o usuário a fornecer uma fonte meteorológica.

## Melhoria proposta

- rejeitar respostas genéricas `NA`, `null` e equivalentes em campos de erro;
- gerar mensagem com causa, limitação e próximo passo;
- testar clareza por revisão humana e regras mínimas de conteúdo.

**Indicador:** mensagem identifica causa e ação recomendada em todas as
repetições do CT-04.

**Risco residual:** médio por depender de linguagem natural.
