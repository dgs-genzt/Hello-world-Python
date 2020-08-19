import flask
from flask import jsonify
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

status = { "status": "OK", "version": "0.0.1", "uptime": datetime.datetime.now()}

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello!</p>"

@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify(status)

app.run('0.0.0.0', port=8080)