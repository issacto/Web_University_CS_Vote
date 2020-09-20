
from flask import Flask, render_template,  redirect, url_for
from datetime import datetime
import forms
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import flask_resize



app = Flask(__name__)
app.config['SECRET_KEY']= 'ekag hjgeabg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RESIZE_URL'] = 'http://localhost:5000'
app.config['RESIZE_ROOT'] = 'static/Images'
db = SQLAlchemy(app)
resize = flask_resize.Resize(app)

from routes import *


if __name__ == '__main__':  
     app.run(debug=True,host='0.0.0.0')