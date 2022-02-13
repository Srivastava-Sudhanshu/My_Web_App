from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    roll_no  = models.CharField(max_length=10)
    year_of_admissn = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.name