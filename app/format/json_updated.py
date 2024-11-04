from app.format.check import jsonButtonError

def txt_json(number, txt):
    msg = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "text": {
            "preview_url": False,
            "body": txt
        }
    }
    return msg

def button_json(number, text, footer, id, options):
    value = jsonButtonError(text, footer,id, options)
    if value:
        buttons = []
        # Loop through based on the quantity provided
        for i in range(len(id)):
            button_ = {
                "type": "reply",
                "reply": {
                    "id": id[i],
                    "title": options[i]
                }
            }
            buttons.append(button_)
        
        buttton = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": text
                    },
                    "footer": {
                        "text": footer
                    },
                    "action": {
                        "buttons": buttons
                    }
                }
            }
        return buttton
    else:
        return txt_json(number, "Check logs for button_json")

def list_json(number, text, footer, title, id, options):
    
    
    list_ = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": text
                },
                "footer": {
                    "text": footer
                },
                "action":{
                    "button": "See Options",
                    "sections": [
                        {
                            "title": title,
                            "rows": [
                                {
                                    "id": id[0],
                                    "title": options[0],
                                    "description": "Compra los mejores artículos de tecnología"
                                },
                                {
                                    "id": id[1],
                                    "title": options[1],
                                    "description": "Vende lo que ya no estés usando"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    return list_