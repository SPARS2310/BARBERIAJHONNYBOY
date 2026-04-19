import requests

# CREDENCIALES
ACCESS_TOKEN = "APP_USR-2284254783039512-041522-7482d2511c851d0237cc5f5ee5ac43e7-3339085529"
# Formato completo requerido por la API de hardware
DEVICE_ID = "NEWLAND_N950_N950NCCA05086207"

def cobro_directo():
    # Esta es la URL para hablarle al hardware sin pasar por 'cajas' virtuales
    url = f"https://api.mercadopago.com/point/integration-api/devices/{DEVICE_ID}/payment-intents"
    
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "amount": 5,
        "description": "Prueba Barberia Directa",
        "payment": {
            "installments": 1,
            "type": "credit_card"
        }
    }

    print(f"Enviando orden directa a la terminal {DEVICE_ID}...")
    response = requests.post(url, headers=headers, json=data)
    
    print(f"Status: {response.status_code}")
    print(f"Respuesta: {response.text}")

if __name__ == "__main__":
    cobro_directo()