from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
import requests
name = ''
Pword = ''
email =''
address = ''
contact = ''
# Create your views here.
def recipientsignup(request):
    global name,Pword,contact,address,email
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
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
        c = "select recipientemail from recipient where recipientemail ='{}';".format(email)
        cursor.execute(c)
        verifyduplicate = tuple(cursor.fetchall())
        if verifyduplicate==():
            c = "insert into recipient Values('{}','{}','{}','{}','{}')".format(name,contact,address,email,Pword)
            cursor.execute(c)
            m.commit()
            #SMS
            url = "https://www.fast2sms.com/dev/bulk"
            numbers="{}".format(contact)
            my_data = {
                        'sender_id': 'Inspired Engine', 
                        'message': 'Congratulations you are registered as a Recipient.', 
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
            messages.warning(request,"Already registered with the same email ID")
    
    return render(request,'recipientsignup.html')
