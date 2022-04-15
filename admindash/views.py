from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
# from .models import hospital
# Create your views here.
def admindashboard(request):
    print("lov kumar")
    m = sql.connect(host="localhost",user="root",passwd="P@nky7050",database='DBMSproject')
    cursor = m.cursor()
    c = "select * from hospital"
    cursor.execute(c)
    t = cursor.fetchall()
    return render(request,'admindashboard.html',{"all":t})