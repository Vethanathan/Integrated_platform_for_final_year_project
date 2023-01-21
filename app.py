from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField
import ibm_db
from passlib.hash import sha256_crypt
from functools import wraps
from sendgrid import *

app = Flask(__name__)

app.secret_key='a'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard',methods=["POST"])
def final():
    user_name=request.form.get("email")
    password=request.form.get("password")
    print(user_name,password)
    if user_name=="vethanathanvk@gmail.com" and password=="qwerty@12345":
        return render_template("dashboard.html")
    else:
        return render_template("home.html")

@app.route('/signup')
def dashboard():
    return render_template('signup.html')

app.run(debug=1)
