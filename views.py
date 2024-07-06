from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def home(request):
    return render(request,"home.html")
def res(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('login')
        
    else:
        form = SignUpForm()
    return render(request, 'res.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleandata['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in.")
                return redirect('home')
            
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form}) 

def forgetpass(request):
    return render(request,'forgetpass.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def atc(request):
    return render(request,'atc.html')

def payment(request):
    return render(request,'payment.html')

def UPI(request):
    return render(request,'UPI.html')

def card(request):
    return render(request,'card.html')

def success(request):
    return render(request,'success.html')    
    

