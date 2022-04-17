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
def admindashboard(request):
    global hdel,option,hName,hContact,hAddress
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
    cursor = m.cursor()
    c = "select * from hospital"
    cursor.execute(c)
    t = cursor.fetchall()
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
                
                return redirect('/admindashboard') 
        
    return render(request,'admindashboard.html',{"all":t})