from django.shortcuts import render


def task(request):
    return render(request, 'task/task.html')

def index_page(requests):
    return render(requests, 'task/index.html')
