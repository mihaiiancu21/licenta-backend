# Generated by Django 4.1.6 on 2023-04-08 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapi', '0004_sendmailrepeatedfailure_usersubmission_rank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rank',
            new_name='UsersRank',
        ),
    ]
