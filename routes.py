
import forms
from models import Task
from app import app, db
from flask import render_template, redirect, url_for
from datetime import datetime


@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task (title = form.title.data, date = datetime.utcnow(), comment = form.comment.data)
        db.session.add(t)
        db.session.commit()
        print("Submitted Title: ", form.title.data)
        return redirect(url_for('index'))
    return render_template('home.html', form =form)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks = tasks)