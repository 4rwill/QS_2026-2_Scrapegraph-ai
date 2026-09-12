# Plano da Atividade 1 — ScrapeGraphAI

Documento principal de acompanhamento da Equipe 08. Atualizar este arquivo
sempre que uma validação humana, contribuição, entrega ou decisão for concluída.

## 1. Resumo da atividade

Avaliar a qualidade inicial do `SmartScraperGraph`, componente do
ScrapeGraphAI, na extração estruturada por schema a partir de HTML controlado.
O estudo cobre correção, completude, rastreabilidade, robustez, segurança,
privacidade, supervisão humana e variabilidade.

Linha de base:

- projeto oficial: <https://github.com/ScrapeGraphAI/Scrapegraph-ai>;
- versão: `v2.2.4`;
- commit: `c75c8084fae2d4f5ba01a8c218bc1168b67e3569`;
- provedor: Ollama `0.34.0`;
- modelo: `llama3.2:latest`, digest `a80c4f17acd5`;
- temperatura: `0`;
- fonte: `fontes/catalogo_controlado.html`;
- repositório acadêmico:
  <https://github.com/4rwill/QS_2026-2_Scrapegraph-ai/>.

## 2. Requisitos identificados no enunciado

- [x] Equipe e projeto definidos; exceção para oito integrantes autorizada.
- [x] Reserva do projeto informada como concluída.
- [x] Recorte e versão do projeto congelados.
- [x] Quatro partes interessadas, riscos e contexto descritos.
- [x] Doze requisitos verificáveis estruturados.
- [x] Oito características da ISO/IEC 25010:2023 relacionadas ao estudo.
- [x] Quatorze casos cobrindo todos os cenários do enunciado.
- [x] Cinco prompts repetidos três vezes.
- [x] Seis achados técnicos preliminares documentados.
- [~] Uso de IA declarado; revisão humana ainda pendente.
- [ ] Contribuições individuais reais registradas.
- [ ] Apresentação, vídeo e entrega final concluídos.

## 3. Entregáveis

| Entregável | Situação |
|---|---|
| Relatório técnico PDF de 8–12 páginas | Versão preliminar com 10 páginas |
| Apresentação em PDF ou slides | Pendente |
| Requisitos e testes estruturados | Concluídos em CSV |
| Evidências | Execuções técnicas registradas; revisão humana pendente |
| Declaração de uso de IA | Estruturada; revisão final pendente |
| Contribuição individual | Modelo criado; preenchimento real pendente |
| Repositório público | Definido |
| Vídeo de até 10 minutos | Pendente |
| Apresentação oral de 10–12 minutos | Pendente |

Prazo indicado no enunciado para os arquivos e URL do vídeo: **16/09/2026,
23h59**. Apresentação oral: **17/09/2026**, no horário da disciplina.

## 4. Critérios de avaliação

- atendimento aos mínimos quantitativos do enunciado;
- requisitos e critérios de aceitação verificáveis;
- pontuação dos testes em escala de 0 a 2;
- coerência com fontes e ausência de falhas críticas;
- rastreabilidade entre requisito, teste, evidência e achado;
- análise de variabilidade e riscos de IA generativa;
- plano de melhoria mensurável;
- transparência e verificação do uso de IA;
- participação e domínio dos oito integrantes;
- qualidade, formato, acessibilidade e prazo dos entregáveis.

O enunciado não informa pesos por seção. `A`, `P` e `R` são convenções internas
para atende, atende parcialmente e reprovado, sujeitas à confirmação docente.

## 5. Resultado técnico atual

### Suíte principal

- 14/14 casos executados;
- 8 `A`, 3 `P` e 3 `R`;
- pontuação: 19/28 (67,9%);
- tempo acumulado: 155,044 segundos;
- 17.995 tokens informados pelos grafos;
- custo local: US$ 0.

### Variabilidade

- 15/15 execuções concluídas;
- 9 `A`, 3 `P` e 3 `R`;
- pontuação: 21/30 (70%);
- cinco de cinco prompts estáveis byte a byte;
- conclusão: estabilidade não implica correção, como mostram CT-03 e CT-10.

### Achados preliminares

1. Contradição no tratamento de ambiguidade — alta.
2. Ausência representada como texto `"null"` — alta.
3. Mensagem não acionável fora do domínio — média.
4. Exposição contraditória de dado sensível sintético — crítica.
5. Classificação enviesada sem critério objetivo — alta.
6. Aviso assíncrono após timeout — média.

Esses resultados derivam de execução real e revisão técnica por IA. Não devem
ser apresentados como conclusões humanas até a assinatura dos revisores.

## 6. Checklist de execução

### Concluído tecnicamente

- [x] Preparar Ollama, modelo e ambiente Python.
- [x] Registrar baseline, versões e configurações.
- [x] Congelar fonte, gabarito, schema e resultados esperados.
- [x] Executar CT-01 a CT-14.
- [x] Preservar entradas, saídas, logs e avaliações automáticas.
- [x] Executar as 15 repetições.
- [x] Consolidar resultados e variabilidade.
- [x] Criar seis achados e ações de melhoria.
- [x] Gerar e inspecionar o PDF preliminar de 10 páginas.
- [x] Distribuir os revisores em rodízio.

