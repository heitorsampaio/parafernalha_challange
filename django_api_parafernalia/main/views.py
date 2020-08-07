from collections import OrderedDict
from datetime import date

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from requests.exceptions import ConnectionError
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Users
from .serializers import ProductsSerializer, UserSerializer

# Create your views here.


class UsersList(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UsersCreate(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsersRUD(APIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        try:
            users = Users.objects.get(pk=pk)
            serializer = self.serializer_class(users)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            msg = {'error': 'User not found.'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        users = Users.objects.get(pk=pk)
        serializer = self.serializer_class(users, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            users = Users.objects.get(pk=pk)
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(message, status=status.HTTP_404_NOT_FOUND)


class ProductsList(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductsCreate(APIView):
    serializer_class = ProductsSerializer

    def post(self, request, format=None):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            msg = {'error': 'Base discount above allowed (25%)'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class ProductsRUD(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, pk):
        products = Products.objects.get(pk=pk)
        serializer = self.serializer_class(products)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        products = Products.objects.get(pk=pk)
        serializer = self.serializer_class(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            products = Products.objects.get(pk=pk)
            products.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(message, status=status.HTTP_404_NOT_FOUND)


class ProductsDiscount(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, pk, format=None):
        try:
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many=True)

            id_products = [i['id'] for i in serializer.data]

            re_list = []
            for idp in id_products:
                re = requests.get(
                    f'http://localhost:3000/api/discounts/{idp}/{pk}').json()
                product = list(products.filter(pk=idp).values())
                product.append(re)
                product_o = OrderedDict(product[0], **product[1])
                re_list.append(product_o)

            return Response(data=re_list, status=status.HTTP_200_OK)

        except ConnectionError:
            msg = {'error': 'Server is not running'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as message:
            re = requests.get(f'http://localhost:8000/products/').json()
            return Response(data=re, status=status.HTTP_200_OK)
