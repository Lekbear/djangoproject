from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils import timezone
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    middlename = models.CharField(max_length=50)
    group = (
        ('02121-ДБ','02121-ДБ'),('02122-ДБ','02122-ДБ'),('02141-ДБ','02141-ДБ'),('02161-ДБ','02161-ДБ'),
        ('02171-ДБ','02171-ДБ'),('02172-ДБ','02172-ДБ'),('02173-ДБ','02173-ДБ'),
        ('02221-ДБ','02221-ДБ'),('02222-ДБ','02222-ДБ'),('02241-ДБ','02241-ДБ'),
        ('02242-ДБ','02242-ДБ'),('02261-ДБ','02261-ДБ'),('02271-ДБ','02271-ДБ'),
        ('02311-ДБ','02311-ДБ'),('02321-ДБ','02321-ДБ'),('02322-ДБ','02322-ДБ'),
        ('02341-ДБ','02341-ДБ'),('02361-ДБ','02361-ДБ'),('02371-ДБ','02371-ДБ'),
        ('02411-ДБ','02411-ДБ'),('02421-ДБ','02421-ДБ'),('02422-ДБ','02422-ДБ'),
        ('02441-ДБ','02441-ДБ'),('02461-ДБ','02461-ДБ'),('02471-ДБ','02471-ДБ')
    )
    group = models.CharField(max_length=30,choices=group,default='02121-ДБ',blank=True, null=True)
    role = (
        ('Студент','Студент'), ('Преподаватель','Преподаватель')
    )
    role = models.CharField(max_length=50,choices=role, default='Студент')

class Discipline(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s' % (self.course, self.User.username)

class Attendance(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Discipline,on_delete=models.CASCADE)
    status = (
    ('+','+'),('-','-')
    )
    status = models.CharField(max_length=1,choices=status, default='-',blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return '%s %s %s' % (self.User.username, str(self.data), self.course)