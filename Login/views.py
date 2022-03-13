from logging import exception
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

#from My_Web_App import Login

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
                    return redirect('/student/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request,'Login/index.html',{"form":form})
    except:
        print(exception)

# def logout_request(request):
#     logout(request)
#     #messages.info(request, "Logged out successfully!")
#     return redirect("main:homepage")