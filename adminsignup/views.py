from django.shortcuts import render
import mysql.connector as sql
Uname = ''
Pword = ''
# Create your views here.
def adminsignup(request):
    global Uname,Pword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="Paranitrophenol@10",database='dbms_project')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "username":
                Uname = value
            if key == "password":
                Pword = value
        
        c = "insert into admin Values('{}','{}')".format(Uname,Pword)
        cursor.execute(c)
        m.commit()
    
    return render(request,'adminsignup.html')