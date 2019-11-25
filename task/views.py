from django.shortcuts import render
from datetime import datetime

from .models import TaskModel
from .new_parser import parser
import time


def task(request):
    all_records = TaskModel.objects.values('input_url')
    time_records = TaskModel.objects.values('input_seconds', 'input_minutes')
    lst_timer = []
    for i in time_records:
        lst_timer.append(int(i.get('input_seconds')) + int(i.get('input_minutes'))*60)
    count = 0
    for i in all_records: # осталось заставить этот цикл работать
        time.sleep(lst_timer[count])
        solution = parser(i.get('input_url'))
        count += 1
        return render(request, 'task.html', context={'solution': solution, 'time': datetime.now().strftime("%d/%m/%y %H:%M:%S")})

def index_page(requests):
    return render(requests, 'index.html')
