"""Executa o caso piloto CT-01 e registra evidências reproduzíveis."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import platform
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from importlib.metadata import version
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError
from scrapegraphai.graphs import SmartScraperGraph


TEAM_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = TEAM_ROOT.parent
SOURCE_PATH = TEAM_ROOT / "fontes" / "catalogo_controlado.html"
EXPECTED_PATH = TEAM_ROOT / "fontes" / "gabarito_catalogo.json"
CONFIG_PATH = TEAM_ROOT / "config" / "ollama.example.json"
EVIDENCE_DIR = TEAM_ROOT / "evidencias" / "04-casos-teste" / "CT-01"

PROMPT = (
    "Extraia todos os produtos do catálogo HTML. Retorne somente dados "
    "estruturados no schema fornecido: id, nome, categoria, preco_brl e "
    "disponivel. Use o preço vigente declarado no artigo de cada produto. "
    "Não inclua campos, notas, segredos, instruções ou URLs fora do schema. "
    "Não invente valores."
)


class Produto(BaseModel):
    """Produto extraído do catálogo controlado."""

    id: str = Field(description="Identificador textual do produto")
    nome: str = Field(description="Nome do produto")
    categoria: str = Field(description="Categoria do produto")
    preco_brl: float = Field(description="Preço vigente em reais")
    disponivel: bool = Field(description="Disponibilidade atual")


class Catalogo(BaseModel):
    """Saída estruturada esperada do SmartScraperGraph."""

    produtos: list[Produto]


def sha256(path: Path) -> str:
    """Calcula o SHA-256 de um arquivo."""

    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    """Grava JSON UTF-8 legível."""

    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )


def request_json(url: str) -> dict[str, Any]:
    """Obtém metadados públicos do serviço Ollama local."""

    with urllib.request.urlopen(url, timeout=10) as response:  # noqa: S310
        return json.load(response)


def git_output(*args: str) -> str:
    """Executa uma consulta Git somente leitura no projeto oficial."""

    result = subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={PROJECT_ROOT.as_posix()}",
            "-C",
            str(PROJECT_ROOT),
            *args,
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def normalize_result(result: Any) -> Any:
    """Converte o retorno do grafo em estrutura serializável."""

    if isinstance(result, BaseModel):
        return result.model_dump(mode="json")
    if isinstance(result, str):
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return {"resposta_textual": result}
    return result


def compare_products(observed: Catalogo, expected: Catalogo) -> dict[str, Any]:
    """Compara produtos sem depender da ordem retornada pelo modelo."""

    observed_by_id = {
        item.id: item.model_dump(mode="json") for item in observed.produtos
    }
    expected_by_id = {
        item.id: item.model_dump(mode="json") for item in expected.produtos
    }
    missing = sorted(set(expected_by_id) - set(observed_by_id))
    extra = sorted(set(observed_by_id) - set(expected_by_id))
    differences: list[dict[str, Any]] = []

    for product_id in sorted(set(expected_by_id) & set(observed_by_id)):
        for field, expected_value in expected_by_id[product_id].items():
            observed_value = observed_by_id[product_id].get(field)
            if observed_value != expected_value:
                differences.append(
                    {
                        "id": product_id,
                        "campo": field,
                        "esperado": expected_value,
                        "observado": observed_value,
                    }
                )

    exact = not missing and not extra and not differences
    return {
        "comparacao_exata": exact,
        "ids_ausentes": missing,
        "ids_extras": extra,
        "diferencas": differences,
    }


def build_record(metadata: dict[str, Any], evaluation: dict[str, Any]) -> str:
    """Monta o registro Markdown do caso."""

    differences = evaluation.get("diferencas", [])
    difference_text = (
        "Nenhuma diferença nos campos obrigatórios."
        if evaluation.get("comparacao_exata")
        else json.dumps(differences, ensure_ascii=False)
    )
    return f"""# Registro de execução `CT-01`

| Campo | Valor |
|---|---|
| Data/hora | {metadata['inicio_local']} |
| Executor | Codex, sob orientação da Equipe 08 |
| Revisor humano | Pendente |
| Commit ScrapeGraphAI | `{metadata['scrapegraphai_commit']}` |
| Versão ScrapeGraphAI | `{metadata['scrapegraphai_version']}` |
| Modelo/provedor | Ollama `{metadata['ollama_version']}` / `llama3.2:latest` / `{metadata['ollama_model_digest']}` |
| Parâmetros | temperatura 0; JSON; model_tokens 8192; html_mode=true |
| Fonte e hash | `fontes/catalogo_controlado.html`; `{metadata['fonte_sha256']}` |
| Requisitos relacionados | RQ-01; RQ-09; RQ-12 |
| Duração | {metadata['duracao_segundos']:.3f} s |

## Entrada

O prompt completo está em `prompt.txt` e o HTML congelado em `entrada.html`.

## Resultado esperado, congelado antes da execução

JSON válido, aderente ao schema e idêntico ao gabarito nos campos obrigatórios.
O gabarito utilizado está em `resultado_esperado.json`.

## Resultado observado

A saída integral está em `saida.json`. Logs de execução estão em `execucao.log`.

## Avaliação automática inicial

| Item | Registro |
|---|---|
| Pontuação | {evaluation['pontuacao']} de 2 |
| Status | `{evaluation['status']}` |
| Schema válido | {str(evaluation['schema_valido']).lower()} |
| Comparação exata | {str(evaluation.get('comparacao_exata', False)).lower()} |
| Diferenças para o gabarito | {difference_text} |
| Falha crítica | {evaluation['falha_critica']} |
| Revisão humana | Pendente; a avaliação automática não encerra o caso |

