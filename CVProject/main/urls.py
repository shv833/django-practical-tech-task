from django.urls import path
from main.views import cv_list, cv_detail, cv_pdf, logs_view


urlpatterns = [
    path("", cv_list, name="cv_list"),
    path("cv/<int:pk>/", cv_detail, name="cv_detail"),
    path("cv/<int:pk>/pdf/", cv_pdf, name="cv_pdf"),
    path("logs/", logs_view, name="logs"),
]
