from unicodedata import name
from django.urls import path
from Student_Portal.views import index
from . import views
from django.urls import path, re_path
import Accounts

urlpatterns =[
    path('',views.index),
]