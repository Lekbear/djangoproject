from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/', views.register, name = 'registration'),
    path('', views.login, name = 'login'),
    path('main/', views.mainPage, name = 'main'),
    path('logout/', views.logoutUser, name='logout'),
    path('groups/', views.list_group, name='groups'),
    path('groups/<table>/', views.detail_group, name ='detail_group'),
]
