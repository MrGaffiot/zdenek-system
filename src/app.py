from flask import Flask, request, render_template, session
import databaseHandler
import jsonHandler

app = Flask(__name__)

images = jsonHandler.read()["posts"]

with open("data\secretKey.txt", "r") as file:
    print(file.read())
    app.secret_key = file.read().encode("utf-8")

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

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/editorTest')
def editorTest():
    return render_template('editor_test.html')

@app.route('/scrollingTest')
def scrollingTest():
    return render_template('scrolling_test.html')
if __name__ == "__main__":
    app.run(debug=True)
