# ACH-06 — Aviso assíncrono após timeout

| Campo | Registro |
|---|---|
| Severidade | Média |
| Requisitos | RQ-02; RQ-03; RQ-07; RQ-11 |
| Caso | CT-14 |
| Evidência primária | `../04-casos-teste/CT-14/execucao.log`; `../04-casos-teste/CT-14/AVISO_TERMINAL.txt` |
| Revisão humana | Pendente |

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
