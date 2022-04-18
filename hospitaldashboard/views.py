from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
# from hospitallogin.views import HOSPITAL_PIN
import hospitallogin.views
from datetime import datetime, timedelta

hospital_pin = ''
delpouch=''
deletebooking=''

Pwt=''
Pht=''
Pcs=''
Page=''
Pvol=''
PG=''
PDD=''
PiB=0
PBG=''
PAdd=''

Bookemail=''
BookPID=''
BookTime=''
BookDate=''

# Create your views here.
def authenticate(var):
    response = redirect('/hospitaldashboard/')
    global hospital_pin,delpouch
    hospital_pin = var
    # hospitaldashboard()
    return response

def hospitaldashboard(request):
    # print(hospitallogin.views.HOSPITAL_PIN)
    global Uname,Pword,delpouch,Pwt,Pht,Pcs,Page,Pvol,PG,PDD,PiB,PBG,PAdd,BookDate,Bookemail,BookPID,BookTime
    m = sql.connect(host="localhost",user="root",passwd="pushpanjali",database='djangocrud')
    cursor = m.cursor()
    date42 = datetime.today() - timedelta(days = 42 )
    c = "delete pouchbooking from pouchbooking inner join pouch on pouchbooking.PID = pouch.PouchID and pouch.DonationDate < '{}'".format(date42)
    cursor.execute(c)
    m.commit()
    c="delete from pouch where DonationDate < '{}'".format(date42)
    cursor.execute(c)
    m.commit()
    d = request.POST
    for key,value in d.items():
        if key == "regpin":
            pin = value
            
    print(hospital_pin)
    c = "select * from pouch where HospitalPIN = '{}' order by DonationDate".format(hospital_pin)
    cursor.execute(c)
    t = tuple(cursor.fetchall())
    print(t)
    #donorbookings-> 24hr from current time
    Current_Date = datetime.today()
    NextDay_Date = datetime.today() + timedelta(days=1)
    c="select * from donationslot where HPin='{}' and DonationTime>='{}' and DonationTime<='{}'".format(hospital_pin,Current_Date,NextDay_Date)
    print(c)
    cursor.execute(c)
    slots=tuple(cursor.fetchall())
    #receipentbookings
    c="select * from pouchbooking inner join pouch on pouch.PouchID=pouchbooking.PID where pouch.HospitalPIN='{}'".format(hospital_pin)
    cursor.execute(c)
    recbook=tuple(cursor.fetchall())


    if request.method=="POST":
        cursor = m.cursor()
        d = request.POST

        for key,value in d.items():
            if key == "delpouch":
                delpouch = value
            if key == "deletebooking":
                deletebooking = value
            if key == "Pwt":
                Pwt = value
            if key == "Pht":
                Pht = value
            if key == "Pcs":
                Pcs = value
            if key == "Page":
                Page = value
            if key == "Pvol":
                Pvol = value
            if key == "PG":
                PG = value
            if key == "PDD":
                PDD = value
            if key == "PBG":
                PBG = value
            if key == "PAdd":
                PAdd = value
            if key == "Bookemail":
                Bookemail = value
            if key == "BookPID":
                BookPID = value
            if key == "BookTime":
                BookTime = value
            if key == "BookDate":
                BookDate = value
        if delpouch!='' and deletebooking=='':
            c="delete from pouchbooking where PID={}".format(delpouch)
            cursor.execute(c)
            m.commit()
            c="delete from pouch where PouchID={}".format(delpouch)
            cursor.execute(c)
            m.commit()
            delpouch=''
            return redirect("/hospitaldashboard")
            
        elif deletebooking!='':
            
            BookDate=BookTime
            BookDate=BookDate.split('T')
            BookTime=BookDate[0]+" " + BookDate[1]
            BookDate=BookDate[0]
            delbook="delete pouchbooking from pouchbooking where REmail='{}' and PID={} and RTime='{}' and RDate='{}'".format(Bookemail,BookPID,BookTime,BookDate)
            cursor.execute(delbook)
            print(delbook)
            m.commit()
            messages.success(request,"Booking Processed")
            deletebooking=''
            return redirect('/hospitaldashboard')

        else :
            c = "select * from pouch".format(hospital_pin)
            cursor.execute(c)
            t = tuple(cursor.fetchall())  
            c = "select max(PouchID) from pouch"
            cursor.execute(c)
            pouchid = cursor.fetchall()
            print(pouchid)
            print("test")
            if(len(t)==0):# if first most hospital
                pouchid = 1
            else:
                pouchid=pouchid[0][0]+1
            
            c = "insert into pouch values({},'{}',{},{},{},{},{},'{}','{}',{},'{}','{}')".format(pouchid,hospital_pin,Pwt,Pht,Pcs,Page,Pvol,PG,PDD,PiB,PBG,PAdd)
            cursor.execute(c)
            m.commit()
            return redirect("/hospitaldashboard")

    return render(request,'hospitaldashboard.html', {'pouches':t,'slots':slots,'recbook':recbook})
