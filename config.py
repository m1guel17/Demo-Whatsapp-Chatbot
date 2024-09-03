import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temporal-password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///bookstore.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
