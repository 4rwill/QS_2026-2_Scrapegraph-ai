# ACH-06 — Aviso assíncrono após timeout

| Campo | Registro |
|---|---|
| Severidade | Média |
| Requisitos | RQ-02; RQ-03; RQ-07; RQ-11 |
| Caso | CT-14 |
| Evidência primária | `../02-casos-teste/CT-14/execucao.log`; `../02-casos-teste/CT-14/AVISO_TERMINAL.txt` |
| Revisão humana | Eduardo Ferreira Bomfim Filho — confirmada em 13/09/2026 |
| Responsável pela melhoria | Arthur Soares Santana |
| Prioridade | Média |
| Dependências | Controle do ciclo de vida do Playwright e consumo das tarefas canceladas |

O timeout principal funcionou e não houve resultado fabricado, mas o Playwright
emitiu posteriormente `Future exception was never retrieved` com
`TargetClosedError`. O aviso sugere cancelamento ou fechamento incompleto de uma
tarefa assíncrona e pode poluir logs ou ocultar problemas em execução em lote.

## Melhoria proposta

- aguardar e consumir exceções das tarefas canceladas;
- fechar página, contexto e navegador em ordem e de forma idempotente;
- adicionar teste de ausência de warnings após timeout.

**Indicador:** CT-14 encerra dentro do limite sem mensagens assíncronas posteriores.

**Risco residual:** baixo após correção do ciclo de vida.

**Critério de conclusão:** três execuções do CT-14 encerram dentro do timeout sem
`Future exception was never retrieved` ou `TargetClosedError` tardio.
