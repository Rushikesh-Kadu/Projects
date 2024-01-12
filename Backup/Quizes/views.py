from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from django.contrib.auth.models import User

@api_view(['GET'])                   # Decorator which converts Data into JSON format which is known as Web API
def getQuize(request):
    # print(request.data)
    # data = Quize.objects.filter(Title=request.data)
    data = Quize.objects.filter()
    # print(data)
    serializer = Quizeserializer( data = data, many=True)
    serializer.is_valid()
    status = 1      # Score not set Successfully
    for item in data:
        if item.Score == '0':
            status = 0
            print("Condition Matched")
        # print(item.Question ,item.Score)
    print("Status",status)
    # print(serializer.data)
    if status==1:                               # return when Score for every question is set
        return Response({
            'status':"201",
            'message':"Score set Successfully",
            'data': "Score Set Successfully",
            })
    else:                                       # return only when Score for every question is not set
        return Response({
            'status':"200",
            'message':"Quize Questions Fetched",

            'data': serializer.data,
            })


@api_view(['GET','POST'])                   # Decorator which converts Data into JSON format which is known as Web API
def setQuize(request):
    if request.method=="POST":
        data = request.data
        # print("data:",data)s
        # print("Type :",type(data))
        serializer = Quizeserializer(data = data)
        today = datetime.now()
        date = str(today.day)+"/"+str(today.month)+"/"+str(today.year)
        data['Date'] = date
        option = 'Option'+chr(64+int(data['Answer']))
        print(option)
        data['Answer'] = data[option]
        # print(data['Answer'])
        # if data['Title'].split(' ')[-1]!=date:
        #     data['Title']= data['Title']+" "+date
        data['Created_by'] = "rushikeshkadu@gmail.com"    #request.session['username'];
        # request.data.update({'Created_by':request.session['username']})
        # request.data.update({'Title': data.Title+" "+date})
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({
                'status':"True",
                'message':"valid Data", 
                'data':serializer.data
            })
        else:
            return Response({
                'status':"False",
                'message':"Invalid Data",
                'data':serializer.errors
            })
    else:
        return Response({
            'status':"False",
            'message':"Get Request is not allowed",
            'data':serializer.errors
        })



@api_view(['GET','POST'])   
def setUser(request):
    if request.method == "POST":
        user = request.data
        # print("User:",user)
        obj = Test_user()
        obj.Firstname = user['firstName']
        obj.Lastname = user['lastName']
        obj.Email = user['email']
        obj.Ph_number = user['ph_Number']
        obj.Gender = user['gender']
        obj.Password = make_password(user['password'])
        obj.Roll = user['Roll']
        obj.save()    

        return Response({
                'status':"True",
                'message':"Data Saved Successfully",
            })
    else:
         return Response({
                'status':"False",
                'message':"Something Went Wrong",
            })
    
@api_view(['GET','POST'])   
def userLogin(request):
    if request.method=='POST':
        print("Login page")
        formData=request.data
        username=formData['username']
        password=formData['password']
        roll = formData['roll']
        # print(roll)
        if roll == 'Admin Login':
            prof = User.objects.get(username=username)
            if(check_password(password,prof.password)):
                request.session['username']=username
                return Response({
                    'status':"True",
                    'message':"Admin Logged In",
                })                                              # After Login User will get Profil Account
            else:
                # print("Wrong User Credential")
                return Response({
                    'status':"401",
                    'message':"Admin Credential is not matched",
                })
        else:
            prof = Test_user.objects.get(Email=username)
            # print("Password:",check_password(password,prof.Password))
            # print("Password:",check_password(password,prof.Password))
            if(roll==prof.Roll and check_password(password,prof.Password)):
                request.session['username']=username
                print(request.session)
                # print("Session:",request.session['username'])
                # print("Logged In")
                data = {"Firstname":prof.Firstname,"Email":username}
                return Response({
                    'status':"True",
                    'message':"User Logged In",
                    'data':data
                })                                              # After Login User will get Profil Account
            else:
                # print("Wrong User Credential")
                return Response({
                    'status':"401",
                    'message':"User Credential is not matched",
                })
    else:
        # print("Something went Wrong")
        return Response({
            'status':"",
            'message':"Something Went Wrong",
        })

