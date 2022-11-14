from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///subscription.db'
app.config['SECRET_KEY'] = '509b8dc676b6b2bac3b1d925'
db = SQLAlchemy(app)
from access import routes