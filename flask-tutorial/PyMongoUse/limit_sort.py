
from flask import Flask,request
from flask.ext.pymongo import PyMongo,pymongo
from bson.json_util import dumps

app=Flask(__name__)

app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

mongo=PyMongo(app)

@app.route('/',methods=['GET'])
def index():
    numberss=mongo.db.numbers
    results=numberss.find().sort('name',pymongo.ASCENDING).limit(2)
    output = ''
    for r in results:
        output += r['name'] + ' - ' + str(r['Number']) + '<br>'
    return output
    #return dumps(results)


if __name__=='__main__':
    app.run(debug=True)