from flask import Flask, render_template, url_for, request
#from app.models.base import Base
#from models.model import Products

app = Flask(__name__)

app.config['SECRET_KEY'] = '15AGcuVuTNogJo'

from app import routes
