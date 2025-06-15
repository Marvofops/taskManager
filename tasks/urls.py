from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete_task/<int:task_id>/',views.delete_task, name='delete_task'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('update/<int:task_id>', views.update, name='update'),
]