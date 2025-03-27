from flask import Flask
from flask import render_template
import databaseHandler
import jsonHandler

app = Flask(__name__)

images = jsonHandler.read()["posts"]

@app.route("/")
def hello_world():
    return render_template('test.html', images=images)