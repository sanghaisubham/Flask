
from flask import Flask,request
from flask.ext.pymongo import PyMongo,pymongo
from bson.json_util import dumps

app=Flask(__name__)

app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

mongo=PyMongo(app)

@app.route('/',methods=['POST'])
def index():
    query=request.json['q']
    sortval=request.json['s']
    numberss=mongo.db.numbers
    if sortval=='asc':
        result=numberss.find(query)
    else:
        result = numberss.find(query).sort('Number', pymongo.DESCENDING)
    return dumps(result)
#Dumps will take the result and convert it into a JSON object


if __name__=='__main__':
    app.run(debug=True)