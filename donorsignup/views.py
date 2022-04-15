from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

name = ''
Pword = ''
email =''
address = ''
contact = ''
# Create your views here.
def donorsignup(request):
    global name,Pword,contact,address,email
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "name":
                name = value
            if key == "password":
                Pword = value
            if key == "email":
                email = value
            if key == "contact":
                contact = value
            if key == "address":
                address = value
        
        c = "insert into donor Values('{}','{}','{}','{}','{}')".format(name,contact,address,email,Pword)
        cursor.execute(c)
        m.commit()
        messages.success(request, 'Registered successfully!')
    
    return render(request,'donorsignup.html')