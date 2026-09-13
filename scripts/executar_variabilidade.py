"""Executa cinco prompts each three times for variability analysis."""

from __future__ import annotations

import contextlib
import csv
import hashlib
import io
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from scrapegraphai.graphs import SmartScraperGraph

from executar_ct01 import PROMPT as CT01_PROMPT
from executar_suite import (
    CASES,
    CONFIG_PATH,
    REVIEWERS,
    SOURCE_PATH,
    Catalogo,
    Case,
    evaluate_catalog,
    git_output,
    normalize_result,
    request_json,
    score,
    write_json,
)


TEAM_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = TEAM_ROOT / "evidencias" / "03-variabilidade"

VARIABILITY_CASES = {
    "CT-01": Case(
        "CT-01",
        "Caso esperado",
        CT01_PROMPT,
        Catalogo,
        "RQ-01;RQ-09;RQ-12",
        "Catálogo idêntico ao gabarito.",
        evaluate_catalog,
    ),
    "CT-03": CASES["CT-03"],
    "CT-06": CASES["CT-06"],
    "CT-10": CASES["CT-10"],
    "CT-12": CASES["CT-12"],
}


def canonical_hash(value: Any) -> str:
    """Calcula hash de uma saída JSON em representação canônica."""

    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run_repetition(
    case: Case,
    repetition: int,
    config: dict[str, Any],
    environment: dict[str, Any],
) -> dict[str, Any]:
    """Executa e registra uma repetição dedicada."""

    folder = EVIDENCE_ROOT / case.case_id / f"rep-{repetition:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    source = SOURCE_PATH.read_text(encoding="utf-8")
    primary, secondary = REVIEWERS[case.case_id]
    started_local = datetime.now().astimezone().isoformat(timespec="seconds")
    started = time.perf_counter()
    capture = io.StringIO()
    raw_result: Any = None
    execution_info: Any = None
    technical_error: str | None = None
    log_lines = [
        f"{started_local} BEGIN VAR-{case.case_id}-R{repetition}",
        f"model={environment['ollama_model']}",
        "temperature=0",
        "html_mode=true",
    ]

    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        try:
            graph = SmartScraperGraph(
                prompt=case.prompt,
                source=source,
                schema=case.schema,
                config=config,
            )
            raw_result = graph.run()
            execution_info = graph.get_execution_info()
            log_lines.append("graph_run_completed=true")
        except Exception as exc:  # noqa: BLE001
            technical_error = f"{type(exc).__name__}: {exc}"
            log_lines.append(f"technical_error={technical_error}")
            import traceback

            traceback.print_exc()

    duration = time.perf_counter() - started
    finished_local = datetime.now().astimezone().isoformat(timespec="seconds")
    normalized = normalize_result(raw_result)

    if technical_error:
        evaluation = {
            "schema_valido": False,
            "pontuacao": 0,
            "status": "ERRO_TECNICO",
            "falha_critica": False,
            "erro_tecnico": technical_error,
            "criterios": [],
        }
    else:
        try:
            validated = case.schema.model_validate(normalized)
            checks, critical = case.evaluator(validated)
            points, status = score(checks, critical)
            evaluation = {
                "schema_valido": True,
                "pontuacao": points,
                "status": status,
                "falha_critica": critical,
                "criterios": checks,
            }
        except Exception as exc:  # noqa: BLE001
            evaluation = {
                "schema_valido": False,
                "pontuacao": 0,
                "status": "R",
                "falha_critica": True,
                "erro_validacao": f"{type(exc).__name__}: {exc}",
                "criterios": [],
            }

    output_hash = canonical_hash(normalized)
    total_info = next(
        (
            item
            for item in (execution_info or [])
            if item.get("node_name") == "TOTAL RESULT"
        ),
        {},
    )
    metadata = {
        **environment,
        "caso_base": case.case_id,
        "repeticao": repetition,
        "inicio_local": started_local,
        "fim_local": finished_local,
        "duracao_segundos": duration,
        "saida_sha256_canonico": output_hash,
        "human_review_primary": primary,
        "human_review_secondary": secondary,
        "human_review_status": "pendente",
    }
    log_lines.extend(
        [
            f"duration_seconds={duration:.6f}",
            f"status={evaluation['status']}",
            f"output_sha256={output_hash}",
            f"{finished_local} END VAR-{case.case_id}-R{repetition}",
        ]
    )

    (folder / "entrada.html").write_text(source, encoding="utf-8")
    (folder / "prompt.txt").write_text(case.prompt + "\n", encoding="utf-8")
    write_json(folder / "config.json", config)
    write_json(folder / "schema.json", case.schema.model_json_schema())
    write_json(folder / "saida.json", normalized)
    write_json(folder / "avaliacao.json", evaluation)
    write_json(folder / "ambiente.json", metadata)
    write_json(folder / "execution_info.json", execution_info)
    (folder / "execucao.log").write_text(
        "\n".join(log_lines) + "\n\n" + capture.getvalue(), encoding="utf-8"
    )

    print(
        f"VAR-{case.case_id}-R{repetition}: {evaluation['status']} "
        f"({evaluation['pontuacao']}/2), {duration:.3f}s, {output_hash[:12]}",
        flush=True,
    )
    return {
        "caso_base": case.case_id,
        "repeticao": repetition,
        "pontuacao": evaluation["pontuacao"],
        "status": evaluation["status"],
        "duracao_segundos": round(duration, 3),
        "tokens": total_info.get("total_tokens", 0),
        "saida_sha256_canonico": output_hash,
        "evidencia": f"evidencias/03-variabilidade/{case.case_id}/rep-{repetition:02d}",
    }


def main() -> int:
    """Executa as quinze repetições e consolida variabilidade."""

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    ollama_version = request_json("http://localhost:11434/api/version")["version"]
    tags = request_json("http://localhost:11434/api/tags")["models"]
    model = next(item for item in tags if item["name"] == "llama3.2:latest")
    environment = {
        "scrapegraphai_commit": git_output("rev-parse", "HEAD"),
        "scrapegraphai_tag": git_output("describe", "--tags", "--exact-match"),
        "ollama_version": ollama_version,
        "ollama_model": model["name"],
        "ollama_model_digest": model["digest"],
    }

    results: list[dict[str, Any]] = []
    for case in VARIABILITY_CASES.values():
        for repetition in range(1, 4):
            results.append(run_repetition(case, repetition, config, environment))

    summary: dict[str, Any] = {
        "execucoes": len(results),
        "modelo": environment,
        "prompts": {},
    }
    for case_id in VARIABILITY_CASES:
        selected = [item for item in results if item["caso_base"] == case_id]
        hashes = [item["saida_sha256_canonico"] for item in selected]
        statuses = [item["status"] for item in selected]
        summary["prompts"][case_id] = {
            "saidas_distintas": len(set(hashes)),
            "hashes": hashes,
            "status": statuses,
            "estavel_byte_a_byte": len(set(hashes)) == 1,
            "todas_execucoes_aceitas": all(status == "A" for status in statuses),
        }

    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    write_json(EVIDENCE_ROOT / "RESUMO_VARIABILIDADE.json", summary)
    csv_path = EVIDENCE_ROOT / "RESUMO_REPETICOES.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
