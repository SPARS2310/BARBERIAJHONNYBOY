import requests
import json

# --- CONFIGURACIÓN ---
TOKEN = "EAAOHTV5vDkwBRIaxzecMcHiKYZCpwZCkUZCHhDKkL8s8gZAmVZAHZBVrFjMFOP4ycNu7xgXYCtRpOjQJUs2ZBXhJCyYuzJZCTE3ROhDknsPkkZBfpRGAgoBZBrHu6ZCqIViW3RXNZB0iCYoramJQNXCj3eoKDs1qAVfoTJycIS0m3fNRawULNZCh63GvXZBK3ZCOTU7YrdbYwlbnG8vVLc0o9FE9U7WLp3VY4wTKtFxUHRWKfmyDhysuqv6FsZCBeFB3fedHHykvntJmrIqPk4Qk5ZAEmqF5Y"
ID_NUMERO_TELEFONO = "1092201717308687"
MI_NUMERO = "526642808850" # El número que ya verificaste

def enviar_mensaje():
    url = f"https://graph.facebook.com/v18.0/{ID_NUMERO_TELEFONO}/messages"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    
    data = {
        "messaging_product": "whatsapp",
        "to": MI_NUMERO,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": { "code": "en_US" }
        }
    }
    
    print("Intentando enviar...")
    # Usamos json.dumps para asegurar que el formato sea perfecto
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("¡LOGRADO DESDE PYTHON! Revisa tu WhatsApp.")
    else:
        print(f"Error detectado: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    enviar_mensaje()