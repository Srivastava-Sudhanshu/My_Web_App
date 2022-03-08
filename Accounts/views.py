from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import re
from django.views.decorators.csrf import csrf_exempt
from Accounts.models import Fees,StudentFeeDetails
from Student_Portal.models import Student
from .forms import FeesForm,StudentFeeDetailsForm
from django.contrib import messages
from Student_Portal.forms import StudentForm

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "GET":
        fees = Fees.objects.all()
        return render(request, 'Accounts/index.html',{"fees":fees})

def GetStudentFeeDetails(request):
    if request.method == "GET":
        student_fee_details = StudentFeeDetails.objects.all()
        #student = Student.objects.all()
        total_fee=[]
        #count = 0
        for stud in student_fee_details:
            #count += 1
            fees_details = Fees.objects.get(year = stud.student.current_year)
            total_fee.append(fees_details.fee)
        return render(request,'Accounts/studentfeedetails.html',{"student_fee_details":student_fee_details,"total_fee":total_fee})
    
def PayFee(request,id):
    if request.method == "POST":
        studentfee = StudentFeeDetails.objects.get(student= id)
        form = StudentFeeDetailsForm(request.POST,instance=studentfee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fee Paid successfully')
            form = StudentFeeDetailsForm()
    else:
        student = Student.objects.get(pk=id)
        studform = StudentForm(instance=student)
        current_year_fee = Fees.objects.get(pk=student.current_year)
        current_year_fee_form = FeesForm(instance=current_year_fee)
        studentfee = StudentFeeDetails.objects.filter(student=student).first()
        form = StudentFeeDetailsForm(instance = studentfee)

    return render(request,'Accounts/payfee.html',{"studform":studform,"form":form,"current_year_fee_form":current_year_fee_form})

