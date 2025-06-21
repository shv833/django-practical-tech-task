from celery import shared_task
from django.core.mail import EmailMessage
from django.http import Http404
from main.models import CV
from main.utils import generate_cv_pdf


@shared_task
def send_cv_pdf_to_email(cv_id, to_email):
    try:
        cv = CV.objects.get(pk=cv_id)
    except CV.DoesNotExist:
        raise Http404("CV not found")
    pdf = generate_cv_pdf(cv)
    subject = f"CV for {cv.firstname} {cv.lastname}"
    body = f"Please find attached the CV for {cv.firstname} {cv.lastname}."
    email = EmailMessage(subject, body, to=[to_email])
    email.attach(f"cv_{cv.pk}.pdf", pdf, "application/pdf")
    email.send()
