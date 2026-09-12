# Ajuste do protocolo do CT-01

Na tentativa inicial, iniciada em 12/09/2026 às 16:27:42 (UTC-03:00), o
SmartScraperGraph concluiu o caso em 24,940 segundos e a saída coincidiu com o
gabarito. Entretanto, o arquivo `execucao.log` ficou vazio porque as mensagens
internas do projeto estavam vinculadas ao fluxo original do terminal e não ao
redirecionamento do executor.

O protocolo foi corrigido antes da consolidação do caso para:

- gravar uma trilha estruturada independente do fluxo de terminal;
- armazenar `execution_info.json`, retornado pelo próprio grafo;
- identificar a execução consolidada como tentativa 2.

O prompt, schema, fonte, gabarito, configuração, versão do projeto e modelo não
foram alterados. Os arquivos principais da pasta correspondem à tentativa 2.
