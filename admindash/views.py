from os import stat
from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
# from .models import hospital
# Create your views here.
hdel=''
option=''
hName=''
hContact=''
hAddress=''
username=''
def authenticateadmin(var):
    response = redirect('/admindashboard/')
    global username
    username = var
    # hospitaldashboard()
    if(var==''):
        return redirect('/')
    return response

def admindashboard(request):
    global hdel,option,hName,hContact,hAddress
    m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')

    cursor = m.cursor()
    c = "select * from hospital"
    cursor.execute(c)
    t = cursor.fetchall()
    print(username)
    print("admin")
    c = "select * from admin where username = '{}'".format(username)
    cursor.execute(c)
    adminprofile = tuple(cursor.fetchall()) # use for profile
    print(adminprofile)
    c = "select count(*),Hospitalname from pouch inner join hospital on hospital.PIN = pouch.HospitalPin group by PIN;"
    cursor.execute(c)
    hospital_pouch_count = cursor.fetchall()
    hospital_pouch_count1=[]
    for x in hospital_pouch_count:
        hospital_pouch_count1.append(x[0])

    print("count of pouches , hospital name")
    print(hospital_pouch_count)
    c = "select count(*),Hospitalname from donationslot inner join hospital on hospital.PIN = donationslot.HPin group by PIN;"
    cursor.execute(c)
    hospital_slot_count = cursor.fetchall()
    hospital_slot_count1 = []
    for x in hospital_slot_count:
        hospital_slot_count1.append(x[0])
    print("count of slots , hospital name")
    print(hospital_slot_count)
    c = "select count(*) from pouchbooking;"
    cursor.execute(c)
    pouchbooking_count = cursor.fetchall()
    pouchbooking_count = pouchbooking_count[0]
    print("count of total active pouchbookings")
    print(pouchbooking_count)
    c = "select count(*),hospitalname from pouchbooking inner join pouch on pouch.pouchid=pouchbooking.pid inner join hospital on hospital.PIN = pouch.hospitalPIN group by hospitalname;"
    cursor.execute(c)
    hospital_booking_count = cursor.fetchall()
    hospital_booking_count1 = []
    for x in hospital_booking_count:
        hospital_booking_count1.append(x[0])
    print("count of total hospitalwise pouchbookings")
    print(hospital_booking_count)
    c="select count(*),BloodGroup from pouch group by BloodGroup"
    cursor.execute(c)
    BG=cursor.fetchall()
    BG1 = []
    for x in BG:
        BG1.append(x[0])

    stats={'hospital_pouch_count':hospital_pouch_count,'hospital_pouch_count1':hospital_pouch_count1,'pouchbooking_count':pouchbooking_count,'hospital_slot_count':hospital_slot_count,'hospital_slot_count1':hospital_slot_count1,'hospital_booking_count':hospital_booking_count,'hospital_booking_count1':hospital_booking_count1,'BG':BG, 'BG1':BG1}

    if request.method=="POST":
        cursor = m.cursor()
        d = request.POST

        for key,value in d.items():
            if key == "hpin":
                hdel = value
            if key== "editordelete":
                option=value
            if key == "name":
                    hName = value
            if key== "contact":
                hContact=value
            if key == "address":
                hAddress = value
        
        if(option=='edit'):
                ss = "select * from hospital where PIN = '{}'".format(hdel)
                cursor.execute(ss)
                backup = cursor.fetchall()
                print(backup)
                if(hName == ''):
                    hName = t[0][1]

                if(hContact == ''):
                    hContact = t[0][2]

                if(hAddress == ''):
                    hAddress = t[0][3]
   
                c = "update hospital set HospitalName='{}' ,HospitalContact={} , HospitalAddress='{}' where PIN='{}'".format(hName,hContact,hAddress,hdel)
                cursor.execute(c)
                m.commit()
                authenticateadmin(username)
                return redirect('/admindashboard')
        else:   
                c = "delete pouchbooking from pouchbooking inner join pouch on pouchbooking.PID = pouch.PouchID and pouch.HospitalPin='{}'".format(hdel)
                cursor.execute(c)
                m.commit()
                c = "delete from pouch where HospitalPIN='{}'".format(hdel)
                cursor.execute(c)
                m.commit()
                c = "delete from donationslot where HPin='{}'".format(hdel)
                cursor.execute(c)
                m.commit()
                c = "delete from hospital where PIN='{}'".format(hdel)
                cursor.execute(c)
                m.commit()
                authenticateadmin(username)
                return redirect('/admindashboard') 
        
    return render(request,'admindashboard.html',{"all":t,"stats":stats})