### Validação humana

- [ ] Cada dupla abrir fonte, prompt, saída e avaliação do caso.
- [ ] Confirmar ou corrigir nota e status em cada `registro.md`.
- [ ] Informar nome, data, justificativa e divergências.
- [ ] Validar os seis achados e suas severidades.
- [ ] Confirmar as conclusões da análise de variabilidade.
- [ ] Aprovar requisitos, mapeamento ISO e limitações.

### Entrega

- [ ] Inserir instituição, curso/turma e docente.
- [ ] Arquivar comprovante da reserva e autorização para oito integrantes.
- [ ] Preencher contribuições individuais verificáveis.
- [ ] Produzir apresentação e roteiro.
- [ ] Gravar vídeo de até 10 minutos com todos os integrantes.
- [ ] Publicar o vídeo por URL acessível sem solicitação de permissão.
- [ ] Inserir a URL no relatório, README, VIDEO.md e Classroom.
- [ ] Gerar novamente o PDF e revisar as 8–12 páginas.
- [ ] Testar todos os links e arquivos em ambiente limpo.
- [ ] Entregar antes do prazo e guardar os comprovantes.
- [ ] Ensaiar a apresentação oral e as perguntas.

## 7. Plano de execução restante

| Ordem | Tarefa | Dependência | Resultado/evidência | Paralelismo |
|---:|---|---|---|---|
| 1 | Revisar humanamente CT-01 a CT-14 | Evidências técnicas | Decisões assinadas nos registros | Duplas podem atuar em paralelo |
| 2 | Validar achados e plano de melhoria | Revisão dos casos | ACH-01 a ACH-06 aprovados ou corrigidos | Paralelo entre achados |
| 3 | Completar dados institucionais | Dados da equipe | Capa sem marcadores | Independente |
| 4 | Registrar contribuições reais | Trabalho dos integrantes | `docs/CONTRIBUICOES.md` completo | Contínuo |
| 5 | Produzir apresentação e roteiro | Resultados validados | Slides e roteiro cronometrado | Paralelo à revisão editorial |
| 6 | Gravar e publicar vídeo | Roteiro e presença de todos | URL funcional, duração até 10 min | Atividade conjunta |
| 7 | Fechar relatório | Etapas 1–6 | PDF final de 8–12 páginas | Após consolidação |
| 8 | Auditar e entregar | Todos os artefatos | Checklist e comprovantes | Revisão cruzada |
| 9 | Ensaiar apresentação oral | Slides finalizados | Exposição de 10–12 min | Atividade conjunta |

## 8. Evidências necessárias

- baseline: `evidencias/01-baseline/`;
- casos: `evidencias/04-casos-teste/`;
- resumo da suíte: `evidencias/04-casos-teste/RESUMO_EXECUCAO.csv`;
- revisão técnica: `evidencias/04-casos-teste/REVISAO_TECNICA_IA.md`;
- variabilidade: `evidencias/05-variabilidade/`;
- achados: `evidencias/06-achados/`;
- validação do PDF: `evidencias/07-entrega/VALIDACAO_PDF_PRELIMINAR.md`;
- revisão humana: `docs/REVISORES.md` e `registro.md` de cada caso.

## 9. Pontos de atenção

- não inventar assinatura, revisão ou contribuição humana;
- não armazenar chaves, cookies ou dados pessoais reais;
- CT-05 usa exclusivamente um token sintético controlado;
- preservar resultados negativos e ajustes de protocolo;
- não alterar retrospectivamente os resultados esperados;
- manter relatório, CSVs, evidências, slides e vídeo coerentes;
- confirmar o significado oficial de `A/P/R` com o docente;
- testar anonimamente a URL do vídeo;
- não anexar o arquivo de vídeo ao Classroom, apenas a URL;
- todos devem participar do vídeo e da apresentação oral.

## 10. Dúvidas em aberto

- instituição, curso/turma e docente;
- comprovação arquivável da reserva e da autorização para oito integrantes;
- significado oficial de `A/P/R`;
- existência de rubrica ou pesos adicionais no Classroom;
- formato preferido da apresentação;
- responsáveis reais pelas ações de melhoria;
- URL, data e plataforma do vídeo.

## 11. Status geral

| Bloco | Estado |
|---|---|
| Planejamento e recorte | Concluído |
| Ambiente | Concluído |
| Requisitos e casos | Concluído tecnicamente |
| Suíte principal | Concluída tecnicamente |
| Variabilidade | Concluída tecnicamente |
| Achados | Seis preliminares |
| Revisões humanas | Pendente |
| PDF | Preliminar, 10 páginas |
| Apresentação e vídeo | Pendente |
| Entrega | Pendente |
