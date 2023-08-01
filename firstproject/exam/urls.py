from django.urls import path
from .views import *

urlpatterns=[
    path('testpaper/',testpaper),
    path('result/',result),
]