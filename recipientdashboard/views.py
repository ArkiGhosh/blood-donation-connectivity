from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages

email = ''
recipp = ''
# Create your views here.
def authenticate(var):
    response = redirect('/recipientdashboard/')
    global email 
    email = var
    # hospitaldashboard()
    return response

def recipientprofile(request):
    return render(request, 'recipientprofile.html', {'dp': recipp})

def recipientdashboard(request):
    print(email)
    m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
    cursor = m.cursor()
    c = "select * from recipient where recipientemail = '{}'".format(email)
    cursor.execute(c)
    global recipp
    recipp = tuple(cursor.fetchall()) # use for profile
    print(recipp)
    messages.success(request, 'You are signed in as '+email)
    return render(request,'recipientdashboard.html')
