from django.urls import path
from main.views import cv_list, cv_detail


urlpatterns = [
    path("", cv_list, name="cv_list"),
    path("<int:pk>/", cv_detail, name="cv_detail"),
]
