from django.contrib import admin
from Profile.models import profile

class profileAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Contactno','Course','Year','Gender']

admin.site.register(profile,profileAdmin)