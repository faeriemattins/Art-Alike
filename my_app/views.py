from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'my_app/home.html')

def login(request):
    return render(request,'my_app/login.html')

def signup(request):
    return render(request,'my_app/signup.html')
