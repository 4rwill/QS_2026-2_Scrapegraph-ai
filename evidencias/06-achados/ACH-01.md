# ACH-01 — Contradição no tratamento de ambiguidade

| Campo | Registro |
|---|---|
| Severidade | Alta |
| Requisitos | RQ-04; RQ-10; RQ-11 |
| Caso | CT-02 |
| Evidência primária | `../04-casos-teste/CT-02/saida.json` e `avaliacao.json` |
| Revisão humana | Pendente |

O resultado declarou que o critério de promoção não estava definido e explicou
que não havia produtos em promoção, mas simultaneamente listou Produto Aurora e
Produto Cedro. A contradição pode levar o usuário a decisões baseadas em uma
classificação inventada.

## Melhoria proposta

- validar coerência entre flags, explicação e listas antes de liberar a saída;
- quando `criterio_promocao_definido=false`, exigir lista vazia;
- adicionar teste de propriedade para estados mutuamente incompatíveis.

**Indicador:** zero contradições em três repetições do CT-02.

**Risco residual:** médio, pois novos schemas podem criar combinações não cobertas.
