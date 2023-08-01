from django.shortcuts import render
from QuestionPaper.models import *

def Addque(request):
    return render(request,'AddQuestion/addquestion.html')

def saveQuestion(request):
    if request.method=='POST':
        Question = Questions()
        if request.POST['Subject'].lower()=='python':
            Question.Question=request.POST['Question']
            Question.option_a=request.POST['Option_a']
            Question.option_b=request.POST['Option_b']
            Question.option_c=request.POST['Option_c']
            Question.option_d=request.POST['Option_d']
            Question.answer=request.POST['Answer']
            Question.save()
            msg='Question Added Successfully...'
            Msg={'msg':msg}
            return render(request,'AddQuestion/addquestion.html',Msg)
