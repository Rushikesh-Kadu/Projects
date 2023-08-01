from django.urls import path
from .views import *

urlpatterns=[
    path('',viewContact),
    path('saveContact/',saveContact),
]