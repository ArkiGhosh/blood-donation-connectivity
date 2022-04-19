from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages

email = ''
recipp = ''
# Create your views here.
def authenticate(var):
    response = redirect('/recipientdashboard/')
    global email 
    email = var
    # hospitaldashboard()
    return response

def recipientprofile(request):
    return render(request, 'recipientprofile.html', {'dp': recipp})

def recipientdashboard(request):
    print(email)
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
    cursor = m.cursor()
    c = "select * from recipient where recipientemail = '{}'".format(email)
    cursor.execute(c)
    global recipp
    recipp = tuple(cursor.fetchall()) # use for profile
    print(recipp)
    #showing only non booked blood pouches
    c = "select * from pouch inner join hospital on hospital.pin = pouch.hospitalpin where isbooked = 0"
    cursor.execute(c)
    unbookedpouch = tuple(cursor.fetchall())
    print(unbookedpouch)
    #when the pouch is booked we will have to change the isbooked to 1 here in backend



    #here we have booked slots by the recipient only with all details needed (pouch details + hospital details) associated to the booking show just the essentials ones
    d="select * from pouchbooking inner join pouch inner join hospital on hospital.pin = pouch.hospitalpin on pouch.pouchid=pouchbooking.pid where REmail ='{}'".format(email)
    cursor.execute(d) 
    bookings = tuple(cursor.fetchall())
    messages.success(request, 'You are signed in as '+email)
    
    return render(request,'recipientdashboard.html',{'ubp':unbookedpouch,'mb':bookings})
