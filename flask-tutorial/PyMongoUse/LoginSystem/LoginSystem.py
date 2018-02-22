from flask import Flask,render_template,url_for,request,session,redirect
from flask.ext.pymongo import PyMongo
import  bcrypt
#Flask Pymongo is a wrapper around the pymongo library for flask
#Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.
app=Flask(__name__)
app.config['MONGO_DBNAME']='rasberry'
app.config['MONGO_URI']='mongodb://Subham:codeblocks@ds231987.mlab.com:31987/rasberry'

#instantiating the database connection
mongo=PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return  'You are logged in as '+session['username']

    return render_template('index.html')

@app.route('/login',methods=['POST'])#This is post because it takes the login credentials and checks if it correct or not
# by querying the database
def login():
    users = mongo.db.loginuser
    loginname=users.find_one({'name':request.form['username']})
    if loginname:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),loginname['password'])==loginname['password']:
            session['username']=request.form['username']
            return redirect(url_for('index'))
        return 'Invalid username/password combination'
    return 'Invalid Username'


@app.route('/register',methods=['POST','GET'])
#Post allows user to register and get method returns the registration template
def register():
    if request.method=='POST':
        users=mongo.db.loginuser
        existing_user=users.find_one({'name':request.form['username']})
        if existing_user is None:
            #What we want to do is to salt the passwords which means that instead of just hashing the password we hash the password + a salt.
            hashpass=bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt()) #Here in inverted comma we pass in the name of the form data under name
            users.insert({'name':request.form['username'],'password':hashpass})
            session['username']=request.form['username']
            return redirect(url_for('index'))
        return 'That username already exists'
    return render_template('register.html')#This is when the method is GET ,when called from the index.html page
if __name__=='__main__':
    app.secret_key='mysecret'
    app.run(debug=True)
