from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
from twilio.rest import Client
pin = ''
name = ''
contact = ''
address = ''
# Create your views here.
def hospitalsignup(request):
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "pin":
                pin = value
            if key == "name":
                name = value
            if key == "contact":
                contact = value
            if key == "address":
                address = value
        c = "insert into hospital Values('{}','{}','{}','{}')".format(pin,name,contact,address)
        cursor.execute(c)
        m.commit()
        # authtoken = "3f634b22f2d9c8024681ebd000d47760"
        # authsid = "ACd6387bcde5a6fe3030c8afb480add54b"
        # client = Client(authsid,authtoken)
        # client.messages.create(to = "+91"+contact,from_ = "+19705174927",body="You have registered succesfully as Hospital")
        
        messages.success(request, 'Registered successfully!')

    return render(request, 'hospitalsignup.html')