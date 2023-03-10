from django.db import models
from django_fsm import FSMField


class Problem(models.Model):
    LEVEL_SCHOOL = "School"
    LEVEL_BASIC = "Basic"
    LEVEL_EASY = "Easy"
    LEVEL_MEDIUM = "Medium"
    LEVEL_HIGH = "High"

    LEVEl_CHOICES = (
        (LEVEL_SCHOOL, "School"),
        (LEVEL_BASIC, "Basic"),
        (LEVEL_EASY, "Easy"),
        (LEVEL_MEDIUM, "Medium"),
        (LEVEL_HIGH, "High")
    )

    STATUS_SOLVED = "Solved"
    STATUS_UNSOLVED = "Unsolved"
    STATUS_ATTEMPTED = "Attempted"
    STATUS_BOOKMARKED = "Bookmarked"

    STATUS_CHOICES = (
        (STATUS_SOLVED, "Solved"),
        (STATUS_UNSOLVED, "Unsolved"),
        (STATUS_ATTEMPTED, "Attempted"),
        (STATUS_BOOKMARKED, "Bookmarked"),
    )

    topic_type = models.ForeignKey(
        'restapi.ProblemTopics', on_delete=models.CASCADE, null=False,
        blank=False
    )

    title = models.CharField(
        max_length=250, help_text="Title of the problem", null=False,
        blank=False
    )

    description = models.TextField(
        help_text="Description of the problem", null=False, blank=False
    )

    restrictions = models.TextField(
        help_text="Restrictions of the problem or other mentions", null=False,
        blank=False
    )

    difficulty_level = FSMField(
        default=LEVEL_SCHOOL, choices=LEVEl_CHOICES,
        help_text="Level of the problem"
    )

    status = FSMField(
        default=STATUS_UNSOLVED, choices=STATUS_CHOICES,
        help_text="Status of the problem"
    )

    task_description = models.TextField(
        max_length=2048,
        help_text="Describe what user should do in the current problem",
        null=False, blank=False
    )

    points = models.IntegerField(
        default=100,
        help_text="How much points you can get if you solve the problem",
        null=False,
    )
