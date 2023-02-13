from django.db import models
from django.contrib.auth.models import User


class Rank(models.Model):

    username = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False,
        blank=False
    )