from django.shortcuts import render
from datetime import datetime
from .models import TaskModel
from .parser import parser

import time


#временной сдвиг??
# ввести позже очередь Queue


def text_area(requests):
    urls_name = TaskModel.objects.values()
    solutions, seconds = parser(urls_name)
    # time_now = datetime.now().strftime("%d/%m/%y %H:%M:%S")


    return render(requests, 'task.html', context={'solutions': solutions, 'seconds': seconds})


def index_page(requests):
    return render(requests, 'index.html')
