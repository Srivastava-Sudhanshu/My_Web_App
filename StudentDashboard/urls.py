from django.urls import path
from StudentDashboard.views import index
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('signup',views.signup, name="signup"),
    path('generateOTP',views.generateOTP,name="generateOTP"),
    path('dashboard',views.dashboard,name="dashboard")
]