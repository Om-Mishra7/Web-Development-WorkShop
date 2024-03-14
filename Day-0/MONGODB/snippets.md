# Web Development Workshop - Hack On Campus | K.R. Mangalam University
Organized by: Om Mishra | [GitHub](https://github.com/Om-Mishra7) and Yash Soni | [GitHub](https://github.com/Yash-Soni774)   


## MongoDB

### What is MongoDB?
MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.

### Why MongoDB?
- MongoDB is a NoSQL database, which means it is a non-relational database. It is a database that does not require a fixed schema, avoids joins, and is easy to scale.
- MongoDB is a document-oriented database, which means it stores data in JSON-like documents.
- MongoDB is a distributed database at its core, so high availability, horizontal scaling, and geographic distribution are built in and easy to use.

### MongoDB With Flask

#### Installation
- Get URI from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Install pymongo using pip
```bash
pip install pymongo
```

#### Usage
```python
import pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("URI")
db = client.get_database("test")

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    db.get_collection("test").insert_one(data)
    return jsonify({"message": "Data added successfully"})

@app.route('/get', methods=['GET'])
def get():
    data = db.get_collection("test").find()
    return jsonify({"data": list(data)})
```

### MongoDB Atlas
- MongoDB Atlas is a fully-managed cloud database developed by the same people that build MongoDB. It is a database as a service offering that runs on the cloud, and it is designed to be secure, scalable, and reliable.

#### Steps to create a cluster
- Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Sign up and create a new cluster
- Choose a cloud provider and region
- Create a cluster
- Create a database user
- Whitelist your IP address
- Connect to your cluster
- Choose a connection method
- Connect your application

### MongoDB Compass
- MongoDB Compass is the GUI for MongoDB. It allows you to explore your databases, run queries, and interact with your data with full CRUD functionality.

#### MongoDB Commands in pymongo

- Insert a document
```python
db.get_collection("test").insert_one({"name": "Om Mishra"})
```

- Find a document
```python
data = db.get_collection("test").find_one({"name": "Om Mishra"})
```

- Update a document
```python
db.get_collection("test").update_one({"name": "Om Mishra"}, {"$set": {"name": "
Yash Soni"}})
```

- Delete a document
```python
db.get_collection("test").delete_one({"name": "Yash Soni"})
```

- Drop a collection
```python
db.get_collection("test").drop()
```

- Drop a database
```python
client.drop_database("test")
```


