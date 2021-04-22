from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'my_app/home.html')

def login(request):
    return render(request,'my_app/login.html')

def signup(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('my_app-login')
    else:
        form=UserRegistrationForm()

    return render(request,'my_app/signup.html',{'form':form})
