from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as djanjologin
from . forms import *
from . models import *
from django.contrib.auth.models import Group

# Create your views here.
def register(request):
    formreg = CreateUserForm(request.POST or None)
    if request.method == 'POST' and formreg.is_valid():
        new_user = formreg.save(commit=False)
        new_user.username = formreg.cleaned_data['username']
        new_user.password = formreg.cleaned_data['password1']    
        new_user.middlename = formreg.cleaned_data['middlename']
        new_user.group = formreg.cleaned_data['group']
        new_user.role = formreg.cleaned_data['role']
        new_user.save()
        if formreg.cleaned_data['role'] == 'Преподаватель':
            new_user.groups.add(Group.objects.get(name='Преподаватели'))
        else:
            new_user.groups.add(Group.objects.get(name='Студенты'))
        return redirect('login')
    return render(request, 'mainApp/register.html',{'formreg':formreg})

def login(request):
    #if request.user.is_authenticated:
        #return redirect('main')
    #else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)
            if user is not None:
                djanjologin(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Логин или пароль введен неверно')
        return render(request, 'mainApp/login.html')
    
def mainPage(request):
    return render(request,"mainApp/mainPage.html")