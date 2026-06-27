from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "kiril-bekulov-vinted-ai-automation-cv.pdf"

ACCENT = colors.HexColor("#0f766e")
ACCENT_DARK = colors.HexColor("#0a5550")
ACCENT_SOFT = colors.HexColor("#e4f4f1")
INK = colors.HexColor("#172326")
MUTED = colors.HexColor("#4f5f62")
LINE = colors.HexColor("#bed1cd")
FAINT = colors.HexColor("#e4eeeb")
WHITE = colors.white


def p(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"- {text}", style)


def make_styles():
    base = getSampleStyleSheet()
    return {
        "target": ParagraphStyle(
            "target",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=9.4,
            textColor=ACCENT_DARK,
            spaceAfter=1,
        ),
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=29,
            textColor=INK,
            spaceAfter=1,
        ),
        "headline": ParagraphStyle(
            "headline",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=13.4,
            textColor=ACCENT_DARK,
            spaceAfter=0,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.8,
            leading=9.8,
            textColor=ACCENT_DARK,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.8,
            leading=9.7,
            textColor=ACCENT_DARK,
            spaceBefore=5,
            spaceAfter=3.2,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.4,
            leading=9.3,
            textColor=INK,
            spaceAfter=0,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.6,
            leading=9,
            textColor=MUTED,
        ),
        "body_dark": ParagraphStyle(
            "body_dark",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.9,
            leading=9.4,
            textColor=INK,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.1,
            leading=8.4,
            textColor=MUTED,
        ),
        "date": ParagraphStyle(
            "date",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=7.4,
            leading=8.8,
            textColor=ACCENT_DARK,
            alignment=TA_RIGHT,
        ),
    }


def section_title(text, styles):
    return p(text.upper(), styles["h2"])


def card(title, body, styles):
    return [
        p(title, styles["h3"]),
        p(body, styles["small"]),
    ]


