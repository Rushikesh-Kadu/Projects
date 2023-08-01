from django.db import models

class Contact(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=12)
    Message = models.CharField(max_length=3000)
    def __str__(self):
        return self.First_name+" "+self.Last_name