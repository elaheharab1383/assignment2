from django.contrib import admin
from django.urls import path,include
from.views import say_something

urlpatterns = [
    path('hi/',say_something,name='say_something'),
    ]
