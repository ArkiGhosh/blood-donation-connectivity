from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages

email = ''
# Create your views here.
def authenticate(var):
    response = redirect('/donordashboard/')
    global email 
    email = var
    # hospitaldashboard()
    return response

    
def donordashboard(request):
    print(email)
    messages.success(request, 'You are signed in as '+email)
    return render(request,'donordashboard.html')
