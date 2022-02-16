from dataclasses import field, fields
from django.forms import ModelForm
from Student_Portal.models import Student
class StudentForm (ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

