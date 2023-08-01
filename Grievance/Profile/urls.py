from django.urls import path
from Profile.views import *

urlpatterns=[
    path('',setProfile),
]