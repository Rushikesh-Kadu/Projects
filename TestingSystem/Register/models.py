from django.db import models
from django.contrib.auth.models import *

class SystemUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    def __str__(self):
        return self.First_name+" "+self.Last_name