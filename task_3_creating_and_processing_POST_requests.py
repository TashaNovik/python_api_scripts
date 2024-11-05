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
    response = requests.post(url, headers=headers, data=json.dumps(data))
    new_post = response.json()
    print("Создан новый пост:")
    print(f"  ID: {new_post['id']}")
    print(f"  Содержимое: {new_post}")



if __name__ == '__main__':
    title = input("Введите заголовок поста: ")
    body = input("Введите текст поста: ")
    create_post(title, body)