from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# generated with secrets.token_hex(16)
app.config['SECRET_KEY'] = '54a4fb91181f930961e26797a6314e43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
