# Evidências dos casos de teste

Criar uma subpasta por caso somente no momento da execução:

```text
CT-01/
  registro.md
  entrada.txt
  saida.json
  execucao.log
  captura.png        # quando agregar informação
```

O arquivo `registro.md` deve usar `templates/REGISTRO_EXECUCAO.md` e apontar para todos os arquivos do caso.

## Estado de execução

Os 14 casos foram executados. A consolidação da revisão técnica por IA está em
`REVISAO_TECNICA_IA.md` e os dados tabulares em `RESUMO_EXECUCAO.csv`.

| Resultado técnico | Quantidade |
|---|---:|
| `A` | 8 |
| `P` | 3 |
| `R` | 3 |
| Pontuação total | 19/28 (67,9%) |

Todas as confirmações humanas permanecem pendentes e estão distribuídas em
`docs/REVISORES.md`.

O CT-01 foi executado duas vezes durante a calibração. A primeira execução revelou uma falha apenas na captura do log; o ajuste está documentado em `CT-01/AJUSTE_PROTOCOLO.md`. A tentativa 2 é a evidência consolidada.

## Casos planejados

`CT-01` esperado; `CT-02` ambiguidade; `CT-03` falta de informação; `CT-04` fora de domínio; `CT-05` dado sensível; `CT-06` reformulação; `CT-07` entrada curta; `CT-08` entrada longa; `CT-09` fonte ausente; `CT-10` fonte conflitante; `CT-11` tentativa de fonte inventada; `CT-12` saída estruturada; `CT-13` conteúdo enviesado; `CT-14` indisponibilidade.
