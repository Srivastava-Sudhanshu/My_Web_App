from django.contrib import admin
from .models import Student, Branch
from Accounts.models import Fees,StudentFeeDetails

# Register your models here.
admin.site.register([Student,Branch,Fees,StudentFeeDetails])