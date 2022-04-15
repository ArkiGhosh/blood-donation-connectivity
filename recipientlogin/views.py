from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
email = ''
Pword = ''
# Create your views here.
def recipientlogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
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
            return render(request,'recipientdashboard.html')

    return render(request,'recipientlogin.html')