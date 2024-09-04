from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.TEXT, nullable=True)
    cellphone = db.Column(db.TEXT, unique=True, nullable=True)
    id_number = db.Column(db.Integer, unique=True, nullable=True)
    address = db.Column(db.TEXT, nullable=True)
    address_reference = db.Column(db.TEXT, nullable=True)
    email = db.Column(db.TEXT, unique=True, nullable=True)
    status = db.Column(db.TEXT, nullable=True)
    registrationDate = db.Column(db.DateTime, default = datetime.utcnow)


class Conversations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cellphone = db.Column(db.TEXT, unique=True, nullable=False)
    msg = db.Column(db.TEXT, nullable=True)
    ex_funct = db.Column(db.TEXT, nullable=True)
    branch = db.Column(db.TEXT, nullable=True)
    status = db.Column(db.TEXT, nullable=True)
    date_time = db.Column(db.DateTime, default = datetime.utcnow)
    