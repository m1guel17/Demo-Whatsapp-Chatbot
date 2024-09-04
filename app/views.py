from flask import  jsonify, render_template, request
from .business_logic import get_all_users,get_all_convs
from app.msgs.msg_receive import receive_message
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
    
    
    