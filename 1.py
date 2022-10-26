from aiohttp import web
import asyncio
import time
from datetime import datetime
import env


async def handle_home(request):
    return web.Response(text='OK')


async def func(sleep, text):
    await asyncio.sleep(sleep)
    return text


async def handle_start(request):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    task1 = asyncio.create_task(func(1, "Func 1 complete"))
    task2 = asyncio.create_task(func(3, "Func 2 complete"))
    text = f"{await task1} {await task2}"
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return web.Response(text=text, status=201)


async def handle_env(request):
    return web.Response(text=env.TEST, status=201)


app = web.Application()
app.add_routes([web.get('/', handle_home),
                web.get('/start', handle_start),
                web.get('/env', handle_env)])

if __name__ == '__main__':
    web.run_app(app)
