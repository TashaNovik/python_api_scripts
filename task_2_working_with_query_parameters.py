import asyncio
import aiohttp

# город, введенный пользователем - это параметр запроса
# из ответа нужно только вывести температуру и описание погоды
async  def fetch_data_(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    print(f'Error: {response.status}')
                    return None
        except aiohttp.ClientError as e:
            print(f"Connection error: {e}")
            return None


async def print_weather(data):
    if data and 'name' in data and 'main' in data and 'weather' in data:  # Проверка наличия ключей
        print(f"Город: {data['name']}, "
              f"Температура: {data['main']['temp']}°C, "  
              f"Описание погоды: {data['weather'][0]['description']}")
    elif data and 'cod' in data and data['cod'] != 200:  # Проверка на ошибку от API
        print(f"Error: {data.get('message', 'Unknown error')}")  # Вывод сообщения об ошибке
    else:
        print("Ошибка получения данных о погоде.")


async def main(city):
    api_key = '35004922030a00907407ab7d030b3d9b'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru&units=metric"
    # Добавили units=metric для температуры в Цельсиях и lang=ru для русского языка.
    data = await fetch_data_(url)
    if data: # Проверяем, что data не None
       await print_weather(data)  # Передаем response в fetch_posts_

if __name__ == '__main__':
    city = input('Город: ')
    asyncio.run(main(city))
