from django.http import HttpResponse
from django.shortcuts import render
from admindash.views import authenticateadmin
from recipientdashboard.views import authenticaterecipient
from donordashboard.views import authenticatedonor
from hospitaldashboard.views import authenticatehospital
# Create your views here.
def index(request):
    authenticateadmin('')
    authenticatedonor('')
    authenticatehospital('')
    authenticaterecipient('')
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')