from django.shortcuts import render, get_object_or_404
from main.models import CV


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, "cv_list.html", {"cvs": cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, "cv_detail.html", {"cv": cv})