def job(title, org, date, bullets, styles, compact=False):
    heading = Table(
        [
            [
                [p(title, styles["h3"]), p(org, styles["small"])],
                p(date, styles["date"]),
            ]
        ],
        colWidths=[140 * mm, 36 * mm],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    rows = [heading]
    for item in bullets:
        rows.append(bullet(item, styles["body"]))
    return rows + [Spacer(1, 2 if compact else 3)]


def build_story(styles):
    story = []

    contact = p(
        "kiril@bekulov.com<br/>+370 621 25650<br/>linkedin.com/in/kiril711<br/>"
        "cv.bekulov.com<br/>Vilnius, Lithuania",
        styles["contact"],
    )
    header = Table(
        [
            [
                [
                    p("Automation Process Architecture | AI Workflow Design", styles["target"]),
                    p("Kiril Bekulov", styles["name"]),
                    p("Process automation specialist focused on reliable workflow logic", styles["headline"]),
                ],
                contact,
            ]
        ],
        colWidths=[130 * mm, 46 * mm],
        hAlign="LEFT",
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (1, 0), (1, 0), ACCENT_SOFT),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 6),
                ("LEFTPADDING", (1, 0), (1, 0), 6),
                ("RIGHTPADDING", (1, 0), (1, 0), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.extend([header, Spacer(1, 3)])

    story.append(section_title("Professional Summary", styles))
    story.append(
        p(
            "Senior automation developer with FinTech process discipline, RPA CoE delivery, "
            "custom C# platform work, and recent LLM/RPA integration experience. Strongest "
            "value is translating ambiguous human handoffs into deterministic process maps, "
            "data requirements, validation gates, fallback paths, and technical briefs that "
            "engineers and automated systems can execute safely.",
            styles["body_dark"],
        )
    )

    story.append(section_title("Role-Relevant Evidence", styles))
    match = Table(
        [
            [
                card("Reliable workflow logic", "RPA delivery across edge cases, retries, exception routes, human escalation, and audit-friendly process states.", styles),
                card("Data contracts and briefs", "SQL/VBA reporting, API PoCs, payload thinking, BA/PO-adjacent requirements, and developer-facing standards.", styles),
                card("Automation-first delivery", "100+ RPA solutions, 50+ operations automations, custom C#/.NET tooling, and LLM extensions to existing flows.", styles),
            ]
        ],
        colWidths=[58.5 * mm, 58.5 * mm, 58.5 * mm],
        hAlign="LEFT",
    )
    match.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fbfa")),
                ("BOX", (0, 0), (-1, -1), 0.25, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
            ]
        )
    )
    story.extend([match, Spacer(1, 3)])

    metrics = Table(
        [
            [
                [p("100+", ParagraphStyle("metric", fontName="Helvetica-Bold", fontSize=15, leading=15.5, textColor=ACCENT)), p("RPA solutions delivered or maintained", styles["small"])],
                [p("50+", ParagraphStyle("metric", fontName="Helvetica-Bold", fontSize=15, leading=15.5, textColor=ACCENT)), p("operations procedures automated before RPA", styles["small"])],
                [p("99%", ParagraphStyle("metric", fontName="Helvetica-Bold", fontSize=15, leading=15.5, textColor=ACCENT)), p("success rate on urgent award-winning automation work", styles["small"])],
            ]
        ],
        colWidths=[58.5 * mm, 58.5 * mm, 58.5 * mm],
        hAlign="LEFT",
    )
    metrics.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), ACCENT_SOFT),
                ("BOX", (0, 0), (-1, -1), 0.25, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.extend([metrics, Spacer(1, 2.5), section_title("Experience", styles)])

    story.extend(
        job(
            "Senior Developer, Robotic Process Automation",
            "FinTech Automation CoE",
            "Sep 2021 - Present",
            [
                "Implemented LLM-assisted extensions to classic RPA business logic, focusing on clear validation boundaries, exception handling, and human escalation when automation should not infer.",
                "Built extensive multi-bot Blue Prism automations and custom C#, JavaScript, and VB components to remove repeated developer effort and standardise delivery patterns.",
                "Contributed to reusable internal C# automation components that provide familiar workflow-orchestration features and support a transition toward in-house tooling.",
                "Supported BA/PO responsibilities during a resourcing gap: clarified stakeholder needs, structured requirements, and supported delivery follow-through.",
                "Established coding standards, QA practices, reusable development guidance, and quality-control chapter coordination for a growing automation team.",
                "Trained developers, resolved technical blockers, interviewed junior/mid-level candidates, supported Scrum ceremonies, and built PoCs for APIs, C# apps, VBA, Power Automate, and UiPath.",
            ],
            styles,
        )
    )

    story.append(section_title("Earlier Experience", styles))
    story.extend(
        job(
            "Developer, Robotic Process Automation",
            "FinTech Automation CoE",
            "Mar 2020 - Sep 2021",
            [
                "Delivered and maintained Blue Prism automations as a certified Blue Prism Developer and Solution Designer.",
                "Received a WU Star team award for two urgent automation projects delivered under exceptional time pressure, saving multiple FTEs and reaching 99% worked-item success.",
                "Expanded custom-code capability across C#, .NET Core, XAML, WPF, VBA, and cross-team troubleshooting support.",
            ],
            styles,
            compact=True,
        )
    )
    story.extend(
        job(
            "Database Administrator 2",
            "FinTech operations",
            "May 2019 - Mar 2020",
            [
                "Automated or redesigned 50+ recurring tasks using VBA and WinForms, connecting Microsoft Office workflows with mainframe, web, and backend FinTech applications.",
                "Designed Access/SQL reporting queries, compiled management reports, trained groups on SQL/VBA/Access/mainframe topics, and helped define office cooperation rules.",
            ],
            styles,
            compact=True,
        )
    )
    story.extend(
        job(
            "Database Administrator 1",
            "FinTech operations",
            "May 2018 - May 2019",
            [
                "Managed data in FinTech systems, built SQL reports, supported CIS-region business teams, and began automating recurring operational work with VBA.",
            ],
            styles,
            compact=True,
        )
    )

    story.append(section_title("Core Skills for This Role", styles))
    skills = Table(
        [
            [
                card("Process Architecture", "workflow mapping, decision trees, exception gates, fallback loops, control logic, documentation libraries", styles),
                card("Technical Interfaces", "C#, .NET, JavaScript, VB/VBA, SQL, Access, APIs, JSON/payload requirements, mainframe/web workflows", styles),
            ],
            [
                card("Automation and AI", "Blue Prism, UiPath, Power Automate, LLM/RPA integration, low-code orchestration, AI-assisted workflow design", styles),
                card("Delivery Leadership", "SAFe 5 Practitioner, Scrum support, BA/PO-adjacent requirements, QA standards, developer training and hiring", styles),
            ],
        ],
        colWidths=[87.5 * mm, 87.5 * mm],
        hAlign="LEFT",
    )
    skills.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fbfa")),
                ("BOX", (0, 0), (-1, -1), 0.25, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.extend([skills, Spacer(1, 2.5), section_title("Selected Proof Points", styles)])

    for item in [
        "<b>Reusable in-house automation platform:</b> helped build C# components that preserve familiar automation workflows while moving repeatable capabilities into internal tooling.",
        "<b>Applied AI tooling project:</b> shipped a playable five-level platformer prototype with a completed boss encounter, using LLM-assisted coding and generative-media workflows for art and music.",
        "<b>Business-to-engineering translator:</b> combines process mapping, SQL reporting, technical training, custom code, QA standards, and stakeholder-facing documentation.",
    ]:
        story.append(bullet(item, styles["body"]))

    story.append(section_title("Education, Certifications, Languages", styles))
    for item in [
        "<b>Education:</b> Cardiff University, BScEcon, Bachelor of Economics and Social Studies in International Relations and Politics",
        "<b>Certifications:</b> Blue Prism Developer AD01; Blue Prism Solution Designer ASD01; SAFe 5 Practitioner",
        "<b>Languages:</b> English C2; Russian C2; Lithuanian C1; French B2; Japanese B2",
    ]:
        story.append(p(item, styles["body"]))

    return story


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=11 * mm,
        bottomMargin=11 * mm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    template = PageTemplate(id="cv", frames=[frame])
    doc.addPageTemplates([template])
    doc.build(build_story(styles))
    print(OUT)


if __name__ == "__main__":
    main()
