from django.db import models


class ProblemExamples(models.Model):
    class Meta:
        db_table = "restapi_problem_examples"

    example_description = models.CharField(
        max_length=2048,
        help_text="Examples for problems", null=False,
        blank=False
    )

    problem = models.ForeignKey(
        'restapi.Problem', on_delete=models.CASCADE, null=False,
        blank=False, help_text="Give an example for current problem"
    )
