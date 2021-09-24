from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flash Cards Application !!"


@app.route("/date")
def date():
    return "This page is served at:" + str(datetime.now())


counter = 0


@app.route("/count")
def count_views():
    global counter
    counter += 1
    return "This page is served: " + str(counter) + " times "
