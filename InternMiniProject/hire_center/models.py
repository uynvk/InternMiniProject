from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=88)
    contact = models.CharField(max_length=88)
