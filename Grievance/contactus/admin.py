from django.contrib import admin
from .models import Contact

class contactAdmin(admin.ModelAdmin):
    list_display=['First_name','Last_name','Email','Phone_number','Message']

admin.site.register(Contact,contactAdmin)