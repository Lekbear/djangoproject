from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
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
        return redirect('register')
    return render(request, 'mainApp/register.html',{'formreg':formreg})