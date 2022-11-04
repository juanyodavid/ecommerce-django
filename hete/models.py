# from asyncio.windows_events import NULL
# from doctest import debug_script
# from email.policy import default
# from html.entities import name2codepoint
# from logging.config import _LoggerConfiguration
# from pickle import STACK_GLOBAL
# from pickletools import read_unicodestring1
# from socket import INADDR_UNSPEC_GROUP
# from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#The type of food that the restaurant can offer
class Food_category(models.Model):
    name = models.CharField(max_length = 31)
    description = models.CharField(max_length = 63)

#The menu that the Resto offer
class Menu(models.Model):
    name = models.CharField(max_length= 63)
    price = models.IntegerField()
    #! TODO: Cambiar category
    category = models.ManyToManyField(Food_category)
    state = models.BooleanField(default = True) # T -> la comida esta para ser comprada, F no esta disponible

class Dispatcher(models.Model):
    name = models.CharField(max_length= 63)
    cellphone = models.IntegerField()
    debt = models.IntegerField()
    zone = models.URLField()# zona en la que suele repartir

class Client(models.Model):
    name = models.CharField(max_length=255)
    observation = models.CharField(max_length=255)
    cellphone = models.CharField (max_length= 16)
    location = models.URLField()
    house_photo = models.ImageField(null = True, blank = True, upload_to = "images/")

class Invoice(models.Model):
    name1 = models.CharField(max_length= 63)
    name2 = models.CharField(max_length= 63)
    ruc1 = models.CharField(max_length= 63)
    ruc2 = models.CharField(max_length= 63)

class Order(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    departure_time = models.DateTimeField() #la hora que desea el comensal
    comment = models.CharField(max_length=255)
    state = models.BooleanField()#if the order is already ready

class Order_details(models.Model):
    order = models.ManyToManyField(Order) # aca estan todas las ordenes de la persona ese dia
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    author = models.ManyToManyField(User) #who writes the order
    first_order_time = models.DateTimeField(auto_now= False)
    zone = models.URLField()

class Distribution(models.Model): # el distribution es por persona, un distributio es todo para una persona, por eso tiene muchos order en el mismo
    order = models.ManyToManyField(Order_details)
    # client = models.ForeignKey(Client,null=True, on_delete=models.SET_NULL)
    dispatcher = models.ForeignKey(Dispatcher,default = None,null = True, on_delete=models.SET_NULL)
    zone = models.URLField()
    departure_time = models.DateField
    # debt = models.DecimalField(max_digits = 6, decimal_places = 3,default= NULL) #cuanto falto pagar, asi se sabe el delivery
    class StateOrder(models.IntegerChoices):
        Preparandose = 0
        Entregandose = 1
        Pagado = 2
        Deuda = 3
    state = models.IntegerField(choices=StateOrder.choices)#if the order already came out 0=no salio,1 = ya salio, 3 = pagado(si debt es 0 y state es 1, se setea automatico), 4=deuda
