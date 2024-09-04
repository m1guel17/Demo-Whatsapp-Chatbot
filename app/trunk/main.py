from app.business_logic import get_row, get_branch
from app.trunk.newclient_flow import start_point

def init_flow(txt, number):
    txt = txt.lower()
    
    user_state = get_row(number)
    conv_state = get_branch(number)
    
    match user_state.status:
        case "newclient":
            if txt == "hola":
                start_point(number, conv_state)
    
    