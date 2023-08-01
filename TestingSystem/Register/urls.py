from django.urls import path
from Register.views import *

urlpatterns=[
    path('',register),
    path('register/',saveUser),
]