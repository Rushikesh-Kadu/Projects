from django.urls import path
from .views import *

urlpatterns = [
    path('setQuize/',setQuize),
    path('getQuize/',getQuize),
    path('setUser/',setUser),
    path('userLogin/',userLogin),
    path('saveQuize/',saveQuize),
    path('getQuizeList/',getQuizeList),
      path('getUserQuize/',getUserQuize),
      path('result/',result),
]