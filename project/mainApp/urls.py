from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/', views.register, name = 'registration'),
    path('', views.login, name = 'login'),
    path('main/', views.mainPage, name = 'main')
]