@api_view(['GET'])   
def getQuizeList(request):
    print(request.session.has_key('username'))
    list = []
    quizelist = []     # [{},{}]
    counter = 1
    Quizes = Quize.objects.all()
    if Quizes!='' or Quizes!=None:
        for item in Quizes:
            if item.Title.capitalize() not in list:
                list.append(item.Title.capitalize())
                quizeName = item.Title.capitalize()
                if '/' in quizeName.split(' ')[-1]:
                    quizeName = ' '.join(quizeName.split(' ')[:-1])
                quizelist.append({'id':counter,'quize':quizeName,'date':item.Date})
                counter+=1
        # print("QuizeList:",quizelist)
        # print("List:",list)
        return Response({
                'status':"True",
                'message':"Quize Fetched",
                'data':quizelist
            })
    else:
        return Response({
            'status':"False",
            'message':"Quizes are not Available",
        })


@api_view(['GET','POST'])   
def saveQuize(request):
    # print("SaveQuize")
    if request.method == "POST":
        user = request.data
        # print(user)
        for id in user:
            obj = Quize.objects.get(id=id)
            obj.Score = user[id]
            obj.save()   
        return Response({
                'status':"True",
                'message':"Data Saved Successfully",
            })
    else:
        return Response({
            'status':"False",
            'message':"Something Went Wrong",
        })
    

@api_view(['GET','POST']) 
def getUserQuize(request):
    data = Quize.objects.filter(Title=request.data['quizename'])
    serializer = Quizeserializer( data = data, many=True)
    serializer.is_valid()
    if data!='' or data!=None:
        return Response({
            'status':"True",
            'message':"valid Data", 
            'data':serializer.data
        })
    else:
        return Response({
            'status':"False",
            'message':"Invalid Data",
            'data':serializer.errors
        })


@api_view(['GET','POST']) 
def result(request):
    if request.method == "POST":
        # print("result")
        # print(request.data)
        score = 0
        total_Score = 0
        grade = ''
        result_Format = ''
        Title = ''
        formData = request.data['options']
        print("FormData:",formData)
        for id in formData:
            record = Quize.objects.get(id=id)
            if score==0:                           # it checks at once only what is the result format for this quize
                result_Format = record.Resultformat
                Title = record.Title

            # print(record.Questionformat)
            if record.Questionformat=='/Multiplechoice':
                final_answer = formData[id][0]
                print(formData[id][0])
            elif record.Questionformat=='/Checkbox':
                final_answer = ','.join(formData[id])
                print(','.join(formData[id]),len(','.join(formData[id])),type(','.join(formData[id])))
                print(record.Answer,len(record.Answer),type(record.Answer))

            if record.Answer == final_answer:
                score+=int(record.Score)
            
            # print(record.Answer,"  ",formData[id][0])
            # print(id,"  ",score)
            total_Score+=int(record.Score)
        percentage = score / total_Score * 100
        if percentage>=80:
            grade = 'A'
        elif percentage>=55:
            grade = 'B'
        else:
            grade = 'C'

        result = Result()
        data = request.data['state']['state']
        print("Data:",data,type(data))
       
        user = Test_user.objects.get(Firstname=data['Firstname'], Email = data['Email'])
        result.Firstname = user.Firstname
        result.Lastname = user.Lastname
        result.Email = user.Email
        result.Score = score
        result.Title = Title
        result.Total_score = total_Score
        result.Resultformat = result_Format
        result.save()

        if result_Format.lower() == "show a score":
            return Response({
                'status':"True",
                'message':"Score", 
                'data': "Score:"+str(score)
             })
        elif result_Format.lower() == "show a score & grade":
             return Response({
                'status':"True",
                'message':"score & grade", 
                'data': "Score:"+str(score)+"\n"+"Grade:"+grade
             }) 
        elif result_Format.lower() == "show a grade only":
             return Response({
                'status':"True",
                'message':"grade", 
                'data': "Grade:"+grade
             }) 
        # # print(score," ",total_Score)
            


