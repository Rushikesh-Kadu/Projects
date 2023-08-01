from django.shortcuts import render
from .models import *
# Create your views here.
def viewContact(request):
    return render(request,'contactus/index.html')

def saveContact(request):
    if request.method=='POST':
        formData = request.POST
        contact = Contact(First_name=formData['firstName'],Last_name=formData['lastName'],Email=formData['email'],Message=formData['message'],Phone_number=formData['number'])
        contact.save()
        message={'msg':'Our team will Contact u Soon...'}
        return render(request,'contactus/index.html',message)
    else:
        return render(request,'contactus/index.html')