from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# MongoDb password: 1do6U3WiHhy21keR

mongodb_uri = "mongodb+srv://om:1do6U3WiHhy21keR@primary-cluster.xli9dt7.mongodb.net/?retryWrites=true&w=majority&appName=Primary-Cluster"

mongodb_client = MongoClient(mongodb_uri)

mongodb_database = mongodb_client['main']


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

@app.route('/')
def index():
    if "logged_in" not in session:
        return redirect(url_for('sign_in'), code=302)

    user_data = mongodb_database.users.find_one({'email': session['email']})
    tasks_list = user_data['tasks']
    return render_template('index.html', tasks=tasks_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if "logged_in" not in session:
        return redirect(url_for('sign_up'), code=302)
    if request.method == "POST":
        task = request.form['task']
        mongodb_database.users.update_one({'email': session['email']}, {'$push': {'tasks': task}})
        return redirect(url_for('index'), code=302)     
    return render_template('add.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if mongodb_database.users.find_one({'email': email}):
            return 'User already exists'
        else:
            mongodb_database.users.insert_one({'name': name, 'email': email, 'password': password, 'tasks': []})
            return redirect(url_for('index'), code=302)
    return render_template('sign-up.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        user = mongodb_database.users.find({'email': email, 'password': password})
        print(user)
        if user is not None:
            session['logged_in'] = True
            session['email'] = email
            return redirect(url_for('index'), code=302)
        else:
            return 'Invalid credentials'
    return render_template('sign-in.html')

app.run(debug=True)