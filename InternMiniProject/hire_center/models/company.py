import os

from django.db import models
from dotenv import load_dotenv

load_dotenv()


class Company(models.Model):
    name = models.CharField(max_length=88)
    secret_key = models.CharField(
        max_length=int(os.getenv("JWT_SECRET_CHAR_LEN")), null=True
    )
