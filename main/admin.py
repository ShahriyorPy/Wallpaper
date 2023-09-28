from django.contrib import admin
from .models import *

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image','created_at']
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(MyPhoto, MyModelAdmin)


