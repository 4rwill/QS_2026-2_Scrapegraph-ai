# Evidências de linha de base

Arquivar aqui:

- versão/commit do ScrapeGraphAI;
- licença MIT e data de acesso;
- versão do Python e dependências;
- sistema operacional;
- modelo/provedor e parâmetros;
- hash das fontes controladas;
- configuração sanitizada, sem chaves.

## Estado inicial

- Projeto: <https://github.com/ScrapeGraphAI/Scrapegraph-ai>
- Versão observada: `v2.2.4`
- Commit observado: `c75c8084fae2d4f5ba01a8c218bc1168b67e3569`
- Data de acesso: 12/09/2026
- Provedor escolhido: Ollama.
- Ollama instalado: versão `0.34.0`.
- Modelo disponível: `llama3.2:latest`, ID `a80c4f17acd5`, 3.2B, Q4_K_M.
- Parâmetros do experimento: temperatura 0, JSON/schema e contexto declarado de 8192 tokens.
- Verificação mínima do modelo: concluída com resposta `OK` em 12/09/2026.
- Execução pelo SmartScraperGraph: pendente; a verificação mínima não conta como caso de teste da avaliação.

Arquivos registrados:

- `BASE-01_2026-09-12_ollama-versao.txt`;
- `BASE-02_2026-09-12_modelo-llama3.2.txt`;
- `BASE-03_2026-09-12_teste-minimo.txt`.
