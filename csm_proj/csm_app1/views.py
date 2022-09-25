from http.client import HTTPResponse
#from tkinter.ttk import Style
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
import uuid
from django.db import models
from csm_app1.models import Registration

# Create your views here.
def index(request):
    return render(request, "csm_app1/index.html")


def signup(request): #this is signup view
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass1']
        newUser=User.objects.create_user(username=username,email=email,password=password)
        newUser.save()
        msg="User created successfully"
        messages.success(request,'User created successfully')
        return render(request, 'csm_app1/index.html',{'msg':msg})
    else:
        messages.error(request,'Something went wrong')
        msg="User created successfully"
        return render(request, 'csm_app1/index.html',{'msg':msg})

    











    return render(request, "csm_app1/index.html")




def signin(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass2']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ' Logged in successfully')
            return redirect('/homepage/')
        else:
            messages.success(request, "Login Error:- please check your credentials or create an account to login")
            return redirect('index')
    return render(request,'csm_app1/index.html')


#@login_required(login_url='signin')
def form(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        address=request.POST['addr']
        email=request.POST['email']
        phno=request.POST['mob']
        city=request.POST['city']
        pincode=request.POST['pin']
        c_reg=request.POST['regno']
        c_own=request.POST['owner']
        c_model=request.POST['model']
        c_fuel=request.POST['fuel']
        c_color=request.POST['color']
        c_insdate=request.POST['insurdate']
        s_del=request.POST['delivery']
        s_sdate=request.POST['servdate']
        s_pdate=request.POST['pickdate']
        s_type=request.POST['servtype']
        s_oth=request.POST['otherserv']

        bookservice=Registration.objects.create(
            fullname=fullname,
            address=address,
            email=email,
            phno=phno,
            city=city,
            pincode=pincode,
            regno=c_reg,
            owner=c_own,
            model=c_model,
            fuel=c_fuel,
            colour=c_color,
            expdate=c_insdate,
            delivery=s_del,
            servdate=s_sdate,
            pickdate=s_pdate,
            serv=s_type,
            oth=s_oth 
        )
        bookservice.save()

        d_book={
            'fullname':fullname,
            'address':address,
            'email':email,
            'phno':phno,
            'city':city,
            'pin':pincode,
            'regno':c_reg,
            'owner':c_own,
            'model':c_model,
            'fuel':c_fuel,
            'color':c_color,
            'expdate':c_insdate,
            'delivery':s_del,
            'servdate':s_sdate,
            'pickdate':s_pdate,
            'serv':s_type,
            'oth':s_oth


        }
        #return render(request, 'csm_app1/bookdetails.html',{'d_book':d_book})
        return render(request, 'csm_app1/popup.html')
    











    return render(request, "csm_app1/Form.html")
    
    







@login_required(login_url='signin')
def aboutus(request):
    return render(request, "csm_app1/about-us.html")








@login_required(login_url='signin')
def homepage(request):
    return render(request, "csm_app1/homepage.html")






@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('index')



@login_required(login_url='signin')
def bookdetails(request):
    return render(request,'csm_App1/bookdetails.html' )



def popup(request):
    return render(request,'csm_app1/popup.html')