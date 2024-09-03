from flask import json, jsonify, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from .business_logic import *
from .data_access import *
from app.msgs.msg_send import send_txt
import os

cellphone = os.environ.get('cellphone') or "51998249361"

def init_app(app):
    @app.route('/')
    def index():
        registros = get_all_users()
        conversations = get_all_convs()
        return render_template('index.html', registros = registros, conversations = conversations)
    
    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook():
        if request.method == 'GET':
            challenge = verify_token(request)
            return challenge
        elif request.method == 'POST':
            response = receive_message(request)
            return response
        
    def verify_token(req):
        token = req.args.get('hub.verify_token')
        challenge = req.args.get('hub.challenge')
        if challenge and token == 'token':
            return challenge
        else:
            return jsonify({'error': 'Token Invalido'}), 401
    
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
                            number = messages["from"]
                            update_user_row(number = number)
                            update_conversation_logs(number = number, msg = txt)
                            send_txt(txt, number)
                            
                        elif interactive_type == "list_reply":
                            txt = messages["interactive"]["list_reply"]["id"]
                            number = messages["from"]
                            update_user_row(number = number)
                            update_conversation_logs(number = number, msg = txt)
                            send_txt(txt, number)
                            
                    if "text" in messages:
                        txt = messages["text"]["body"]
                        number = messages["from"]
                        update_user_row(number = number)
                        update_conversation_logs(number = number, msg = txt)
                        send_txt(txt, number)
            
            return jsonify({'message': 'EVENT_RECEIVED'})
        except Exception as e:
            return jsonify({'message': 'EVENT_RECEIVED'})
    