from asyncio.windows_events import NULL
from statistics import mode
from django.db import models
from Student_Portal.models import Student
# Create your models here.
class Fees(models.Model):
    year = models.CharField(max_length=10)
    fee = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.fee

class StudentFeeDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees_paid = models.CharField(max_length=20,default='0')
    payment_status = models.BooleanField()
    pay = models.CharField(max_length=20,default='0')
    last_paid_amount = models.CharField(max_length=20,default='0')
    payment_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.student.name