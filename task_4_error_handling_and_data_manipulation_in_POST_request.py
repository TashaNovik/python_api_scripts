import requests
import json

def create_post(title, body, userId=1):
    """Создает новый пост и выводит его ID и содержимое."""

    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    data = {
        'title': title,
        'body': body,
        'userId': userId
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Поднимает исключение для плохих статусов (4xx или 5xx)

        new_post = response.json()
        print("Создан новый пост:")
        print(f"  ID: {new_post['id']}")
        print(f"  Содержимое: {new_post}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Ошибка обработки ответа: {e}")
        print(response.text)


if __name__ == '__main__':
    title = input("Введите заголовок поста: ")
    body = input("Введите текст поста: ")
    create_post(title, body)