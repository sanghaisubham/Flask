from flask import Flask #ask the application to import Flask module from flask package .
                        # Flask is used to create instances of web appliction

app=Flask(__name__)#Creates an instance of our application.(__name__ is a special variable in python)
                   #It will be equal to "__main__" if the module(python file) being executed as the main program

@app.route("/") #Indicates the route ,
                # if we set route to "/hello" then "hello world" will be shown only when we access localhost:5000/hello
def hello():
    return "Hello World!"

#This means the flask app will begin run if we run from app.py.Debug is set to True which will print the possible
#Python errors on the web Page helping us to trace the errors
if __name__=='__main__':
    app.run(debug=True)
