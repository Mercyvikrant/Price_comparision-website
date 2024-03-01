from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'Home.html')

def index(request):
    
    
    if request.method == 'POST':
        userid=request.POST.get('name')
        psswd=request.POST.get('pass')
        
    
    return render(request,'login.html')

def sign(request):
    """

    if request.method=='post':
        psswd=request.post.get('pass')
        userid=request.post.get('Name')
        phone=request.post.get('phone')
        mail=request.post.get('email')
        country=request.post.get('country')
        adress=request.post.get('adress')
        
    myuser=User.objective.create.create_user(userid,psswd,mail,adress)
    myuser.ph=phone
    myuser.cy=country
    
    myuser.save()
 
    messages.success(request,"You have sucessfully logged in")
   """
    
        
        
    return render(request,'sign.html')




