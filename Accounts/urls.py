from unicodedata import name
from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path
import Accounts

urlpatterns =[
    path('',views.index),
    path('GetStudentFeeDetails',views.GetStudentFeeDetails,name="GetStudentFeeDetails"),
    path('PayFee/<id>',views.PayFee,name="PayFee"),
]