from app.msgs.api_wsp import send_response
from app.format.json import txt_json, button_json
from app.business_logic import get_conv_row, update_user_row, update_conversation_logs
from app.trunk.node1 import start_node1

def init_flow(txt, number):
    txt = txt.lower()
    
    if "hola" in txt:
        msg = "🤖 Hi there! 👋 Welcome to [Company Name]. I'm here to help you get started. How can I assist you today? \n1️⃣ Show Available Features\n2️⃣ Provide Assistance\n3️⃣ Schedule an Appointment \n4️⃣ About [Company Name]"
        data = txt_json(number, msg)
        send_response(data)
        update_conversation_logs(number, branch = "001")
        
    else:
        branch = get_conv_row(number)
        
        match branch.branch:
            case "001":
                initial_options(number, txt)
                
            case "010":
                start_node1(number, txt)
                
        
                
def initial_options(number, txt):
    match txt:
        case "1":
            msg = "Here’s a list of what I can help you with. Choose any feature to see it in action!"
            data = txt_json(number, msg)
            send_response(data)
                
            msg = "1️⃣ Buttons 🔘\n2️⃣ List 📋\n3️⃣ \n4️⃣ Link 🔗\n5️⃣ Image 🖼️\n6️⃣ Document 📄\n7️⃣ Send Email 📧"
            data = txt_json(number, msg)
            send_response(data)
            
            update_conversation_logs(number = number, msg = txt, branch = "010")

            
        case "2":
            msg = "Let me guide you through! What kind of assistance are you looking for?"
            data = txt_json(number, msg)
            send_response(data)
            
            update_conversation_logs(number = number, msg = txt, branch = "020")
        
        case "3":
            msg = "You can book an appointment with us. Choose your preferred service and time below."
            data = txt_json(number, msg)
            send_response(data)
            
            msg = "1️⃣Consultation Call \n2️⃣Product Demo \n3️⃣Troubleshooting Session"
            data = txt_json(number, msg)
            send_response(data)
            
            update_conversation_logs(number = number, msg = txt, branch = "030")
            
        case "4":
            msg = "We are [Company Name], a team dedicated to providing top-quality services and innovative solutions tailored to your needs. Our mission is to [insert mission statement], and we pride ourselves on [core values or unique aspects]. Whether you’re here to explore our services or need assistance, we’re always here to help \n\n * 🌐 link_demo.com \n* 📞 (xx) xx x xxxx \n* 💬 email_demo@domain.w3"
            data = txt_json(number, msg)
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "040")
    


def gather_info(number, txt):
    msg = "To make sure I can assist you properly, could you please provide your name or the best way to contact you?"
    data = txt_json(number, msg)
    send_response(data)
    update_user_row(number, full_name = txt)