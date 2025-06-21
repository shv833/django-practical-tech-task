from django.urls import path, include
from main.views import CVViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"cv", CVViewSet, basename="cv")

urlpatterns = [
    path("", include(router.urls)),
]
