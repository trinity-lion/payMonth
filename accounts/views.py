from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    form=AuthenticationForm
    return render(request, 'login.html',{'form' : form})



# Create your views here.
