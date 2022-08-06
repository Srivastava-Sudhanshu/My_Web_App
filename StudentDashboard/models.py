import email
from django.db import models
from Accounts.models import StudentFeeDetails
from Student_Portal.models import Student
# Create your models here.
class StudentDashboard(models.Model):
    #studentFeeDetails = models.ForeignKey(StudentFeeDetails,on_delete=models.CASCADE)
    #student = models.ForeignKey(Student,on_delete=models.CASCADE)
    loginid=models.CharField(max_length=10,default="")
    email=models.EmailField(max_length=255,default="")
    password=models.CharField(max_length=30,default="")
