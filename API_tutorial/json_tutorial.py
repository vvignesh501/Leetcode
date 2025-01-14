import aiohttp
import asyncio
import json
import pprint
from API_tutorial import *


async def request_api():
    conn = aiohttp.TCPConnector(limit_per_host=5)

    with open('restaurants.json') as fopen:
        datas = fopen.read()
        datas = json.loads(datas)
        # map works with a function. Lambda does the job of converting to a function
        # and using it as an iterable.
        address = list(map(lambda d: str(d['fields'].get('address', '')), datas))
        replaced_word = map(lambda d: d.replace(' ', '//'), address)
        words = list(replaced_word)
        for word in words:
            print(word)
        split_word = list(word.split('//') for word in words)
        print(split_word)

    # async with aiohttp.ClientSession(connector=conn) as session:
    #     async with session.get('https://dummyjson.com/products/1') as response:
    #         json_data = await json.loads(response.text())
    #         images = json_data['images']
    #         for idx, val in enumerate(images):
    #             json_data['images'][idx] = str(val).replace(':', '?')
    #         pprint.pprint(json)

asyncio.run(request_api())