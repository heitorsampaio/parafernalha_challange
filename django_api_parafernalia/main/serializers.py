from rest_framework import serializers
from .models import Products, Users


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = Users
        fields = '__all__'
