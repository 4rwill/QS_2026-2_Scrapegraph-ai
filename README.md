# Qualidade de Software 2026.2 - ScrapeGraphAI

Repositório acadêmico da Atividade 1 (AV1) de Qualidade de Software.

**Equipe 08:** oito integrantes identificados em `docs/CONTRIBUICOES.md`, em ordem alfabética.

## Estado atual

O ambiente experimental, o protocolo e os 14 casos de teste foram executados. A
revisão técnica por IA resultou em 8 casos `A`, 3 `P` e 3 `R`, totalizando
19/28 (67,9%). Também foram concluídas 15 execuções de variabilidade (cinco
prompts, três repetições cada), todas estáveis byte a byte. Em 13/09/2026, os
oito integrantes concluíram o rodízio de validação humana e confirmaram as
classificações técnicas sem alterações.

## Recorte adotado

Avaliação do `SmartScraperGraph` na extração de dados estruturados por schema a partir de uma fonte HTML controlada, com foco em:

- correção e completude da extração;
- aderência da saída ao schema;
- rastreabilidade dos valores à fonte;
- comportamento diante de entradas ambíguas, incompletas, adversas ou indisponíveis;
- privacidade, segurança e robustez;
- variabilidade entre repetições equivalentes.

Versão de referência inicialmente congelada:

- projeto oficial: <https://github.com/ScrapeGraphAI/Scrapegraph-ai>;
- licença: MIT;
- versão observada: `v2.2.4`;
- commit observado: `c75c8084fae2d4f5ba01a8c218bc1168b67e3569`;
- data de acesso: 12/09/2026.

Configuração experimental escolhida:

- provedor local: Ollama;
- modelo: `llama3.2:latest`;
- temperatura: `0`;
- formato: `json` com schema Pydantic;
- contexto declarado: `8192` tokens;
- ambiente confirmado em 12/09/2026: Ollama `0.34.0`, modelo `llama3.2:latest`, ID `a80c4f17acd5` (3.2B, Q4_K_M);
- verificação mínima: serviço local respondeu `OK`;
- suíte principal: 14/14 casos executados em 12/09/2026; 155,044 s acumulados,
  17.995 tokens informados pelos grafos e custo local US$ 0;
- variabilidade: 15/15 repetições concluídas, com 9 `A`, 3 `P` e 3 `R`.

## Estrutura do repositório

| Caminho | Finalidade |
|---|---|
| `config/` | Configuração experimental sanitizada, sem credenciais |
| `docs/` | Escopo, decisões, metodologia, uso de IA e contribuições |
| `dados/` | Requisitos, casos de teste e matriz de rastreabilidade em formato estruturado |
| `fontes/` | Entradas controladas e respectivos gabaritos |
| `evidencias/` | Provas organizadas por etapa e indexadas por ID |
| `relatorio/` | Orientações e fonte editorial do relatório |
| `scripts/` | Gerador reproduzível do PDF |
| `output/pdf/` | PDF gerado para revisão e, futuramente, entrega |

## Regra de evidência

Toda afirmação de resultado deve apontar para uma evidência com ID único. A evidência deve registrar data/hora, versão, modelo/provedor, parâmetros, entrada, saída completa, pessoa responsável e relação com requisito/caso de teste. Segredos e dados pessoais não devem ser armazenados.

## Entregáveis

- [ ] Relatório técnico final em PDF, com 8 a 12 páginas sem contar anexos.
- [ ] Apresentação em PDF ou slides.
- [x] Arquivos estruturados iniciais de requisitos e casos de teste.
- [x] Evidências técnicas dos 14 casos e das 15 repetições registradas.
- [x] Declaração de uso de IA generativa estruturada e revisada.
- [x] Tabela de contribuição individual preenchida conforme confirmação da equipe.
- [ ] Vídeo de até 10 minutos com participação de todos.
- [ ] Apresentação oral de 10 a 12 minutos.

## Vídeo da atividade

**URL:** <https://drive.google.com/drive/folders/1_njyIG21NX0ne1NxJ7N5D7cV5NQ-Gis4>;

O vídeo ainda não foi gravado. Após a publicação, a mesma URL deverá ser registrada também no relatório, no arquivo [`VIDEO.md`](VIDEO.md) e no Google Classroom.
