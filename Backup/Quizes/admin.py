from django.contrib import admin
from Quizes.models import *
from django.contrib import admin
from .models import *

class quizeAdmin(admin.ModelAdmin):
    list_display = ['id','Question','OptionA','OptionB','OptionC','OptionD','Answer','Date']

class userAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Lastname','Email','Ph_number','Gender','Roll']

class resultAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Lastname','Email','Title','Resultformat','Score','Total_score']

admin.site.register(Quize,quizeAdmin)
admin.site.register(Test_user,userAdmin)
admin.site.register(Result,resultAdmin)

# admin.site.register(Quize)
