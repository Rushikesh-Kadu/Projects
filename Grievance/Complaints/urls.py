from django.urls import path
from Complaints.views import *


urlpatterns=[
    path('',complaintForm),
    path('complaint/',complaint),
    path('anonymous/',anonymousComplaintForm),
    path('anonymousform/',anonymousComplaint),
    path('solved/',solvedComplaints),
    path('unsolved/',unSolvedComplaints),
    path('inprocess/',inProcessComplaints),
    path('statistic/',generate_graph),
]