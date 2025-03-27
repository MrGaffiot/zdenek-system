from flask import Flask
from flask import render_template
import databaseHandler

app = Flask(__name__)

images = [
    ["1.webp", "https://www.google.com/", "1"],
    ["1.webp", "https://www.google.com/", "1"],
    ["1.webp", "https://www.google.com/", "1"],
    ["1.webp", "https://www.google.com/", "1"],
    ["1.webp", "https://www.google.com/", "1"],
    ["2.webp", "https://www.google.com/", "2"],
    ["3.gif", "https://www.google.com/", "3"],
    ["4.gif", "https://www.google.com/", "4"],
    ["5.gif", "https://www.google.com/", "5"],
    ["6.png", "https://www.google.com/", "6"]
]

@app.route("/")
def hello_world():
    return render_template('test.html', images=images)