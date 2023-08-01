from django.db import models


class profile(models.Model):
    Password = models.CharField(max_length=200,default='')
    Name = models.CharField(max_length=200,null=True)
    Email = models.EmailField(primary_key=True,null=False)
    Contactno = models.CharField(max_length=12,null=True)
    Course = models.CharField(max_length=50,null=False)
    Year = models.CharField(max_length=50,null=False)
    Gender = models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.Name)
