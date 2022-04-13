from django.shortcuts import render
import mysql.connector as sql
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
    return render(request, 'hospitalsignup.html')