from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','start_time']
    search_fields = ['title']
    list_filter = ['title','start_time']
    
