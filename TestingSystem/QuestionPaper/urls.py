from django.urls import path
from QuestionPaper.views import *

urlpatterns=[
    path('Quepaper/<str:sub>/',Quepaper),
    path('checkAns/<str:sub>/',checkAns),
    path('result/',result),
    path('history/',history),
    path('statistics/',statistics),
]