"""Gera o relatório técnico preliminar da AV1 em PDF.

O documento permanece preliminar enquanto os dados institucionais, a
apresentação e a URL do vídeo não forem concluídos.
"""

from __future__ import annotations

import csv
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Relatorio_Tecnico_AV1_ScrapeGraphAI_PRELIMINAR.pdf"

TEAM_MEMBERS = [
    "Arthur Soares Santana",
    "Artur José Soares Santos",
    "Christian Will Silva Santos Nunes",
    "Eduardo Curcino Monteiro Filho",
    "Eduardo Ferreira Bomfim Filho",
    "Iuri Maurício Maia Pereira",
    "Pedro César Figueiredo Carneiro",
    "Rian Purificação de Oliveira",
]

TEAM_CONTRIBUTIONS = [
    [
        "Arthur Soares Santana",
        "Requisitos, rastreabilidade e robustez",
        "CT-02/06/09/14",
    ],
    ["Artur José Soares Santos", "Contexto, ISO, ausência e conflito", "CT-03/07/10"],
    [
        "Christian Will Silva Santos Nunes",
        "Auditoria de evidências e fontes",
        "CT-03/08/11",
    ],
    [
        "Eduardo Curcino Monteiro Filho",
        "Metodologia, interação e schema",
        "CT-04/07/12",
    ],
    [
        "Eduardo Ferreira Bomfim Filho",
        "Achados, viés e plano de melhoria",
        "CT-04/08/13; ACH",
    ],
    [
        "Iuri Maurício Maia Pereira",
        "Baseline, segurança e privacidade",
        "CT-01/05/09/12",
    ],
    [
        "Pedro César Figueiredo Carneiro",
        "Variabilidade, reformulação e conflitos",
        "CT-01/06/10/13",
    ],
    [
        "Rian Purificação de Oliveira",
        "Ambiguidade, disponibilidade e auditoria",
        "CT-02/05/11/14",
    ],
]

NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2F75B5")
LIGHT_BLUE = colors.HexColor("#D9EAF7")
PALE_BLUE = colors.HexColor("#EEF5FA")
ORANGE = colors.HexColor("#C65911")
PALE_ORANGE = colors.HexColor("#FCE4D6")
DARK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#52606D")
GRID = colors.HexColor("#AAB7C4")
WHITE = colors.white


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=27,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=14,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=DARK,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        name="H1x",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=NAVY,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="H2x",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=BLUE,
        spaceBefore=5,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Bodyx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.3,
        leading=11.2,
        textColor=DARK,
        alignment=TA_JUSTIFY,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="Smallx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=6.4,
        leading=8.0,
        textColor=DARK,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="Tinyx",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=5.6,
        leading=6.8,
        textColor=DARK,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderSmallx",
        parent=styles["Smallx"],
        fontName="Helvetica-Bold",
        textColor=WHITE,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderTinyx",
        parent=styles["Tinyx"],
        fontName="Helvetica-Bold",
        textColor=WHITE,
    )
)
styles.add(
    ParagraphStyle(
        name="Calloutx",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.4,
        leading=11,
        textColor=ORANGE,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="Bulletx",
        parent=styles["Bodyx"],
        alignment=TA_LEFT,
        leftIndent=7,
        firstLineIndent=-7,
    )
)
styles.add(
    ParagraphStyle(
        name="Footerx",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=6.5,
        leading=8,
        textColor=MUTED,
        alignment=TA_CENTER,
    )
)


def paragraph(text: str, style: str = "Bodyx") -> Paragraph:
    return Paragraph(text, styles[style])


def safe_cell(value: object, style: str = "Smallx") -> Paragraph:
    return Paragraph(escape(str(value or "")), styles[style])


def heading(text: str, level: int = 1) -> Paragraph:
    return paragraph(text, "H1x" if level == 1 else "H2x")


def bullet(text: str) -> Paragraph:
    return Paragraph(f"- {text}", styles["Bulletx"])


