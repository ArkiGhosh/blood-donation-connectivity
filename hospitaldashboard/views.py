from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
# from hospitallogin.views import HOSPITAL_PIN
import hospitallogin.views


hospital_pin = ''
delpouch=''
# Create your views here.
def authenticate(var):
    response = redirect('/hospitaldashboard/')
    global hospital_pin,delpouch
    hospital_pin = var
    # hospitaldashboard()
    return response

def hospitaldashboard(request):
    # print(hospitallogin.views.HOSPITAL_PIN)
    global Uname,Pword
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
    cursor = m.cursor()
    d = request.POST
    for key,value in d.items():
        if key == "regpin":
            pin = value
            
    print(hospital_pin)
    c = "select * from pouch where HospitalPIN = '{}' order by DonationDate".format(hospital_pin)
    cursor.execute(c)
    t = tuple(cursor.fetchall())
    print(t)
    if request.method=="POST":
        cursor = m.cursor()
        d = request.POST

        for key,value in d.items():
            if key == "delpouch":
                delpouch = value
        c="delete from pouchbooking where PID={}".format(delpouch)
        cursor.execute(c)
        m.commit()
        c="delete from pouch where PouchID={}".format(delpouch)
        cursor.execute(c)
        m.commit()
        return redirect("/hospitaldashboard")

    return render(request,'hospitaldashboard.html', {'pouches':t})