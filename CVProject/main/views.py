from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from main.models import CV
import pdfkit


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, "cv_list.html", {"cvs": cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, "cv_detail.html", {"cv": cv})


def cv_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    html = render_to_string("cv_pdf.html", {"cv": cv})
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="cv_{cv.pk}.pdf"'
    return response
