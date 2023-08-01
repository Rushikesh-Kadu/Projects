from django.urls import path
from Login.views import *

urlpatterns=[
    path('signin/',signin),
    path('',greetlogin),
    path('userLogin/',userLogin),
    path('register/',register),
    path('signup/',signup),
    path('Logout/',Logout),
]