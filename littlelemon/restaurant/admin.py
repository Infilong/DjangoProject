from django.contrib import admin
from .models import *


class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Menu, MenuModelAdmin)
admin.site.register(Booking)
