"""
URL configuration for barber_project project.
"""
from django.contrib import admin
from django.urls import path
# Importamos todas las vistas, incluyendo el webhook
from ventas.views import (
    seleccionar_cita, 
    menu_servicios, 
    seleccionar_pago, 
    finalizar_pago, 
    webhook
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal (Cajero/Tablet)
    path('', seleccionar_cita, name='inicio'),
    path('servicios/<str:barbero_nombre>/', menu_servicios, name='menu'),
    path('pago/<str:barbero_nombre>/<int:servicio_id>/', seleccionar_pago, name='pago'),
    path('finalizar/<str:barbero_nombre>/<int:servicio_id>/<str:metodo>/', finalizar_pago, name='finalizar'),
    
    # Ruta del Bot (WhatsApp Webhook)
    # Esta es la que Meta usará: https://barberiajhonnyboy.onrender.com/webhook/
    path('webhook/', webhook, name='webhook'),
]