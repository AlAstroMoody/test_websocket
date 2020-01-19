import requests

from bs4 import BeautifulSoup

from task.models import OutputModel


def parser(url):
    if OutputModel.objects.filter(save_url=url).exists(): 
        for element in OutputModel.objects.filter(save_url=url):
            url = element.save_url
            h1 = element.save_h1
            title = element.save_title
            header = element.save_encoding
        inf = f'{url} — {title} {h1} {header}'
        return inf, 0 
    else:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                h1 = '\n' + f'H1: {soup.find("h1").text.strip()}'
            except:
                h1 = ""
            try:
                title = '\n' + f'Заголовок: {soup.find("title").text.strip()}'
            except:
                title = ""
            try:
                header = '\n' + f'Кодировка страницы: {r.headers["Content-Type"]}'
            except:
                header = "" 
            inf = f'{url} — {title} {h1} {header}'
            b = OutputModel(save_url=url, save_title=title,
                            save_h1=h1, save_encoding=header)
            b.save()
            return inf, 1

        except:
            inf = f'{url}'
            return inf, 2
