from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as djanjologin
from . forms import *
from . models import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import dateformat
from django.conf import settings
from django.urls import reverse

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        formreg = CreateUserForm(request.POST or None)
        if request.method == 'POST' and formreg.is_valid():
            new_user = formreg.save(commit=False)
            new_user.username = formreg.cleaned_data['username']
            new_user.password1 = formreg.cleaned_data['password1']    
            new_user.middlename = formreg.cleaned_data['middlename']
            new_user.group = formreg.cleaned_data['group']
            new_user.role = formreg.cleaned_data['role']
            new_user.save()
            new_user.groups.add(Group.objects.get(name = formreg.cleaned_data['group']))
            if formreg.cleaned_data['role'] == 'Преподаватель':
                new_user.groups.add(Group.objects.get(name='Преподаватели'))
            else:
                new_user.groups.add(Group.objects.get(name='Студенты'))
            return redirect('login')
        return render(request, 'mainApp/register.html',{'formreg':formreg})

def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
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
    
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def mainPage(request):
    return render(request,"mainApp/mainPage.html")

@login_required(login_url='login')
def list_group(request):
    groups_list = Group.objects.all()
    return render(request,"mainApp/group.html",{'groups_list':groups_list})

@login_required(login_url='login')
def detail_group(request,detail_group):
    group = Group.objects.get(id = detail_group)
    courses = Discipline.objects.all()
    return render(request,"mainApp/list_courses.html",{'group':group,'courses':courses})
    #return render(request, "mainApp/detail_group.html", {'group':group,'users':users,'attendance':attendance,'courses':courses})

@login_required(login_url='login')
def list_courses(request,detail_group,list_courses):
    group = Group.objects.get(id = detail_group)
    users = group.user_set.all()
    attendance = Attendance.objects.order_by('data')
    data_select = Attendance.objects.filter(User = users[0]).order_by('data')
    course = Discipline.objects.get(id = list_courses)
    if request.POST:
        if request.POST.get("form_type") == 'Добавить':
            date_cal = request.POST.get('form_type_1')
            for i in users:
                a = Attendance(User = i,course = course, status = '-', data = date_cal)
                a.save()      
            return redirect('list_courses', detail_group=group.id,list_courses=course.id)
                
        elif request.POST.get("form_type_2") == 'Удалить':
            date_sel = request.POST.get('form_type2')
            att = Attendance.objects.all()
            for i in att:
                if dateformat.format(i.data, settings.DATE_FORMAT) == date_sel:
                    d = Attendance.objects.get(id = i.id) 
                    d.delete() 
            return redirect('list_courses', detail_group=group.id,list_courses=course.id)
        else:
            for j in attendance:
                if j.course.course == course.course and j.User.group == group.name:
                    st = request.POST.get('in_checkbox='+str(j.id))
                    ob_st = Attendance.objects.get(id = j.id)
                    if st == 'on':
                        ob_st.status = '+'
                    else:
                        ob_st.status = '-'
                    ob_st.save()
            return redirect('list_courses', detail_group=group.id,list_courses=course.id)
    return render(request,"mainApp/table.html",{'data_select':data_select,'users':users,'attendance':attendance,'group':group,'course':course})


@login_required(login_url='login')
def create_dis(request,detail_group):
    group = Group.objects.get(id = detail_group)
    courses = Discipline.objects.all()
    form = create_dis_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        users = group.user_set.all()
        new_dis = form.save(commit=False)
        new_dis.User = request.user
        new_dis.group = group
        new_dis.course = form.cleaned_data['course']
        for i in users:
            if i.role == 'Студент':
                a = Discipline(User = i, group = group, course = form.cleaned_data['course'])
                a.save()
        new_dis.save()
        return render(request,"mainApp/list_courses.html",{'group':group,'courses':courses})
    return render(request, 'mainApp/create_dis.html',{'form':form,'group':group})
    
