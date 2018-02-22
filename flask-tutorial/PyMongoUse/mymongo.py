from flask import Flask
from flask.ext.pymongo import PyMongo
#Flask Pymongo is a wrapper around the pymongo library for flask

app=Flask(__name__)
app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

#instantiating the database connection
mongo=PyMongo(app)

@app.route('/add')
def add():

    #'mongo' is the object created by pymongo
    #'db' is the default databse we declared under the DBName
    #'Data' is the collection that we are going to use
    # if the collection does not exist ,it will create it

    user=mongo.db.Data
    user.insert({'name':'Subham','Lang':'Python'})
    user.insert({'name': 'Rajat', 'Lang': 'JS'})
    user.insert({'name': 'Aman', 'Lang': 'HTML'})
    return 'Added User'

@app.route('/find')
def find():
    user=mongo.db.Data
    userdata=user.find_one({'name':'Subham'}) #userdata is a python dictionary(JSON object in DB)
    return 'You Found '+userdata['name']+' His Fav lang is '+userdata['Lang']

@app.route('/update')
def update():
    user = mongo.db.Data
    userdata = user.find({'name': 'Aman'})  # userdata is a python dictionary(JSON object in DB)
    #If we use find_one then only one user comes which can be accessed ,
    # while with find an array is returned which can be traversed using for loop
    for users in userdata:
        users['Lang']='Bakchodi :P '
        user.save(users)
    return 'Updated!!'

@app.route('/delete')
def delete():
    user=mongo.db.Data
    userdata = user.find_one({'name': 'Aman'})
    user.remove(userdata)
    return 'Removed!'

if __name__=='__main__':
    app.run(debug=True)
