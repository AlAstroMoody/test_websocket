import requests
from bs4 import BeautifulSoup
from .models import OutputModel


def parser(urls_name):
    lst = list(urls_name)
    links = []
    times = []
    for i in range(len(lst)):
        links.append(lst[i].get('input_url'))
        times.append(int(lst[i].get('input_minutes'))*60 + int(lst[i].get('input_seconds')))

    data = []
    data_time = []
    for time in times:
        data_time.append(time)


    for link in links:
        try:                # проверка на доступ к сайту
            if OutputModel.objects.filter(save_url=link).exists():
                j = ''
                result = OutputModel.objects.filter(save_url=link).values('save_url', 'save_title', 'save_h1', 'save_encoding')
                list_result = [entry for entry in result]
                for i in list_result:   # хитромудрый способ вытащить данные из queryset
                    k = i.values()
                    e = ''
                    r = 0
                    for q in k:
                        r += 1
                        if r ==1:
                            e += str(q) + ' — '
                        else:
                            e += str(q) + '  '
                    j += str(e)
                data.append(j)
            else:
                r = requests.get(link)
                soup = BeautifulSoup(r.text, 'lxml')
                try:
                    h1 = soup.find('h1').text.strip()
                except:
                    h1 = " "

                try:
                    title = soup.find('title').text.strip()
                except:
                    title = " "
                header = r.headers['Content-Type']
                data.append((link + " — " + title + ' | ' + h1 + ' | ' + header))

                b = OutputModel(save_url=link, save_title=title, save_h1=h1, save_encoding=header)
                b.save()
        except:
            data.append(link + ' - ошибочный url')

    return data, data_time
