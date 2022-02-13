from django.shortcuts import render
from django.http import HttpResponse
from . import serializer
from json import dumps

# Create your views here.

def index(request):
    #portal_nam = {'portal':"IMSEC STUDENT ERP"}
    return render(request,'Student_Portal/index.html')

def GetAllStudents(request):
    if request.method == "GET":
        all_students =  dict(serializer.GetAllStudents())
        #all_students = dumps(all_students)
        return render(request,'Student_Portal/allstudents.html',context=all_students)

