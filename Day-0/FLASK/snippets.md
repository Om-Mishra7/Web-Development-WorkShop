# Web Development Workshop - Hack On Campus | K.R. Mangalam University
Organized by: Om Mishra | [GitHub](https://github.com/Om-Mishra7) and Yash Soni | [GitHub](https://github.com/Yash-Soni774)   


## Flask

Flask is a micro web framework written in Python, that will allow us to generate dynamic web pages. Most of the websites we use today are dynamic, meaning that the content of the website is not fixed, but is generated by a program.

So, we are going to learn how to create a web program that runs on a server and generates dynamic content to be sent to the client's web browser.

### HTTP

HTTP stands for Hyper Text Transfer Protocol. It is a protocol that allows the web server to communicate with the client's web browser. It is the protocol that allows the web server to understand the client's request and send the appropriate response.

Example: When you type a URL in your web browser, the browser sends an HTTP request to the web server. The server then sends an HTTP response back to the browser.

#### HTTP Codes

- 200: OK
- 404: Not Found
- 500: Internal Server Error

### Flask Installation

```bash
pip install flask
```

### Hello World

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

Now, run the above code and open your web browser and type `http://127.0.0.1/` in the address bar. You should see `Hello, World!` on the web page.

The `@app.route('/')` is a decorator that tells Flask what URL should trigger the function `hello_world()`. In this case, when you type `http://


## Routing

Routing is the process of selecting a path for traffic in a network or between or across multiple networks. In the context of web development, routing is the process of selecting a web page to display based on the URL.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/') # This says that when user goes to url: http://127.0.0.1:5000/ then the function index() will be called.
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/user/om')
def om():
    return 'Om Mishra'

@app.route('/user/yash')
def yash():
    return 'Yash Soni'

if __name__ == '__main__':
    app.run()
```

As you can see, we have defined multiple routes in the above code to just greet the user with their name, a better way to do this is to use a variable in the URL.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username.capitalize()}' # Capitalize the first letter of the username

if __name__ == '__main__':
    app.run()
```

### HTML Response

Let's return an HTML response instead of plain text response.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<h1>User {username.capitalize()}</h1>' # Capitalize the first letter of the username

if __name__ == '__main__':
    app.run()
```

As you can see, we have returned an HTML response instead of plain text response but as we can imagine saving the HTML as a string in the Python code is not a good practice. So, we can use templates to separate the HTML from the Python code.

### Templates

Create a folder named `templates` in the same directory as your Python file and create a file named `index.html` in the `templates` folder.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
</head>
<body>
    <h1>Index Page</h1>
</body>
</html>
```

Now, we can use the `render_template` function to render the HTML file.

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', username=username.capitalize()) # We are passing the context to the HTML file using the render_template function

if __name__ == '__main__':
    app.run()
```

Till now, we have seen how to return a static HTML file but what if we want to return a dynamic HTML file. For example, we want to username to be displayed on the web page.

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Page</title>
</head>
<body>
    <h1>User {{ username }}</h1> <!-- We are using the username variable here, this syntax is called Jinja2 -->
</body>

</html>
```

Let's create a simple website to tell user's is it new year or not.

```python
from flask import Flask, render_template
import datetime # You can read about datetime module here: https://docs.python.org/3/library/datetime.html

app = Flask(__name__)

@app.route('/')
def index():
    new_year = datetime.datetime.now().month == 1 and datetime.datetime.now().day == 1
    return render_template('index.html', new_year=new_year)

if __name__ == '__main__':

    app.run()
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
</head>
<body>
    {% if new_year %}
        <h1>Yes, it is New Year 🥳!</h1>
    {% else %}
        <h1>No, it is not New Year!</h1>
    {% endif %}
</body>
</html>
```

### Static Files

We till now have seen how to return HTML files but what if we want to return CSS, JavaScript, images, etc. We can use the `static` folder to store all the static files.

Create a folder named `static` in the same directory as your Python file and create a file named `style.css` in the `static/css` folder.

```css
body {
    background-color: #f0f0f0;
}
```

Now, we can use the `url_for` function to include the CSS file in the HTML file.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    {% if new_year %}
        <h1>Yes, it is New Year 🥳!</h1>
    {% else %}
        <h1>No, it is not New Year!</h1>
    {% endif %}
</body>
</html>
```

### To Do List

Let's create a simple to-do list website.

```python
from flask import Flask, render_template
app = Flask(__name__)

tasks = ["Complete the assignment", "Go to the gym", "Buy groceries"]

@app.route('/')
def index():
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>To Do List</title>
</head>
<body>
    <h1>To Do List</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

As you can see, we have used the `for` loop to loop through the tasks and display them on the web page, but still, we are not able to add or delete tasks. So, let's add the functionality to add and delete tasks.

```python
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

tasks = ["Complete the assignment", "Go to the gym", "Buy groceries"]

@app.route('/')
def index():
    return render_template('todo.html', tasks=tasks)

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>To Do List</title>
</head>
<body>
    <h1>To Do List</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add') }}">Add Task</a>
</body>
</html>
```

```html

<!DOCTYPE html>
<html>
<head>
    <title>Add Task</title>
</head>
<body>
    <h1>Add Task</h1>
    <form>
        <input type="text" name="task" placeholder="Enter task">
        <input type="submit" value="Add">
    </form>
</body>
</html>
```
Before we move forward, let's see that we are repeating the same code in the `add.html` file and the `index.html` file. Flask provides a way to include the HTML file in another HTML file using the concept of `extends` and `block`.


```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>To Do List</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>To Do List</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add') }}">Add Task</a>
{% endblock %}
```

```html
<!-- add.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Add Task</h1>
    <form>
        <input type="text" name="task" placeholder="Enter task">
        <input type="submit" value="Add">
    </form>
{% endblock %}
```


Let's add the functionality to add and delete tasks.

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>To Do List</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }} <a href="{{ url_for('delete', task=task) }}">Delete</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add') }}">Add Task</a>
{% endblock %}
```

```html
<!-- add.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Add Task</h1>
    <form method="POST"> <!-- We are using the POST method here, as we are sending the data to the server -->
        <input type="text" name="task" placeholder="Enter task">
        <input type="submit" value="Add">
    </form>
{% endblock %}
```

```python
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

tasks = ["Complete the assignment", "Go to the gym", "Buy groceries"]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST': # The request object has a method attribute that contains the method used by the client
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('index'), code=302)
    return render_template('add.html')

@app.route('/delete/<task>')
def delete(task):
    tasks.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
```

### Session

In the current implementation, if we close the web browser and open it again, the tasks will be lost, as well as all users will see the same tasks. We can use the `session` to store the tasks to a user.

```python
from flask import Flask, render_template, request, redirect, url_for, session   
app = Flask(__name__)
app.secret = 'secret' # This is the secret key used to sign the session cookie

app.config['SESSION_TYPE'] = 'filesystem' # This is the type of session, we are using filesystem here, you can use other types as well

@app.route('/')
def index():
    if 'tasks' not in session:
        session['tasks'] = []
    return render_template('index.html', tasks=session['tasks'])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task = request.form['task']
        session['tasks'].append(task)
        return redirect(url_for('index'), code=302)
    return render_template('add.html')

@app.route('/delete/<task>')
def delete(task):
    session['tasks'].remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
```



We have just scratched the surface of Flask, there is a lot more to learn especially how Flask can use databases to store the data. We will learn about databases in the next session.