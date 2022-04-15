from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

pin = ''
name = ''
contact = ''
address = ''
# Create your views here.
def hospitalsignup(request):
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
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
        messages.success(request, 'Registered successfully!')

    return render(request, 'hospitalsignup.html')