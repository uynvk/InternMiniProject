from django.db import models

from hire_center.models import Company


class Api(models.Model):
    code = models.CharField(max_length=69, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
