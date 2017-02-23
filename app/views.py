from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape
from app import app
import json, requests

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.secret_key = os.urandom(24)


# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
	if 'email' in session:
		return 'Logged in as %s' % escape(session['email'])
	else:
		return render_template("search.html",
                        title='Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
	error=None
	if request.method == 'POST':
		session['email'] = request.form['email']
		return redirect('/index')
	# if request.method == 'POST':
	# 	if request.form['email'] != app.config['EMAIL']:
	# 		error = 'Invalid username'
	# 	elif request.form['password'] != app.config['PASSWORD']:
	# 		error = 'Invalid password'
	# 	else:
	# 		# session['logged_in'] = True
    #         # flash('You were logged in','normal')
	# 		session['email'] = request.form['email']
	# 		return redirect('/index')

	return render_template("login.html",
						title='Sign In',
						error=error)



@app.route('/signup', methods=['GET'])
def signup():
    return render_template("signup.html",
                        title='Sign Up')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return redirect(url_for('index'))
