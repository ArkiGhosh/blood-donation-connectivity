from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from recipientdashboard.views import authenticate
email = ''
Pword = ''
# Create your views here.
def recipientlogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "email":
                email = value
            if key == "password":
                Pword = value
        
        c = "select * from recipient where RecipientEmail = '{}' and RecipientPassword = '{}'".format(email,Pword)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.warning(request, 'Incorrect credentials!')
        else:
            authenticate(t[0][3])
            response = redirect('/recipientdashboard/')
            return response

    return render(request,'recipientlogin.html')