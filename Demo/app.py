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
    if 'tasks' not in session:
        session['tasks'] = []
    return render_template('index.html', tasks=session['tasks'])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if "logged_in" not in session:
        return redirect(url_for('sign_up'), code=302)
    if request.method == "POST":
        task = request.form['task']
        session['tasks'] += [task]
        return redirect(url_for('index'), code=302)     
    return render_template('add.html')

@app.route('/delete/<index>')
def delete(index):
    if "logged_in" not in session:
        return redirect(url_for('sign_up'), code=302)
    index = int(index) - 1
    session['tasks'] = session['tasks'][:int(index)] + session['tasks'][int(index)+1:]
    return redirect(url_for('index'), code=302)

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if mongodb_database.users.find_one({'email': email}):
            return 'User already exists'
        else:
            mongodb_database.users.insert_one({'name': name, 'email': email, 'password': password})
            return redirect(url_for('index'), code=302)
    return render_template('sign-up.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = mongodb_database.users.find_one({'email ': email, 'password': password})
        if user:
            session['logged_in'] = True
            return redirect(url_for('index'), code=302)
        else:
            return 'Invalid credentials'
    return render_template('sign-in.html')

app.run(debug=True)