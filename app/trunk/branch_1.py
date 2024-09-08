from app.msgs.api_wsp import send_response
from app.format.json import txt_json

def branch_011(number, txt):
    data = txt_json(number, "You chose product A")
    send_response(data)
    
def branch_012(number, txt):
    data = txt_json(number, "You chose product B")
    send_response(data)
    
def branch_013(number, txt):
    data = txt_json(number, "You chose product C")
    send_response(data)
    