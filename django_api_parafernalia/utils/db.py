
import json
from main.models import Users, Products


with open('/home/pho3nix/Tools/parafernalia_challange/django_api_parafernalia/utils/users.json', 'r') as users:
    data = json.load(users)
for value in data:
    users = Users(first_name=value['first_name'],
                  last_name=value['last_name'], birthdate=value['birthdate'])
    users.save()

with open('/home/pho3nix/Tools/parafernalia_challange/django_api_parafernalia/utils/products.json') as products:
    data = json.load(products)

for value in data:
    products = Products(price=value['price'], title=value['title'],
                        description=value['description'], base_discount_percent=value['base_discount_percent'])
    products.save()
