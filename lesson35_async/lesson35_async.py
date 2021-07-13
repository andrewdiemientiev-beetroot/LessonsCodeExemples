import asyncio
import aiohttp
import aiofiles
import time


async def get_list(name_of_api, session):
    async with session.get(url=f"https://www.dnd5eapi.co/api/{name_of_api}/") as resp:
        return await resp.text()


async def write_to_file(filename, resp_json):
    async with aiofiles.open(filename, mode='w') as file:
        await file.write(resp_json)


async def get_resp_and_write_to_file(name_of_api, session):
    resp = await get_list(name_of_api, session)
    await write_to_file(f"{name_of_api}.txt", resp)


async def main():
    async with aiohttp.ClientSession() as session:
        t1 = asyncio.create_task(get_resp_and_write_to_file("classes", session))
        t2 = asyncio.create_task(get_resp_and_write_to_file("spells", session))
        await asyncio.gather(t1, t2)


if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    print(f"Time consumed {time.perf_counter()}")
