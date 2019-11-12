from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'input_url', 'input_minutes', 'input_seconds'
    ]
admin.site.register(TaskModel, TaskAdmin)
