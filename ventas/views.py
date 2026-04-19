from django.shortcuts import render, redirect
from .models import Venta

def seleccionar_cita(request):
    barberos = [
        {'nombre': 'Rafael', 'foto': 'rafael.jpg'},
        {'nombre': 'Antonio', 'foto': 'antonio.jpg'},
        {'nombre': 'Benito', 'foto': 'benito.jpg'},
    ]
    return render(request, 'ventas/seleccionar_cita.html', {'barberos': barberos})

def menu_servicios(request, barbero_nombre):
    servicios = [
        {'id': 1, 'nombre': 'Corte', 'precio': 250},
        {'id': 2, 'nombre': 'Barba', 'precio': 150},
        {'id': 3, 'nombre': 'Corte y Barba', 'precio': 350},
        {'id': 4, 'nombre': 'Servicio VIP', 'precio': 1500},
    ]
    return render(request, 'ventas/menu_servicios.html', {
        'servicios': servicios,
        'barbero': barbero_nombre
    })

def seleccionar_pago(request, barbero_nombre, servicio_id):
    return render(request, 'ventas/seleccion_pago.html', {
        'barbero': barbero_nombre,
        'servicio_id': servicio_id
    })

def finalizar_pago(request, barbero_nombre, servicio_id, metodo):
    servicios_data = {
        "1": {"nombre": "Corte", "precio": 250},
        "2": {"nombre": "Barba", "precio": 150},
        "3": {"nombre": "Corte y Barba", "precio": 350},
        "4": {"nombre": "Servicio VIP", "precio": 1500},
    }
    datos = servicios_data.get(str(servicio_id), {"nombre": "Otro", "precio": 0})
    
    Venta.objects.create(
        barbero=barbero_nombre,
        servicio=datos['nombre'],
        monto=datos['precio'],
        metodo_pago=metodo
    )
    return render(request, 'ventas/gracias.html')