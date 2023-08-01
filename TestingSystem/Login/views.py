from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

def greetlogin(request):
    return render(request,'Login/login.html')

def userLogin(request):
    if request.method=='POST':
        formData=request.POST
        username=formData['username']
        password=formData['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return render(request,'Login/starttest.html')
        else:
            data={}
            data['error']='Username or Password are Incorrect'
            return render(request,'Login/login.html',data)
    else:
        s='http://localhost:8000/Login/'
        return HttpResponseRedirect(s)
    
def test(request):
    if 'username' in request.session:
        return render(request,'Login/starttest.html')

def Logout(request):
    logout(request)
    return render(request,'Login/login.html')


    
