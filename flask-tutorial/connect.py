from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

app=Flask(__name__)
app.config['MONGOALCHEMY_DATABASE']='mydatabase'
app.config['MONGOALCHEMY_CONNECTION_STRING']='mongodb://Subham:codeblocks@ds121118.mlab.com:21118/mydatabase'

db=MongoAlchemy(app)

class Example(db.Document):
    name=db.StringField()

