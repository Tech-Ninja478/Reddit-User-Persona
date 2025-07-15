# pdf_generator.py using reportlab

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.fonts import addMapping
import os

def save_persona_as_pdf(username, persona_txt_path):
    output_path = f"output/{username}_persona.pdf"
    doc = SimpleDocTemplate(output_path, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    Story = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Heading', fontSize=14, spaceAfter=6, leading=16, alignment=TA_LEFT, fontName="Helvetica-Bold"))
    styles.add(ParagraphStyle(name='Body', fontSize=12, spaceAfter=12, leading=16, alignment=TA_LEFT, fontName="Helvetica"))

    with open(persona_txt_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    current_heading = ""
    current_content = ""

    for line in lines:
        if line.startswith("###") or line.startswith("####"):
            if current_heading:
                Story.append(Paragraph(current_heading, styles["Heading"]))
                Story.append(Paragraph(current_content.strip(), styles["Body"]))
                Story.append(Spacer(1, 0.2 * inch))
            current_heading = line.strip("## ").strip()
            current_content = ""
        else:
            current_content += line + "\n"

    if current_heading:
        Story.append(Paragraph(current_heading, styles["Heading"]))
        Story.append(Paragraph(current_content.strip(), styles["Body"]))

    doc.build(Story)
    print(f"[✓] Persona PDF saved to: {output_path}")
