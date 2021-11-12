from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("login/",views.loginPage,name='loginPage'),
    path("register/",views.registerPage,name='registerPage'),
    path("logout/",views.logoutUser,name='logout'),
    path("",views.home,name='home'),
    path("room/<str:pk>/",views.room,name='room'),
    path('create-room/',views.createRoom, name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom, name="delete-room")
]
