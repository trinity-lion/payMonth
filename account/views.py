from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout 

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): #유효성 검사해서 통과된 데이터 =cleaned data
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(request=request, usernmae=username, password=password )
            if user is not None : #USER가 없는게 아니라면(즉 테이블에 존재하는 상태라면)
                login(request,user) #이 로그인 기능을 위해 auth에서 로긔인 기능 import
        return redirect('home') #인덴트중요!
    else :
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})
def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method=='POST' :
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("home")
    else :
        form=UserCreationForm()
    return render(request, 'signup.html', {'form':form})