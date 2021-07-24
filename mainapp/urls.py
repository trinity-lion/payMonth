from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("ott/", ott, name="ott"),
    path("music/", music, name="music"),
    path("shopping/", shopping, name="shopping"),
    path("etc/", etc, name="etc"),
    path("addService/", addService, name="addService"),
    path("updateService/<str:id>", updateService, name="updateService"),
    path("deleteService/<str:id>", deleteService, name="deleteService"),
]
