from django.contrib import admin

from .models import Record
# Register your models here.

from django.contrib.auth.models import Group, User

class Video(admin.ModelAdmin):
    readonly_fields = ['video']
    list_display = ['client', 'time']

admin.site.register(Record, Video)

admin.site.unregister(Group)
admin.site.unregister(User)