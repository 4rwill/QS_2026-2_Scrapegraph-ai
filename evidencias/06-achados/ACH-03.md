# ACH-03 — Mensagem não acionável fora do domínio

| Campo | Registro |
|---|---|
| Severidade | Média |
| Requisitos | RQ-03; RQ-11 |
| Caso | CT-04 |
| Evidência primária | `../04-casos-teste/CT-04/saida.json` e `avaliacao.json` |
| Revisão humana | Eduardo Ferreira Bomfim Filho — confirmada em 13/09/2026 |
| Responsável pela melhoria | Eduardo Curcino Monteiro Filho |
| Prioridade | Média |
| Dependências | Contrato padronizado de erro e regra mínima de conteúdo acionável |

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

**Critério de conclusão:** três execuções do CT-04 explicam a ausência de fonte
meteorológica e indicam uma ação possível ao usuário.
