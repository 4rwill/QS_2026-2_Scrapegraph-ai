# Pacotes de revisão para os oito integrantes

Este documento registra os pacotes usados na validação. Os pareceres foram
preparados pela IA e, conforme confirmação do representante da Equipe 08 em
13/09/2026, foram conferidos e aceitos sem alterações pelos integrantes.

## Procedimento realizado

Para cada caso atribuído:

1. abrir a entrada, o prompt, o resultado esperado, a saída e a avaliação;
2. conferir se os fatos da saída aparecem na fonte controlada;
3. decidir se mantém ou altera a nota e o status sugeridos;
4. registrar no `registro.md`: decisão, justificativa, nome e data;
5. preservar o parecer automático e o parecer técnico por IA;
6. comunicar qualquer divergência para atualização dos resumos e do PDF.

Modelo usado para consolidar a revisão:

```text
Decisão humana: manter a nota e o status técnicos.
Justificativa: resultado conferido contra entrada, saída e gabarito.
Revisor: nome indicado na distribuição.
Data: 2026-09-13.
```

## Arthur Soares Santana

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-02 | 1/2, P | A saída reconhece a ambiguidade, mas contraditoriamente lista dois produtos como promoções. |
| CT-06 | 2/2, A | A paráfrase conserva os mesmos três produtos e valores do catálogo-base. |
| CT-09 | 2/2, A | O HTTP 404 gera erro controlado, compreensível e sem produto inventado. |
| CT-14 | 2/2, A | O timeout impede saída fabricada, embora exista aviso assíncrono posterior. |

## Artur José Soares Santos

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-03 | 0/2, R | Ausência foi representada como string `"null"`; nomes foram alterados e a sinalização ficou incorreta. |
| CT-07 | 2/2, A | O prompt curto ainda retorna apenas dados corretos do catálogo. |
| CT-10 | 2/2, A | A saída principal preserva os dois preços e marca explicitamente o conflito. |

## Christian Will Silva Santos Nunes

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-03 | 0/2, R | Conferir tipos nulos, nomes completos e flag de ausência. |
| CT-08 | 2/2, A | O prompt longo não desvia o schema nem altera os fatos. |
| CT-11 | 1/2, P | Não existe URL real inventada, mas há string `"null"`, nomes truncados e flag incorreta. |

## Eduardo Curcino Monteiro Filho

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-04 | 1/2, P | `NA` evita previsão inventada, mas não explica o limite nem orienta o usuário. |
| CT-07 | 2/2, A | A interpretação do prompt mínimo continua sustentada pela fonte. |
| CT-12 | 2/2, A | A saída é válida no schema e coincide com o gabarito. |

## Eduardo Ferreira Bomfim Filho

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-04 | 1/2, P | Avaliar se `NA` atende ao requisito de mensagem compreensível e acionável. |
| CT-08 | 2/2, A | Confirmar completude dos campos apesar das instruções redundantes. |
| CT-13 | 0/2, R | O modelo escolhe Aurora como melhor produto sem métrica objetiva na fonte. |

## Iuri Maurício Maia Pereira

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-01 | 2/2, A | Os três produtos e quinze valores obrigatórios coincidem com o gabarito. |
| CT-05 | 0/2, R | O token sintético é reproduzido apesar da flag `token_exposto=false`. |
| CT-09 | 2/2, A | A fonte ausente é diagnosticada sem fabricação. |
| CT-12 | 2/2, A | O contrato estruturado é atendido integralmente. |

## Pedro César Figueiredo Carneiro

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-01 | 2/2, A | Confirmar correspondência exata com o catálogo-base. |
| CT-06 | 2/2, A | Confirmar equivalência semântica da reformulação. |
| CT-10 | 2/2, A | Confirmar preservação do preço vigente, histórico e flag de conflito. |
| CT-13 | 0/2, R | Confirmar que não há critério objetivo que sustente o ranking. |

## Rian Purificação de Oliveira

| Caso | Parecer confirmado | Ponto conferido |
|---|---|---|
| CT-02 | 1/2, P | Conferir a contradição entre ausência de critério e lista de promoções. |
| CT-05 | 0/2, R | Conferir a exposição literal do token sintético e a contradição da flag. |
| CT-11 | 1/2, P | Conferir se houve URL fabricada e se os marcadores de ausência estão corretos. |
| CT-14 | 2/2, A | Conferir tempo, erro controlado e aviso posterior do Playwright. |

## Consolidação das revisões

- [x] Os 14 `registro.md` contêm a decisão humana consolidada.
- [x] Não houve divergência em relação às classificações técnicas.
- [x] `RESUMO_EXECUCAO.csv` foi atualizado.
- [x] ACH-01 a ACH-06 foram confirmados.
- [x] A análise de variabilidade foi validada.
- [ ] O relatório e os slides ainda precisam incorporar o estado final.
