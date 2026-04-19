import json
import os
import requests
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Venta

# --- CONFIGURACIÓN DE APIS ---
# Sustituye con tus claves reales o usa variables de entorno en Render
GEMINI_KEY = "TU_API_KEY_DE_GEMINI_AQUI"
WHATSAPP_TOKEN = "TU_TOKEN_DE_META_AQUI"
WA_ID_TELEFONO = "1092201717308687"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "Eres el asistente oficial de 'Barbería JhonnyBoy' en Tijuana. "
        "Ayuda a los clientes a conocer servicios y agendar. "
        "Barberos disponibles: Rafael, Paulina y Valentina. "
        "Servicios: Corte ($250), Barba ($150), Corte y Barba ($350), VIP ($1500). "
        "Sé breve, amable y usa un lenguaje moderno."
    )
)

# --- 1. FUNCIONES DEL CAJERO (TABLET/WEB) ---

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

# --- 2. FUNCIONES DE APOYO (ENVÍO) ---

def enviar_whatsapp_api(numero, texto):
    url = f"https://graph.facebook.com/v18.0/{WA_ID_TELEFONO}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    requests.post(url, headers=headers, json=payload)

# --- 3. EL WEBHOOK (WHATSAPP + IA) ---

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        token_verificacion = 'BarberIA' 
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        
        if mode == 'subscribe' and token == token_verificacion:
            return HttpResponse(challenge)
        return HttpResponse('Token incorrecto', status=403)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Extraer el mensaje y el número
            entry = data['entry'][0]['changes'][0]['value']
            if 'messages' in entry:
                message = entry['messages'][0]
                numero_cliente = message['from']
                texto_usuario = message['text']['body']

                # Generar respuesta con Gemini
                chat = model.start_chat(history=[])
                response = chat.send_message(texto_usuario)
                respuesta_ia = response.text

                # Enviar respuesta real a WhatsApp
                enviar_whatsapp_api(numero_cliente, respuesta_ia)
                
                print(f"Chat: {numero_cliente} -> {respuesta_ia}")

        except Exception as e:
            print("Error procesando Webhook:", e)

        return HttpResponse('EVENT_RECEIVED', status=200)

    return HttpResponse('Método no permitido', status=405)