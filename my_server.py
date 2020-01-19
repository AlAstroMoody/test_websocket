from datetime import datetime
import asyncio
import websockets
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "challenge.settings")
django.setup() 

from task.models import TaskModel, OutputModel
from task.new_parser import parser


async def server(websocket, path):
    count = 0
    while True:
        # true = 0 - url есть в базе; 1 - нет в базе, парсить; 2 - нет доступа к сайту
        solution, true = parser(all_records[count].get('input_url'))
        timer = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        if true != 0:
            await asyncio.sleep(lst_timer[count])
        if true == 2:
            data = {
            'info': solution,
            'time': f'{timer} ошибка обработки URL’a'}
        else:
            data = {
            'info': solution,
            'time': f'{timer} успешно'}
        await websocket.send(json.dumps(data))
        count += 1


start_server = websockets.serve(server, "127.0.0.1", 5001)
lst_timer = []
all_records = TaskModel.objects.values('input_url')
time_records = TaskModel.objects.values('input_seconds', 'input_minutes')
for i in time_records:
    lst_timer.append(int(i.get('input_seconds')) + int(i.get('input_minutes')) * 60)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
