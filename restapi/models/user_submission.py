from django.contrib.auth.models import User
from django.db import models


class UserSolutionSubmitted(models.Model):
    class Meta:
        db_table = "restapi_user_solution_submitted"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False,
        blank=False
    )

    problem = models.ForeignKey(
        'restapi.Problem', on_delete=models.CASCADE, null=False,
        blank=False, help_text="Give an example for current problem"
    )

    time_submitted = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=50, help_text="Status of the submission", null=False, blank=False
    )

    lang = models.CharField(
        max_length=20, help_text="Language", null=False, blank=False
    )

    test_cases = models.CharField(
        max_length=20, help_text="Test cases passed", null=False, blank=False
    )

    code_submitted = models.TextField(
        help_text="Code submitted", null=False, blank=False
    )

    points = models.IntegerField(
        null=False, blank=False, default=0, help_text="Total points obtained"
    )
