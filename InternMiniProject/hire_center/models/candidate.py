from django.db import models

from hire_center.models import Company


class Candidate(models.Model):
    name = models.CharField(max_length=88)
    contact = models.CharField(max_length=88)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
