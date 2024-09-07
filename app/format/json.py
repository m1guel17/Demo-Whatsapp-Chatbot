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

def button_json(number, text, footer, options):
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
                                "id": "011",
                                "title": options[0]
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "012",
                                "title": options[1]
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "013",
                                "title": options[2]
                            }
                        }
                    ]
                }
            }
        }
    return buttton