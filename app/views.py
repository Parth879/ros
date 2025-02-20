from .models import *
from django.shortcuts import render
from rest_framework import status
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# Restaurants Apis
@api_view(['GET'])
def get_restaurants(request):
    restaurant = Restaurants.objects.all()
    serializer = RestaurantSerializer(restaurant,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_restaurants(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def restaurants_details(request,pk):

    try:
        restaurant = Restaurants.objects.get(pk=pk)
    except Restaurants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Customer Apis
@api_view(['GET'])
def get_customer(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def customer_details(request,pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Login Apis
@api_view(['GET'])
def get_login(request):
    login = Logins.objects.all()
    serializer = LoginSerializer(login,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def login_details(request,pk):
    try:
        login = Logins.objects.get(pk=pk)
    except Logins.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoginSerializer(login)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LoginSerializer(login,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ItemCategory Apis
@api_view(['GET'])
def get_itemcategory(request):
    itemcategory = ItemCategory.objects.all()
    serializer = ItemCategorySerializer(itemcategory,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_itemcategory(request):
    serializer = ItemCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def itemcategory_details(request,pk):
    try:
        itemcategory = ItemCategory.objects.get(pk=pk)
    except ItemCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemCategorySerializer(itemcategory)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ItemCategorySerializer(itemcategory,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        itemcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Menus Apis
@api_view(['GET'])
def get_menu(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_menu(request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def menu_details(request,pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuSerializer(menu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

