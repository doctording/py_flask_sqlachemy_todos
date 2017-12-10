from web.model import User
from web.model import Todo
import os
from web import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g
import datetime

@app.route('/')
def show_entries():
    todos = Todo.Todo.query.all()
    return render_template('show_entries.html',entries=todos)

@app.route('/tologin')
def tologin():
    return render_template('tologin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    #sno = request.form['sno']
    #password = request.form['password']
    user = User.User.query.filter_by(sno=request.form['sno']).first()
    passwd = User.User.query.filter_by(password=request.form['password']).first()

    if user is None:
        error = 'Invalid sno'
    elif passwd is None:
        error = 'Invalid password'
    else:
        session['logged_in'] = True
        session['sno'] = user.sno
        #flash('You were logged in')
        return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)
    task = request.form['text']
    sno = session['sno']
    createtime = datetime.datetime.now()
    todo_new = Todo.Todo(sno, task, 0, createtime)
    db.session.add(todo_new)
    db.session.commit()

    #flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('sno', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))