import asyncio
from aiohttp import ClientSession
import time

url_1 = 'https://www.7timer.info/bin/astro.php?lon=36.2304&lat=49.9935&output=json'
url_2 = 'https://api.open-meteo.com/v1/forecast?latitude=49.9935&longitude=36.2304&current_weather=True'
url_3 = 'https://www.metaweather.com/api/location/922137/'


async def temp_timer(site, session):
    async with session.get(site) as resp:
        if resp.status == 200:
            result = await resp.json(content_type='text/html')
            temperature = result['dataseries'][0]['temp2m']
            print(f"{site}")
    await asyncio.sleep(1)
    return temperature


async def temp_meteo(site, session):
    async with session.get(site) as resp:
        if resp.status == 200:
            result = await resp.json()
            temperature = result['current_weather']['temperature']
            print(f"{site}")
    await asyncio.sleep(1)
    return temperature


async def temp_weather(site, session):
    async with session.get(site) as resp:
        if resp.status == 200:
            result = await resp.json()
            temperature = result['consolidated_weather'][0]['the_temp']
            print(f"{site}")
    await asyncio.sleep(1)
    return temperature


async def main():
    async with ClientSession() as session:
        res = await asyncio.gather(temp_timer(url_1, session), temp_meteo(url_2, session), temp_weather(url_3, session))
    return round(sum(res) / len(res), 2)


if __name__ == '__main__':
    start = time.time()
    print(f'Started')
    print(f'Average temperature: {asyncio.run(main())}')
    print(f'Ended in {round(time.time() - start, 5)}')