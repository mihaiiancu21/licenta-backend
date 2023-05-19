from django.contrib.auth.models import User
from django.db import models


class UsersRank(models.Model):
    class Meta:
        db_table = "restapi_users_rank"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False,
        blank=False
    )

    overall_coding_points = models.IntegerField(
        null=False, blank=False, default=0, help_text="Total points"
    )

    total_problems_solved = models.IntegerField(
        null=False, blank=False, default=0, help_text="Total problems solved"
    )
