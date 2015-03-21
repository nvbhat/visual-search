import flask
from flask import render_template, request, jsonify

app = flask.Flask(__name__)

    
@app.route("/")
def hello():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug = True)

