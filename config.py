import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'MY_SECREY_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymsql://jessi:1a2b3c@127.0.0.1/idgs802'
    SQLALCHEMY_TRACK_MODIFICATION = False
 