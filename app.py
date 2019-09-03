from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask, url_for
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
     
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            flash('successful')
            return redirect(url_for('intro'))
        else:
            flash('wrong password')
            error= 'wrong'
     
        
    return render_template('login.html',error=error)


@app.route('/home', methods =['GET','POST'])
def home():
    return render_template('home.html')
  
@app.route('/signup', methods = ['GET','POST'])
def signup():
  return render_template('signup.html')

@app.route('/forgotpassword', methods = ['GET','POST'])
def forgotpassword():
  return render_template('forgot.html')

@app.route('/passreset', methods = ['GET','POST'])
def passreset():
  return render_template('passreset.html')

@app.route('/intro', methods = ['GET','POST'])
def intro():
  return render_template('intro.html')

@app.route("/logout")
def logout():
    return home()
  