from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput({'class':'form-control','style':'font-size:14px'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'class':'form-control','style':'font-size:14px'}))
    first_name=forms.CharField(widget=forms.TextInput({'class':'form-control','style':'font-size:14px'}))
    username=forms.CharField(widget=forms.TextInput({'class':'form-control','style':'font-size:14px'}))
    email=forms.EmailField(widget=forms.EmailInput({'class':'form-control','style':'font-size:14px'}))
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']
