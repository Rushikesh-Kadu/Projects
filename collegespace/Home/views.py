from django.shortcuts import render

def home(request):
    return render(request,'Home page/index.html')



    data=[]
    for key in Data:
        data.append([key,Data[key]])

    dict_data={'Data':data,'first':first,'second':second,'third':third,'learner':learners}
    return render(request,'Home/highstat.html',dict_data)