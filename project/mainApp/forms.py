from django import forms
from django.contrib.auth.forms import UserCreationForm 
from . models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','first_name','last_name','middlename','group','role')