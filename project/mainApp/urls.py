from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/', views.register, name = 'registration'),
    path('', views.login, name = 'login'),
    path('main/', views.mainPage, name = 'main'),
    path('logout/', views.logoutUser, name='logout'),
    path('groups/', views.list_group, name='groups'),
    path('groups/group=<detail_group>/', views.detail_group, name ='detail_group'),
    path('groups/group=<detail_group>/create_dis',views.create_dis, name = "create_dis"),
    path('groups/group=<detail_group>/course=<list_courses>/',views.list_courses, name ='list_courses'),
    path('courses/',views.student_courses, name = 'student_courses'),
    path('courses/course=<stud_course>/',views.stud_course, name='stud_course'),
]
