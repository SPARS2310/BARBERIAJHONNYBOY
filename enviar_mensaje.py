import requests
import json

# --- CONFIGURACIÓN ---
TOKEN = "EAAOHTV5vDkwBRDHhyoD7p5yJTVZCpDcJ3XSaMIGHoh9C6DoQw27xryfybyilQYHAmYXfhEWTl921w65yCl9HyajefFLWI5V5Kvuo58wIF7ov430k13Tdw62GVjvUDoJh7qefw2w4hJJGnDrrYZCtZCPHyPtCzhgOaynPM5yPYgdvP3Q1qAFDKRT21B5q43cceoMF9zefLO8T7eMbxXsiAsU04ueK5xHANijpuVGZCqWLTgV12XhLDtgh4KuMFmtudF2PZAtZBrZA56ScrhI8Tyt"
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