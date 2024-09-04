from app.msgs.api_wsp import send_response
from app.format.json import json

def init_flow(txt, number):
    txt = txt.lower()
    
    if txt == "hola":
        data = json(number, "🤖 Hola, ¿Cómo estas? Bienvenido.")
        send_response(data)