from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login_view, name="login"),
    #path('signup/', signup_view, name="signup"),
    #path('logout/', logout_view, name="logout"),
   
]