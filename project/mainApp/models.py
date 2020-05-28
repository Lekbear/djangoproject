from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    middlename = models.CharField(max_length=50)
    group = models.CharField(max_length=30, blank=True)
    role = (
        ('Студент','Студент'), ('Преподаватель','Преподаватель')
    )
    role = models.CharField(max_length=50,choices=role, default='Студент')