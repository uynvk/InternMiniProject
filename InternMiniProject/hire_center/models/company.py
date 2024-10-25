from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=88)
    token = models.CharField(max_length=333, null=True)
