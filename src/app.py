from flask import Flask, request, render_template, session
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
        file = request.files['newFile']
        file.save(f"static/{file.filename}")
        jsonHandler.write([[file.filename, request.form['url'], request.form['description']]])
        return render_template('test.html', images=jsonHandler.read()["posts"])
    
    return render_template('form.html')
