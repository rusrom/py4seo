import asyncio
from time import sleep


async def coro_one():
    while True:
        await asyncio.sleep(0.01)
        # sleep(0.01) #  Will run only coro_one() because no await keyword (syncro code with infinite loop)
        # await sleep(0.01) # TypeError: object NoneType can't be used in 'await' expression
        print(" >>>>>>>>>> Coro 1 Working!")

async def coro_two():
    while True:
        await asyncio.sleep(0.04)
        print("Coro 2Working! >>>>>>>>>>")

task1 = asyncio.Task(coro_one())
task2 = asyncio.Task(coro_two())

runer = asyncio.gather(task1, task2)

loop = asyncio.get_event_loop()
loop.run_until_complete(runer)
