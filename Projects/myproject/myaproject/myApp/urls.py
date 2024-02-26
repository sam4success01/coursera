from django.contrib import admin
from django.urls import path

from . import views
from . import forms

urlpatterns = [
    path('home/', views.home,),
    path('date/', views.display_date,),
    path('menus/', views.menus,),
    path('dishes/<str:dish>', views.menuitems,),
    path('form/', views.form_view,),
    path('demo/', views.Demo_form,),
    path('about/', views.about,),
    path('menu/', views.menu,),
    path('menuid/', views.menu_by_id,),

]
