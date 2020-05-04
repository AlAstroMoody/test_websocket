import requests
from bs4 import BeautifulSoup

from task.models import OutputModel, TaskModel


def parser(url):
    if OutputModel.objects.filter(save_url=url).exists():
        for element in OutputModel.objects.filter(save_url=url):
            url = element.save_url
            h1 = element.save_h1
            title = element.save_title
            header = element.save_encoding
            data = {'url': url, 'title': title, 'h1': h1, 'header': header, 'status': 'from_db'}
            return data
    else:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                h1 = soup.find("h1").text.strip()
            except AttributeError:
                h1 = 'отсутствует'
            try:
                title = soup.find("title").text.strip()
            except AttributeError:
                title = 'отсутствует'
            try:
                header = r.headers["Content-Type"]
            except AttributeError:
                header = 'отсутствует'
            record = TaskModel.objects.get(input_url=url)
            seconds = int(record.input_minutes)*60 + int(record.input_seconds)
            data = {'url': url, 'title': title, 'h1': h1, 'header': header, 'status': 'ok', 'seconds': seconds}
            OutputModel.objects.create(save_url=url, save_title=title,
                                       save_h1=h1, save_encoding=header, seconds=seconds)
            return data
        except ValueError:
            data = {'url': url, 'status': 'error', 'seconds': 0}
            return data
