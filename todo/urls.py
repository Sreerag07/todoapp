from django.urls import path
from todo import views
from django.shortcuts import render
urlpatterns=[
    path("todo",views.home,name="home"),
    path("todo/userhome",views.userhome,name="userhome"),
    path("todo/registration",views.user_registration,name="register"),
    path("todo/login",views.user_signin,name="signin"),
    path("todo/logout",views.signout,name="logout"),

]