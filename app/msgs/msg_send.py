from app.msgs.api_wsp import send_response
from app.format.json_format import msg_format

def send_txt(txt, number):
    txt = txt.lower()
    
    if txt == "hola":
        data = msg_format(number, "🤖 Hola, ¿Cómo estas? Bienvenido.")
        send_response(data)