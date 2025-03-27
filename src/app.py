from flask import Flask, request, render_template
import databaseHandler
import jsonHandler

app = Flask(__name__)

images = jsonHandler.read()["posts"]

@app.route("/")
def hello_world():
    return render_template('test.html', images=images)

@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        jsonHandler.write([[request.form['pathToImage'], request.form['url'], request.form['description']]])
        return render_template('test.html', images=images)
    
    return render_template('form.html')