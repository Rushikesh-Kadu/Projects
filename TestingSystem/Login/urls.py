from django.urls import path
from Login.views import *

urlpatterns=[
    path('',greetlogin),
    path('userLogin/',userLogin,name='login'),
    path('test/',test),
    path('Logout/',Logout),
]