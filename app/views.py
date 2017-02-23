from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape
from app import app
import json, requests

# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	else:
		return render_template("search.html",
                        title='Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['email'] != app.config['EMAIL']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            # session['logged_in'] = True
            # flash('You were logged in','normal')

            return redirect('/main2')

    return render_template("login.html",
                        title='Sign In',
                        error=error)



@app.route('/signup', methods=['GET'])
def signup():
    return render_template("signup.html",
                        title='Sign Up')
