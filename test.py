from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    tmp = 1+2
    return render_template('test.html', result = tmp)