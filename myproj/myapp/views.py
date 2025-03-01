from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='sanu', database='price')
mycur = conn.cursor()

def sign(request):
    if request.method == 'POST':
        name = request.POST.get('Name', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        country = request.POST.get('country', '')
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')
        
        # Validate phone number
        if phone.isdigit():  # Check if phone contains only digits
            # Prevent SQL injection by using parameterized queries
            query = "INSERT INTO user1 VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, phone, address, country, email, password)
            mycur.execute(query, data)
            conn.commit()
            return render(request, 'login.html')
        else:
            # Handle invalid phone number
            messages.error(request, 'Invalid phone number')
            return render(request, 'sign.html')
    
    return render(request, 'sign.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')
        
        # Prevent SQL injection by using parameterized queries
        query = "SELECT * FROM user1 WHERE email=%s AND password=%s"
        data = (email, password)
        mycur.execute(query, data)
        result = mycur.fetchall()
        
        if result:
            return render(request, 'Home.html')
        else:
            # Redirect to a specific URL when login fails
            return redirect('https://www.smartprix.com/')
    
    return render(request, 'login.html')

