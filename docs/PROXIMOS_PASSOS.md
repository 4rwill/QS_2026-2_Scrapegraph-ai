# Próximos passos

## Dados humanos necessários

- instituição, curso/turma e docente;
- confirmação/documento da autorização para 8 integrantes;
- captura ou comprovante da reserva no Classroom;
- responsáveis e revisores de cada bloco.

## Recurso técnico necessário para executar os testes

Foi instalado o Ollama `0.34.0` com o modelo `llama3.2:latest`, ID `a80c4f17acd5`. A configuração planejada está em `config/ollama.example.json`. Não há chave de API externa e nenhum segredo deve ser versionado.

Preparação concluída em 12/09/2026:

1. [x] instalar o Ollama no computador de execução;
2. [x] baixar a tag acordada de `llama3.2`;
3. [x] registrar a versão do Ollama e o identificador do modelo;
4. [x] confirmar o serviço local por uma resposta mínima do modelo;
5. [x] executar o CT-01 como piloto pelo SmartScraperGraph;
6. [x] executar CT-02 a CT-14;
7. [x] executar 15 repetições de variabilidade;
8. [x] consolidar a revisão técnica por IA e seis achados preliminares.

A suíte principal obteve 8 casos `A`, 3 `P` e 3 `R` na revisão técnica por IA,
com 19/28 (67,9%). As 15 repetições foram concluídas. Esses resultados somente
se tornam conclusões finais após a revisão humana registrada.

## Ordem imediata

1. Completar instituição, curso/turma e docente na capa.
2. Revisar e aprovar os 12 requisitos e 14 casos.
3. [x] Integrar o ambiente Python/ScrapeGraphAI ao Ollama já instalado.
4. [x] Executar CT-01 como piloto e revisar o protocolo técnico.
5. [x] Executar CT-02 a CT-14 e preservar saídas, logs e avaliações.
6. [x] Executar as 15 repetições de variabilidade.
7. Fazer a revisão humana dos 14 casos conforme `docs/REVISORES.md`.
8. Validar os seis achados e seus planos de melhoria por revisão cruzada.
9. Completar dados institucionais e contribuições individuais verificáveis.
10. Revisar o PDF preliminar, produzir slides, vídeo e entrega.
