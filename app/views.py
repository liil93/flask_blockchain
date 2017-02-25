from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape
from app import app
import json, requests
from . import function
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.secret_key = os.urandom(24)


# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():



	if 'email' in session:
		return render_template("search.html",
                        title='Welcome',
						session=session['email'])
	else:
		return render_template("search.html",
                        title='Welcome',
						session=None)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'email' in session:
		return redirect('/')
	else:
	    error=None
	    if request.method == 'POST':
	        Email= request.form.get("email")
	        PW = request.form.get("password")
	        result1 = function.Check_email(Email)
	        result2 = function.Check_pw(Email, PW)
	        if result1 ==[]:
	            error = 'Invalid username'
	        elif result2 ==[]:
	            error = 'Invalid password'
	        else:
	            session['email'] = Email
	            return redirect('/')

	    return render_template("login.html",
	                        title='Sign In',
	                        error=error)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	# ImmutableMultiDict([('user[last_name]', 'yoo'),
	# 					('user[password]', '1q2w3e4r'),
	# 					('user[birthday_month]', '1'),
	# 					('user[birthday_day]', '4'),
	# 					('user[birthday_year]', '2011'),
	# 					('utf8', '✓'),
	# 					('from', 'email_signup'),
	# 					('user[first_name]', 'dongwon'),
	# 					('user[email]', 'asldkfj@nave.rcom'),
	# 					('user_profile_info[receive_promotional_email]', '0'),
	# 					('user_profile_info[receive_promotional_email]', '1'),
	# 					('authenticity_token', '#j')])

	if request.method == 'POST':
		Email= request.form.get("user[email]")
		PW = request.form.get("user[password]")
		result = function.Save_mem(Email, PW)
		if result == 1:
			session['email'] = Email
			return redirect('/')
		else:
			error = 'Email already exists.'
			return render_template("signup.html",
								title='SignUp',
								error=error)
	else:
		return render_template("signup.html",
							title='SignUp',
							error=None)





@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return redirect('/')


@app.route('/enrollment_home/address', methods=['GET', 'POST'])
def enrollment_home_address():
	# Check session
	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		print(request.form)
		# ImmutableMultiDict([('country_code', 'US'),
		# 					('city', '1'),
		# 					('street', '1'),
		# 					('zipcode', '1'),
		# 					('apt', '1'),
		# 					('state', '1')])
		return redirect('/enrollment_home/room')

	return render_template("address.html",
                        title='progress',
						session='OK')


@app.route('/enrollment_home/room', methods=['GET', 'POST'])
def enrollment_home_room():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		print(request.form)
		# ImmutableMultiDict([('house_type', '2'),
		# 					('number_of_room', '1')])
		return redirect('/enrollment_home/car_elevator')

	return render_template("room.html",
                        title='progress',
						session='OK')

@app.route('/enrollment_home/car_elevator', methods=['GET', 'POST'])
def enrollment_home_car_elevator():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		print(request.form)
		# ImmutableMultiDict([('elevatorType', 'yes'),
		# 					('parkingType', 'no')])
		return redirect('/enrollment_home/complete')

	return render_template("car_elevator.html",
                        title='progress',
						session='OK')

@app.route('/enrollment_home/complete', methods=['GET', 'POST'])
def enrollment_home_complete():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		print(request.form)
		# ImmutableMultiDict([('elevatorType', 'yes'),
		# 					('parkingType', 'no')])
		return redirect('/')

	return render_template("enrollment_home_complete.html",
                        title='progress',
						session='OK')

@app.route('/test', methods=['GET', 'POST'])
def test():
	if request.method == 'POST':
		print(request.form)

	return render_template("car_elevator.html",
                        title='progress',
						session='OK')
