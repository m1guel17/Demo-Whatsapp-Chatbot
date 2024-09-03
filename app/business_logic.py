from app.data_access import User, Conversations, db
from flask import  jsonify
from sqlalchemy import desc

# ======================= Queries =======================
def get_all_users():
    return User.query.all()

def get_row(number):
    return User.query.filter_by(cellphone=number).first()

def update_user_row(number, **kwargs):
    user_state = get_row(number)
    
    if not user_state:
        user_state = User(cellphone=number, status="newcient")
        db.session.add(user_state)
        db.session.commit()
        
    for key, value in kwargs.items():
        setattr(user_state, key, value)
        db.session.commit()

def get_conv_row(number):
    return Conversations.query.filter_by(cellphone=number).order_by(desc(Conversations.id)).first()

def get_branch(number):
    return Conversations.query.filter_by(cellphone=number).order_by(desc(Conversations.id)).with_entities(Conversations.branch).first()

def update_conversation_logs(number , **kwargs):
    conv_state = get_conv_row(number)
    
    if not conv_state:
        conv_state = Conversations(cellphone=number)
        db.session.add(conv_state)
        db.session.commit()
        
    for key, value in kwargs.items():
        setattr(conv_state, key, value)
        db.session.commit()




