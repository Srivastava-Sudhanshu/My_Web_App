# Generated by Django 4.0.2 on 2022-03-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Portal', '0003_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]