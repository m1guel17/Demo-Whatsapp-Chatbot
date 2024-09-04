from app.data_access import User, Conversations, db
from flask import json
from sqlalchemy import desc
import inspect

# ======================= Queries =======================
def get_all_users():
    return User.query.all()

def get_row(number):
    return User.query.filter_by(cellphone=number).first()

def update_user_row(number, **kwargs):
    user_state = get_row(number)
    
    if not user_state:
        user_state = User(cellphone=number, status="newclient")
        db.session.add(user_state)
        db.session.commit()
        
    for key, value in kwargs.items():
        setattr(user_state, key, value)
        db.session.commit()

def get_all_convs():
    return Conversations.query.all()

def get_conv_row(number):
    #return Conversations.query.filter_by(cellphone=number).first()
    return Conversations.query.filter_by(cellphone=number).order_by(desc(Conversations.id)).first()

def get_branch(number):
    return Conversations.query.filter_by(cellphone=number).order_by(desc(Conversations.id)).with_entities(Conversations.branch).first()

def update_conversation_logs(number , **kwargs):
    stack = inspect.stack()
    contexts = {}
    if len(stack) > 1:
        parent_frame = stack[1]
        contexts['parent'] = {
            'function_name': parent_frame.function}
    if len(stack) > 2:
        grandparent_frame = stack[2]
        contexts['grandparent'] = {
            'function_name': grandparent_frame.function}
        
    conv_state = get_conv_row(number)
        
    if not conv_state:
        conv_state = Conversations(cellphone=number, branch = "001", ex_funct = json.dumps(contexts), status = "OPEN")
        db.session.add(conv_state)
        db.session.commit()
        
    for key, value in kwargs.items():
        setattr(conv_state, key, value)
        db.session.commit()




