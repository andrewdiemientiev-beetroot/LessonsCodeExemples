import asyncio


async def callee():
    await asyncio.sleep(1)
    return 'Hello'


async def caller():
    t1 = asyncio.create_task(callee())
    t1.add_done_callback(lambda f: print(f.result() + ' World'))
    await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(caller())