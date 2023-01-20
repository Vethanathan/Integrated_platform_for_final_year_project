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

app.run(debug=1)
