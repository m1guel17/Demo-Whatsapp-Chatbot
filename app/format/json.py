def json(number, txt):
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