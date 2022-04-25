from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from admindash.views import authenticateadmin
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
            authenticateadmin(t[0][0])
            return redirect('/admindashboard')

    return render(request,'adminlogin.html')

#test comment