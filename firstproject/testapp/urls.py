from django.urls import path
from .views import *

urlpatterns=[
    path('',greeting),
    path('contact/',showContact),
    path('about/',about),
]

