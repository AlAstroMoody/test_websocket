from datetime import datetime
import asyncio
import websockets

# не работает импорт
# from .models import TaskModel
# from .new_parser import parser


async def server(websocket, path):
    # for i in time_records:
    #     lst_timer.append(int(i.get('input_seconds')) + int(i.get('input_minutes')) * 60)
    # count = 0
    while True:
        timer = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        # await asyncio.sleep(lst_timer[count])
        # solution = parser(all_records[count].get('input_url'))
        #await websocket.send(solution)
        await websocket.send(timer)
        await asyncio.sleep(1)
        # count += 1


start_server = websockets.serve(server, "127.0.0.1", 5680)
lst_timer = []
# all_records = TaskModel.objects.values('input_url')
# time_records = TaskModel.objects.values('input_seconds', 'input_minutes')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()