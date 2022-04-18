from django.contrib import admin
from django.urls import path
from donordashboard import views

urlpatterns = [
    path('donorprofile/', views.donorprofile, name = 'donorprofile'),
]