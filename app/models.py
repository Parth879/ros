from django.db import models

# Create your models here.

CHOICE = [
    ("ADMIN", "Admin"),
    ("CHEF", "Chef"),
    ("COWORKER", "Coworker"),
]


class Restaurants(models.Model):
    name            =   models.CharField(max_length=255)
    owner_name      =   models.CharField(max_length=255)
    phone_number    =   models.CharField(max_length=15)
    email           =   models.EmailField(unique=True)
    gst_number      =   models.CharField(max_length=255,blank=True)
    food_license    =   models.CharField(max_length=255,blank=True)
    created_at      =   models.DateTimeField(auto_now_add=True, db_index=True)
    is_active       =   models.BooleanField(default=True)

class Customer(models.Model):
    name            =   models.CharField(max_length=255)
    mobile          =   models.CharField(max_length=15)
    restaurants     =   models.ForeignKey(Restaurants,on_delete=models.SET_NULL,blank=True,null=True)
    created_at      =   models.DateTimeField(auto_now_add=True, db_index=True)

class Logins(models.Model):
    login_id        =   models.CharField(max_length=255)
    login_password  =   models.CharField(max_length=255)
    choices         =   models.CharField(max_length=255,choices=CHOICE)
    restaurants     =   models.ForeignKey(Restaurants,on_delete=models.SET_NULL,blank=True,null=True)
    is_active       =   models.BooleanField(default=True)

class Table(models.Model):
    table_number    =   models.IntegerField()
    restaurants     =   models.ForeignKey(Restaurants,on_delete=models.SET_NULL,blank=True,null=True)

class ItemCategory(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='category_image',null=True,blank=True)

class Menu(models.Model):
    item_name       =   models.CharField(max_length=255)
    item_category   =   models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    image           =   models.ImageField(upload_to='disease')
    price           =   models.IntegerField()
    description     =   models.TextField(blank=True)
    restaurants     =   models.ForeignKey(Restaurants,on_delete=models.SET_NULL,blank=True,null=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    restaurants     =   models.ForeignKey(Restaurants,on_delete=models.SET_NULL,blank=True,null=True)
    customer        =   models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    table           =   models.ForeignKey(Table,on_delete=models.SET_NULL,blank=True,null=True)
    total           =   models.IntegerField()
    notes           =   models.TextField(blank=True)
    status          =   models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', db_index=True)
    created_at      =   models.DateTimeField(auto_now_add=True, db_index=True)

class OrderItem(models.Model):
    order           =   models.ForeignKey(Order,on_delete=models.CASCADE)
    menu_item       =   models.ForeignKey(Menu,on_delete=models.SET_NULL,blank=True,null=True)
    quantity        =   models.IntegerField()
    price           =   models.IntegerField()
    created_at      =   models.DateTimeField(auto_now_add=True, db_index=True)
