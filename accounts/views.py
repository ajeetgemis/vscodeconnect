from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import profile
import random

from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        avail=profile.objects.filter(phone_number=number).first()
        if avail:
            messages.error(request,'User Already Existes')
            return render(request,'signup.html')
        else:    
            user=User.objects.create(username=name,first_name=name,email=email)
            user.save()
            otp=random.randint(100000,999999)
            pr=profile.objects.create(user=user,phone_number=number,otp=otp)
            pr.save()
            
            request.session['phonenumber']=number
            print(request.session.get('phonenumber'))

           
           
            #send_mail()

            messages.success(request,'User Saved Successfully')
            return redirect('/verify_otp')
    
    return render(request,'signup.html')
#@login_required
#def home(request):
 #    return render(request,'home.html')
  
def login_otp_verify(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        session_number=request.session.get('l_number')
        print(otp,session_number)
        p=profile.objects.filter(phone_number=session_number).first()
        
        if otp==p.otp:
            user=User.objects.get(id=p.user.id)
            login(request,user)
            return render(request,'home.html')


    
        
    return render(request,'login_otp_verify.html')


def signal_fun(request):
    session_number=request.session.get('l_number')
    return session_number

def signin(request):
    if request.method=='POST':
        l_number=request.POST.get('number')
        request.session['l_number']=l_number
        try:
            obj=profile.objects.get(phone_number=l_number)

            if obj:
                otp=random.randint(100000,999999)
                obj1=profile.objects.get(id=obj.id)
                obj1.otp=otp
                obj1.save()
                print(otp)
                return redirect('/login_verify_otp')


        except:
            messages.error(request,"User doesn't Exists")
            return render(request,'signin.html')
    
    return render(request,'signin.html')
def verify_otp(request):
    if request.method=='POST':
        print("verifing")
        v_number=request.session.get('phonenumber')
        otp_v=request.POST.get('otp')
        print(v_number,otp_v)
       # p=profile.objects.filter(Q(phone_number=v_number) &  Q(otp=otp_v))
       # print("p object")
        #print(p)
        #for pp in p:
         #   print(pp.is_verified)
        try:
            p=profile.objects.filter(Q(phone_number=v_number) &  Q(otp=otp_v)).first()
            print(p)
            if p:
                
                p.is_verified=True
                p.save()
                return render(request,'signin.html')


        except:
            messages.error(request,'Your OTP is not correct')
    return render(request,'verify.html')
def signout(request):
    logout(request)
    del request.session['l_number']
    return render(request,'signin.html')