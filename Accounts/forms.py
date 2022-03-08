from dataclasses import field, fields
from turtle import width
from unicodedata import name
from django.forms import CheckboxInput, ModelForm, TextInput
from Accounts.models import Fees,StudentFeeDetails
class FeesForm (ModelForm):
    class Meta:
        model = Fees
        fields = "__all__"

class StudentFeeDetailsForm(ModelForm):
    class Meta:
        model = StudentFeeDetails
        fields = "__all__"
        
    

