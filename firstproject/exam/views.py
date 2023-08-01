from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
@csrf_protect

def testpaper(request):
    return render(request,'exam/testpaper.html')

def result(request):
    if request.method=='POST':
        if request.POST['option']==str(33):
            s='Congratulations ur answer is correct'
        else:
            s='Sorry ur answer is not correct'
    else:
          s = 'Please submit form'
    msg={'data':s}
    return render(request,'exam/result.html',msg)
    

