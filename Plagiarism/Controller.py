from flask import Flask, render_template, request, url_for, redirect
from Plagiarism import plagiarism_checker
from logincode import login, logoff
#Code to write to get server running
#export FLASK_APP=Controller.py
#export FLASK_DEBUG=1
#flask run

app = Flask(__name__)

plagiarism_percent=0.0

plagiarism_message=""

color=""

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('homepage.html')
    

@app.route('/documentation')
def documentation_page():
    return render_template('documentation.html')

@app.route('/documentation' , methods=('GET', 'POST'))
def input_field():
    if request.method == 'POST':
        content= request.form['content']
        global plagiarism_percent
        plagiarism_percent= plagiarism_checker(content) 
        global color
        global plagiarism_message
        if plagiarism_percent < 30:
            plagiarism_message="Your written piece of text is within the plagiarism standards as it's plagiarised percentage is less than 30%"
            color="green"
        else:
            plagiarism_message="Your written piece of text contains too much of plagiarised information as its plagiarised percentage is above 30%"
            color="red"
        

        return redirect('index')

    return render_template('documentation.html')

@app.route('/index')
def index_page():
    return render_template('index.html', plagiarism_percent=plagiarism_percent, plagiarism_message=plagiarism_message, color=color)

@app.route('/login')
def authentication_page():
    return render_template('loginpage.html')

@app.route('/login' , methods=('GET', 'POST'))
def login_field():
    if request.method == 'POST':
        name= request.form['username']
        passw= request.form['password']
        login(name, passw)
        return redirect('home')
    return render_template('homepage.html')

@app.route('/logout')
def logout():
    logoff()
    return render_template('logout.html')
