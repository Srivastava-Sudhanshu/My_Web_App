# Generated by Django 4.0.2 on 2022-03-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Portal', '0002_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=0, max_length=100),
        ),
    ]
