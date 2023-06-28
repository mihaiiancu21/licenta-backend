# Generated by Django 4.1.6 on 2023-06-08 20:04

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0017_alter_usersolutionsubmitted_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersolutionsubmitted',
            name='status',
            field=django_fsm.FSMField(choices=[('Solved', 'Solved'), ('Unsolved', 'Unsolved'), ('Attempted', 'Attempted')], default='Unsolved', help_text='Status of the submission', max_length=50),
        ),
        migrations.DeleteModel(
            name='UsersProblemsStatus',
        ),
    ]
