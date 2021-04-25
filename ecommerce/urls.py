from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include, re_path
from . import views
from .views import register, homeMain, about, signin, logout_views, UniqueProduct, search
from carts.views import cart, update_cart, delete_cart
from orders.views import checkout, orders, time_shipping
from accounts.views import profile
urlpatterns = [ 
    # first page, before sign in
    # path('', home, name='home'),
    path('', homeMain, name="homeMain"),
    # to introduce company
    path('about', about, name='about'),
    # to sign in
    path('signin', signin, name='signin'),
    #  to register
    path('register', register, name='register'),
    # to log out
    path("logout", logout_views, name="logout"),
    # this link is to display product after log in
    # This link is for searching, s for search
    url(r'^s/$',search, name='search'),
    # to specific product, have a unique slug (slug is the unique code for a product), and id of product
    # url(r'^product/(?P<slug>[\w-]+)/(?P<id>\d+)/$', product, name='product'),
    #     (?P<all_items>.*)
    #  if use "\d+" to make the url only digit:     (?P<id>\d+)
    # To show unique product
    path('<slug:slug>UniqueProduct', UniqueProduct , name='product'),
    # To show cart
    path('cart', cart, name='cart'),
    # To change the cart
    url(r'^cart/(?P<slug>[\w-]+)/$',update_cart, name='update_cart'),
    # To remove item
    url(r'^cart/delete/(?P<slug>[\w-]+)/$',delete_cart, name='delete_cart'),
    # To checkout
    path('checkout', checkout , name='checkout'),

    # Order of costumers
    path('orders', orders , name='orders'),

    # the profile of costumer
    path('profile', profile, name='profile'), 
    path('time_shipping', time_shipping, name='time_shipping'), 
]
