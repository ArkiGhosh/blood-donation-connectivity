from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages

email = ''
# Create your views here.
def authenticate(var):
    response = redirect('/recipientdashboard/')
    global email 
    email = var
    # hospitaldashboard()
    return response
def recipientdashboard(request):
    print(email)
    messages.success(request, 'You are signed in as '+email)
    return render(request,'recipientdashboard.html')
