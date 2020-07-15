import aiohttp
import asyncio
loop = asyncio.get_event_loop()

async def fetch(i):
    while True:
        print(i)

connector = aiohttp.TCPConnector(limit_per_host=199)
async def main():
    # async with aiohttp.ClientSession(connector=connector) as session:
    #     for i in range(2):
    #         html = await fetch(session)
        # print(html)
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [loop.create_task(fetch(i)) for i in range (2)]
        await asyncio.gather(*tasks)
loop.run_until_complete(mainA())

import traceback
traceback.print_exc()