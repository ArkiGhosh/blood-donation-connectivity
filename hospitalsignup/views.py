from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
import requests
pin = ''
name = ''
contact = ''
address = ''
# Create your views here.
def hospitalsignup(request):
    if request.method=="POST":
        cursor = m.cursor()
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
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
        c = "select PIN from hospital where PIN ='{}'".format(pin)
        cursor.execute(c)
        verify = tuple(cursor.fetchall())
        if verify==():
            c = "insert into hospital Values('{}','{}','{}','{}')".format(pin,name,contact,address)
            cursor.execute(c)
            m.commit()
            #SMS



            url = "https://www.fast2sms.com/dev/bulk"
            numbers="{}".format(contact)
            my_data = {
                        'sender_id': 'Inspired Engine', 
                        'message': 'Congratulations you are registered as a Hospital.', 
                        'language': 'english',
                        'route': 'p',
                        'numbers': numbers  
            }
            headers = {
                        'authorization': "KYQHzs86LewARVTbh9Ii0j7dcgaJSuDF4OMBo3qXEpWUmnykfCEcf7SVZNblrA8K9kGQgxqw6RnmD1zy",
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache"
            }
            response = requests.request("POST",url,data = my_data,headers = headers)
            
            messages.success(request, 'Registered successfully!')
        else:
            messages.warning(request,"This License has already been used")

    return render(request, 'hospitalsignup.html')
