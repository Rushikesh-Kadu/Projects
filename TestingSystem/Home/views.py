from django.shortcuts import render
from QuestionPaper.models import *

def Home(request):
    return render(request,'Home/home.html')


def highStatistics(request):
    Data={}

    queryset = History.objects.order_by('-Score')           # Fetching score data from the History table 
    for record in queryset:
        if record.Name not in list(Data.keys()): 
            Data[record.Name]=record.Score
    
    high_Score = list(Data.keys())
    learners = len(high_Score)
    first = high_Score[0]
    second = high_Score[1]
    third = high_Score[2]

    data=[]
    for key in Data:
        data.append([key,Data[key]])

    dict_data={'Data':data,'first':first,'second':second,'third':third,'learner':learners}
    return render(request,'Home/highstat.html',dict_data)