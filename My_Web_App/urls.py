"""My_Web_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path,include
from Student_Portal import views
import Student_Portal
import Accounts
import Login
from Accounts import views
import StudentDashboard
from StudentDashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/statuscheck/', include('celerybeat_status.urls')),
    path('student/',include('Student_Portal.urls')),
    path('accounts/',include('Accounts.urls')),
    path('',include('Login.urls')),
    path('studentdashboard/',include('StudentDashboard.urls'))
]
