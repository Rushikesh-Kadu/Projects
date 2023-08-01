from django.db import models

class Questions(models.Model):
    Question= models.CharField(max_length=200)
    option_a= models.CharField(max_length=100)
    option_b= models.CharField(max_length=100)
    option_c= models.CharField(max_length=100)
    option_d= models.CharField(max_length=100)
    answer= models.CharField(max_length=100)
    def __str__(self):
        return self.Question
    

class CQuestions(models.Model):
    Question= models.CharField(max_length=200)
    option_a= models.CharField(max_length=100)
    option_b= models.CharField(max_length=100)
    option_c= models.CharField(max_length=100)
    option_d= models.CharField(max_length=100)
    answer= models.CharField(max_length=100)
    def __str__(self):
        return self.Question
    
class CPPQuestions(models.Model):
    Question= models.CharField(max_length=200)
    option_a= models.CharField(max_length=100)
    option_b= models.CharField(max_length=100)
    option_c= models.CharField(max_length=100)
    option_d= models.CharField(max_length=100)
    answer= models.CharField(max_length=100)
    def __str__(self):
        return self.Question
    

class History(models.Model):
    Name = models.CharField(max_length=200)
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Score = models.IntegerField()
    Sub = models.CharField(max_length=100,default=False)
    Email = models.EmailField(null=True)
    def __str__(self):
        return self.Name+"       "+str(self.Score)

