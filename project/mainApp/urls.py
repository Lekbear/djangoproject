from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/', views.register, name = 'registration'),
    path('', views.login, name = 'login'),
    path('main/', views.mainPage, name = 'main'),
    path('logout/', views.logoutUser, name='logout'),
    path('groups/', views.list_group, name='groups'),
    path('groups/<detail_group>/', views.detail_group, name ='detail_group'),
    path('groups/<detail_group>/create_dis',views.create_dis, name = "create_dis"),
    path('groups/<detail_group>/<list_courses>/',views.list_courses, name ='list_courses'),
]
