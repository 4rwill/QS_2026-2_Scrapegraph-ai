# ACH-02 — Ausência representada como texto `"null"`

| Campo | Registro |
|---|---|
| Severidade | Alta |
| Requisitos | RQ-04; RQ-09; RQ-10 |
| Casos | CT-03; CT-11 |
| Evidência primária | `../04-casos-teste/CT-03/saida.json`; `../04-casos-teste/CT-11/saida.json` |
| Revisão humana | Pendente |

O modelo usou a string `"null"` onde o schema admitia valor JSON nulo. Em CT-03
também marcou que a ausência não havia sido sinalizada; em CT-11 marcou
incorretamente que a fonte de Cedro não estava ausente. Consumidores podem tratar
`"null"` como um valor real e perder a indicação de falta de evidência.

## Melhoria proposta

- normalizar marcadores textuais de ausência para nulo verdadeiro;
- aplicar validação semântica posterior ao Pydantic;
- exigir consistência entre valor nulo e flag de ausência.

**Indicador:** 100% dos campos ausentes serializados como `null`, com flags
coerentes, em CT-03 e CT-11.

**Risco residual:** baixo após validação determinística.
