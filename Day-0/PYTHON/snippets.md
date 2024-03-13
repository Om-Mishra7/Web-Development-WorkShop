# Web Development Workshop - Hack On Campus | K.R. Mangalam University
Organized by: Om Mishra | [GitHub](https://github.com/Om-Mishra7) and Yash Soni | [GitHub](https://github.com/Yash-Soni774)   


## Python

We will now start with our first language of this workshop, Python. Python allows us to build application quickly because of lots of inbuilt libraries and frameworks,  we will be introducing you to Python today and some of it's advanced topics.

### Hello World
```python
print("Hello, World!")
```

This is how you print something in python. The `print` function is used to print something on the screen, and the thing inside the parenthesis we provide a argument to the function. In this case, we are providing a string "Hello, World!".

Now the file is saved as `hello.py`, .py is the extension of python files. To run the file, open the terminal and type `python hello.py` and press enter. You will see the output as `Hello, World!` on the terminal.

The `python command` is used to run the python files. As python is an interpreted language, the python interpreter reads the file line by line and executes it.

```bash
$ python hello.py
Hello, World!
```

### Variables

Like any other programming language, Python also has variables. Variables are used to store data. In python, we don't need to specify the type of the variable, python automatically detects the type of the variable.

```python
integer_variable = 10
string_variable = "Hello, World!"
float_variable = 10.5
boolean_variable = True
none_variable = None # None is a special type in python, it is used to represent the absence of a value.
```

### Input in Python

```python
name = input("Enter your name: ")
print("Hello, " + name) # `+` is used to concatenate strings
```

The `input` function is used to take input from the user. The argument to the input function is the prompt that will be shown to the user. The input function returns the input given by the user as a string.

We can also use the f-strings to format the string.

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

### Conditional Statements

In addition to variables, python also has conditional statements. Conditional statements are used to execute a block of code based on some condition.

```python
number = input("Enter your number: ")
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")
```

The condition in python begins with `if` keyword, followed by the condition and a colon. The block of code to be executed if the condition is true is indented. The `else` keyword is used to execute a block of code if the condition is false.

The indentation is very important in python, it is used to define the block of code. The standard indentation is 4 spaces.

We can also use the `elif` keyword to check multiple conditions.

```python
number = int(input("Enter your number: "))
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
```

### Sequence Data Types

Python has many inbuilt sequence data types. The most common ones are strings, lists, and tuples.

#### Strings

Strings are used to store text data. Strings are immutable, which means once a string is created, it cannot be changed.

```python
string = "Hello, World!"
print(string[0]) # H
print(string[7]) # W
print(string[0:5]) # Hello
print(string[7:]) # World!
```

#### Lists

Lists are used to store multiple items in a single variable. Lists are mutable, which means the items in the list can be changed.

```python
list = [1, 2, 3, 4, 5]
print(list[0]) # 1
print(list[2]) # 3
print(list[0:3]) # [1, 2, 3]
print(list[2:]) # [3, 4, 5]

# Adding a new item to the list
list.append(6)

# Sorting the list
list.sort()
```

#### Tuples

Tuples are used to store multiple items in a single variable. Tuples are immutable, which means the items in the tuple cannot be changed. e.g. coordinates, colors, etc.

```python
tuple = (1, 2, 3, 4, 5)
print(tuple[0]) # 1
print(tuple[2]) # 3
print(tuple[0:3]) # (1, 2, 3)
print(tuple[2:]) # (3, 4, 5)
```

### Sets

Sets are used to store multiple items in a single variable. Sets are immutable, unordered and unindexed, which means the items in the set can appear in any order. They are similar to the concept of sets in mathematics.

```python
set = {1, 2, 3, 4, 5}
print(set) # {1, 2, 3, 4, 5}
set.add(5)
print(set) # {1, 2, 3, 4, 5}

set.remove(2)

print(f"The length of the set is {len(set)}") # The length of the set is 4
```

### Dictionaries

Just like a dictionary, a dictionary in python is used to store key-value pairs. Dictionaries are mutable, which means the items in the dictionary can be changed.

```python
dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(dictionary["name"]) # John
print(dictionary["age"]) # 30

# Adding a new key-value pair
dictionary["email"] = "test@example.com"
print(dictionary) # {'name': 'John', 'age': 30, 'city': 'New York', 'email': '
```

### Loops

The idea of a loop is to repeat a set of statements as long as the condition is true, python has two types of loops, `for` and `while`.

#### For Loop

The `for` loop is used to iterate over a sequence (list, tuple, string, etc.) or other iterable objects.

```python
for i in [1, 2, 3, 4, 5]:
    print(i)
```

For large sequences, we can use the `range` function.

```python
for i in range(1000):
    print(i)
```

The `range` function is used to generate a sequence of numbers. The `range` function takes 3 arguments, `start`, `stop`, and `step`. The `start` argument is optional and the default value is 0, the `step` argument is also optional and the default value is 1.

```python
for i in range(1, 10, 2):
    print(i)
```

#### While Loop

The `while` loop is used to execute a block of code as long as the condition is true.

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

### Functions

A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

```python
def square(x):
    return x * x

for i in range(1, 10):
    print(f"The square of {i} is {square(i)}")
```

The `def` keyword is used to define a function, followed by the function name and the parameters in the parenthesis. The block of code to be executed is indented.

### Modules and Packages

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. A package is a collection of modules.

```python
# functions.py
def square(x):
    return x * x

# main.py
import functions

for i in range(1, 10):
    print(f"The square of {i} is {functions.square(i)}")
```

The `import` keyword is used to import a module or a package. The `as` keyword is used to give an alias to the module or package.


### Classes and Objects

Python is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects. Objects are instances of classes, where classes are representations of real-world entities.

```python
# Creating a cooridnate class

class Coordinate:
    def __init__(self, x, y): # The __init__ method is used to initialize the object with the given values
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        return (x_diff + y_diff) ** 0.5

c1 = Coordinate(1, 2) # Creating a new object of the class Coordinate
c2 = Coordinate(4, 6)

print(c1.distance(c2))
```

Let's take a look at a more complex example.

```python
class Flight:
    def __init__(self, origin, destination, duration, capacity):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.capacity:
            print("The flight is full, cannot add more passengers")
            return
        self.passengers.append(name)
        self.capacity -= 1
        print(f"Added {name} to the flight successfully")

    def print_info(self):
        print(f"The flight from {self.origin} to {self.destination} is of {self.duration} minutes and has {self.capacity} seats left")

flight_1 = Flight("New York", "Paris", 540, 10)

passengers = ["John", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia", "Parker", "Quinn", "Ryan", "Sophia", "Thomas", "Uma", "Victoria", "William", "Xander", "Yasmine", "Zachary"]

for passenger in passengers:
    flight_1.add_passenger(passenger)


flight_1.print_info()

```

### Decorators

In python, functions are first-class objects, which means that they can be passed around and used as arguments.

Decorators are a way to modify the behavior of a function or a class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

```python
def decorator_function(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
```

### Lambda Functions

Lambda functions are small anonymous functions. They can have any number of arguments but only one expression.

```python

student_info = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 21},
    {"name": "Charlie", "age": 23},
    {"name": "David", "age": 24},
    {"name": "Eve", "age": 25},
    {"name": "Frank", "age": 26},
    {"name": "Grace", "age": 27},
    {"name": "Hannah", "age": 28},
    {"name": "Ivy", "age": 29},
]

# We can't use the sort method directly on the list of dictionaries because the sort method only works on lists of numbers or strings.

# We can use the sorted function with the key argument to sort the list of dictionaries based on the age.

def get_age(student):
    return student["age"]

student_info.sort(key=get_age)

print(student_info)

# We can also use the lambda function to achieve the same result.

student_info.sort(key=lambda student: student["age"])

print(student_info)

```

### Exception Handling

Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong), so that the program can handle the error in a specific way and not just crash.

```python

a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("The program has ended")
```

The `try` block lets you test a block of code for errors. The `except` block lets you handle the error. The `finally` block lets you execute code, regardless of the result of the try and except blocks.

