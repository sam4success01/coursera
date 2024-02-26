from django.contrib import admin

from django.urls import path

from .import views

urlpatterns = [
    path ('index/', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path ('menu/', views.menu, name='menu'),
]