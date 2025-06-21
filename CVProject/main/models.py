from django.db import models


class CV(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    skills = models.JSONField(help_text="List of skills")
    projects = models.JSONField(help_text="List of projects")
    bio = models.TextField()
    contacts = models.JSONField(help_text="Contact information (email, phone, etc.)")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
