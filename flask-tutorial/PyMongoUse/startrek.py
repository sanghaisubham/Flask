from flask import Flask,request
from flask.ext.pymongo import PyMongo,pymongo
from bson.json_util import dumps

app=Flask(__name__)

app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

mongo=PyMongo(app)

@app.route('/add_episode/<code>/<name>/<season>')
def add_episode(code,name,season):
    series=mongo.db.Series
    the_series=series.find_one({'code':code})
    episodes=mongo.db.episodes
    episodes.insert({'name':name,'season':season,'series_id':the_series['_id']})
    return 'Added '+name+' to the collection!'

@app.route('/get_episodes/<code>')
def get_episodes(code):
    series=mongo.db.Series
    the_series=series.find_one({'code':code})
    episodes=mongo.db.episodes
    series_episodes=episodes.find({'series_id':the_series['_id']})

    episode_list=''
    for e in series_episodes:
        episode_list+=e['name']+''
    return episode_list
if __name__=='__main__':
    app.run(debug=True)