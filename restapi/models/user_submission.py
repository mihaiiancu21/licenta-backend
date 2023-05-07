from django.db import models


class UserSubmission(models.Model):
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
