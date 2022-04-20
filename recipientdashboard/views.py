import razorpay
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from datetime import datetime, timedelta

email = ''
recipp = ''
pouchid=''
amt=0
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
    global recipp,pouchid,amt
    recipp = tuple(cursor.fetchall()) # use for profile
    print(recipp)

    #auto deletion code snippet
    date42 = datetime.today() - timedelta(days = 42 )
    c = "delete pouchbooking from pouchbooking inner join pouch on pouchbooking.PID = pouch.PouchID and pouch.DonationDate < '{}'".format(date42)
    cursor.execute(c)
    m.commit()
    c="delete from pouch where DonationDate < '{}'".format(date42)
    cursor.execute(c)
    m.commit()
    #showing only non booked blood pouches
    c = "select * from pouch inner join hospital on hospital.pin = pouch.hospitalpin where isbooked = 0"
    cursor.execute(c)
    unbookedpouch = tuple(cursor.fetchall())
    print(unbookedpouch)
    #when the pouch is booked we will have to change the isbooked to 1 here in backend
    if request.method=="POST":
        cursor = m.cursor()
        d = request.POST
        print("--------------------------------------------------")
        for key,value in d.items():
            if key == "pouchid":
                pouchid = value
        
        amount="select Volume from pouch where PouchID={}".format(pouchid)
        cursor.execute(amount)
        amt=cursor.fetchall()
        amt = 50000*float(amt[0][0])
        print(amt)
        
        

        now=datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:00")
        now_string=dt_string
        dt_string=dt_string.split()[0]
        print(now_string,dt_string)
        bookp="insert into pouchbooking values('{}',{},'{}','{}')".format(email,pouchid,now_string,dt_string)
        cursor.execute(bookp)
        m.commit()
        bookp="update pouch set IsBooked=1 where PouchId={}".format(pouchid)
        cursor.execute(bookp)
        m.commit()
        messages.success(request,"Pouch Booked")
        return redirect("/recipientdashboard")

    #here we have booked slots by the recipient only with all details needed (pouch details + hospital details) associated to the booking show just the essentials ones
    d="select * from pouchbooking inner join pouch inner join hospital on hospital.pin = pouch.hospitalpin on pouch.pouchid=pouchbooking.pid where REmail ='{}'".format(email)
    cursor.execute(d) 
    bookings = tuple(cursor.fetchall())
    messages.success(request, 'You are signed in as '+email)

    return render(request,'recipientdashboard.html',{'ubp':unbookedpouch,'mb':bookings,'amount':amt})
