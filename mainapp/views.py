from mainapp.forms import ServiceForm
from .models import Service
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "home.html")


def ott(request):
    return render(request, "ott.html")


def music(request):
    return render(request, "music.html")


def shopping(request):
    return render(request, "shopping.html")


def etc(request):
    return render(request, "etc.html")


@login_required(redirect_field_name=None, login_url="login")
def addService(request):
    if request.method == "GET":
        form = ServiceForm()
        return render(request, "addService.html", {"form": form})

    form = ServiceForm(request.POST, request.FILES)
    if form.is_valid():  # 유효한 입력
        new_service = form.save()
        return redirect('home')

    else:  # 유효하지 않은 입력
        return redirect("home")
