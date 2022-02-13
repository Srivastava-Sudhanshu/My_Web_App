from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('GetAllStudents',views.GetAllStudents),
]