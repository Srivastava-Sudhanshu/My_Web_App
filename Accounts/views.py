from ast import pattern
import logging
from tkinter.ttk import Style
from xml.sax.handler import DTDHandler as dt
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import re
from django.views.decorators.csrf import csrf_exempt
from .models import Fees,StudentFeeDetails
from Student_Portal.models import Student,Branch
from .forms import FeesForm,StudentFeeDetailsForm
from django.contrib import messages
from Student_Portal.forms import StudentForm
from datetime import datetime
import xlwt
import My_Web_App.send_mails as send_mails

# Create your views here.
logger = logging.getLogger('django')
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
            fees_details = Fees.objects.get(year = detail.student.current_year)
            detail.fees = fees_details
            detail.due_amount = int(str(detail.fees)) - int(detail.fees_paid)
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

#This function exports the record to excel format
def export_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Feesrecord.xls"'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Fee Data')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["ID","Fees Paid","Not Due ?","Last Paid Amount","Name","Current Year","Email","Due"]

    for col_num in range(len(columns)):
        ws.write(row_num,col_num, columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()
    rows = StudentFeeDetails.objects.values_list('student','fees_paid','payment_status','last_paid_amount')
    for row in rows:
        row_num += 1
        row = list(row)
        rows_=(Student.objects.get(pk=row[0]))
        row.append(rows_.name)
        row.append(rows_.current_year)
        row.append(rows_.email)

        if(row[2] == False):
            current_year_fee = Fees.objects.filter(pk=rows_.current_year).first()
            rows_.dueamount = int(current_year_fee.fee) - int(row[1]) 
            font_style = xlwt.XFStyle()
            pattern = xlwt.Pattern()
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
            font_style.pattern = pattern
        else:
            rows_.dueamount = 0
        
        row.append(rows_.dueamount)
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response

def DueFeeNotification(request):
    try:
        logger = logging.getLogger('django')
        student_fee_details = StudentFeeDetails.objects.all()
        for stud in student_fee_details:
            fees_details = Fees.objects.get(year = stud.student.current_year)
            stud.fees = fees_details.fee
            stud.due_amount = int(stud.fees) - int(stud.fees_paid)
            if stud.due_amount > 0:
                logger.info("Calling send mails for due")
                status = send_mails.SendMailForDue(stud)
    except Exception as e:
        logger.info(f"Error: {e}")
        status = "Something went wrong!!"
        return status
    return HttpResponse(status)

    
