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
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
    cursor = m.cursor()
    c = "select * from recipient where recipientemail = '{}'".format(email)
    cursor.execute(c)
    recipientprofile = tuple(cursor.fetchall()) # use for profile
    print(recipientprofile)
    messages.success(request, 'You are signed in as '+email)
    return render(request,'recipientdashboard.html')
