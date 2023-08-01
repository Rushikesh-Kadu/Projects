from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return HttpResponse('<h1>Be a pro with django & react </h1>')