from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path

import Student_Portal

urlpatterns = [
    path('',views.index),
    path('GetAllStudents',views.GetAllStudents),
    path('AddStudent',views.AddStudentScreen),
    path('AddNewStudent',views.AddNewStudent),
    path('<id>/',views.UpdateStudentScreen),
    path('<id>/UpdateStudent',views.UpdateStudent),
]