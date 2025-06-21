from django.db import models
from django.utils import timezone


class CV(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    skills = models.JSONField(help_text="List of skills")
    projects = models.JSONField(help_text="List of projects")
    bio = models.TextField()
    contacts = models.JSONField(help_text="Contact information (email, phone, etc.)")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class RequestLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_string = models.TextField(blank=True)
    remote_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} {self.method} {self.path}"
