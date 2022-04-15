from email import message
from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
Uname = ''
Pword = ''
# Create your views here.
def adminsignup(request):
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
        
        c = "insert into admin Values('{}','{}')".format(Uname,Pword)
        messages.success(request, 'New Admin Added!')
        
        cursor.execute(c)
        m.commit()
    
    return render(request,'adminsignup.html')