from django.shortcuts import render
import mysql.connector as sql
name = ''
Pword = ''
email =''
address = ''
contact = ''
# Create your views here.
def recipientsignup(request):
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
        
        c = "insert into recipient Values('{}','{}','{}','{}','{}')".format(name,contact,address,email,Pword)
        cursor.execute(c)
        m.commit()
    
    return render(request,'recipientsignup.html')