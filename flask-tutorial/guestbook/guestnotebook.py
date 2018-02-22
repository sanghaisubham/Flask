from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)#(__name__ is the module name)
#app object contains all the configurations and the routes


app.config['SQLALCHEMY_DATABASE_URI']='mysql://sql12218878:1jMaFZ7kSU@sql12.freemysqlhosting.net/sql12218878'
#This is connection string for MYSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Avoids warny message in our console everytime something happens in the database

#intantiate the database object
db=SQLAlchemy(app)

#Model represents a table in a database
class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    comment=db.Column(db.String(1000))

#route is something which we can type in our browser URL or the HTTP request we make
@app.route('/')
def index():
    results=Comments.query.all() #Get a list of SQL alchemy objects
    return render_template('index.html',results=results)

@app.route('/sign')
def signpage():
    return render_template('sign.html')

@app.route('/process',methods=['POST']) # We can only access it using the post request
def process():
    name=request.form['name']
    comment=request.form['comment']
    signature=Comments(name=name,comment=comment)
    db.session.add(signature)
    db.session.commit()#save everything
    results = Comments.query.all()  # Get a list of SQL alchemy objects
    #return 'Name is :'+name+' and the comment is: '+comment
    #return render_template('index.html',results=results)
    return redirect(url_for('index')) #Now it will be redirected to 'index' endpoint not index.html

#If we just write POST here,then we will get an error here,
# because when we send something or access an endpoint using the URL we actually GET and not POST,so to correct that we use
#both the methods 'GET' and 'POST'.By default the method is 'GET'
@app.route('/home',methods=['GET','POST'])
def home():
    links=['https://www.youtube.com','https://www.python.org','https://www.google.com']
    return render_template('example.html',myvar='variable passed in ',links=links)

#<place> here is a variable
#Everything going from a browser is a GET method
@app.route('/home/<place>')
def homeplace(place):
    return '<h1> You are on the  '+place+' page! </h1>'

if __name__=='__main__':
    app.run(debug=True)

