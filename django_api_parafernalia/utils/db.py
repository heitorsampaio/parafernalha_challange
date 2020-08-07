
import json
import requests
from requests import Request, Session


def users():
    with open('users.json', 'r') as users_file:
        datas = json.load(users_file)

    for i in datas:
        requests.post('http://127.0.0.1:8000/users/crud', data=i)

    print('User data inserted')


def products():
    with open('products.json', 'r') as products_file:
        datas = json.load(products_file)

    for i in datas:
        requests.post('http://127.0.0.1:8000/products/crud', data=i).json()

    print('Products data inserted')


if __name__ == "__main__":
    users()
    products()
