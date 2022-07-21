#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/index")

#‘/’ URL is bound with first_flask function.
def first_webpage():
    name= "Flask"
    return render_template("index.html", index_variable = name)

#Define a function with different endpoint


#run using debug argument
app.run(debug=True)
