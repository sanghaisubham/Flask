from flask import Flask
from flask.ext.pymongo import PyMongo,pymongo

app=Flask(__name__)

app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

mongo=PyMongo(app)

@app.route('/add')
def add():
    numbers = mongo.db.numbers
    numbers.insert({'name':'One','Number':1})
    numbers.insert({'name': 'Two', 'Number': 2})
    numbers.insert({'name': 'Three', 'Number': 3})
    numbers.insert({'name': 'Four', 'Number': 4})
    return 'Added'

@app.route('/')
def index():
    numberss=mongo.db.numbers
    #results=numberss.find({'name':'Two'})
    #results = numberss.find()
    #results=numberss.find({'Number':{'$lt':3}})#Numbers less than 3
    #results = numberss.find({'Number': {'$lte': 3}})  # Numbers less than or equal to 3
    #results = numberss.find({'Number': {'$gte': 3}})  # Numbers greater than or equal to 3
    #results = numberss.find({'Number': {'$ne': 3}})  # Numbers not equal to 3
    #results = numberss.find({'Number': {'$lt': 3},'name':{'gt':'g'}})  # Numbers less than 3 and name greater than g(first letter)
    results = numberss.find({'$or': [{'number':{'$gt':2}},{'number':{'$lt':3}}]})  # Numbers <3 or >2
    output=''
    for r in results:
        output+=r['name']+' - '+str(r['Number'])+'<br>'
    return output

if __name__=='__main__':
    app.run(debug=True)