from datetime import datetime
import asyncio
import websockets
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "challenge.settings")
django.setup() 

from task.models import TaskModel
from task.new_parser import parser


async def server(websocket, path):
    for i in time_records:
        lst_timer.append(int(i.get('input_seconds')) + int(i.get('input_minutes')) * 60)
    count = 0
    while True:
        await asyncio.sleep(lst_timer[count])
        solution = parser(all_records[count].get('input_url'))
        await websocket.send(solution)
        count += 1


start_server = websockets.serve(server, "127.0.0.1", 5680)
lst_timer = []
all_records = TaskModel.objects.values('input_url')
time_records = TaskModel.objects.values('input_seconds', 'input_minutes')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()