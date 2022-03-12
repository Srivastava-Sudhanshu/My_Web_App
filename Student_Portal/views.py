from email import message
from pyexpat.errors import messages
import re
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

from Student_Portal.models import Student, Branch
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm
from django.contrib import messages
import xlwt

# Create your views here.
@csrf_exempt
#This function navigates Home Screen
def index(request):
    #branches = Branch.objects.all()
    return render(request,'Student_Portal/index.html')

#This function gets all Students 
def GetAllStudents(request):
    if request.method == "GET":
        students = Student.objects.all()
        total = students.count()
        branches = Branch.objects.all().order_by('branch')
        return render(request,'Student_Portal/allstudents.html',{'students':students,'branches':branches, 'total':total})

#This function gets all Students based on branch filter
def GetAllStudentsBranchwise(request,branch):
    if request.method == "GET":
        students = Student.objects.all().filter(branch = branch)
        total = students.count()
        branches = Branch.objects.all().order_by('branch')
        return render(request,'Student_Portal/allstudents.html',{'students':students,'branches':branches,'branch':branch, 'total':total})

#This function navigates Add Student Screen
def AddStudentScreen(request):
    context = {}
    context['form'] = StudentForm()
    return render(request,'Student_Portal/newstudent.html',context)

#This function adds New Student
def AddNewStudent(request):
    from_post = False

    if request.POST:
        from_post = True
        form = StudentForm(request.POST)
        if form.is_valid():   
            form.save()
            messages.success(request, 'Added successfully')
            form = StudentForm()
            return HttpResponseRedirect(reverse('admin:index')) 
    else:
       form = StudentForm()
    if from_post:
        if form.errors:
            print(form.errors)
    return render(request,'Student_Portal/newstudent.html',{'form':form})

#This function updates the record of existing Student
def UpdateStudent(request,id):
    from_post = False
    if request.POST:
        from_post = True
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated successfully')
            form = StudentForm()
    else:
        student = Student.objects.get(pk = id)
        form = StudentForm(instance=student)
        #form.fields['payment_status'].widget.attrs['disabled'] = True
        form.fields['year_of_admissn'].widget.attrs['readonly'] = True
    if from_post:
        if form.errors:
            print(form.errors)
    return render(request,'Student_Portal/editstudent.html',{"form":form})

#This function exports the record to excel format
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Studentrecords.xls"'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Student Data')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["ID","Name","Branch","Roll No","Year Of Addmission"]

    for col_num in range(len(columns)):
        ws.write(row_num,col_num, columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()
    rows = Student.objects.all().values_list()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response
