from django.http import HttpResponseRedirect
from django.shortcuts import render
from Attendance.models import *
from django.contrib.auth import authenticate,login,logout
import datetime


def save(request):
    att_data = request.POST
    date = att_data['date']
    subject = att_data['subject']
    id=1
    student_length=len(Student_Data.objects.all())
    if subject=='MC':
        while id<=student_length:
            a=MC_Attendance()
            stud_data=Student_Data.objects.get(stu_id=id)
            a.student_name=stud_data.student_name
            a.date=date
            if 'present'== att_data[str(id)]:
               a.attendance=1
            else:
                a.attendance=0
            a.save()
            id+=1
    elif subject=="CGMA":
        while id<=student_length:
            a=CGMA_Attendance()
            stud_data=Student_Data.objects.get(stu_id=id)
            a.student_name=stud_data.student_name
            a.date=date
            if 'present'== att_data[str(id)]:
               a.attendance=1
            else:
                a.attendance=0
            a.save()
            id+=1
    elif subject=="PHP":
        while id<=student_length:
            a=PHP_Attendance()
            stud_data=Student_Data.objects.get(stu_id=id)
            a.student_name=stud_data.student_name
            a.date=date
            if 'present'== att_data[str(id)]:
               a.attendance=1
            else:
                a.attendance=0
            a.save()
            id+=1
    elif subject=="AI":
        while id<=student_length:
            a=AI_Attendance()
            stud_data=Student_Data.objects.get(stu_id=id)
            a.student_name=stud_data.student_name
            a.date=date
            if 'present'== att_data[str(id)]:
               a.attendance=1
            else:
                a.attendance=0
            a.save()
            id+=1
    return HttpResponseRedirect('http://localhost:8000/www.HVPMcollegespace.com/')
 

def Login(request):
    res=render(request,'Attendance/login.html')
    return res

def report(request):
    res=render(request,'Attendance/reports.html')
    return res

def give_report(request):
    if request.method=="POST":
        sub=request.POST['subject']
        name=request.POST['name']
        try:
            if sub=='MC':
                a=Student_Data.objects.get(student_name=name)
                b=MC_Attendance.objects.filter(student_name__iexact=name)
                data={'data':b,'s':a}
                return render(request,'Attendance/reports.html',data)
            elif sub=='CGMA':
                a=Student_Data.objects.get(student_name=name)
                b=CGMA_Attendance.objects.filter(student_name__iexact=name)
                data={'data':b,'s':a}
                return render(request,'Attendance/reports.html',data)
            elif sub=='PHP':
                a=Student_Data.objects.get(student_name=name)
                b=PHP_Attendance.objects.filter(student_name__iexact=name)
                data={'data':b,'s':a}
                return render(request,'Attendance/reports.html',data)
            elif sub=='AI':
                a=Student_Data.objects.get(student_name=name)
                b=AI_Attendance.objects.filter(student_name__iexact=name)
                data={'data':b,'s':a}
                return render(request,'Attendance/reports.html',data)
        except:
             return render(request,'Attendance/reports.html',{"msg":"Student record doesn't Exist"})
    else:
        return render(request,'Attendance/reports.html')
  
def show(request):
    data=Student_Data.objects.all()
    return render(request,'Attendance/studentData.html',{"data":data})
   
# def save_attendance(request,id,name,presenty,sub,date):
#         if sub=='MC':
#             a=MC_Attendance()
#             a.student_name=name
#             a.date=date
#             a.attendance=presenty
#             a.save()
#             # b=MC_Attendance.objects.filter(student_name=name)
#             s=Student_Data.objects.all()
#             d=name
#             now=datetime.datetime.now()
#             x=now.strftime("%d-%m-")
#             y=str(now.year)
#             x+=y
#             data={'data':s,'d':d,'date':x}
#             return render(request,'Attendance/attendance.html',data)
#         elif sub=="CGMA":
#             a=CGMA_Attendance()
#             a.student_name=name
#             a.date=date
#             a.attendance=presenty
#             a.save()
#             s=Student_Data.objects.all()
#             d=name
#             now=datetime.datetime.now()
#             x=now.strftime("%d-%m-")
#             y=str(now.year)
#             x+=y
#             data={'data':s,'d':d,'date':x}
#             return render(request,'Attendance/attendance.html',data)
#         elif sub=="PHP":
#             a=PHP_Attendance()
#             a.student_name=name
#             a.date=date
#             a.attendance=presenty
#             a.save()
#             s=Student_Data.objects.all()
#             d=name
#             now=datetime.datetime.now()
#             x=now.strftime("%d-%m-")
#             y=str(now.year)
#             x+=y
#             data={'data':s,'d':d,'date':x}
#             return render(request,'Attendance/attendance.html',data)
#         elif sub=="AI":
#             a=AI_Attendance()
#             a.student_name=name
#             a.date=date
#             a.attendance=presenty
#             a.save()
#             s=Student_Data.objects.all()
#             d=name
#             now=datetime.datetime.now()
#             x=now.strftime("%d-%m-")
#             y=str(now.year)
#             x+=y
#             data={'data':s,'d':d,'date':x}
#             return render(request,'Attendance/attendance.html',data)


def take_attendance(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            s=Student_Data.objects.all()
            now=datetime.datetime.now()
            x=now.strftime("%d-%m-")
            y=str(now.year)
            x+=y
            data={'data':s,'date':x}
            return render(request,'Attendance/attendance.html',data)
        else:
            data['error']='Username or password is incorrect'
            return render(request,'Attendance/login.html',data)
    else:
        return HttpResponseRedirect('http://localhost:8000/Attendance/login/')
    
def add_data(request):
    return render(request,'Attendance/login1.html')

def add_dataLogin(request):
     data={}
     if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            res=render(request,'Attendance/add_data.html')
            return res
    
        else:
            data['error']='Username or password is incorrect'
            return render(request,'Attendance/login1.html',data)

     else:
        return render(request,'Attendance/login1.html')

def signup(request):
    if request.method=='POST':
        d1=Student_Data()
        formdata=request.POST
        d1.stu_id=formdata['st_id']
        d1.student_name=formdata['st_name']
        d1.roll_no=formdata['st_rollno']
        d1.sem=formdata['st_sem']
        d1.save()
        x={'data':'Record added Successfully!'}
        return render(request,'Attendance/add_data.html',x)