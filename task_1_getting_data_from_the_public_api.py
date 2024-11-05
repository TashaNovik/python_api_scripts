import asyncio
import aiohttp

async def fetch_posts(response, data):  # Добавили response в аргументы
    for i in range(min(5, len(data))):
        post = data[i]
        print(f"Пост {i+1}:")
        print("Заголовки:")
        for key, value in response.headers.items():  # Используем response.headers
            print(f"  {key}: {value}")
        print("Тело:")
        print(post)
        print("---")

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return response, data # Возвращаем и response, и data
                else:
                    print(f'Error: {response.status}')
                    return None, None # Возвращаем None, если ошибка

        except aiohttp.ClientError as e:
            print(f"Connection error: {e}")
            return None, None # Возвращаем None, если ошибка


async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response, data = await fetch_data(url) # Получаем и response, и data
    if data: # Проверяем, что data не None
       await fetch_posts(response, data)  # Передаем response в fetch_posts


if __name__ == '__main__':
    asyncio.run(main())