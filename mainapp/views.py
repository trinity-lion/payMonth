from mainapp.forms import ServiceForm
from .models import Service
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    services = Service.objects.all()
    entertainments = Service.objects.filter(category='entertainment')
    shoppings = Service.objects.filter(category='shopping')
    programs = Service.objects.filter(category='program')
    games = Service.objects.filter(category='game')
    etcs = Service.objects.filter(category='etc')
    return render(request, "home.html", {
        'services': services,
        'entertainments': entertainments,
        'shoppings': shoppings,
        'programs': programs,
        'games': games,
        'etcs': etcs,
    })


def entertainment(request):
    return render(request, "entertainment.html")


def shopping(request):
    return render(request, "shopping.html")


def program(request):
    return render(request, "program.html")


def game(request):
    return render(request, "game.html")


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


@login_required(redirect_field_name=None, login_url="login")
def updateService(request, id):
    if request.method == "GET":
        service = get_object_or_404(Service, pk=id)
        # 기본값 설정
        form = ServiceForm(initial={
            "name": service.name,
            "category": service.category,
            "cost": service.cost,
            "pay_interval": service.pay_interval,
            "shared": service.shared,
            "image": service.image,
        })
        return render(request, "updateService.html", {"form": form, 'service': service})

    form = ServiceForm(request.POST, request.FILES)
    if form.is_valid():
        new_service = form.save()
        return redirect("home", new_service.id)
    else:
        return redirect("home")


@login_required(redirect_field_name=None, login_url="login")
def deleteService(request, id):
    diary = get_object_or_404(Service, pk=id)
    diary.delete()
    return redirect("home")
