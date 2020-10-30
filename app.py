# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/mL")
def mL():
    return render_template("mL.html")

@app.route("/Tableau")
def Tabluea():
    return render_template("Tableau.html")

@app.route("/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)
