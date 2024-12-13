import asyncio
from aiohttp import ClientSession


async def get_city_info(*, city: str) -> dict:
    async with ClientSession() as session:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params={'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as responce:
            weather_json = await responce.json()
            try:
                return f'{city}: {weather_json['weather'][0]['main']}'
            except KeyError:
                print('Данных нет')


cities = ['Moscow', 'Dubai', 'Kotovo', 'London', 'New York', 'Sochi']


async def main(cities_):
    tasks = []

    for city in cities_:
        tasks.append(asyncio.create_task(get_city_info(city=city)))

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


asyncio.run(main(cities_=cities))