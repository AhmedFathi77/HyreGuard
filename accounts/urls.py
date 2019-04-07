from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register.as_view(), name='register'),
    path('login', views.Login, name='login'),
]
