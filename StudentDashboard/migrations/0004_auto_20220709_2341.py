# Generated by Django 3.2.12 on 2022-07-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0003_studentdashboard_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdashboard',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentdashboard',
            name='studentFeeDetails',
        ),
    ]
