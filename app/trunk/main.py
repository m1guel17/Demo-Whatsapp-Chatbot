from app.msgs.api_wsp import send_response
from app.format.json import json
from app.business_logic import get_row, get_conv_row

def init_flow(txt, number):
    txt = txt.lower()
    
    user_state = get_row(number)
    branch_state = get_conv_row(number)
    
    msg = "🤖 Hola, ¿Cómo estas? Bienvenido. \n branch state: " + branch_state.status
    
    if txt == "hola":
        data = json(number, msg)
        send_response(data)