import asyncio
import json
import os
from datetime import datetime
from queue import Queue

import django
import websockets

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "challenge.settings")
django.setup()

from task.models import TaskModel
from task.new_parser import parser


async def server(websocket, path):
    print('Сервер запущен!')
    while True:
        # раз в пять секунд проверка не появилось ли новых url, если очередь пуста.
        # ошибочный подход, но как изменить?
        while q.qsize() == 0:
            await cycle()
            if q.qsize() == 0:
                await asyncio.sleep(5)
        try:
            solution = parser(q.get())
            timer = datetime.now().strftime("%d/%m/%y %H:%M:%S")
            if solution['status'] == 'ok':
                await asyncio.sleep(solution['seconds'])
            if solution['status'] == 'error':
                data = {
                    'info': solution['url'],
                    'time': f'{timer} ошибка обработки URL’a'
                }
            else:
                data = {
                    'info': f"{solution['url']} - \n\ttitle: {solution['title']}, "
                            f"\n\tH1: {solution['h1']}, \n\theader: {solution['header']}",
                    'time': f"{timer} успешно"
                }
            await websocket.send(json.dumps(data))

        except IndexError:
            data = {
                'info': "Кажется в базе нет записей",
                'time': "Попытаемся ещё через 60 секунд"
            }
            await websocket.send(json.dumps(data))
            await asyncio.sleep(60)


async def cycle():
    queryset = TaskModel.objects.all()
    for value in queryset.values('input_url'):
        if value['input_url'] not in url_lst:
            q.put(value['input_url'])
            url_lst.append(value['input_url'])


start_server = websockets.serve(server, "127.0.0.1", 5001)
q = Queue()
url_lst = ['']

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
