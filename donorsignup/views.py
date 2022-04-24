from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
from twilio.rest import Client
name = ''
Pword = ''
email =''
address = ''
contact = ''
# Create your views here.

def donorsignup(request):
    global name,Pword,contact,address,email
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
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
        authtoken = "3f634b22f2d9c8024681ebd000d47760"
        authsid = "ACd6387bcde5a6fe3030c8afb480add54b"
        client = Client(authsid,authtoken)
        client.messages.create(to = "+91"+contact,from_ = "+19705174927",body="You have registered succesfully as Donor")
        
        messages.success(request, 'Registered successfully!')
    
    return render(request,'donorsignup.html')