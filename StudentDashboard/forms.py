from dataclasses import field, fields
from turtle import width
from unicodedata import name
from django.forms import ModelForm, TextInput
from StudentDashboard.models import StudentDashboard
class StudentDashboardForm (ModelForm):
    class Meta:
        model = StudentDashboard
        fields = ["loginid","password","email"]

class StudentDashboardLoginForm (ModelForm):
    class Meta:
        model = StudentDashboard
        fields = ["loginid","password"]

