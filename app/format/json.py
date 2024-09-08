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
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": id[0],
                                "title": options[0]
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": id[1],
                                "title": options[1]
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": id[2],
                                "title": options[2]
                            }
                        }
                    ]
                }
            }
        }
    return buttton