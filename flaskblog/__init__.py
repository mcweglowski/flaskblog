from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1a4d1aebb222cd6d0dd481f4f8def584'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)

from flaskblog import routes