from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About Us'

@app.route('/greet/<username>')
def greet(username):
    return render_template('greet.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)