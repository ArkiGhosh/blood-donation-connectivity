from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
# from hospitallogin.views import HOSPITAL_PIN
import hospitallogin.views


hospital_pin = ''

# Create your views here.
def authenticate(var):
    response = redirect('/hospitaldashboard/')
    global hospital_pin 
    hospital_pin = var
    # hospitaldashboard()
    return response

def hospitaldashboard(request):
    # print(hospitallogin.views.HOSPITAL_PIN)
    global Uname,Pword
    m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
    cursor = m.cursor()
    d = request.POST
    for key,value in d.items():
        if key == "regpin":
            pin = value
            
    print(hospital_pin)
    c = "select * from pouch where HospitalPIN = '{}'".format(hospital_pin)
    cursor.execute(c)
    t = tuple(cursor.fetchall())
    print(t)

    return render(request,'hospitaldashboard.html', {'pouches':t})