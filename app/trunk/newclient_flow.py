from app.msgs.api_wsp import send_response
from app.format.json import txt_json

def start_point(number, conv_state):
    x,y,z = [int(char) for char in conv_state]
    match x:
        case 0:
            match y:
                case 0:
                    match z:
                        case 1:
                            x0y0z1(number)

def x0y0z1(number):
    data = txt_json(number, "🤖 Hola, ¿Cómo estas? Bienvenido!!!!")
    send_response(data)
