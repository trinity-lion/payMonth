from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("entertainment/", entertainment, name="entertainment"),
    path("shopping/", shopping, name="shopping"),
    path("program/", program, name="program"),
    path("game/", game, name="game"),
    path("etc/", etc, name="etc"),
    path("addService/", addService, name="addService"),
    path("updateService/<str:id>", updateService, name="updateService"),
    path("deleteService/<str:id>", deleteService, name="deleteService"),
]
