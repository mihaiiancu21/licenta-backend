from django.conf import settings
from django.template.loader import get_template


# class MailUtils(object):
#
#     @staticmethod
#     def _get_html_template(template_path, template_data):
#         """
#         Return the HTML template rendered using template_data
#         :param template_path: the template path as a string (root path: /restapi/templates)
#         :param template_data: The template data as a JSON collection
#         :return: the HTML template rendered
#         """
#         mail_template = get_template(template_path)
#         return mail_template.render(template_data)
#
#     @classmethod
#     def send_user_awaiting_activation(cls, user, token):
#         to_address = [user.email]
#         subject = "BrainQuest Registration"
#         plain_text = "You registered on BrainQuest, now you must activate your account."
#         html_template = cls._get_html_template(
#             template_path="mails/auth/send_user_awaiting_activation.html",
#             template_data={'token': token,
#                            'frontend_url': settings.FRONTEND_URL,
#                            'user': user})
#
#         cls.send_mail(to_mail_address=to_address,
#                       subject=subject,
#                       message_text=plain_text,
#                       message_html=html_template)
#
#     @classmethod
#     def send_ask_reset_password(cls, user, token):
#         to_address = [user.email]
#         subject = "[Kermit portal] Ask for password reset"
#         plain_text = "You ask to Kermit to reset your password."
#         html_template = cls._get_html_template(
#             template_path="mails/auth/send_ask_reset_password.html",
#             template_data={'token': token,
#                            'frontend_url': settings.FRONTEND_URL,
#                            'user': user})
#
#         cls.send_mail(to_mail_address=to_address,
#                       subject=subject,
#                       message_text=plain_text,
#                       message_html=html_template)
#
#     @classmethod
#     def send_mail(
#             cls, subject, message_text, message_html, to_mail_address=None,
#             cc_mail_address=None, bcc_mail_address=None
#     ):
#         from_email = settings.FROM_EMAIL_PORTAL
#         email_admins = cls._get_email_admins()
#
#         # call celery async task
#
#         send_mail_task(subject=subject,
#                        message_text=message_text,
#                        message_html=message_html,
#                        from_email=from_email,
#                        to_mail_address=to_mail_address,
#                        cc_mail_address=cc_mail_address,
#                        bcc_mail_address=bcc_mail_address,
#                        reply_to=email_admins)
