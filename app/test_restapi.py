from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests

#test
@app.route('/test', methods=['GET'])
def test():
	first = request.args.get('first')
	second = request.args.get('second')
	data = {"fisrt": first, "second": second, "third": "GET"}

	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')

	return resp

#test
@app.route('/test', methods=['POST'])
def test_post():
	first= request.form.get("first")
	second= request.form.get("second")
	data = {"fisrt": first, "second": second, "third": "POST"}

	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')

	return resp

# login
@app.route('/login', methods=['POST', 'GET'])
def login():
	# ImmutableMultiDict([('airlock_id', ''),
	# 					('email', '1234'),
	# 					('authenticity_token', '#f'),
	# 					('utf8', '✓'),
	# 					('password', '1245'),
	# 					('from', 'email_login')])
	first= request.form.get("email")
	second= request.form.get("password")
	data = {"email": first, "password": second, "third": "login"}

	data_decode = request.form
	print(data_decode)

	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')

	return resp

@app.route('/signup_login', methods=['POST', 'GET'])
def signup_login():
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
	data_decode = request.form
	#print(data_decode)

	#js = json.dumps(data)
	#resp = Response(js, status=200, mimetype='application/json')

	return "Hello, World!"
