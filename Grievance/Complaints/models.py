from django.db import models

class Complaints(models.Model):
    User = models.CharField(max_length=100)
    Subject = models.CharField(max_length=200)
    Type_of_complaint = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    Status = models.CharField(max_length=60,choices=([
    ('pending', 'pending'),
    ('process', 'process'),
    ('solved', 'solved'),
    ]))
    Date = models.CharField(max_length=20,null=True)
    Email = models.EmailField(null=True,default='')
    SearchableFields = ['Status']
    def __str__(self):
        return str(self.User)
    
    
class ExamComplaints(models.Model):
    User = models.CharField(max_length=100)
    Subject = models.CharField(max_length=200)
    Type_of_complaint = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    Status = models.CharField(max_length=60,choices=([
    ('pending', 'pending'),
    ('process', 'process'),
    ('solved', 'solved'),
    ]))
    Date = models.CharField(max_length=20,null=True)
    Email = models.EmailField(null=True,default='')
    SearchableFields = ['Status']
    Filter = ['Status']
    def __str__(self):
        return str(self.User)
    

class AnonymousComplaint(models.Model):
    Subject = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Status = models.CharField(max_length=60)
    Date = models.CharField(max_length=20,null=True)
    def __str__(self):
        return str(self.Subject)
    

class AnonymousComplaintUser(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(null=True,default='')
    def __str__(self):
        return str(self.Name)