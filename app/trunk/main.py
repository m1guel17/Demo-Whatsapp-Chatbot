from app.msgs.api_wsp import send_response
from app.format.json import txt_json, button_json
from app.business_logic import get_branch, update_user_row, update_conversation_logs
from app.trunk.branch_1 import branch_010

def init_flow(txt, number):
    txt = txt.lower()
    
    if "hola" in txt:
        msg = "🤖 Hi there! 👋 Welcome to [Company Name]. I'm here to help you get started. How can I assist you today? \n1️⃣ Product information \n2️⃣ Support \n3️⃣ Others"
        data = txt_json(number, msg)
        send_response(data)
    else:
        initial_options(number, txt)
        branch_state = get_branch(number)
        match branch_state:
            case "010":
                branch_010(number, txt)
                
def initial_options(number, txt):
    match txt:
        case "1":
            msg = "Absolutely! We offer a range of products, including [Product A], [Product B], and [Product C]. Would you like a detailed breakdown of features, pricing, or perhaps a demo to see the product in action?"
            data = txt_json(number, msg)
            send_response(data)
            data = button_json(number, "We offer a range of products, including [Product A], [Product B], and [Product C].", "Choose one option", ["[Product A]", "[Product B]", "[Product C]"])
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "010")
            
        case "2":
            msg = "No problem! I'm here to help. Could you describe the issue you're experiencing, or let me know if you're looking for assistance with an order, troubleshooting, or something else?"
            data = txt_json(number, msg)
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "020")
        
        case "3":
            msg = "Got it! Feel free to let me know what you're looking for, and I’ll do my best to assist you"
            data = txt_json(number, msg)
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "030")
    


def gather_info(number, txt):
    msg = "To make sure I can assist you properly, could you please provide your name or the best way to contact you?"
    data = txt_json(number, msg)
    send_response(data)
    update_user_row(number, full_name = txt)