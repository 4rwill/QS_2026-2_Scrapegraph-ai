# Escopo e metodologia

## Objeto

O objeto de avaliação é o fluxo do `SmartScraperGraph` que recebe uma fonte HTML, um prompt e um schema Pydantic, processa o conteúdo e devolve dados estruturados.

## Dentro do escopo

- leitura de HTML controlado;
- extração de campos definidos no schema;
- correspondência entre saída e gabarito da fonte;
- ausência, conflito e tentativa de invenção de dados;
- entrada curta, longa, ambígua, fora do domínio e reformulada;
- dado sensível, conteúdo enviesado e indisponibilidade;
- repetição de prompts para observar variabilidade;
- logs e metadados necessários à rastreabilidade.

## Fora do escopo

- avaliação de todos os grafos do projeto;
- comparação exaustiva de provedores de LLM;
- desempenho em escala de produção;
- páginas que exigem autenticação, CAPTCHA ou autorização de coleta;
- correções no código-fonte oficial.

## Linha de base

| Item | Registro inicial |
|---|---|
| Repositório oficial | <https://github.com/ScrapeGraphAI/Scrapegraph-ai> |
| Versão | `v2.2.4` |
| Commit | `c75c8084fae2d4f5ba01a8c218bc1168b67e3569` |
| Licença | MIT |
| Data de acesso | 12/09/2026 |
| Python indicado no projeto | `>=3.12,<4.0` |
| Modelo/provedor do experimento | Ollama `0.34.0` com `llama3.2:latest`, ID `a80c4f17acd5`, 3.2B, Q4_K_M |
| Parâmetros planejados | Temperatura 0, formato JSON, 8192 tokens e `html_mode=true` |

## Método

1. Congelar fonte, gabarito, versão do projeto, modelo e parâmetros.
2. Definir requisitos e resultados esperados antes da execução.
3. Executar 14 casos de teste e registrar saída integral.
4. Pontuar cada caso de 0 a 2 e atribuir status `A/P/R` conforme a convenção.
5. Executar 5 prompts em 3 repetições com condições comparáveis.
6. Fazer revisão humana dos fatos e das fontes.
7. Relacionar falhas às características ISO e aos riscos.
8. Consolidar pelo menos 5 achados com severidade e ações mensuráveis.

## Regra contra avaliação circular

A IA pode ajudar a redigir, organizar e comparar, mas não será a única autoridade. A aprovação de resultados depende de validação por schema, comparação com gabarito, inspeção de logs/fontes e revisão humana registrada.
