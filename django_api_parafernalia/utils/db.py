
import json
import os
from main.models import Users, Products

directory = os.environ['dir']

with open(f'{directory}/users.json', 'r') as users:
    data = json.load(users)
for value in data:
    users = Users(first_name=value['first_name'],
                  last_name=value['last_name'], birthdate=value['birthdate'])
    users.save()

with open(f'{directory}/products.json') as products:
    data = json.load(products)

for value in data:
    products = Products(price=value['price'], title=value['title'],
                        description=value['description'], base_discount_percent=value['base_discount_percent'])
    products.save()
