from django.db import IntegrityError
from django.test import TestCase
from datetime import date
from model_bakery import baker

from .models import Users, Products

# Create your tests here.


class UsersTestCase(TestCase):
    def setUp(self):
        Users.objects.create(
            first_name='Elon', last_name='Musk', birthdate='1996-05-15')

    def test_new_user(self):
        user = Users.objects.get(
            first_name='Elon', last_name='Musk', birthdate='1996-05-15')
        self.assertEqual(user.first_name, 'Elon')
        self.assertEqual(user.last_name, 'Musk')
        self.assertEqual(user.birthdate, date(1996, 5, 15))

    def test_user(self):
        user = baker.make(Users, first_name='Elon')
        self.assertEqual(user.first_name, 'Elon')


class ProductsTestCase(TestCase):
    def setUp(self):
        Products.objects.create(price=10000, title='Iphone',
                                description='New iphone', base_discount_percent=25.0)

    def test_new_product(self):
        products = Products.objects.get(
            price=10000, title='Iphone', description='New iphone', base_discount_percent=25.0)
        self.assertEqual(products.price, 10000)
        self.assertEqual(products.title, 'Iphone')
        self.assertEqual(products.description, 'New iphone')
        self.assertEqual(products.base_discount_percent, 25.0)
