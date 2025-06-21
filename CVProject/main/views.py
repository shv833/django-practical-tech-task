from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, serializers
from main.models import CV, RequestLog
from main.tasks import send_cv_pdf_to_email
from main.utils import generate_cv_pdf, translate_cv_content


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, "cv_list.html", {"cvs": cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == "POST":
        if "email" in request.POST:
            email = request.POST.get("email")
            if email:
                send_cv_pdf_to_email.delay(cv.pk, email)
                messages.success(request, f"CV PDF is being sent to {email}!")
            else:
                messages.error(request, "Please provide a valid email address.")
        elif "translate" in request.POST:
            target_language = request.POST.get("language")
            if target_language:
                try:
                    translated_content, success = translate_cv_content(cv, target_language)
                    if success:
                        return JsonResponse(
                            {"success": True, "translated_content": translated_content}
                        )
                    else:
                        raise Exception("Didn't translate successfully")
                except Exception as e:
                    return JsonResponse({"success": False, "error": str(e)})
            else:
                messages.error(request, "Please select a language to translate to.")

    return render(request, "cv_detail.html", {"cv": cv})


def cv_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    pdf = generate_cv_pdf(cv)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="cv_{cv.pk}.pdf"'
    return response


def logs_view(request):
    logs = RequestLog.objects.order_by("-timestamp")[:10]
    return render(request, "logs.html", {"logs": logs})


def settings_view(request):
    return render(request, "settings.html")


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
