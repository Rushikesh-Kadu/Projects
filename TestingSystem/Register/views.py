from django.shortcuts import render
from Register.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def register(request):
    return render(request,'Register/register.html')

def saveUser(request):
    if request.method=='POST':
        formData=request.POST
        # print(formData['First_name'],formData['Last_name'],formData['Email'],formData['Password'])
        user=User()
        user.username=formData['Email']
        user_Data = User.objects.filter(username=user.username)
        # print("User Data:",user_Data,type(user_Data),'\nUsername=',user.username)
        try:                                    # If username doesn't Exist it will give the Exception DoesNotExist:
            if user_Data:
               # print("Username Exists")                                # If Username already Exist
                message={'msg':'Username Already Exist You can Login'}
                return render(request,'Login/login.html',message)
            else:
                user.password=formData['Password']
                confirm_pass = formData['Cpassword']
                if user.password==confirm_pass:                 # if password match or not
                    user.email=formData['Email']
                    user.first_name=formData['First_name']
                    user.last_name=formData['Last_name']
                    user.set_password(formData['Password'])
                    user.save()

                    TestUser = SystemUser()
                    TestUser.First_name=formData['First_name']
                    TestUser.Last_name=formData['Last_name']
                    TestUser.Email=formData['Email']
                    TestUser.save()

                    message={'msg':'Student has been Registered Successfully'}
                    return render(request,'Login/login.html',message)
                else:
                    message={'msg':'Password are Mismatched'}
                    return render(request,'Register/register.html',message)
        except:
            pass
    else:
        s='http://localhost:8000/Register/'
        return HttpResponseRedirect(s)

