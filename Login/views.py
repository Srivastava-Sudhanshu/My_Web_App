from logging import exception
from multiprocessing.dummy import Value
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    SetSession(request,username)
                    getSession = request.session["Islogin"]
                    return redirect('/student/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            if("Islogin" in request.session):
                #del request.session["Islogin"]
                logout_request(request)
        form = AuthenticationForm()
        return render(request,'Login/index.html',{"form":form})
    except Exception:
        print(Exception)
def logout_request(request):
    form = AuthenticationForm(request=request, data=request.GET)
    logout(request)
    #del request.session["Islogin"]
    return render(request,'Login/index.html',{"form":form})

def SetSession(request,username):
    request.session["Islogin"] = username