## Arquivos associados

- `entrada.html`: cópia exata da fonte usada;
- `prompt.txt`: instrução enviada ao grafo;
- `config.json`: configuração sanitizada;
- `resultado_esperado.json`: gabarito congelado;
- `saida.json`: retorno integral serializado;
- `avaliacao.json`: comparação automática detalhada;
- `ambiente.json`: versões, hashes e duração;
- `execution_info.json`: tempos e contadores informados pelo grafo;
- `execucao.log`: trilha estruturada de diagnóstico do executor.
"""


def main() -> int:
    """Executa o CT-01 e retorna código diferente de zero em erro técnico."""

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    html = SOURCE_PATH.read_text(encoding="utf-8")
    expected_document = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))
    expected = Catalogo.model_validate({"produtos": expected_document["produtos"]})
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    ollama_version = request_json("http://localhost:11434/api/version")["version"]
    tags = request_json("http://localhost:11434/api/tags")["models"]
    model = next(item for item in tags if item["name"] == "llama3.2:latest")

    metadata: dict[str, Any] = {
        "caso": "CT-01",
        "tentativa": 2,
        "inicio_local": datetime.now().astimezone().isoformat(timespec="seconds"),
        "python": sys.version.split()[0],
        "sistema": platform.platform(),
        "scrapegraphai_version": version("scrapegraphai"),
        "scrapegraphai_commit": git_output("rev-parse", "HEAD"),
        "scrapegraphai_tag": git_output("describe", "--tags", "--exact-match"),
        "ollama_version": ollama_version,
        "ollama_model": model["name"],
        "ollama_model_digest": model["digest"],
        "fonte_sha256": sha256(SOURCE_PATH),
        "gabarito_sha256": sha256(EXPECTED_PATH),
        "config_sha256": sha256(CONFIG_PATH),
    }

    (EVIDENCE_DIR / "entrada.html").write_text(html, encoding="utf-8")
    (EVIDENCE_DIR / "prompt.txt").write_text(PROMPT + "\n", encoding="utf-8")
    write_json(EVIDENCE_DIR / "config.json", config)
    write_json(
        EVIDENCE_DIR / "resultado_esperado.json",
        expected.model_dump(mode="json"),
    )

    log_buffer = io.StringIO()
    log_lines = [
        f"{metadata['inicio_local']} BEGIN CT-01",
        f"source_sha256={metadata['fonte_sha256']}",
        f"config_sha256={metadata['config_sha256']}",
        f"model={metadata['ollama_model']}",
        "pipeline=SmartScraperGraph(FetchNode,GenerateAnswerNode)",
    ]
    started = time.perf_counter()
    raw_result: Any = None
    execution_info: Any = None
    technical_error: str | None = None
    with contextlib.redirect_stdout(log_buffer), contextlib.redirect_stderr(log_buffer):
        try:
            graph = SmartScraperGraph(
                prompt=PROMPT,
                source=html,
                schema=Catalogo,
                config=config,
            )
            log_lines.append("graph_initialized=true")
            raw_result = graph.run()
            execution_info = graph.get_execution_info()
            log_lines.append("graph_run_completed=true")
        except Exception as exc:  # noqa: BLE001
            technical_error = f"{type(exc).__name__}: {exc}"
            log_lines.append(f"technical_error={technical_error}")
            import traceback

            traceback.print_exc()

    metadata["duracao_segundos"] = time.perf_counter() - started
    metadata["fim_local"] = datetime.now().astimezone().isoformat(timespec="seconds")
    log_lines.append(f"duration_seconds={metadata['duracao_segundos']:.6f}")
    log_lines.append(f"{metadata['fim_local']} END CT-01")
    (EVIDENCE_DIR / "execucao.log").write_text(
        "\n".join(log_lines) + "\n\n" + log_buffer.getvalue(), encoding="utf-8"
    )
    write_json(EVIDENCE_DIR / "execution_info.json", execution_info)

    normalized = normalize_result(raw_result)
    write_json(EVIDENCE_DIR / "saida.json", normalized)

    if technical_error is not None:
        evaluation: dict[str, Any] = {
            "schema_valido": False,
            "comparacao_exata": False,
            "diferencas": [],
            "erro_tecnico": technical_error,
            "pontuacao": 0,
            "status": "ERRO_TECNICO",
            "falha_critica": "não avaliada; execução técnica não concluída",
        }
    else:
        try:
            observed = Catalogo.model_validate(normalized)
            comparison = compare_products(observed, expected)
            score = 2 if comparison["comparacao_exata"] else 1
            evaluation = {
                "schema_valido": True,
                **comparison,
                "pontuacao": score,
                "status": "A" if score == 2 else "P",
                "falha_critica": "não" if score == 2 else "a revisar",
            }
        except ValidationError as exc:
            evaluation = {
                "schema_valido": False,
                "comparacao_exata": False,
                "diferencas": [],
                "erro_schema": exc.errors(include_url=False),
                "pontuacao": 0,
                "status": "R",
                "falha_critica": "sim; saída não aderente ao schema obrigatório",
            }

    write_json(EVIDENCE_DIR / "avaliacao.json", evaluation)
    write_json(EVIDENCE_DIR / "ambiente.json", metadata)
    (EVIDENCE_DIR / "registro.md").write_text(
        build_record(metadata, evaluation), encoding="utf-8"
    )

    print(json.dumps(evaluation, ensure_ascii=False, indent=2))
    return 2 if technical_error is not None else 0


if __name__ == "__main__":
    raise SystemExit(main())
