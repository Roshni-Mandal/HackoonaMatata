import os
import backend
from flask import Flask
from flask import render_template, redirect, url_for, request


app = Flask(__name__)
local_username = ""

@app.route('/')
def home():
    return "HOME"

@app.route('/signin', methods=["POST","GET"])
def Sign_In():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if backend.login_validation(username, password) == True:
            local_username = username
            return "Login Succesful"

        else:
            return "Login Failed: Password And Username Do Not Match"
    else:
        print("Not A Post Request")
        return render_template('Login.html')

@app.route('/signup', methods=["POST","GET"])
@app.route('/register', methods=["POST","GET"])
def Sign_Up():
    if request.method == "POST":
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]
        backend.create_user(username, name, password)
        return "User Creation Succesful"

    else:
        print("Not A Post Request")
        return render_template('SignUp.html')

@app.route('/addmoney', methods=["POST","GET"])
def addmoney():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.add_bal(local_username, amount)
        print(amount,"Added to Balance")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

@app.route('/subtractmoney', methods=["POST","GET"])
def submoney():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.subtract_bal(local_username, amount)
        print(amount, "Subtracted From Balance")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

@app.route('/addloan', methods=["POST","GET"])
def addloan():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.add_loan(local_username, amount)
        print(amount, "Added to Loan")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

@app.route('/subtractloan', methods=["POST","GET"])
def subloan():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.subtract_loan(local_username, amount)
        print(amount, "Subtracted From Loan")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

@app.route('/addjob')
def addjob():
    backend.add_job(local_username)
    print("Job Was Added")
    return "Job Was Added"

@app.route('/removejob')
def removejob():
    backend.remove_job(local_username)
    print("Job Was Removed")
    return "Job Was Removed"

@app.route('/addcredit', methods=["POST","GET"])
def addcredit():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.add_creditscore(local_username, amount)
        print(amount, "Added to Credit Score")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

@app.route('/subtractcredit', methods=["POST","GET"])
def subcredit():
    if request.method == "POST":
        amount = request.form["amount"]
        backend.subtract_creditscore(local_username, amount)
        print(amount, "Subtracted Credit Score")
    else:
        print("Not A Post Request")
        return "Not A Post Request"

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)