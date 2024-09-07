from app.msgs.api_wsp import send_response
from app.format.json import txt_json

def branch_010(number, txt):
    data = txt_json(number, "You chose product" + txt)
    send_response(data)