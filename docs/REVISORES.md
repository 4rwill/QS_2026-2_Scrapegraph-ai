# Distribuição das revisões humanas

A revisão técnica por IA não substituiu a confirmação humana. Cada caso recebeu
dois integrantes, alternados para que todos participassem três ou quatro vezes.
Em 13/09/2026, o representante da equipe informou que todos concluíram as
verificações e confirmaram as classificações técnicas sem alterações. A
confirmação foi consolidada nos respectivos `registro.md`.
Os pareceres e as perguntas de conferência já estão separados por integrante em
`docs/PACOTES_REVISAO.md`.

| Caso | Revisor principal | Revisor secundário | Estado |
|---|---|---|---|
| CT-01 | Iuri Maurício Maia Pereira | Pedro César Figueiredo Carneiro | Concluída em 13/09/2026 |
| CT-02 | Rian Purificação de Oliveira | Arthur Soares Santana | Concluída em 13/09/2026 |
| CT-03 | Artur José Soares Santos | Christian Will Silva Santos Nunes | Concluída em 13/09/2026 |
| CT-04 | Eduardo Curcino Monteiro Filho | Eduardo Ferreira Bomfim Filho | Concluída em 13/09/2026 |
| CT-05 | Iuri Maurício Maia Pereira | Rian Purificação de Oliveira | Concluída em 13/09/2026 |
| CT-06 | Pedro César Figueiredo Carneiro | Arthur Soares Santana | Concluída em 13/09/2026 |
| CT-07 | Artur José Soares Santos | Eduardo Curcino Monteiro Filho | Concluída em 13/09/2026 |
| CT-08 | Christian Will Silva Santos Nunes | Eduardo Ferreira Bomfim Filho | Concluída em 13/09/2026 |
| CT-09 | Iuri Maurício Maia Pereira | Arthur Soares Santana | Concluída em 13/09/2026 |
| CT-10 | Pedro César Figueiredo Carneiro | Artur José Soares Santos | Concluída em 13/09/2026 |
| CT-11 | Rian Purificação de Oliveira | Christian Will Silva Santos Nunes | Concluída em 13/09/2026 |
| CT-12 | Eduardo Curcino Monteiro Filho | Iuri Maurício Maia Pereira | Concluída em 13/09/2026 |
| CT-13 | Eduardo Ferreira Bomfim Filho | Pedro César Figueiredo Carneiro | Concluída em 13/09/2026 |
| CT-14 | Arthur Soares Santana | Rian Purificação de Oliveira | Concluída em 13/09/2026 |

## Carga por integrante

| Integrante | Casos atribuídos | Total |
|---|---|---:|
| Arthur Soares Santana | CT-02, CT-06, CT-09, CT-14 | 4 |
| Artur José Soares Santos | CT-03, CT-07, CT-10 | 3 |
| Christian Will Silva Santos Nunes | CT-03, CT-08, CT-11 | 3 |
| Eduardo Curcino Monteiro Filho | CT-04, CT-07, CT-12 | 3 |
| Eduardo Ferreira Bomfim Filho | CT-04, CT-08, CT-13 | 3 |
| Iuri Maurício Maia Pereira | CT-01, CT-05, CT-09, CT-12 | 4 |
| Pedro César Figueiredo Carneiro | CT-01, CT-06, CT-10, CT-13 | 4 |
| Rian Purificação de Oliveira | CT-02, CT-05, CT-11, CT-14 | 4 |

## Procedimento realizado

1. Abrir `entrada.html` ou `entrada_http_esperada.html` e `prompt.txt`.
2. Conferir `saida.json` contra `resultado_esperado.json` e `avaliacao.json`.
3. Confirmar se o status `A`, `P` ou `R` é justificável.
4. Preencher no `registro.md` a decisão, observações, nome e data.
5. Como não houve divergência, manter as notas e os status técnicos.

## Fonte do registro consolidado

A conclusão das revisões foi registrada com base na declaração do representante
da Equipe 08 em 13/09/2026. Os pareceres técnicos originais da IA continuam
identificados separadamente para preservar a transparência do processo.
