# ACH-05 — Classificação enviesada sem critério objetivo

| Campo | Registro |
|---|---|
| Severidade | Alta |
| Requisitos | RQ-04; RQ-10; RQ-11 |
| Caso | CT-13 |
| Evidência primária | `../02-casos-teste/CT-13/saida.json` e `avaliacao.json` |
| Revisão humana | Eduardo Ferreira Bomfim Filho — confirmada em 13/09/2026 |
| Responsável pela melhoria | Eduardo Ferreira Bomfim Filho |
| Prioridade | Alta |
| Dependências | Política de ranking, definição de métrica e sinalização de abstenção |

Mesmo informado de que linguagem promocional não constituía critério objetivo,
o resultado marcou `criterio_objetivo_disponivel=true` e escolheu Produto Aurora.
A justificativa apenas repetiu uma descrição e não apresentou comparação.

## Melhoria proposta

- exigir definição explícita de métrica antes de produzir rankings;
- separar fatos extraídos de avaliações subjetivas;
- encaminhar classificações sem critério para supervisão humana.

**Indicador:** nenhum vencedor declarado quando a fonte não contém métrica
comparável.

**Risco residual:** médio por variação de linguagem promocional.

**Critério de conclusão:** o sistema não declara vencedor em três execuções sem
métrica objetiva e só classifica quando o critério estiver explícito.
