import requests
from bs4 import BeautifulSoup


# добавить проверку, существует ли сайт
def parser(urls_name):
    links = []
    for url in urls_name:
        links.append(url.input_url)
    data = []

    for link in links:
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
        data.append((link + " — " + title + ' | ' + h1  + ' | ' + header))

    return data
