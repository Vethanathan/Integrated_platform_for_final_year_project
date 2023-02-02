from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,send_file
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField,FileField, SubmitField
import daredevil
from passlib.hash import sha256_crypt
from functools import wraps
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired,DataRequired
import deadpool
import Ironman
import bcrypt
import mysql.connector
import zipping
import matplotlib.pyplot as plt
import os
from Ghost import gimme_string
import shutil
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client
url ="https://hzmzxhzqslaoahheatdf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh6bXp4aHpxc2xhb2FoaGVhdGRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzUxNzcxODEsImV4cCI6MTk5MDc1MzE4MX0.BanV3RYn5QMXRMIIpCqGBplJllb57GAKKVpTpwl-xys"
supabase = create_client(url, key)

def hi(h):
    k = list(h)[:-1][0][1]
    u=[]
    for i in k:
        t=[]
        for j in i:
            t+=[i[j]]
        # print(t)
        date,junk=t[1].split('T')
        time,j = junk.split(".")
        r=[t[3],t[2],t[4],t[-1],time,date]
        u+=[r]
    return u
def hash_it(password):

    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, b'$2b$12$ikFJLhhV.1ziQsq0cT94IO')
    hash=str(hash)
    return hash[2:-1]

global current_filename
global global_dict
file_name=''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.secret_key='a'

class UploadFileForm(FlaskForm):
    Project_Name =  StringField("Name of the Project: ",validators=[DataRequired()])
    Author_Name =  StringField("Name of the Author: ",validators=[DataRequired()])
    Language =  StringField("Language used : ",validators=[DataRequired()])

    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

class TextAreaForm(FlaskForm):
    textarea  = StringField("Enter the text you want to check for plaigarism : ",validators=[DataRequired()])
    submit = SubmitField("Check for plaigarsm")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    
    return render_template('dashboard.html',data = hi(h = supabase.table("Projectdetails").select("*").execute()))

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/update_signup',methods=["POST"])
def validate():
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    email=request.form.get("email")
    password=request.form.get("password")
    json={
        "username":email,
        "password" : hash_it(password),
        "first_name":first_name,
        "last_name":last_name
    }
    supabase.table("Details").insert(json).execute()
    

    return render_template("home.html")

@app.route('/dashboard',methods=["POST"])
def final():
    user_name=request.form.get("email")
    password=request.form.get("password")
    q = supabase.table("Details").select("*").execute()
    out  = q.data[0]
    print(out["username"],out["password"])
    if out["username"] == user_name and out["password"]==hash_it(password):

        return render_template("dashboard.html",data = hi(h = supabase.table("Projectdetails").select("*").execute()))
    else:
        return render_template("home.html")

@app.route('/signup')
def dashboard():
    return render_template('signup.html')

@app.route('/download/<filename>')
def download(filename):
    try:
        path = "static\\files\\{}".format(filename)
        print(path)
        return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/temp',methods=["GET","POST"])
def temp():
    form = UploadFileForm()
    Project_Name = None
    Author_Name = None
    if form.validate_on_submit():
        Project_Name = form.Project_Name.data
        form.Project_Name.data = ' '
        Author_Name = form.Author_Name.data
        form.Author_Name.data = ' '
        file = form.file.data # First grab the file
        current_filename = file.filename
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "success"
    return render_template('v.html', form=form,Project_Name=Project_Name,Author_Name=Author_Name)
    


@app.route('/upload',methods=["GET","POST"])
def upload():
    global global_dict
    global current_filename
    form = UploadFileForm()
    Project_Name = None
    Author_Name = None
    Language =None
    if form.validate_on_submit():
        Project_Name = form.Project_Name.data
        form.Project_Name.data = ' '
        Language = form.Language.data
        form.Language.data = ' '
        Author_Name = form.Author_Name.data
        form.Author_Name.data = ' '
        file = form.file.data
        current_filename = file.filename
        file.save("static/files/"+file.filename)
        supabase.storage().from_("vetha").upload(file.filename,"static/files/"+file.filename)
        url = supabase.storage().from_("vetha").get_public_url(file.filename)
        print(url)
        # exit()
        string_dict = gimme_string(url)
        plag_flag , value,index ,d= deadpool.is_plag(string_dict)
        if value < 2:
            v = "2.png"
        elif value < 5:
            v="3.png"
        else:
            v="4.png"
        print()
        if plag_flag:
            labels = ["Plag_Index","Unplag_Index"]
            values = [round(float(index)),100-round(float(index))]
            plt.pie(values, labels=labels)
            plt.savefig('static/images/Index_chart.png')

            labels = ["Copied","own content"]
            values = [value*10,100-(value*10)]
            plt.pie(values, labels=labels)
            plt.savefig('static/images/Plag_chart.png')
            return render_template("valid.html",dict = d,file=v)
        else:
            flash("No chance of Plaigarism is found")
            json={

                "Projectname":Project_Name,
                "Authorname":Author_Name,
                "Language":Language,
                "Filepath" : url
            }
            supabase.table("Projectdetails").insert(json).execute()
            

            return render_template('dashboard.html',data = hi(h = supabase.table("Projectdetails").select("*").execute()))
        

        
    return render_template('upload.html', form=form,Project_Name=Project_Name,Author_Name=Author_Name)
    
@app.route("/ve")
def ve():
    labels = ['Jan', 'Feb', 'Mar', 'Apr']
    values = [12, 19, 3, 5]

    plt.pie(labels, values)
    plt.savefig('static/images/chart.png')
    return render_template("test.html")
@app.route('/valid')
def valid():
    return render_template("valid.html",dict = global_dict)
@app.route('/plaigarism',methods=["GET","POST"])
def plaigarism():
    form = TextAreaForm()
    textarea = None
    if form.validate_on_submit():
        textarea = form.textarea.data
        copied_links,word_count,Index_value=Ironman.plag_cheker(textarea)
        print(copied_links)
        return render_template("plaigarism.html",data = copied_links,form=form,textarea=textarea)
    return render_template("plaigarism.html",form=form,textarea=textarea)
@app.route('/vetha',methods=["POST"])
def vetha():
    print("inga iruken")
    string='<div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> \n <!-- <p>vetha</p> -->'
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


