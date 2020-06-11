from django import forms
from django.contrib.auth.forms import UserCreationForm 
from . models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','first_name','last_name','middlename','group','role')

class create_dis_form(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['course']
        widgets = {
            'course':forms.TextInput(attrs={'class': 'form-control'}),
        }

class table_col(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['data']
        widgets ={
            'data' : forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'})
        }

