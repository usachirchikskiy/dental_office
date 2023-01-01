class Config:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/dental_office'
    SECRET_KEY = 'this is a secret key'