from django.db import models


class ProblemExamples(models.Model):
    class Meta:
        db_table = "restapi_problem_examples"

    example_description = models.CharField(
        max_length=2048,
        help_text="Examples for problems", null=False,
        blank=False, default="Nu exista"
    )
