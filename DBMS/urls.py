"""DBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from adminlogin.views import adminlogin
from adminsignup.views import adminsignup
from donorlogin.views import donorlogin
from donorsignup.views  import donorsignup
from hospitallogin.views import hospitallogin
from hospitalsignup.views import hospitalsignup
from recipientlogin.views import recipientlogin
from recipientsignup.views import recipientsignup
from hospitaldashboard.views import hospitaldashboard
from donordashboard.views import donordashboard
from recipientdashboard.views import recipientdashboard
from admindash.views import admindashboard

urlpatterns = [
    path('', include('BloodDonation.urls')),
    path("admin/",adminlogin,name='admin login'),
    path("adminsignup/",adminsignup,name='admin signup'),
    path("donorlogin/",donorlogin,name='donor login'),
    path("donorsignup/",donorsignup,name='donor signup'),
    path("hospitallogin/",hospitallogin,name='hospital login'),
    path("hospitalsignup/",hospitalsignup,name='hospital signup'),
    path("recipientlogin/",recipientlogin,name='hospital login'),
    path("recipientsignup/",recipientsignup,name='hospital signup'),
    path("hospitaldashboard/", hospitaldashboard,name='hospital dashboard'),
    path("donordashboard/", donordashboard,name='donor dashboard'),
    path("recipientdashboard/", recipientdashboard,name='recipient dashboard'),
    path("admindashboard/",admindashboard,name='admin dashboard'),
]
