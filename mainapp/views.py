from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def ott(request):
    return render(request, "home.html")


def music(request):
    return render(request, "home.html")


def shopping(request):
    return render(request, "home.html")


def iservice(request):
    return render(request, "home.html")


def delievery(request):
    return render(request, "home.html")
