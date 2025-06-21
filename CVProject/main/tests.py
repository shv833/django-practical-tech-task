from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from main.models import CV, RequestLog


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


class CVAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cv = CV.objects.create(
            firstname="Ada",
            lastname="Lovelace",
            skills=["Mathematics", "Programming"],
            projects=[
                {"name": "Analytical Engine", "description": "First computer algorithm"}
            ],
            bio="Mathematician and writer.",
            contacts={"email": "ada@example.com"},
        )

    def test_api_list(self):
        response = self.client.get("/api/cv/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_api_retrieve(self):
        response = self.client.get(f"/api/cv/{self.cv.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["firstname"], "Ada")

    def test_api_create(self):
        data = {
            "firstname": "Alan",
            "lastname": "Gorer)",
            "skills": ["Math"],
            "projects": [],
            "bio": "Pioneer",
            "contacts": {"email": "alan@example.com"},
        }
        response = self.client.post("/api/cv/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["firstname"], "Alan")

    def test_api_update(self):
        data = {
            "firstname": "Ada",
            "lastname": "Lovelace",
            "skills": ["Math", "CS"],
            "projects": [],
            "bio": "Updated bio",
            "contacts": {"email": "ada@example.com"},
        }
        response = self.client.put(f"/api/cv/{self.cv.pk}/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["bio"], "Updated bio")

    def test_api_delete(self):
        response = self.client.delete(f"/api/cv/{self.cv.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(CV.objects.filter(pk=self.cv.pk).exists())


class RequestLogMiddlewareTestCase(TestCase):
    def test_request_log_created_on_view(self):
        initial_count = RequestLog.objects.count()
        response = self.client.get(reverse("cv_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(RequestLog.objects.count(), initial_count + 1)
        log = RequestLog.objects.latest("timestamp")
        self.assertEqual(log.method, "GET")
        self.assertEqual(log.path, reverse("cv_list"))
