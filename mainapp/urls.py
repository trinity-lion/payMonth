from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("ott/", home, name="ott"),
    path("music/", home, name="music"),
    path("shopping/", home, name="shopping"),
    path("etc/", home, name="etc"),
    path("addService/", home, name="addService"),


]
