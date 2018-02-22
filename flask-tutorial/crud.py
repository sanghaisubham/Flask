#Flask=>create instance of web application
#request=>get request data
#jsonify=>Turn Json Output into Response Object with application/json mimetype
#SQLAlchemy from flask_sqlalchemy to access database
#Marshmallow from flask_marshmallow to serialize object
from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
# create instances of our web application and set path of our SQLite uri
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'crud.sqlite')

#Binding SQLAlchemy and Marshmallow into our flask application
db=SQLAlchemy(app)
ma=Marshmallow(app)

#Declare our model called User and define its fields with its properties
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(120),unique=True)

    def __init__(self,username,email):
        self.username=username
        self.email=email

#Defines structure of our endpoint.We want all our endpoint have JSON response.Our JSON response will have two keys(username and email)

class UserSchema(ma.Schema):
    class Meta:
        #Field to expose
        fields=('username','email')

#We also defined user_schema as instance of UserSchema, and user_schemas as instances of list of UserSchema
user_schema=UserSchema()
users_schema=UserSchema(many=True)

#endpoint to create new user
#After setting the route and methods we define function that will be executed on accessing this endpoint
#On this function first we get username and email from request data,then we create new user using data from request data.
#Lastly we add new user to database and show new user in JSON form as response.
@app.route("/user",methods=["POST"])
def add_user():
    username=request.json['username']
    email=request.json['email']
    new_user=User(username,email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)
    #return 1

#endpoint to get list of all users and show the result as JSON response
@app.route("/user",methods=["GET"])
def get_user():
    all_users=User.query.all()
    result=users_schema.dump(all_users)
    #return "1"
    return jsonify(result.data)

#endpoint to get user detail by id
@app.route("/user/<id>",methods=["GET"])
def user_detail(id):
    user=User.query.get(id)
    return user_schema.jsonify(user)

#endpoint to update user based on a given id with value from request data.
@app.route("/user/<id>",methods=["PUT"])
def user_update(id):
    user=User.query.get(id)
    username=request.json['username']
    email=request.json['email']
    user.email=email
    user.username=username
    db.session.commit()
    return user_schema.jsonify(user)

#endpoint to delete user
@app.route("/user/<id>",methods=["DELETE"])
def user_delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

if __name__=='__main__':
    app.run(debug=True)