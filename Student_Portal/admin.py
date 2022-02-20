from django.contrib import admin
from .models import Student, Branch

# Register your models here.
admin.site.register([Student,Branch])