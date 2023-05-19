from django.db import models
from django_fsm import FSMField


class ProblemTopics(models.Model):
    class Meta:
        db_table = "restapi_problem_topics"

    TOPIC_ARRAY = "Arrays"
    TOPIC_STRINGS = "Strings"
    TOPIC_MATRIX = "Matrix"
    TOPIC_NUMBERS = "Numbers"
    TOPIC_SORTING = "Sorting"

    TOPIC_CHOICES = (
        (TOPIC_ARRAY, "Arrays"),
        (TOPIC_STRINGS, "Strings"),
        (TOPIC_MATRIX, "Matrix"),
        (TOPIC_NUMBERS, "Numbers"),
        (TOPIC_SORTING, "sorting"),
    )

    topic = FSMField(
        default=TOPIC_ARRAY, choices=TOPIC_CHOICES,
        help_text="Topic of the problem"
    )
