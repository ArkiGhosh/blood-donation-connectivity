from django.shortcuts import render
import mysql.connector as sql
email = ''
Pword = ''
# Create your views here.
def donorlogin(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "email":
                email = value
            if key == "password":
                Pword = value
        
        c = "select * from Donor where DonorEmail = '{}' and DonorPassword = '{}'".format(email,Pword)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request,'donorloginerror.html')
        else:
            return render(request,'donordashboard.html')

    return render(request,'donorlogin.html')