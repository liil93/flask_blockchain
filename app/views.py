from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape
from app import app
import json, requests

# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
	return render_template("search.html",
                        title='Welcome')


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html",
                        title='Login')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template("signup.html",
                        title='Sign Up')
