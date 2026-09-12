# Índice de evidências

Nenhum arquivo marcado como evidência deve ser criado para “preencher espaço”. Uma evidência só é válida quando resulta de uma ação observável e preserva contexto suficiente para auditoria.

## Organização

| Pasta | Prefixo | Conteúdo esperado |
|---|---|---|
| `00-administrativo/` | ADM | Reserva, autorização da equipe e decisões formais |
| `01-baseline/` | BASE | Versão, commit, licença, ambiente e configuração |
| `02-contexto-riscos/` | CTX | Stakeholders, riscos, supervisão e limites |
| `03-requisitos-iso/` | REQ | Revisões de requisitos e aplicação da ISO |
| `04-casos-teste/` | EV-CT | Entradas, saídas, logs, capturas e avaliação dos testes |
| `05-variabilidade/` | VAR | Três repetições de cinco prompts e comparações |
| `06-achados/` | ACH | Evidência consolidada, severidade e recomendação |
| `07-entrega/` | ENT | Validação de PDFs, links, vídeo e comprovantes de envio |

## Registro mestre

| Bloco | Quantidade/estado | Índice principal | Revisão humana |
|---|---|---|---|
| Baseline | 3 registros do ambiente | `evidencias/01-baseline/README.md` | Pendente |
| Suíte principal | 14/14 casos executados | `evidencias/04-casos-teste/RESUMO_EXECUCAO.csv` | Pendente conforme `docs/REVISORES.md` |
| Revisão técnica | 14 casos consolidados | `evidencias/04-casos-teste/REVISAO_TECNICA_IA.md` | Não substitui revisão humana |
| Variabilidade | 15/15 execuções | `evidencias/05-variabilidade/ANALISE_VARIABILIDADE.md` | Pendente |
| Achados | 6 preliminares | `evidencias/06-achados/README.md` | Pendente |
| PDF | 10 páginas verificadas | `evidencias/07-entrega/VALIDACAO_PDF_PRELIMINAR.md` | Revisão final pendente |

## Convenção de nomes

`<ID>_<AAAA-MM-DD>_<descricao-curta>.<extensão>`

Exemplos:

- `EV-CT-01_2026-09-13_saida.json`
- `EV-CT-01_2026-09-13_execucao.log`
- `VAR-P01-R2_2026-09-13_resposta.json`
- `ENT-VIDEO_2026-09-16_teste-acesso.png`

## Metadados mínimos

- data e hora;
- integrante responsável;
- requisito e caso relacionados;
- commit do ScrapeGraphAI;
- modelo/provedor e versão, se disponíveis;
- parâmetros e configuração;
- hash ou versão da fonte;
- entrada e saída integrais;
- avaliação humana e pessoa revisora;
- observações sobre limitações e privacidade.
