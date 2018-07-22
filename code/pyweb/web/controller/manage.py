from web.model import User
from web.model import Todo
import os
from web import app, db
from flask import make_response, Response, request, render_template, flash, abort, url_for, redirect, session, Flask, g
import datetime


@app.route('/')
def show_entries():
    todos = Todo.Todo.query.all()
    return render_template('show_entries.html', entries=todos)


@app.route('/tologin')
def tologin():
    cookie_sno = request.cookies.get('sno')
    cookie_pass = request.cookies.get('pass')
    app.logger.info("logger info cookie: (%s, %s)", cookie_sno, cookie_pass)
    if cookie_sno is not None:
        return render_template('tologin.html',
                               cookie_sno=cookie_sno,
                               cookie_pass=cookie_pass,
                               checked="checked='checked'")
    else:
        return render_template('tologin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # sno = request.form['sno']
    # password = request.form['password']
    user = User.User.query.filter_by(sno=request.form['sno']).first()
    passwd = User.User.query.filter_by(password=request.form['password']).first()
    remember_pass = None
    if 'checkbox' in request.form:
        remember_pass = request.form['checkbox']
    app.logger.info("logger info test")
    if user is None:
        error = 'Invalid sno'
    elif passwd is None:
        error = 'Invalid password'
    else:
        resp = make_response(redirect(url_for('show_entries')))
        if remember_pass:
            app.logger.info("logger info remember_pass: (%s)", str(remember_pass))

            expire_time = datetime.datetime.today() + datetime.timedelta(days=30)
            resp.set_cookie('sno', request.form['sno'], expires=expire_time)
            resp.set_cookie('pass', request.form['password'], expires=expire_time)
        else:
            resp.delete_cookie('sno')
            resp.delete_cookie('pass')

        session['logged_in'] = True
        session['sno'] = user.sno
        # flash('You were logged in')
        # return redirect(url_for('show_entries'))
        return resp
    return render_template('login.html', error=error)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)
    task = request.form['text']
    sno = session['sno']
    todo_new = Todo.Todo(sno, task, 0, datetime.datetime.now())
    db.session.add(todo_new)
    db.session.commit()

    # flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('sno', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
