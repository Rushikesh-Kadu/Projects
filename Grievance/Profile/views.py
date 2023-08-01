from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def setProfile(request):
     user = request.session['username']
     obj = profile.objects.get(Email=user)
     prof = {'greet':obj.Name.split(' ')[0],'name':obj.Name,'email':obj.Email,'contact':obj.Contactno,'course':obj.Course,'year':obj.Year,'gender':obj.Gender}
     return render(request,'Profile/profile.html',prof)

