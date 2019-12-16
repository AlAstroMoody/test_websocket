from django.urls import path

from task.views import task, index_page

urlpatterns = [
    path('task/', task, name='task'),
    path('', index_page),

]
