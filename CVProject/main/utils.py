from django.template.loader import render_to_string
import pdfkit
from main.models import CV


def generate_cv_pdf(cv: CV) -> bytes:
    html = render_to_string("cv_pdf.html", {"cv": cv})
    pdf = pdfkit.from_string(html, False)
    return pdf
