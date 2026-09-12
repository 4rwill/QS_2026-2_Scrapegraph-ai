# Análise de variabilidade

## Configuração

- ScrapeGraphAI `v2.2.4`, commit `c75c8084fae2d4f5ba01a8c218bc1168b67e3569`;
- Ollama `0.34.0`;
- modelo `llama3.2:latest`, digest `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`;
- temperatura 0, formato JSON, `html_mode=true`;
- três execuções novas e dedicadas por prompt.

## Resultado por prompt

| Prompt-base | Status das repetições | Saídas distintas | Estabilidade byte a byte | Interpretação |
|---|---|---:|---|---|
| CT-01 | A, A, A | 1 | Sim | Catálogo correto e invariável. |
| CT-03 | R, R, R | 1 | Sim | A mesma falha de ausência/`"null"` repetiu-se três vezes. |
| CT-06 | A, A, A | 1 | Sim | Paráfrase correta e invariável. |
| CT-10 | P, P, P | 1 | Sim | Preços e conflito corretos, mas `Produto Aurora` foi reduzido para `Aurora`. |
| CT-12 | A, A, A | 1 | Sim | Schema e fatos corretos e invariáveis. |

## Consolidação

- 15/15 execuções concluídas sem erro técnico;
- 9 resultados `A`, 3 resultados `P` e 3 resultados `R`;
- pontuação: **21/30 (70%)**;
- 5/5 prompts produziram uma única saída canônica nas três repetições;
- revisão humana das amostras: pendente.

## Conclusão técnica

A temperatura zero e o ambiente local produziram estabilidade byte a byte nesta
amostra. Entretanto, CT-03 e CT-10 demonstram que repetibilidade não implica
correção: uma falha pode ser perfeitamente estável. Por isso, o indicador de
variabilidade deve ser analisado junto com aderência ao gabarito, schema e revisão
humana, nunca isoladamente.
