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

@app.route('/ve')
def ve():
    return render_template('test.html')

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



@app.route('/vetha',methods=["POST"])
def vetha():
    print("inga iruken")
    
    fin = open("templates\\dashboard.html", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace("<!-- <p>vetha</p> -->", '<div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> \n <!-- <p>vetha</p> -->')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("templates\\dashboard.html", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    # with open("templates\\upload.html", "r+") as f:
    #         print("naana vandhuten daaa!!!")
    #         html = f.read()
    #         f.seek(0)
    #         f.write(html.replace("<!-- <p>vetha</p> -->", string))
    return render_template("dashboard.html")

app.run(debug=1)
