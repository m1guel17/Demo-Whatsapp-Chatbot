from app.msgs.api_wsp import send_response
from app.format.json import json
from app.business_logic import get_row, get_branch

def init_flow(txt, number):
    txt = txt.lower()
    
    user_state = get_row(number)
    branch_state = get_branch(number)

    if txt == "hola":
        data = json(number, "🤖 Hola, ¿Cómo estas? Bienvenido. " + user_state + branch_state)
        send_response(data)