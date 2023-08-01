"""Grievance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

admin.site.site_url='http://localhost:8000/www.GrievanceSystem.com/'
admin.site.site_title='Admin Panel'
admin.site.site_header='Admin Panel'

urlpatterns = [
    path('Addcomplaints/',include('Complaints.urls')),
    path('Profile/',include('Profile.urls')),
    path('www.GrievanceSystem.com/',include('Home.urls')),
    path('Contact/',include('contactus.urls')),
    path('jet/',include('jet.urls','jet')),
    path('admin/', admin.site.urls),
    path('Login/',include('Login.urls')),
]

