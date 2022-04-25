from email import message
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages

donorp = ''
email = ''
hPIN=''
dontime=''
dondate=''
bookorbookings=''
# Create your views here.
def authenticatedonor(var):
    response = redirect('/donordashboard/')
    global email 
    email = var
    # hospitaldashboard()
    if(var==''):
        return redirect('/')
    return response

def donorprofile(request):
    return render(request, 'donorprofile.html', {'dp':donorp})

def donordashboard(request):
    global hPIN,dontime,dondate
    print(email)
    if(email==''):
        return redirect("/")
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='dbmsproject')
    cursor = m.cursor()
    c = "select * from hospital"
    cursor.execute(c)
    hospitals = cursor.fetchall()
    d="select * from donationslot inner join hospital on donationslot.HPin=hospital.PIN where DEmail='{}'".format(email)
    cursor.execute(d)
    bookings = cursor.fetchall()

    c = "select * from donor where donoremail = '{}'".format(email)
    cursor.execute(c)
    global donorp
    donorp = tuple(cursor.fetchall()) # use for profile
    print(donorp)
    
    if request.method=="POST":
        cursor = m.cursor()
        d = request.POST

        for key,value in d.items():
            if key == "hpin":
                hPIN = value
            if key == "dontime":
                dontime = value
            if key == "dondate":
                dondate = value
            if key=="bookorbookings":
                bookorbookings=value
        
        if bookorbookings=="book":
            bookingq="insert into donationslot values('{}','{}','{} {}:00','{}')".format(hPIN,email,dondate,dontime,dondate)
            cursor.execute(bookingq)
            m.commit()
            messages.success(request,"Slot booked")
            authenticatedonor(email)
            return redirect('/donordashboard')

        else:
            dondate=dontime
            dondate=dondate.split('T')
            dontime=dondate[0]+" " + dondate[1]
            dondate=dondate[0]

            delslot="delete from donationslot where HPin='{}'and DEmail='{}'and DonationTime='{}'and Ddate='{}'".format(hPIN,email,dontime,dondate)
            cursor.execute(delslot)
            m.commit()
            messages.success(request,"Slot Deleted")
            authenticatedonor(email)
            return redirect('/donordashboard')
    messages.success(request, 'You are signed in as '+email)
    return render(request,'donordashboard.html',{'hospitals':hospitals,'bookings':bookings})
