from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    roll_no  = models.CharField(max_length=10)
    year_of_admissn = models.CharField(max_length=4)
    current_year = models.CharField(max_length=4,default=1)
    email = models.EmailField(max_length=100,default="")

    def __str__(self) -> str:
        return self.name

class Branch(models.Model):
    branch = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.branch