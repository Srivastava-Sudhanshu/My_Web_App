import django
from django.http import JsonResponse
from Student_Portal.models import Student
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def GetAllStudents():
    data = serializers.serialize("json", Student.objects.all())
    return JsonResponse(json.loads(data), safe=False)
    
