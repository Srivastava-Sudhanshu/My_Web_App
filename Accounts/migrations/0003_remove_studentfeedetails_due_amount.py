# Generated by Django 4.0.2 on 2022-03-06 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_studentfeedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfeedetails',
            name='due_amount',
        ),
    ]