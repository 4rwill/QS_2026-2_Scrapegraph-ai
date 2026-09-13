# Evidências dos achados

Cada achado deverá possuir um arquivo `ACH-__.md` com:

- título e severidade: baixa, média, alta ou crítica;
- requisitos e casos relacionados;
- descrição objetiva;
- evidências primárias;
- impacto e pessoas afetadas;
- recomendação;
- ação, responsável, prioridade e dependências;
- indicador, risco residual e critério de conclusão;
- revisão e data.

Hipóteses de risco não devem ser apresentadas como achados confirmados antes da execução.

## Achados confirmados

| ID | Título | Severidade | Casos | Revisão humana |
|---|---|---|---|---|
| ACH-01 | Contradição no tratamento de ambiguidade | Alta | CT-02 | Confirmada em 13/09/2026 |
| ACH-02 | Ausência representada como texto `"null"` | Alta | CT-03; CT-11 | Confirmada em 13/09/2026 |
| ACH-03 | Mensagem não acionável fora do domínio | Média | CT-04 | Confirmada em 13/09/2026 |
| ACH-04 | Exposição contraditória de dado sensível | Crítica | CT-05 | Confirmada em 13/09/2026 |
| ACH-05 | Classificação enviesada sem critério objetivo | Alta | CT-13 | Confirmada em 13/09/2026 |
| ACH-06 | Aviso assíncrono após timeout | Média | CT-14 | Confirmada em 13/09/2026 |

Os seis achados foram identificados na revisão técnica por IA e confirmados pela
revisão humana informada pelo representante da equipe em 13/09/2026.
