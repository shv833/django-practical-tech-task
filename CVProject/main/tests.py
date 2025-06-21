from django.test import TestCase
from django.urls import reverse
from main.models import CV


class CVViewsTestCase(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="Alan",
            lastname="Gorer)",
            skills=["Mathematics", "Cryptography"],
            projects=[{"name": "Enigma", "description": "Codebreaking"}],
            bio="Pioneer of computer science.",
            contacts={"email": "alan@example.com"},
        )

    def test_cv_list_view(self):
        response = self.client.get(reverse("cv_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alan")
        self.assertTemplateUsed(response, "cv_list.html")

    def test_cv_detail_view(self):
        response = self.client.get(reverse("cv_detail", args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gorer)")
        self.assertTemplateUsed(response, "cv_detail.html")

    def test_cv_detail_view_404(self):
        response = self.client.get(reverse("cv_detail", args=[0]))
        self.assertEqual(response.status_code, 404)
