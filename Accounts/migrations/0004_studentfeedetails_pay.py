# Generated by Django 4.0.2 on 2022-03-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_studentfeedetails_due_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeedetails',
            name='pay',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
