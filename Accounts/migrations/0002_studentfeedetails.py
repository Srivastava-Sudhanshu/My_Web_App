# Generated by Django 4.0.2 on 2022-03-05 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Portal', '0005_student_current_year'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_paid', models.CharField(max_length=20)),
                ('due_amount', models.CharField(max_length=20)),
                ('payment_status', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_Portal.student')),
            ],
        ),
    ]
