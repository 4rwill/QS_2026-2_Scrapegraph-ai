# Índice de evidências

Esta área reúne apenas registros técnicos e observáveis produzidos durante a
execução, a revisão e a preparação da entrega. Informações de planejamento ou
decisões administrativas não precisam de uma pasta de evidência própria.

## Organização

| Pasta | Prefixo | Conteúdo esperado |
|---|---|---|
| `01-baseline/` | BASE | Versão, commit, licença, ambiente e configuração |
| `02-casos-teste/` | EV-CT | Entradas, saídas, logs, capturas e avaliação dos testes |
| `03-variabilidade/` | VAR | Três repetições de cinco prompts e comparações |
| `04-achados/` | ACH | Evidência consolidada, severidade e recomendação |
| `05-entrega/` | ENT | Validação de PDFs, links, vídeo e comprovantes de envio |

## Onde estão contexto, riscos, requisitos e ISO

Esses itens fazem parte da análise do trabalho, mas não constituem evidências
de execução isoladas:

- contexto, partes interessadas, riscos, limites e supervisão:
  `docs/ESCOPO_E_METODOLOGIA.md` e relatório técnico;
- requisitos verificáveis: `dados/requisitos.csv`;
- relação entre requisitos, casos de teste e características da ISO/IEC 25010:
  `dados/matriz_rastreabilidade.csv`;
- síntese e interpretação dos requisitos e da ISO: relatório técnico.

## Registro mestre

| Bloco | Quantidade/estado | Índice principal | Revisão humana |
|---|---|---|---|
| Baseline | 3 registros do ambiente | `evidencias/01-baseline/README.md` | Validado por Iuri em 13/09/2026 |
| Suíte principal | 14/14 casos executados | `evidencias/02-casos-teste/RESUMO_EXECUCAO.csv` | Concluída conforme `docs/REVISORES.md` |
| Revisão técnica | 14 casos consolidados | `evidencias/02-casos-teste/REVISAO_TECNICA_IA.md` | Confirmada pelos revisores humanos |
| Variabilidade | 15/15 execuções | `evidencias/03-variabilidade/ANALISE_VARIABILIDADE.md` | Validada por Pedro em 13/09/2026 |
| Achados | 6 confirmados | `evidencias/04-achados/README.md` | Validados por Eduardo Ferreira em 13/09/2026 |
| PDF | 10 páginas verificadas | `evidencias/05-entrega/VALIDACAO_PDF_PRELIMINAR.md` | Nova versão final ainda necessária |

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
