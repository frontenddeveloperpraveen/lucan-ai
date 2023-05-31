from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('playground',views.Home,name="Home"),
    path('image-gen', views.Imagine,name='Generate'),
    path('',views.Redirect,name='return'),
    path('<str:name>',views.Redirect,name='return')
]
