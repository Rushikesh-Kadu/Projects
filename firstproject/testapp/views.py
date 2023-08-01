from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    return render(request,'testapp/greeting.html')

def showContact(request):
    return render(request,'testapp/showContact.html')

def about(request):
    return render(request,'testapp/about.html')