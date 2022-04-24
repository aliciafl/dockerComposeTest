import pymongo
from bson.json_util import dumps, loads
from datetime import date


from flask import Flask

app = Flask(__name__)

def connect(database_name, collection_name):
    #client = pymongo.MongoClient(host='localhost', port=27017, username='root',password='pass', authSource="admin")
    #client = pymongo.MongoClient("mongodb://root:pass@composetest-mongo-1", authSource="admin")
    client = pymongo.MongoClient("mongodb://root:pass@mongo")
    client.server_info()
    # Database connection
    database = client.get_database(database_name)
    # Collection connection
    table = database.get_collection(collection_name)
    return table

def to_json(table):
    # Convert from Mongo cursor type to JSON
    cursor = table.find()
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    json_data = loads(json_data)
    return json_data

def write_data(table):
    query_object = {
    'name': 'Test',
    #'date': date.today()
    }
    query = table.insert_one(query_object)
    print(query) 

@app.route('/')
def hello():
    table = connect('test_db', 'test_col')
    write_data(table)
    json_data = to_json(table)
    return 'Hello World! This is the data available {} .\n'.format(json_data)
    #return "hello"

""" 
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)  """