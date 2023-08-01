from django.urls import path
from AddQuestion.views import *

urlpatterns=[
    path('',Addque),
    path('Savequestion/',saveQuestion)
]