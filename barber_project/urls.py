"""
URL configuration for barber_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from ventas.views import seleccionar_cita, menu_servicios, seleccionar_pago, finalizar_pago, webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', seleccionar_cita, name='inicio'),
    path('servicios/<str:barbero_nombre>/', menu_servicios, name='menu'),
    path('pago/<str:barbero_nombre>/<int:servicio_id>/', seleccionar_pago, name='pago'),
    path('finalizar/<str:barbero_nombre>/<int:servicio_id>/<str:metodo>/', finalizar_pago, name='finalizar'),
    path('webhook/', webhook, name='webhook'),
]