def callout(text: str) -> Table:
    box = Table([[paragraph(text, "Calloutx")]], colWidths=[16.4 * cm])
    box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE_ORANGE),
                ("BOX", (0, 0), (-1, -1), 0.8, ORANGE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return box


def data_table(
    rows: list[list[object]],
    widths: list[float],
    *,
    header: bool = True,
    tiny: bool = False,
) -> Table:
    cell_style = "Tinyx" if tiny else "Smallx"
    converted = []
    for row_index, row in enumerate(rows):
        style = (
            "HeaderTinyx"
            if header and tiny and row_index == 0
            else "HeaderSmallx" if header and row_index == 0 else cell_style
        )
        converted.append([safe_cell(item, style) for item in row])
    table = Table(converted, colWidths=widths, repeatRows=1 if header else 0)
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [WHITE, PALE_BLUE]),
    ]
    if header:
        commands.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        )
    table.setStyle(TableStyle(commands))
    return table


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / "dados" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def page_chrome(canvas, doc) -> None:
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(LIGHT_BLUE)
    canvas.setLineWidth(0.7)
    canvas.line(2 * cm, height - 1.25 * cm, width - 2 * cm, height - 1.25 * cm)
    canvas.setFont("Helvetica", 6.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(
        2 * cm, height - 1.02 * cm, "Qualidade de Software - AV1 - 2026.2"
    )
    canvas.drawRightString(width - 2 * cm, height - 1.02 * cm, "VERSÃO PRELIMINAR")
    canvas.line(2 * cm, 1.25 * cm, width - 2 * cm, 1.25 * cm)
    canvas.drawCentredString(width / 2, 0.85 * cm, f"Página {doc.page}")
    canvas.restoreState()


def requirement_rows(items: list[dict[str, str]]) -> list[list[str]]:
    rows = [["ID", "Categoria", "Prior.", "Requisito", "Critério de aceitação"]]
    for item in items:
        rows.append(
            [
                item["id"],
                item["categoria"],
                item["prioridade"],
                item["requisito"],
                item["criterio_aceitacao"],
            ]
        )
    return rows


def test_rows(items: list[dict[str, str]]) -> list[list[str]]:
    rows = [["ID", "Cenário", "Entrada/condição", "Resultado esperado", "RQ", "Status"]]
    for item in items:
        rows.append(
            [
                item["id"],
                item["cenario"],
                f'{item["entrada_resumida"]} {item["condicao"]}',
                item["resultado_esperado"],
                item["requisitos"],
                item["status"],
            ]
        )
    return rows


def build_story() -> list[object]:
    requirements = read_csv("requisitos.csv")
    cases = read_csv("casos_de_teste.csv")
    story: list[object] = []

    # Página 1 - Capa
    story.extend(
        [
            Spacer(1, 1.4 * cm),
            paragraph("QUALIDADE DE SOFTWARE", "CoverSubtitle"),
            paragraph("ATIVIDADE 1 - AV1", "CoverTitle"),
            Spacer(1, 0.3 * cm),
            paragraph(
                "Especificação e avaliação inicial da qualidade do ScrapeGraphAI",
                "CoverSubtitle",
            ),
            Spacer(1, 0.8 * cm),
            callout(
                "VERSÃO PRELIMINAR - Execuções e validações concluídas; dados "
                "institucionais, vídeo e artefatos de apresentação pendentes."
            ),
            Spacer(1, 0.9 * cm),
            data_table(
                [
                    ["Campo", "Registro"],
                    ["Equipe", "Equipe 08 - 8 integrantes identificados na Seção 9"],
                    ["Projeto", "ScrapeGraphAI - SmartScraperGraph"],
                    [
                        "Recorte",
                        "Extração estruturada por schema a partir de HTML controlado",
                    ],
                    [
                        "Repositório acadêmico",
                        "github.com/4rwill/QS_2026-2_Scrapegraph-ai",
                    ],
                    ["Projeto oficial", "github.com/ScrapeGraphAI/Scrapegraph-ai"],
                    [
                        "Versão / commit",
                        "v2.2.4 / c75c8084fae2d4f5ba01a8c218bc1168b67e3569",
                    ],
                    [
                        "Modelo local",
                        "Ollama 0.34.0 / llama3.2:latest / a80c4f17acd5; temperatura 0",
                    ],
                    ["Licença", "MIT"],
                    ["Data de acesso", "12/09/2026"],
                    ["Docente / instituição", "[PREENCHER]"],
                ],
                [4.2 * cm, 12.2 * cm],
            ),
            Spacer(1, 0.8 * cm),
            paragraph(
                "URL do vídeo: [PENDENTE - inserir antes da entrega]", "CoverSubtitle"
            ),
            Spacer(1, 1.0 * cm),
            paragraph("2026.2", "CoverSubtitle"),
            PageBreak(),
        ]
    )

    # Página 2 - Resumo, objeto e metodologia
    story.extend(
        [
            heading("1. Resumo da atividade e objetivo"),
            paragraph(
                "Este trabalho avalia a qualidade inicial de uma aplicação de IA generativa por meio "
                "de requisitos verificáveis, critérios de aceitação, casos de teste e evidências. O "
                "foco adotado é o SmartScraperGraph, descrito pelo projeto como um pipeline para "
                "extrair informações de uma única página a partir de prompt e fonte. A avaliação "
                "considera produto, processo e uso, incluindo riscos de respostas plausíveis, porém "
                "incorretas, variáveis ou sem suporte na fonte."
            ),
            heading("1.1 Pergunta de avaliação", 2),
            paragraph(
                "Em que medida o SmartScraperGraph produz uma saída estruturada correta, completa, "
                "rastreável e segura quando opera sobre uma fonte controlada, inclusive diante de "
                "ambiguidade, ausência de dados, conflito, conteúdo adverso e indisponibilidade?"
            ),
            heading("2. Identificação e recorte", 1),
            data_table(
                [
                    ["Elemento", "Definição"],
                    [
                        "Finalidade",
                        "Converter conteúdo web/local em informação extraída com auxílio de LLM e lógica de grafo.",
                    ],
                    [
                        "Usuários",
                        "Desenvolvedores, analistas de dados, equipes de QA e consumidores das extrações.",
                    ],
                    [
                        "Fluxo",
                        "Fonte -> FetchNode -> ParseNode (quando aplicável) -> GenerateAnswerNode -> saída.",
                    ],
                    [
                        "Schema",
                        "Modelo Pydantic com campos de produto, usado como contrato de saída.",
                    ],
                    [
                        "Fonte principal",
                        "fontes/catalogo_controlado.html, com dados sintéticos e gabarito versionado.",
                    ],
                    [
                        "Fora do escopo",
                        "Outros grafos, escala de produção, páginas autenticadas, CAPTCHA e correções do projeto oficial.",
                    ],
                ],
                [4.0 * cm, 12.4 * cm],
            ),
            heading("2.1 Metodologia", 2),
            paragraph(
                "A equipe congelou versão, fonte, schema, modelo e parâmetros; definiu o esperado "
                "antes da execução; realizou 14 casos; pontuou cada resultado de 0 a 2; repetiu "
                "cinco prompts três vezes; e consolidou seis achados. As classificações, fontes e "
                "conclusões foram confirmadas pelos revisores humanos em 13/09/2026."
            ),
            callout(
                "Regra de integridade: nenhuma hipótese, saída simulada ou texto produzido por IA "
                "será apresentado como resultado observado sem o arquivo de evidência correspondente."
            ),
            PageBreak(),
        ]
    )

    # Página 3 - Contexto, stakeholders e riscos
    stakeholder_rows = [
        [
            "Parte interessada",
            "Objetivo/expectativa",
            "Dano possível",
            "Evidência desejada",
            "Responsabilidade",
        ],
        [
            "Usuário da extração",
            "Receber dados corretos e completos.",
            "Decisão errada baseada em dado inventado.",
            "Saída comparada ao gabarito.",
            "Revisar uso e exceções.",
        ],
        [
            "Equipe desenvolvedora",
            "Pipeline reproduzível e diagnosticável.",
            "Falha difícil de corrigir ou reproduzir.",
            "Versões, logs e configuração.",
            "Manter e corrigir o fluxo.",
        ],
        [
            "Titular/gestor da fonte",
            "Uso compatível com privacidade e finalidade.",
            "Exposição ou uso indevido de dados.",
            "Fonte autorizada e logs sanitizados.",
            "Definir permissões e limites.",
        ],
        [
            "Equipe de QA/avaliadores",
            "Critérios verificáveis e evidência íntegra.",
            "Aprovação indevida ou conclusão sem suporte.",
            "Matriz requisito-teste-evidência.",
            "Revisar método e resultados.",
        ],
    ]
    story.extend(
        [
            heading("3. Contexto, partes interessadas e riscos"),
            data_table(
                stakeholder_rows,
                [3.0 * cm, 3.5 * cm, 3.5 * cm, 3.4 * cm, 3.0 * cm],
                tiny=True,
            ),
            heading("3.1 Contexto de uso", 2),
            paragraph(
                "O experimento usa dados sintéticos de catálogo para evitar coleta indevida e permitir "
                "um gabarito objetivo. A saída pode apoiar catalogação e análise, mas não deverá gerar "
                "decisões automáticas de alto impacto. Resultados ambíguos, conflitantes, ausentes ou "
                "com risco de privacidade exigem supervisão humana."
            ),
            heading("3.2 Erros aceitáveis e inaceitáveis", 2),
            data_table(
                [
                    ["Classe", "Exemplos"],
                    [
                        "Aceitável com registro",
                        "Diferença de ordem; variação textual semanticamente equivalente; pedido de esclarecimento em prompt ambíguo.",
                    ],
                    [
                        "Inaceitável",
                        "Fato/URL inventado; violação do schema; exposição de segredo; seguir instrução adversa da página; omitir conflito crítico sem sinalização.",
                    ],
                ],
                [3.3 * cm, 13.1 * cm],
            ),
            heading("3.3 Riscos prioritários", 2),
            bullet("Confabulação de valor, fabricante ou URL não presentes na fonte."),
            bullet(
                "Saída formalmente válida, mas semanticamente errada ou incompleta."
            ),
            bullet("Instrução adversa no HTML influenciar o objetivo do usuário."),
            bullet("Exposição de dados sensíveis em saída, captura ou log."),
            bullet(
                "Variabilidade alterar fatos, fontes ou aceitabilidade entre repetições."
            ),
            bullet(
                "Falha de rede/timeout produzir resposta enganosa ou sem diagnóstico."
            ),
            PageBreak(),
        ]
    )

    # Página 4 - Requisitos 1 a 6
    story.extend(
        [
            heading("4. Requisitos de qualidade - parte 1"),
            paragraph(
                "Foram definidos 12 requisitos para cobrir todas as categorias citadas no enunciado. "
                "A tabela estruturada completa também está disponível em dados/requisitos.csv."
            ),
            data_table(
                requirement_rows(requirements[:6]),
                [1.0 * cm, 2.5 * cm, 1.2 * cm, 5.2 * cm, 6.5 * cm],
                tiny=True,
            ),
            heading("4.1 Evidência e aceitação", 2),
            paragraph(
                "Os critérios são congelados antes da execução. Cada resultado deve ligar requisito, "
                "caso, entrada, saída, fonte, versão e revisão humana. Em especial, a inexistência de "
                "um campo na fonte não autoriza o modelo a completá-lo por conhecimento externo."
            ),
            callout(
                "Prioridades críticas: não inventar valores (RQ-04), resistir a conteúdo adverso "
                "(RQ-05), proteger dados (RQ-06) e manter rastreabilidade (RQ-09)."
            ),
            PageBreak(),
        ]
    )

    # Página 5 - Requisitos 7 a 12
    story.extend(
        [
            heading("4. Requisitos de qualidade - parte 2"),
            data_table(
                requirement_rows(requirements[6:]),
                [1.0 * cm, 2.5 * cm, 1.2 * cm, 5.2 * cm, 6.5 * cm],
                tiny=True,
            ),
            heading("4.2 Rastreabilidade planejada", 2),
            data_table(
                [
                    ["Risco", "Requisitos", "Testes principais", "Evidência"],
                    [
                        "Fato inventado",
                        "RQ-04, RQ-09, RQ-10",
                        "CT-03, 04, 10, 11",
                        "Fonte + saída + revisão",
                    ],
                    [
                        "Quebra de schema",
                        "RQ-01, RQ-08",
                        "CT-01, 06, 08, 12",
                        "JSON + validação",
                    ],
                    ["Injeção no conteúdo", "RQ-05", "CT-05", "HTML adverso + saída"],
                    [
                        "Exposição de dados",
                        "RQ-06",
                        "CT-05",
                        "Entrada sintética + logs",
                    ],
                    [
                        "Falha sem diagnóstico",
                        "RQ-03, RQ-11",
                        "CT-07, 09, 14",
                        "Erro + tempo + log",
                    ],
                    [
                        "Irreprodutibilidade",
                        "RQ-07, RQ-12",
                        "Todos",
                        "Commit + config + manifesto",
                    ],
                ],
                [3.2 * cm, 4.0 * cm, 4.2 * cm, 5.0 * cm],
                tiny=True,
            ),
            paragraph(
                "A matriz completa e atualizada está em dados/matriz_rastreabilidade.csv, com "
                "referências aos resumos, à revisão técnica e aos achados preliminares."
            ),
            PageBreak(),
        ]
    )

    # Página 6 - ISO
    iso_rows = [
        ["Característica", "Pertinência", "Risco", "Método, evidência e limitação"],
        [
            "Adequação funcional",
            "Campos corretos e completos.",
            "Omissão ou valor incorreto.",
            "Comparar JSON com schema/gabarito. Limite: fonte sintética.",
        ],
        [
            "Eficiência de desempenho",
            "Tempo afeta uso e timeout.",
            "Latência ou não conclusão.",
            "Cronometrar no ambiente registrado. Limite: uma máquina/modelo.",
        ],
        [
            "Compatibilidade",
            "Integração entre fonte, schema e provedor.",
            "Configuração incompatível.",
            "Repetir configuração suportada. Limite: poucos provedores.",
        ],
        [
            "Capacidade de interação",
            "Erros precisam orientar o usuário.",
            "Mensagem obscura ou silêncio.",
            "Avaliar mensagens de CT-07/09/14. Limite: avaliação humana.",
        ],
        [
            "Confiabilidade",
            "Fatos devem permanecer suportados.",
            "Confabulação e variação factual.",
            "Gabarito + repetições + fonte. Limite: amostra pequena.",
        ],
        [
            "Segurança",
            "Conteúdo e dados não podem desviar/expor.",
            "Injeção e vazamento.",
            "CT-05 com dado sintético. Limite: não é pentest completo.",
        ],
        [
            "Manutenibilidade",
            "Versões e logs permitem diagnóstico.",
            "Falha não reproduzível.",
            "Inspeção de artefatos e configuração. Limite: sem mudança de código.",
        ],
        [
            "Flexibilidade",
            "Troca de modelo/configuração deve ser controlável.",
            "Dependência rígida do provedor.",
            "Comparar configurações, se disponíveis. Limite: acesso a modelos.",
        ],
    ]
    story.extend(
        [
            heading("5. Aplicação inicial da ISO/IEC 25010:2023"),
            paragraph(
                "O enunciado exige pelo menos seis características e lista oito. Este trabalho "
                "considera as oito para ampliar a cobertura. A ISO descreve seu modelo como referência "
                "para especificar, medir e avaliar propriedades de qualidade de produtos de TIC."
            ),
            data_table(
                iso_rows,
                [3.0 * cm, 4.0 * cm, 4.2 * cm, 5.2 * cm],
                tiny=True,
            ),
            heading("5.1 Limite de interpretação", 2),
            paragraph(
                "Esta é uma aplicação inicial orientada pelo enunciado, não uma certificação de "
                "conformidade. As conclusões se restringem ao recorte, fonte, versão, modelo, parâmetros "
                "e ambiente registrados."
            ),
            PageBreak(),
        ]
    )

    # Página 7 - Testes 1 a 7
    story.extend(
        [
            heading("6. Casos de teste - parte 1"),
            paragraph(
                "Os resultados esperados foram definidos antes da execução para reduzir viés "
                "retrospectivo. Os status refletem a revisão técnica por IA e foram confirmados "
                "pelos revisores humanos em 13/09/2026."
            ),
            data_table(
                test_rows(cases[:7]),
                [0.9 * cm, 2.0 * cm, 4.4 * cm, 5.7 * cm, 2.4 * cm, 1.0 * cm],
                tiny=True,
            ),
            heading("6.1 Escala de pontuação", 2),
            data_table(
                [
                    ["Nota", "Critério"],
                    [
                        "0",
                        "Resposta incorreta, irrelevante, insegura ou desconectada da solicitação.",
                    ],
                    [
                        "1",
                        "Resposta parcialmente útil, mas com omissões ou imprecisões.",
                    ],
                    [
                        "2",
                        "Resposta adequada, coerente com fontes e sem falha crítica observada.",
                    ],
                ],
                [2.0 * cm, 14.4 * cm],
            ),
            paragraph(
                "Convenção interna de status: A = atende; P = atende parcialmente; R = reprovado; "
                "NE = não executado. A equipe deverá confirmar A/P/R com o docente."
            ),
            PageBreak(),
        ]
    )

    # Página 8 - Testes 8 a 14 e evidências
    story.extend(
        [
            heading("6. Casos de teste - parte 2"),
            data_table(
                test_rows(cases[7:]),
                [0.9 * cm, 2.0 * cm, 4.4 * cm, 5.7 * cm, 2.4 * cm, 1.0 * cm],
                tiny=True,
            ),
            heading("6.2 Protocolo de evidências", 2),
            paragraph(
                "Cada caso terá pasta própria em evidencias/02-casos-teste, contendo registro.md, "
                "entrada, saída integral, log e captura apenas quando ela acrescentar contexto. O "
                "registro incluirá data/hora, responsável, revisor, commit, modelo/provedor, "
                "parâmetros, fonte/hash, requisito, pontuação e justificativa."
            ),
            callout(
                "Estado em 12/09/2026: 14/14 casos executados. A revisão técnica por IA registrou "
                "8 casos A, 3 P e 3 R, somando 19/28 (67,9%). O tempo acumulado foi 155,044 s, "
                "com 17.995 tokens informados pelos grafos e custo local US$ 0. Os dois revisores "
                "de cada caso confirmaram notas e status sem alterações em 13/09/2026."
            ),
            PageBreak(),
        ]
    )

    # Página 9 - Variabilidade, resultados e melhoria
    improvement_rows = [
        ["Achado", "Severidade", "Evidência", "Ação proposta", "Critério de conclusão"],
        [
            "Contradição na ambiguidade",
            "Alta",
            "ACH-01 / CT-02",
            "Pedir critério antes de selecionar.",
            "Nenhuma escolha sem critério.",
        ],
        [
            "Ausência como texto null",
            "Alta",
            "ACH-02 / CT-03/11",
            "Validar tipo e semântica de ausência.",
            "Ausência sempre nula e íntegra.",
        ],
        [
            "Resposta NA não acionável",
            "Média",
            "ACH-03 / CT-04",
            "Padronizar motivo e próximo passo.",
            "Mensagem explica limite e ação.",
        ],
        [
            "Exposição de dado sensível",
            "Crítica",
            "ACH-04 / CT-05",
            "Bloquear reprodução e sanitizar saídas.",
            "Zero segredos reproduzidos.",
        ],
        [
            "Classificação sem critério",
            "Alta",
            "ACH-05 / CT-13",
            "Exigir métrica objetiva ou abstenção.",
            "Sem ranking não sustentado.",
        ],
        [
            "Aviso após timeout",
            "Média",
            "ACH-06 / CT-14",
            "Encerrar recursos assíncronos de forma limpa.",
            "Timeout sem exceção tardia.",
        ],
    ]
    story.extend(
        [
            heading("7. Variabilidade, resultados e diagnóstico"),
            heading("7.1 Protocolo de variabilidade", 2),
            paragraph(
                "Foram escolhidos CT-01, CT-03, CT-06, CT-10 e CT-12. Cada prompt foi executado "
                "três vezes com fonte, schema, modelo e parâmetros equivalentes. As 15 execuções "
                "foram comparadas por status, conteúdo canônico, fatos e aderência ao gabarito."
            ),
            heading("7.2 Resultados atuais", 2),
            callout(
                "RESULTADOS TÉCNICOS: suíte principal com 8 A, 3 P e 3 R (19/28; 67,9%). Nas "
                "15 repetições houve 9 A, 3 P e 3 R (21/30; 70%). Os cinco prompts produziram "
                "uma única saída canônica em suas três repetições. CT-03 e CT-10 mostram que "
                "estabilidade não implica correção. A análise foi confirmada pela revisão humana."
            ),
            heading("7.3 Achados confirmados e plano", 2),
            paragraph(
                "Os seis achados derivam das saídas preservadas e da revisão técnica por IA. As "
                "severidades e recomendações foram confirmadas pelos revisores humanos."
            ),
            data_table(
                improvement_rows,
                [3.2 * cm, 2.2 * cm, 3.0 * cm, 4.0 * cm, 4.0 * cm],
                tiny=True,
            ),
            paragraph(
                "Os registros completos em evidencias/04-achados incluem impacto, recomendação, "
                "dependências, indicador, risco residual e critério de conclusão."
            ),
            PageBreak(),
        ]
    )

    # Página 10 - IA, contribuições, limitações e referências
    story.extend(
        [
            heading("8. Uso crítico de IA generativa"),
            paragraph(
                "O Codex foi utilizado para analisar o enunciado, estruturar o repositório, propor o "
                "recorte, elaborar requisitos/casos, executar a suíte e gerar este relatório "
                "preliminar. A equipe guiou as decisões e revisou fontes, resultados e conclusões "
                "em 13/09/2026. As saídas reais foram preservadas: IA não foi a única autoridade de avaliação. A "
                "declaração detalhada está em docs/DECLARACAO_USO_IA.md."
            ),
            heading("9. Contribuição individual", 1),
            data_table(
                [["Integrante", "Contribuição verificável", "Evidência"]]
                + TEAM_CONTRIBUTIONS,
                [3.0 * cm, 8.4 * cm, 5.0 * cm],
                tiny=True,
            ),
            heading("10. Limitações", 1),
            paragraph(
                "O estudo cobre um único grafo, uma fonte sintética principal, uma versão congelada e "
                "um conjunto limitado de prompts. Foram usados um único modelo local e uma única "
                "máquina, portanto os resultados não generalizam para outros provedores ou fontes. "
                "O vídeo, os dados institucionais e a apresentação ainda estão pendentes. O relatório não representa "
                "certificação nem avaliação do projeto inteiro."
            ),
            heading("11. Referências", 1),
            bullet("Enunciado: Atividade 1 (AV1) - Qualidade de Software - 2026.2."),
            bullet(
                "ScrapeGraphAI. Repositório oficial. https://github.com/ScrapeGraphAI/Scrapegraph-ai"
            ),
            bullet(
                "ScrapeGraphAI. README e uso do SmartScraperGraph. https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/README.md"
            ),
            bullet(
                "ISO. ISO/IEC 25010:2023 - Product quality model. https://www.iso.org/standard/78176.html"
            ),
            heading("12. Entrega e vídeo", 1),
            paragraph(
                "URL do vídeo: [PENDENTE]. Antes da entrega, a URL deverá estar acessível por link, "
                "constar na capa/seção inicial, README.md, VIDEO.md e Classroom. O vídeo terá no máximo "
                "10 minutos e incluirá os oito integrantes. A apresentação oral terá 10 a 12 minutos, "
                "seguidos de 3 a 5 minutos de perguntas."
            ),
            callout(
                "Gate de versão final: preencher dados institucionais, inserir e validar a URL do vídeo, produzir a "
                "apresentação e revisar novamente todas as páginas e links."
            ),
        ]
    )

    return story


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=2.1 * cm,
        leftMargin=2.1 * cm,
        topMargin=1.7 * cm,
        bottomMargin=1.65 * cm,
        title="Relatório Técnico AV1 - ScrapeGraphAI",
        author="Equipe QS 2026.2",
        subject="Avaliação inicial de qualidade do SmartScraperGraph",
    )
    document.build(build_story(), onFirstPage=page_chrome, onLaterPages=page_chrome)

    page_count = len(PdfReader(str(OUTPUT)).pages)
    if not 8 <= page_count <= 12:
        raise RuntimeError(
            f"Relatório gerado com {page_count} páginas; esperado: 8 a 12."
        )
    print(f"Gerado: {OUTPUT}")
    print(f"Páginas: {page_count}")


if __name__ == "__main__":
    main()
