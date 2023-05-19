from django.db import models


class SendMailRepeatedFailure(models.Model):
    class Meta:
        db_table = 'restapi_send_mail_repeated_failure'

    create_date = models.DateTimeField(auto_now_add=True)
    fail_traceback = models.TextField()
    arg_info = models.TextField()
