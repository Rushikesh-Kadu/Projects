from django.db import models

class Quize(models.Model):
    Title = models.CharField(max_length=100)
    Resultformat = models.CharField(max_length=70)
    Question = models.CharField(max_length=200)
    Questionformat = models.CharField(max_length=50)
    OptionA = models.CharField(max_length=100)
    OptionB = models.CharField(max_length=100)
    OptionC = models.CharField(max_length=100)
    OptionD = models.CharField(max_length=100)    
    Answer = models.CharField(max_length=100)   
    Date = models.CharField(max_length=100,null=True) 
    Created_by = models.CharField(max_length=200,null=True)
    Score = models.CharField(max_length=10,blank=True,default="0")
    def __str__(self):
        return self.Question


# class Test_User(models.Model): 
#     Firstname = models.CharField(max_length=100)
#     Lastname = models.CharField(max_length=100)
#     Email = models.EmailField(max_length=50,unique=True)
#     Ph_number = models.CharField(max_length=12)
#     Gender = models.CharField(max_length=20)
#     Roll = models.CharField(max_length=100,default="")
#     Password = models.CharField(max_length=500)
    
class Test_user(models.Model): 
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50,unique=True)
    Ph_number = models.CharField(max_length=12)
    Gender = models.CharField(max_length=20)
    Roll = models.CharField(max_length=100,default="")
    Password = models.CharField(max_length=500)

class Result(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50,primary_key=True)
    Title = models.CharField(max_length=100)
    Resultformat = models.CharField(max_length=70)
    Score = models.CharField(max_length=15,default='0')
    Total_score = models.CharField(max_length=15,default='0')