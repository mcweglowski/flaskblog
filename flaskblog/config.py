class Config:
    SECRET_KEY = '1a4d1aebb222cd6d0dd481f4f8def584'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask_blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'emailsender240@gmail.com'
    MAIL_PASSWORD = '1qazXSW@3edc'