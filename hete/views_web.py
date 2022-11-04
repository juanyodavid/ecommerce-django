from contextlib import redirect_stderr
from faulthandler import cancel_dump_traceback_later
from pdb import post_mortem
from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def ordenar(request):
    return render(request,"web/ordenar.html")

def sumar(request): # esta es la funcion que trae valores de ordenar.html y muestra en resumen.html
    val1 = request.GET['num1']
    val2 = request.GET['num2']
   
    suma = int(val1) + int(val2)
   
    return render(request,"resumen.html",{'suma': suma})
def sumar2(request): # esta es la funcion que trae valores de ordenar.html y muestra en resumen.html
   
    val3 = request.POST['num3']
    val4 = request.POST['num4']
   
    suma2 = int(val3) + int(val4)
    return render(request,"inicio.html",{'suma2':suma2})

def menu(request):
    menu = Menu.objects.all()
    return render(request,"web/menu.html",{'menus':menu})

def clientes(request):
    clientes = Client.objects.filter(name='aoeu')
    return render(request,"web/clientes.html",{'clientes':clientes})

def imprimir(request):
    return render(request,"")

def modal_cat(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria = Food_category.objects.create(name = nombre,description = descripcion)
        categoria.save()
        messages.success(request,"Se ha agregado la categoría.")
    return clientes(request)


def modal_client(request):
    if request.method == "POST":
        nombre = request.POST['name']
        obs = request.POST['obs']
        cel = request.POST['cel']
        location = request.POST['location']
        # photo = request.POST.get('photo', False);         #TODO:FIX this get
        object = Clients.objects.create(name = nombre,observation = obs,cellphone=cel,location=location)
        object.save()
        messages.success(request,"Se ha agregado un cliente.")
    return clientes(request)

def modal_order(request):
    if request.method == "POST":
        cliente = request.POST['name']
        menu = request.POST['obs']
        cantidad = request.POST['cel']
        departure = request.POST['location']
        comentario = request.POST['location']
        object = Order.objects.create(client=cliente,menu=menu,quantity=cantidad,departure_time=departure,comment=comentario,state=False)
        object.save()
        messages.success(request,"Se ha agregado la orden.")
    else:
        messages.error(request,"Se ha producido un error.")

    return clientes(request)

def modal_menu(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['precio']
        categoria = request.POST['cat']
        estado = request.POST['estado']
        object = Menu.objects.create(name=name,price=price,state=estado)
        object.save()
        if categoria:
            cat = Food_category.objects.filter(name=categoria).first() #todo: cambiar el first
            object.category.add(cat)
        messages.success(request,"Se ha agregado la orden.")
    else:
        messages.error(request,"Se ha producido un error.")

    return clientes(request)

def modal_delivery(request):
    if request.method == "POST":
        nombre = request.POST['name']
        cel = request.POST['cel']
        location = request.POST['location']
        object = Dispatcher.objects.create(name = nombre,cellphone=cel,zone=location,debt = 0)
        object.save()
        messages.success(request,"Se ha agregado al delivery-guy.")
    else:
        messages.error(request,"Se ha producido un error.")

    return clientes(request)

def inicio(request):
    return render(request,"web/inicio.html")

def resumen(request):
    return render(request,"resumen.html")

def ordenes(request):
    pass
