from django.shortcuts import render
import mysql.connector as sql
pin = ''
# Create your views here.
def hospitallogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "regpin":
                pin = value
            
        
        c = "select * from hospital where PIN = '{}'".format(pin)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request,'hospitalloginerror.html')
        else:
            return render(request,'hospitaldashboard.html')

    return render(request,'hospitallogin.html')