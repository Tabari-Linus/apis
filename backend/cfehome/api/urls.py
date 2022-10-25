from operator import ipow
from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home)
]
