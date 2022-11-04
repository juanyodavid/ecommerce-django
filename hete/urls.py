from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth
from . import views_web

urlpatterns = [
    path('', views_auth.home, name='home'), # esto es home, entonces
    path('signup',views_auth.signup, name='signup'), # ''/signup es donde va a estar esta funcion
    path('activate/<slug:uidb64>/<slug:token>',views_auth.activate, name='activate'),
    path('signin',views_auth.signin, name='signin'),
    path('signout',views_auth.signout, name='signout'),
    path('inicio',views_web.inicio, name='inicio'),
    path('resumen',views_web.resumen, name='resumen'),
    path('menu',views_web.menu, name='menu'), #aca van a estar los distintos platos
    path('ordenar',views_web.ordenar, name='ordenar'),
    path('imprimir',views_web.imprimir, name='imprimir'),
    path('ordenes',views_web.ordenes, name='ordenes'),
    path('clientes',views_web.clientes,name='clientes'),
    path('modal_cat',views_web.modal_cat,name='modal_cat'),
    path('modal_client',views_web.modal_client,name='modal_client'),
    path('modal_order',views_web.modal_order,name='modal_order'),
    path('modal_menu',views_web.modal_menu,name='modal_menu'),
    path('modal_delivery',views_web.modal_delivery,name='modal_delivery'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
