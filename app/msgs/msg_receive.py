from flask import request, jsonify
from app.business_logic import update_user_row, update_conversation_logs
from app.trunk.main import init_flow

def receive_message(req):
        try:
            req = request.get_json()
            entry = req["entry"][0]
            changes = entry["changes"][0]
            value = changes["value"]
            msg_object = value["messages"]
            
            if msg_object:
                messages = msg_object[0]

                if "type" in messages:
                    type = messages["type"]
                    
                    if type == "interactive":
                        interactive_type = messages["interactive"]["type"]

                        if interactive_type == "button_reply":
                            txt = messages["interactive"]["button_reply"]["id"]
                            title = messages["interactive"]["button_reply"]["title"]
                            number = messages["from"]
                            update_user_row(number = number)
                            update_conversation_logs(number = number, msg = (txt + " - " + title))
                            init_flow(txt, number)
                            
                        elif interactive_type == "list_reply":
                            txt = messages["interactive"]["list_reply"]["id"]
                            title = messages["interactive"]["list_reply"]["title"]
                            number = messages["from"]
                            update_user_row(number = number)
                            update_conversation_logs(number = number, msg = (txt + " - " + title))
                            init_flow(txt, number)
                            
                    if "text" in messages:
                        txt = messages["text"]["body"]
                        number = messages["from"]
                        update_user_row(number = number)
                        update_conversation_logs(number = number, msg = txt)
                        init_flow(txt, number)
            
            return jsonify({'message': 'EVENT_RECEIVED'})
        except Exception as e:
            return jsonify({'message': 'EVENT_RECEIVED'})