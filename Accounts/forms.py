from dataclasses import field, fields
from msilib.schema import CheckBox
from turtle import width
from unicodedata import name
from django.forms import CheckboxInput, ModelForm, TextInput
from Accounts.models import Fees,StudentFeeDetails
class FeesForm (ModelForm):
    class Meta:
        model = Fees
        fields = "__all__"
        widgets = {
            'fee' : TextInput(attrs={
                'readonly':'True',
            }),
        }

class StudentFeeDetailsForm(ModelForm):
    class Meta:
        model = StudentFeeDetails
        exclude = ['student','last_paid_amount','payment_date']
        widgets = {
            'fees_paid' : TextInput(attrs={
                'readonly':'True',
            }),
        }
        
    

