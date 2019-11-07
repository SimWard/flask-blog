import os


class Config:
    # generated with secrets.token_hex(16) (should be env var for production)
    SECRET_KEY = '54a4fb91181f930961e26797a6314e43'

    # definitely use env var if any more complicated than sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('USER')
    MAIL_PASSWORD = os.environ.get('PASS')
