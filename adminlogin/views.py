from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

Uname = ''
Pword = ''
# Create your views here.
def adminlogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "username":
                Uname = value
            if key == "password":
                Pword = value
        
        c = "select * from admin where Username = '{}' and Password = '{}'".format(Uname,Pword)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.warning(request, 'Incorrect credentials!')
        else:
            return render(request,'admindashboard.html')

    return render(request,'adminlogin.html')