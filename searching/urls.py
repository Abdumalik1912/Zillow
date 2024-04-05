from itertools import product

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from searching import views

urlpatterns = [
    path('', views.search_home),
]