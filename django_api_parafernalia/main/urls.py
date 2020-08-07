from django.conf.urls import url
from .views import UsersList, UsersCreate, UsersRUD
from .views import ProductsList, ProductsCreate, ProductsRUD, ProductsDiscount

urlpatterns = [

    url(r'^products/(?P<pk>[0-9]+)/?$',
        ProductsDiscount.as_view(), name='produtos-list'),

    url(r'^users/?$', UsersList.as_view(), name='usuarios-list'),
    url(r'^users/crud?/?$', UsersCreate.as_view(), name='usuarios-create'),
    url(r'^users/crud?/(?P<pk>[0-9]+)/?$',
        UsersRUD.as_view(), name='usuarios-rud'),

    url(r'^products/?$', ProductsList.as_view(), name='produtos-list'),
    url(r'^products/crud?/?$', ProductsCreate.as_view(), name='produtos-create'),
    url(r'^products/crud?/(?P<pk>[0-9]+)/?$',
        ProductsRUD.as_view(), name='produtos-rud'),

]
