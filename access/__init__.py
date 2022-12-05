from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscription.db'
app.config['SECRET_KEY'] = '509b8dc676b6b2bac3b1d925'
db = SQLAlchemy(app)
# bcrypt =Bcrypt(app)
from access import routes