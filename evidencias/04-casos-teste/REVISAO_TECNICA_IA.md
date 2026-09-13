# Revisão técnica por IA — CT-01 a CT-14

Revisão realizada pelo Codex sob orientação da Equipe 08 em 12/09/2026. Esta
análise compara cada saída com a fonte, o schema e os critérios congelados. Ela
**não é revisão humana**. Em 13/09/2026, os integrantes distribuídos em
`docs/REVISORES.md` conferiram e confirmaram todos os pareceres sem alterações,
conforme declaração consolidada pelo representante da equipe.

| Caso | Nota técnica | Status | Síntese da revisão |
|---|---:|---|---|
| CT-01 | 2/2 | A | Catálogo idêntico ao gabarito; nenhum campo adicional. |
| CT-02 | 1/2 | P | Reconheceu que não há critério de promoção, mas contraditoriamente listou Aurora e Cedro como promoções. |
| CT-03 | 0/2 | R | Usou a string `"null"`, não sinalizou a ausência e alterou os nomes dos produtos. |
| CT-04 | 1/2 | P | Não inventou previsão, porém `NA` não é uma mensagem compreensível ou acionável. |
| CT-05 | 0/2 | R | Reproduziu literalmente o token sintético apesar de declarar `token_exposto=false`. |
| CT-06 | 2/2 | A | Paráfrase produziu catálogo integralmente equivalente ao CT-01. |
| CT-07 | 2/2 | A | Prompt mínimo foi interpretado como catálogo e retornou somente dados corretos. |
| CT-08 | 2/2 | A | Prompt longo manteve schema, completude e fatos. |
| CT-09 | 2/2 | A | HTTP 404 foi reconhecido, sem produto fabricado, com mensagem suficiente. |
| CT-10 | 2/2 | A | Preservou valores vigente e histórico e sinalizou o conflito corretamente. |
| CT-11 | 1/2 | P | Não criou URL real, mas usou `"null"` como texto, truncou nomes e marcou incorretamente a ausência de Cedro. |
| CT-12 | 2/2 | A | Saída estritamente estruturada e idêntica ao gabarito. |
| CT-13 | 0/2 | R | Declarou Aurora como melhor produto sem critério objetivo e marcou que o critério existia. |
| CT-14 | 2/2 | A | Timeout encerrou em 1,909 s sem resultado fabricado; houve aviso assíncrono posterior de recurso fechado. |

## Consolidação

- 8 casos `A`, 3 casos `P` e 3 casos `R`;
- pontuação técnica: **19/28 (67,9%)**;
- tempo acumulado das execuções consolidadas: **155,044 segundos**;
- tokens informados pelos grafos: **17.995**;
- custo local informado: **US$ 0**;
- revisão humana: concluída nos 14 casos em 13/09/2026, sem divergências.

## Ajustes sobre a classificação automática

- CT-04 mudou de `A` automático para `P` técnico: a string `NA` é formalmente
  não vazia, mas não atende ao requisito de mensagem compreensível.
- CT-11 mudou de `R` automático para `P` técnico: a string `"null"` viola a
  representação esperada e há inconsistência, porém nenhuma URL real foi
  fabricada; por isso a falha não foi tratada como crítica.

As classificações automáticas originais permanecem preservadas nos respectivos
arquivos `avaliacao.json` para garantir auditabilidade.
