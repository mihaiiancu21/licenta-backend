import json
import logging
import traceback

from django.core.mail import EmailMultiAlternatives

from restapi.models.mail import SendMailRepeatedFailure

logger = logging.getLogger(__name__)


def send_mail_task(
        subject, message_text, message_html, from_email, to_mail_address=None,
        cc_mail_address=None, bcc_mail_address=None, reply_to=None
):
    """
    Start a celery task to send an email with message_text or message_html content from
    from_email to to_mail_address

    :param subject: Subject of the email
    :param message_text: Text message to send in case of the client cannot read HTML
    :param message_html: HTML message to send
    :param from_email: The email from
    :param to_mail_address: Target email to send the message
    :param cc_mail_address: Target emails to add in cc
    :param bcc_mail_address: Target emails to add in bcc
    :param reply_to: List of email that will be placed in the reply part
    """
    try:
        if to_mail_address is not None or cc_mail_address is not None or \
                bcc_mail_address is not None:
            send_mail(
                subject=subject,
                message_text=message_text,
                message_html=message_html,
                from_email=from_email,
                to_mail_address=to_mail_address,
                cc_mail_address=cc_mail_address,
                bcc_mail_address=bcc_mail_address,
                reply_to=reply_to
            )
        else:
            logger.warning(
                "Tried to send an e-mail without destination addresses "
                "(either in to, cc or bcc)"
            )
            return
    except Exception as exc:
        logger.error(f"An error occurred: {str(traceback.format_exc())}")

        SendMailRepeatedFailure.objects.create(
            fail_traceback=traceback.format_exc(),
            arg_info=json.dumps(
                {
                    "subject": subject,
                    "message_text": message_text,
                    "message_html": message_html,
                    "from_email": from_email,
                    "to_mail_address": to_mail_address,
                    "reply_to": reply_to
                }
            )
        )


def send_mail(
        subject, message_text, message_html, from_email, to_mail_address=None,
        cc_mail_address=None,
        bcc_mail_address=None, reply_to=None
):
    """
    Send an email with message_text or message_html content from from_email to to_mail_address
    :param subject:
    :param message_text:
    :param message_html:
    :param from_email:
    :param to_mail_address:
    :param cc_mail_address:
    :param bcc_mail_address:
    :param reply_to:
    :return:
    """
    if to_mail_address is None and cc_mail_address is None and bcc_mail_address is None:
        logger.warning(
            "Tried to send an e-mail without destination addresses "
            "(either in to, cc or bcc)"
        )
        return
    # We add the name of the instance within the mail
    subject_with_name = f"[BrainQuest] {subject}"
    msg = EmailMultiAlternatives(
        subject_with_name, message_text, from_email,
        to_mail_address, cc=cc_mail_address, bcc=bcc_mail_address, reply_to=reply_to
    )
    if message_html is not None:
        msg.attach_alternative(message_html, "text/html")

    msg.send()
