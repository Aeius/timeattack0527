from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_up_view, name='index'),
    path('user/register', views.sign_up, name='sign-up')
]