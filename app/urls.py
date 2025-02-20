from django.urls import path
from .views import *

urlpatterns = [
    # Restaurants urls
    path('restaurants/',get_restaurants,name='get_restaurants'),
    path('restaurants/create/',create_restaurants,name='create_restaurants'),
    path('restaurants/<int:pk>',restaurants_details,name='restaurants_details'),

    # Customer urls
    path('customer/',get_customer,name='get_customer'),
    path('customer/create/',create_customer,name='create_customer'),
    path('customer/<int:pk>',customer_details,name='customer_details'),

    # Logins urls 
    path('login/',get_login,name='get_login'),
    path('login/create/',create_login,name='create_login'),
    path('login/<int:pk>',login_details,name='login_details'),

    # Item Category Urls
    path('itemcategory/',get_itemcategory,name='get_itemcategory'),
    path('itemcategory/create/',create_itemcategory,name='create_itemcategory'),
    path('itemcategory/<int:pk>',itemcategory_details,name='itemcategory_details'),

    # Menu Urls
    path('menu/',get_menu,name='get_menu'),
    path('menu/create/',create_menu,name='create_menu'),
    path('menu/<int:pk>',menu_details,name='menu_details'),
]