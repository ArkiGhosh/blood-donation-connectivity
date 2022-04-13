from django.contrib import admin
from django.urls import path
from BloodDonation import views

urlpatterns = [
    path('', views.index, name = 'BloodDonation'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'),
]