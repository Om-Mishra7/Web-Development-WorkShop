from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

@app.route('/')
def index():
    if 'tasks' not in session:
        session['tasks'] = []
    return render_template('index.html', tasks=session['tasks'])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        task = request.form['task']
        session['tasks'] += [task]
        return redirect(url_for('index'), code=302)     
    return render_template('add.html')

app.run(debug=True)