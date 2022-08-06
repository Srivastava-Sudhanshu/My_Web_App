from django.urls import path
from Student_Portal.views import index
from . import views

import Student_Portal

urlpatterns = [
    path('',views.index),
    path('AllStudents',views.GetAllStudents, name="AllStudents"),
    path('AllStudentsBranchwise/<branch>',views.GetAllStudentsBranchwise, name="AllStudentsBranchwise"),
    path('AddStudent',views.AddStudentScreen),
    path('AddNewStudent',views.AddNewStudent),
    path('<id>/UpdateStudent',views.UpdateStudent, name="UpdateStudent"),
    path('export_excel',views.export_excel, name="export_excel"),
]