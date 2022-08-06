import json
import logging
import math
import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from StudentDashboard.forms import StudentDashboardForm,StudentDashboardLoginForm
from Student_Portal.models import Student
import My_Web_App.send_mails as send_mails
from Accounts.models import StudentFeeDetails
from Login.views import SetSession
from My_Web_App.settings import GENERATE_OTP_TEMPLATE,STUDENT_DASHBOARD_LOGIN
from . models import StudentDashboard

OTP=""
# Create your views here.
def index(request):
    #branches = Branch.objects.all()
    return render(request,'StudentDashboard/index.html')

def login(request):
    try:
        if request.method == 'POST':
            form = StudentDashboardLoginForm(request.POST)
            if form.is_valid():
                Loginid = request.POST.get("loginid")
                Password = request.POST.get("password")
                if student_login := StudentDashboard.objects.filter(loginid=Loginid, password=Password).values():
                    SetSession(request, Loginid)
                    return redirect('dashboard')
                else:
                    messages.error(request, "Invalid Credentials!")
            else:
                print(form.errors)
                messages.error(request, form.errors)
        form = StudentDashboardLoginForm()
        return render(request, 'StudentDashboard/login.html', {'form': form})
    except Exception as e:
        print(e)
 
def signup(request):
    try:
        if request.method == 'POST':
            Loginid = request.POST.get("loginid")
            Password = request.POST.get("password")
            if student_login := StudentDashboard.objects.filter(loginid=Loginid):
                messages.error(request, "This user already exists")
            else:
                form = StudentDashboardForm(request.POST)
                if form.is_valid():
                    _form = form.save(commit=False)
                    try:
                        students = Student.objects.get(roll_no=_form.loginid)
                    except Student.DoesNotExist:
                        students = None
                    global OTP
                    OTP = ""
                    if students is None:
                        messages.error(request, "The given roll no as LoginId does not exist")
                    else:
                        _form.save()
                        return redirect('login')
                else:
                    print(form.errors)
                    messages.error(request, form.errors)
        form = StudentDashboardForm()
        return render(request, 'StudentDashboard/signup.html', {'form': form})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")

def generateOTP(request):
    logger = logging.getLogger('django')
    email = request.GET.get('email')
    students = Student.objects.all()
    global OTP
    OTP = ""
    for student in students:
        if email == student.email:
            digits = "0123456789"
            for _ in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            student.purposeobject = OTP
            student.mailsubject = 'OTP!'
            student.emailTemplate = GENERATE_OTP_TEMPLATE
            logger.info("Calling send mails for OTP")
            status = send_mails.SendMail(student)
            if status != True:
                return False
            break
    return HttpResponse(json.dumps({'OTP': OTP}), content_type="application/json")

def dashboard(request):
    if "Islogin" not in request.session:
        return redirect(STUDENT_DASHBOARD_LOGIN)
    loginid = request.session["Islogin"]
    student_details = StudentFeeDetails.objects.select_related().all().filter(student__roll_no = loginid)
    for stud in student_details:
        stud
    return HttpResponse(f"Welcome {student_details[0]}")
    
            