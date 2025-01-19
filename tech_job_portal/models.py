# jobs/models.py

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)  # URL of the job listing

    def __str__(self):
        return f"{self.title} at {self.company}"
