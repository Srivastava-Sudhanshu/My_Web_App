from unicodedata import name
from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path

urlpatterns =[
    path('',views.index),
    path('StudentFeeDetails',views.GetStudentFeeDetails,name="StudentFeeDetails"),
    path('PayFee/<id>',views.PayFee,name="PayFee"),
    path('GetStudentFeeDetails_Id/<id>',views.GetStudentFeeDetails_Id,name="GetStudentFeeDetails_Id"),
    path('export_to_excel',views.export_to_excel, name="export_to_excel"),
    path('duefeenotification',views.DueFeeNotification,name="duefeenotification")
]