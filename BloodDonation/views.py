from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def donorlogin(request):
    return render(request, 'donorlogin.html')

def donorsignup(request):
    return render(request, 'donorsignup.html')