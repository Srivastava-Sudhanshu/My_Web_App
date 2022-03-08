from dataclasses import field, fields
from turtle import width
from unicodedata import name
from django.forms import ModelForm, TextInput
from Student_Portal.models import Student
class StudentForm (ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'name' : TextInput(attrs={
                'style': 'width : 200px;',
                'placeholder':'Enter Name' 
            }),
            'branch' : TextInput(attrs={
                'style': 'width : 200px;',
                'placeholder':'Enter Branch' 
            }),
            'roll_no' : TextInput(attrs={
                'style': 'width : 200px;',
                'placeholder':'Enter RollNo' 
            }),
            'email' : TextInput(attrs={
                'style': 'width : 200px;',
                'placeholder':'Enter Email' 
            }),
            'year_of_admissn' : TextInput(attrs={
                'style': 'width : 200px;',
                'placeholder':'Enter Year Of Addmission' 
            }),
        }

