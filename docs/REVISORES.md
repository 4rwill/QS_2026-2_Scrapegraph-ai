# Distribuição das revisões humanas

A revisão técnica por IA não substitui a confirmação humana. Cada caso possui
dois integrantes designados, alternados para que todos participem três ou quatro
vezes. O status permanece **pendente** até que os revisores confiram a fonte, o
prompt, a saída e a avaliação e registrem sua decisão no `registro.md` do caso.

| Caso | Revisor principal | Revisor secundário | Estado |
|---|---|---|---|
| CT-01 | Iuri Maurício Maia Pereira | Pedro César Figueiredo Carneiro | Pendente |
| CT-02 | Rian Purificação de Oliveira | Arthur Soares Santana | Pendente |
| CT-03 | Artur José Soares Santos | Christian Will Silva Santos Nunes | Pendente |
| CT-04 | Eduardo Curcino Monteiro Filho | Eduardo Ferreira Bomfim Filho | Pendente |
| CT-05 | Iuri Maurício Maia Pereira | Rian Purificação de Oliveira | Pendente |
| CT-06 | Pedro César Figueiredo Carneiro | Arthur Soares Santana | Pendente |
| CT-07 | Artur José Soares Santos | Eduardo Curcino Monteiro Filho | Pendente |
| CT-08 | Christian Will Silva Santos Nunes | Eduardo Ferreira Bomfim Filho | Pendente |
| CT-09 | Iuri Maurício Maia Pereira | Arthur Soares Santana | Pendente |
| CT-10 | Pedro César Figueiredo Carneiro | Artur José Soares Santos | Pendente |
| CT-11 | Rian Purificação de Oliveira | Christian Will Silva Santos Nunes | Pendente |
| CT-12 | Eduardo Curcino Monteiro Filho | Iuri Maurício Maia Pereira | Pendente |
| CT-13 | Eduardo Ferreira Bomfim Filho | Pedro César Figueiredo Carneiro | Pendente |
| CT-14 | Arthur Soares Santana | Rian Purificação de Oliveira | Pendente |

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

## Procedimento mínimo

1. Abrir `entrada.html` ou `entrada_http_esperada.html` e `prompt.txt`.
2. Conferir `saida.json` contra `resultado_esperado.json` e `avaliacao.json`.
3. Confirmar se o status `A`, `P` ou `R` é justificável.
4. Preencher no `registro.md` a decisão, observações, nome e data.
5. Se houver divergência, preservar a avaliação original e registrar a correção.
