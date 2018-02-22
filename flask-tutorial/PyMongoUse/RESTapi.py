from flask import Flask,request,jsonify
from flask.ext.pymongo import PyMongo,pymongo
from bson.json_util import dumps

app=Flask(__name__)

app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

mongo=PyMongo(app)

@app.route('/framework')
def getting():
    friend_interest=mongo.db.friends_interest
    all_interest=friend_interest.find()
    finalans=''
    for  i in all_interest:
        finalans+='Name: '+i['Name']+' Interest: '+i['Interest']+'<br>'
    return finalans

@app.route('/framework/<name>')
def getting_one(name):
    friend_interest=mongo.db.friends_interest
    all_interest=friend_interest.find_one({'Name':name})
    finalans=''
    if all_interest:
        finalans+='Name: '+all_interest['Name']+' Interest: '+all_interest['Interest']+'\n'
    else:
        finalans='No result Found'
    return finalans
@app.route('/framework',methods=['POST'])
def posting():
    friend_interest = mongo.db.friends_interest
    name=request.json['Name']
    interest=request.json['Interest']
    friend_interest.insert({'Name':name,'Interest':interest})
    return 'Added'

if __name__=='__main__':
    app.run(debug=True)