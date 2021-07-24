from django.shortcuts import render

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
