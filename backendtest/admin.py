from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    fields = ['real_name', 'tz', 'start_activity', 'end_activity']

admin.site.register(User,UserAdmin)
