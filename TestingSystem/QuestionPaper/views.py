from django.shortcuts import render
from random import randrange
from QuestionPaper.models import *
from datetime import datetime
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt

def statistics(request):
    x=[]            #Tests
    y=[]            #Marks

    name=''
    queryset = History.objects.order_by('Score')           # Fetching score data from the History table 
    test_no=1
    for record in queryset:
        x.append(test_no)
        y.append(record.Score)
        name=record.Name
        test_no+=1

    highest_score = y[-1]
    lowest_score = y[0]
    failed = y.count(0)
    # print(highest_score,lowest_score,failed)      #Printing Scores
    # plt.plot(x,y)
    # plt.xlabel("Tests")
    # plt.ylabel("Marks")
    # plt.title("Test Scores Graphically")
    # plt.show()          # display graph after fetching score and test numbers into x and y list

    axes={'x':x,'y':y,'high':highest_score,'low':lowest_score,'failed':failed,'name':name}
    return render(request,'QuestionPaper/statistics.html',axes)




@login_required(login_url='http://localhost:8000/Login/')
def Quepaper(request,sub):
    if 'username' in request.session:
        s=set()
        while len(s)<=7:
            x=randrange(1,42)
            if x!=2:
              s.add(x)
        que_list=[]
        que_no=1

        if sub=='python':
            for index in s:
                questions = Questions.objects.get(id=index)
                que_list.append([questions.id,questions.Question,questions.option_a,questions.option_b,questions.option_c,questions.option_d,que_no])
                que_no+=1
        elif sub=='c':
            for index in s:
                questions = CQuestions.objects.get(id=index)
                que_list.append([questions.id,questions.Question,questions.option_a,questions.option_b,questions.option_c,questions.option_d,que_no])
                que_no+=1
        elif sub=='cpp':
            for index in s:
                questions = CPPQuestions.objects.get(id=index)
                que_list.append([questions.id,questions.Question,questions.option_a,questions.option_b,questions.option_c,questions.option_d,que_no])
                que_no+=1
     
        que={'Que':que_list,'sub':sub}
        return render(request,'QuestionPaper/quepaper.html',que)

def checkAns(request,sub):
    if request.method=='POST':
      attempt=len(request.POST)-1
      correct_ans=0
      wrong_ans=0
      ans=request.POST
      for id in ans:
         if id!='csrfmiddlewaretoken':
            if sub=='python':
                obj=Questions.objects.get(id=int(id))
            elif sub=='c':
                obj=CQuestions.objects.get(id=int(id))
            elif sub=='cpp':
                obj=CPPQuestions.objects.get(id=int(id))

            # print(ans[id].lower(),obj.answer.lower())
            if ans[id].lower()==obj.answer.lower():
                correct_ans+=1
            else:
               wrong_ans+=1
      if correct_ans>=3:
          msg='Congrats!! You are Passsed'
      else:
          msg='Sorry!! You are Fail'
    d={'correct':correct_ans,'wrong':wrong_ans,'attempt':attempt,'msg':msg}

    history=History()                               #Saving History of current user in History Table
    user=User.objects.get(username=request.session['username'])
   # print(user.username,user.first_name,user.last_name,user.password)
    history.Name = user.first_name+" "+user.last_name
    today=datetime.today()
    history.Date=str(today.day)+"/"+str(today.month)+"/"+str(today.year)
    history.Time=str(today.strftime("%I:%M %p"))
    history.Score = correct_ans
    history.Email = user.email
    history.Sub = sub.capitalize()
    history.save()

    return render(request,'QuestionPaper/result.html',d)


def result(request):
   return render(request,'result.html')

def history(request):
    if 'username' in request.session:
        user=User.objects.get(username=request.session['username'])
        his=History.objects.filter(Email=user.email)
        for x in his:
            name=x.Name
            break
        user_data={'data':[],'name':name}
        id=1
        for x in his:
             user_data['data'].append([id,x.Name,x.Date,x.Time,x.Score,x.Sub])
             id+=1
    
        return render(request,'QuestionPaper/history.html',user_data)