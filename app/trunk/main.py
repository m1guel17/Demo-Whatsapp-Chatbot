from app.msgs.api_wsp import send_response
from app.format.json import txt_json, button_json, list_json
from app.business_logic import get_conv_row, update_user_row, update_conversation_logs
from app.trunk.node1 import start_node1

def init_flow(txt, number):
    txt = txt.lower()
    
    if "clear" in txt:
        update_conversation_logs(number, branch = "001")
        send_hi(number)
    if "hola" in txt:
        send_hi(number)
        update_conversation_logs(number, branch = "001")
     
    else:
        branch = get_conv_row(number)
        
        match branch.branch:
            case "001":
                initial_options(number, txt)
                
            case "010":
                match txt:
                    case "1":
                        data = button_json(number, "Buttons Option", "Choose any of the following", ["0111", "0112", "R"], ["Option A", "Option B", "Return"])
                        send_response(data)
                        update_conversation_logs(number)
                        
                    case "2":
                        data = list_json(number, "List Option", "Choose any of the following", "Section", ["0121", "0122", "0123", "R"], ["Option A", "Option B", "Option C", "Return"])
                        send_response(data)
                        update_conversation_logs(number)
                        
                    case "3":
                        data = txt_json(number, "*Send Image*")
                        send_response(data)
                        update_conversation_logs(number)
                        
                    case "4":
                        data = txt_json(number, "*Send Document*")
                        send_response(data)
                        update_conversation_logs(number)

                    case "5":
                        data = txt_json(number, "*Send Email*")
                        send_response(data)
                        gather_info(number, txt)
                        update_conversation_logs(number)
                        
                    case "6":
                        initial_options(number, "1")
                        update_conversation_logs(number)
                        
                    case "R":
                        initial_options(number, "1")

            case "020":
                gather_info(number, txt)
                update_conversation_logs(number, branch = "021")
                
            case "021":
                msg = "Perfect I'll send you an email at: " + txt
                data = txt_json(number, msg)
                send_response(data)
                msg = " You'll be redirected to the main menu"
                data = txt_json(number, msg)
                send_response(data)
                send_hi(number)
                update_conversation_logs(number, branch = "001")
                
            case "030":
                match txt:
                    case "1":
                        msg = "Consultation Call section"
                        data = txt_json(number, msg)
                        send_response(data)
                        update_conversation_logs(number, branch = "031")
                        
                    case "2":
                        msg = "Product Demo section"
                        data = txt_json(number, msg)
                        send_response(data)
                        update_conversation_logs(number, branch = "032")
                        
                    case "3":
                        msg = "Troubleshooting Session"
                        data = txt_json(number, msg)
                        send_response(data)
                        update_conversation_logs(number, branch = "033")
            case "040":
                if "Return" in txt:
                    msg = "Return conversation from " + branch.branch
                    data = txt_json(number, msg)
                    send_response(data)
                    update_conversation_logs(number, branch = "001")

def initial_options(number, txt):
    match txt:
        case "1":
            msg = "Here’s a list of what I can help you with. Choose any feature to see it in action!\n\n1️⃣ Buttons 🔘\n2️⃣ List 📋\n3️⃣ Image 🖼️\n4️⃣ Document 📄\n5️⃣ Send Email 📧 \n6️⃣ Return"
            data = txt_json(number, msg)
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "010")
            
        case "2":
            msg = "Let me guide you through! What kind of assistance are you looking for?"
            data = txt_json(number, msg)
            send_response(data)
            
            update_conversation_logs(number = number, msg = txt, branch = "020")
        
        case "3":
            msg = "You can book an appointment with us. Choose your preferred service and time below. \n\n1️⃣Consultation Call \n2️⃣Product Demo \n3️⃣Troubleshooting Session"
            data = txt_json(number, msg)
            send_response(data)
            
            update_conversation_logs(number = number, msg = txt, branch = "030")
            
        case "4":
            msg = "We are [Company Name], a team dedicated to providing top-quality services and innovative solutions tailored to your needs. Our mission is to [insert mission statement], and we pride ourselves on [core values or unique aspects]. Whether you’re here to explore our services or need assistance, we’re always here to help \n\n * 🌐 link_demo.com \n* 📞 (xx) xx x xxxx \n* 💬 email_demo@domain.w3"
            data = txt_json(number, msg)
            send_response(data)
            update_conversation_logs(number = number, msg = txt, branch = "040")
    


def gather_info(number, txt):
    msg = "To make sure I can assist you properly, could you please provide your email to contact you?"
    data = txt_json(number, msg)
    send_response(data)
    update_user_row(number, full_name = txt)

def send_hi(number):
    msg = "🤖 Hi there! 👋 Welcome to [Company Name]. How can I assist you today? Choose one of the following options: \n1️⃣ Show Available Features\n2️⃣ Provide Assistance\n3️⃣ Schedule an Appointment \n4️⃣ About [Company Name]"
    data = txt_json(number, msg)
    send_response(data)