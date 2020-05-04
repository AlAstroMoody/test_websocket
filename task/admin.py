from django.contrib import admin

from task.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'input_url', 'input_minutes', 'input_seconds'
    ]


admin.site.register(TaskModel, TaskAdmin)
