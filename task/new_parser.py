import requests
from bs4 import BeautifulSoup

from task.models import OutputModel


def parser(url):
    try:
        if OutputModel.objects.filter(save_url=url).exists():

            j = ''
            result = OutputModel.objects.filter(save_url=url).values('save_url', 'save_title', 'save_h1',
                                                                     'save_encoding')
            list_result = [entry for entry in result]
            for i in list_result:  # хитромудрый способ вытащить данные из queryset
                k = i.values()
                e = ''
                r = 0
                for q in k:
                    r += 1
                    if r == 1:
                        e += str(q) + ' — '
                    else:
                        e += str(q) + '  '
                j += str(e)

            return j

        else:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                h1 = soup.find('h1').text.strip()
            except:
                h1 = " "

            try:
                title = soup.find('title').text.strip()
            except:
                title = " "
            header = r.headers['Content-Type']
            inf = url + " — " + title + ' | ' + h1 + ' | ' + header

            b = OutputModel(save_url=url, save_title=title,
                            save_h1=h1, save_encoding=header)
            b.save()

            return inf

    except:
        inf = str(url) + ' ошибка'
        return inf
