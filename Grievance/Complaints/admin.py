from django.contrib import admin
from Complaints.models import *

class comlaintAdmin(admin.ModelAdmin):
    list_display = ['User','Subject','Type_of_complaint','Status','Date']
    search_fields = Complaints.SearchableFields

class examcomlaintAdmin(admin.ModelAdmin):
    list_display = ['User','Subject','Type_of_complaint','Status','Date']
    search_fields = ExamComplaints.SearchableFields

class anonymouscomlaintAdmin(admin.ModelAdmin):
    list_display = ['Subject','Description','Status','Date']


class anonymouscomlaintuserAdmin(admin.ModelAdmin):
    list_display = ['Name','Email']

admin.site.register(Complaints,comlaintAdmin)
admin.site.register(ExamComplaints,examcomlaintAdmin)
admin.site.register(AnonymousComplaint,anonymouscomlaintAdmin)
admin.site.register(AnonymousComplaintUser,anonymouscomlaintuserAdmin)
