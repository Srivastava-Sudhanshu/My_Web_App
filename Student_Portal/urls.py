from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path

import Student_Portal

urlpatterns = [
    path('',views.index),
    path('GetAllStudents',views.GetAllStudents, name="GetAllStudents"),
    path('GetAllStudentsBranchwise/<branch>',views.GetAllStudentsBranchwise, name="GetAllStudentsBranchwise"),
    path('AddStudent',views.AddStudentScreen),
    path('AddNewStudent',views.AddNewStudent),
    path('<id>/UpdateStudent',views.UpdateStudent, name="UpdateStudent"),
    path('export_excel',views.export_excel, name="export_excel"),
]