from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import re
from django.views.decorators.csrf import csrf_exempt
from Accounts.models import Fees,StudentFeeDetails
from Student_Portal.models import Student,Branch
from .forms import FeesForm,StudentFeeDetailsForm
from django.contrib import messages
from Student_Portal.forms import StudentForm
from datetime import datetime
#from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
#Accounts Home Screen
def index(request):
    if request.method == "GET":
        fees = Fees.objects.all()
        return render(request, 'Accounts/index.html',{"fees":fees})

#All Students with their fee records
def GetStudentFeeDetails(request):
    if request.method == "GET":
        student_fee_details = StudentFeeDetails.objects.all()
        for stud in student_fee_details:
            fees_details = Fees.objects.get(year = stud.student.current_year)
            stud.fees = fees_details.fee
            stud.due_amount = int(stud.fees) - int(stud.fees_paid)
        return render(request,'Accounts/studentfeedetails.html',{"student_fee_details":student_fee_details})

#Students by ID
def GetStudentFeeDetails_Id(request,id):
    if request.method == "GET":
        student_fee_details = StudentFeeDetails.objects.filter(student=id)
        for detail in student_fee_details:
            pass
        #fees_details = Fees.objects.filter(year = student_fee_details.student.current_year)
        return render(request,'Accounts/studentfeedetails.html',{"student_fee_details":student_fee_details})

#Pay Fee for a student
def PayFee(request,id):
    student = Student.objects.get(pk=id)
    current_year_fee = Fees.objects.filter(pk=student.current_year).first()
    fees_form = FeesForm(instance=current_year_fee)
    studentfee = StudentFeeDetails.objects.filter(student=id).first()
    from_post = False

    if request.method == "POST":
        form = StudentFeeDetailsForm(request.POST,instance=studentfee)
        from_post = True
        #If Fees is already paid not allow to pay
        if studentfee.fees_paid == current_year_fee.fee:
            messages.info(request,"Fees already paid")
            form = StudentFeeDetailsForm(instance = studentfee)
            form.fields['payment_status'].widget.attrs['disabled'] = True
        else:
            if form.is_valid():
                _form = form.save(commit=False)
                _form.fees_paid = int(_form.fees_paid) + int(_form.pay)
                _form.last_paid_amount = _form.pay
                _form.pay = 0
                _form.payment_date = datetime.now()
                if str(_form.fees_paid) == current_year_fee.fee or str(_form.fees_paid) > current_year_fee.fee:
                    _form.payment_status = True
                _form.save()
                messages.success(request, 'Fee Paid successfully')
                studentfee.due_amount = int(current_year_fee.fee) - int(studentfee.fees_paid)
                form = StudentFeeDetailsForm(instance = studentfee)
                form.fields['payment_status'].widget.attrs['disabled'] = True
    else:
        studentfee.due_amount = int(current_year_fee.fee) - int(studentfee.fees_paid)
        form = StudentFeeDetailsForm(instance = studentfee)
        form.fields['payment_status'].widget.attrs['disabled'] = True

    if(from_post):
        if(form.errors):
            print(form.errors)
    return render(request,'Accounts/payfee.html',{"form":form,"studfee":studentfee,"fees_form":fees_form})
