# admin.py

from django.contrib import admin
from .models import Task
from .models import Employ,Leave


class Employadmin(admin.ModelAdmin):
 list_display = ('name',)
 list_filter = ('name',)
 search_fields = ("name",)

 


admin.site.register(Employ,Employadmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'due_date','priority') # Include fields to display in the list view
    list_filter = ('priority',)  # Add priority to list filter if needed
    search_fields = ("task",)

    fieldsets = (
        ('taxt', {
            'fields': ('task','due_date')
        }),
    )
    
admin.site.register(Task, TaskAdmin)
admin.site.site_header = 'Custom Admin Header'
admin.site.site_title = 'Custom Admin Header'

admin.site.register(Leave)


