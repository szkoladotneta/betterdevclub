#!/usr/bin/env python3
"""Generate a condensed B2B offer PDF for the AI-Native Dev Team workshop."""

from pathlib import Path
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "oferta-ai-native-dev-team.pdf"
LOGO_CANDIDATES = [
    ROOT / "assets" / "logo-bdc.webp",
    ROOT / "assets" / "logo-szkoladotneta.png",
]


def _register_font() -> tuple[str, str]:
    """Register Unicode-friendly regular/bold fonts if available."""
    font_pairs = [
        (
            Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        ),
        (
            Path("/Library/Fonts/Arial.ttf"),
            Path("/Library/Fonts/Arial Bold.ttf"),
        ),
    ]

    for regular_path, bold_path in font_pairs:
        if regular_path.exists() and bold_path.exists():
            pdfmetrics.registerFont(TTFont("OfferFont", str(regular_path)))
            pdfmetrics.registerFont(TTFont("OfferFont-Bold", str(bold_path)))
            return "OfferFont", "OfferFont-Bold"

    return "Helvetica", "Helvetica-Bold"


def _bullet_list(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=0) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=12,
        bulletFontName=style.fontName,
        bulletFontSize=9,
    )


def build_pdf(output_path: Path) -> None:
    font_name, font_bold = _register_font()
    styles = getSampleStyleSheet()

    title = ParagraphStyle(
        "title",
        parent=styles["Heading1"],
        fontName=font_name,
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0A0F1E"),
        spaceAfter=6,
        alignment=TA_LEFT,
    )
    subtitle = ParagraphStyle(
        "subtitle",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#374151"),
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "h2",
        parent=styles["Heading2"],
        fontName=font_bold,
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1D4ED8"),
        spaceBefore=6,
        spaceAfter=3,
    )
    body = ParagraphStyle(
        "body",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=2,
    )
    small = ParagraphStyle(
        "small",
        parent=body,
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#4B5563"),
    )
    strong = ParagraphStyle(
        "strong",
        parent=body,
        fontName=font_bold,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#111827"),
        spaceAfter=1,
    )

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=12 * mm,
        bottomMargin=10 * mm,
        title="Oferta B2B - AI-Native Dev Team",
        author="Better Dev Club",
    )

    story = []

    for logo_path in LOGO_CANDIDATES:
        if logo_path.exists():
            try:
                logo = Image(str(logo_path))
                logo.hAlign = "LEFT"
                logo._restrictSize(34 * mm, 14 * mm)
                story.append(logo)
                story.append(Spacer(1, 3))
                break
            except Exception:
                continue

    story.append(Paragraph("AI-Native Dev Team", title))
    story.append(
        Paragraph(
            "1-dniowy warsztat dla zespołów .NET, który zamienia przypadkowe użycie Copilota w spójny workflow AI.",
            subtitle,
        )
    )

    meta = Table(
        [
            ["Format", "On-site lub online (Zoom / Teams)"],
            ["Czas", "1 dzień (8h) + follow-up po 3 tygodniach"],
            ["Prowadzący", "2x Microsoft MVP: .NET + DevOps"],
            ["Dla kogo", "Działy IT i software house'y pracujące w .NET"],
        ],
        colWidths=[30 * mm, 148 * mm],
    )
    meta.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1F2937")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#BFDBFE")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFDBFE")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(meta)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Dlaczego firmy kupuja ten warsztat", h2))
    story.append(
        _bullet_list(
            [
                "Zakupione licencje Copilot nie dowożą zwrotu i trudno obronić budżet.",
                "Każdy developer pracuje inaczej, a seniorzy nie mają wspólnej checklisty review.",
            ],
            body,
        )
    )

    story.append(Paragraph("Co dostajecie", h2))
    story.append(
        _bullet_list(
            [
                "Discovery Call + Stack Questionnaire przed warsztatem.",
                "8h warsztatu hands-on na przygotowanych przykładach .NET (sandbox).",
                "Pakiet wdrożeniowy: szablony, checklisty AI review, repozytorium i nagranie.",
                "1h follow-up Q&A live po 3 tygodniach.",
            ],
            body,
        )
    )

    story.append(Paragraph("Efekt biznesowy", h2))
    story.append(
        _bullet_list(
            [
                "Spójny i deterministyczny workflow AI dla całego zespołu.",
                "Lepsza jakość PR-ów oraz realny plan poprawy ROI z licencji Copilot.",
            ],
            body,
        )
    )

    story.append(Paragraph("Warianty współpracy (ceny netto)", h2))
    pricing = Table(
        [
            ["Nazwa", "Cena", "Dla kogo"],
            ["Public Workshop", "485 PLN / os.", "Wersja 4h dla mniejszych zespołów."],
            ["Online Expert", "10 000 PLN", "Warsztat 8h online do 16 osób + materiały + follow-up."],
            ["On-site Pro", "Wycena indywidualna", "Pełny zakres stacjonarnie u klienta."],
        ],
        colWidths=[36 * mm, 34 * mm, 108 * mm],
    )
    pricing.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("FONTSIZE", (0, 0), (-1, -1), 8.3),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E5E7EB")),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1F2937")),
                ("FONTNAME", (0, 0), (-1, 0), font_bold),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#D1D5DB")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#E5E7EB")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(pricing)
    story.append(Spacer(1, 3))

    story.append(Paragraph("Model realizacji", h2))
    story.append(
        Paragraph(
            "Start projektu zwykle w 3-4 tygodnie od podpisania umowy. Przed wysłaniem finalnej wyceny "
            "prowadzimy bezpłatny Discovery Call (45 min), aby dopasować zakres i wariant do skali zespołu.",
            body,
        )
    )

    story.append(Paragraph("Programy dodatkowe", h2))
    story.append(Paragraph("Founding Partner Program", strong))
    story.append(
        _bullet_list(
            [
                "Pierwsi 3 klienci otrzymują Founding Partner Bonus Bundle.",
                "Dodatkowa 1h sesja strategiczna dla managementu oraz drugi follow-up Q&A po ok. 3 miesiącach w zamian za case study i logo.",
            ],
            body,
        )
    )
    story.append(Paragraph("Quarterly AI Refresh — 5 000 PLN netto / kwartał", strong))
    story.append(
        _bullet_list(
            [
                "2h sesja live co 3 miesiące.",
                "Nowe funkcje Copilot/GPT/Claude, przegląd plików instrukcji oraz Q&A dla nowych pracowników.",
            ],
            body,
        )
    )

    story.append(
        Paragraph(
            f"<b>Kontakt:</b> kontakt@betterdevclub.pl | Better Dev Club | Faktura B2B | Data oferty: {date.today().isoformat()}",
            small,
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build_pdf(OUTPUT)
    print(f"PDF generated: {OUTPUT}")
