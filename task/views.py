from django.shortcuts import render

from .models import TaskModel
from .parser import parser


#временной сдвиг??
# ввести позже очередь Queue

def text_area(requests):
    urls_name = TaskModel.objects.all()
    solutions = parser(urls_name)

    return render(requests, 'task.html', context={'solutions':solutions})

def index_page(requests):
    return render(requests, 'index.html')
