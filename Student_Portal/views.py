import re
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from Student_Portal.models import Student
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm

# Create your views here.
@csrf_exempt
def index(request):
    #portal_nam = {'portal':"IMSEC STUDENT ERP"}
    return render(request,'Student_Portal/index.html')

def GetAllStudents(request):
    if request.method == "GET":
        students = Student.objects.all()
        return render(request,'Student_Portal/allstudents.html',{'students':students})

def AddStudentScreen(request):
    context = {}
    context['form'] = StudentForm()
    return render(request,'Student_Portal/newstudent.html',context)

def AddNewStudent(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('/student/GetAllStudents')
    else:
       form = StudentForm()
    return render(request,'Student_Portal/allstudents.html',{'form':form})

def UpdateStudentScreen(request,id):
        student = Student.objects.get(id = id)
        form = StudentForm(request,instance = student)
        return render(request,'Student_Portal/editstudent.html',{"form":form, "student":student})

def UpdateStudent(request,id):
    student = get_object_or_404(Student, id = id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/student/GetAllStudents')
    else:
        return render(request,'Student_Portal/allstudents.html',{'form':form})

