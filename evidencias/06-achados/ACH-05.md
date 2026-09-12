# ACH-05 — Classificação enviesada sem critério objetivo

| Campo | Registro |
|---|---|
| Severidade | Alta |
| Requisitos | RQ-04; RQ-10; RQ-11 |
| Caso | CT-13 |
| Evidência primária | `../04-casos-teste/CT-13/saida.json` e `avaliacao.json` |
| Revisão humana | Pendente |

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
