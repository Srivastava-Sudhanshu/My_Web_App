from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> Welcome to Student ERP </h1>')

def index(request):
    return HttpResponse('Hello World')

def emphasized_HTML(request):
    return HttpResponse('<em> Hello World </em>')