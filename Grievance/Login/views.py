from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password,check_password
from django.http import *
from Profile.models import *


def register(request):
    return render(request,'Login/signup.html')


def signup(request):
    if request.method=='POST':
        data=request.POST
        if data['name'] and data['email'] and len(data['number'])==10 and len(data['year'])==4 and data['course'] and data['gender']:
            prof = profile()
            prof.Name = data['name']
            prof.Email = data['email']
            prof.Contactno = data['number']
            prof.Year = data['year']
            prof.Course = data['course']
            prof.Gender = data['gender']
            if(data['password'] and data['cpassword']):
                if(data['password'] == data['cpassword']):
                    prof.Password = make_password(data['password'])         # Password is hashed not in readable format
                    prof.save()
                    return render(request,'Login/signup.html',{'msg':'Student has Registered Successfully!!'})
                else:
                    return render(request,'Login/signup.html',{'msg':'Password is not Matched'})
            else:
                return render(request,'Login/signup.html',{'msg':'Password Should not Blank'})
        else:
            return render(request,'Login/signup.html',{'msg':'Field Can not be Blank and Data should in correct Form !!'})
    else:
        return render(request,'Login/signup.html')


def signin(request):
    return render(request,'Home/signin.html')


def greetlogin(request):
    return render(request,'Login/login.html')

def userLogin(request):
    if request.method=='POST':
        formData=request.POST
        username=formData['username']
        password=formData['password']
        prof = profile.objects.get(Email=username)
        if(check_password(password,prof.Password)):
            request.session['username']=username
            return HttpResponseRedirect('http://localhost:8000/Profile/')     # After Login Student will get his Profile Account
        else:
            return render(request,'Login/login.html',{'error':'Username or Password are Incorrect'})
    else:
        s='http://localhost:8000/Login/'
        return HttpResponseRedirect(s)
    
def Logout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/www.GrievanceSystem.com/')


    
