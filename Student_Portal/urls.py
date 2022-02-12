from django.urls import path
from Student_Portal.views import emphasized_HTML, index
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('emph',views.emphasized_HTML),
]