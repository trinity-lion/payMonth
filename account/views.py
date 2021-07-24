from django.shortcuts import render
from . import views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout 

def login_view(request):
    form=AuthenticationForm
    return render(request, 'login.html',{'form' : form})
