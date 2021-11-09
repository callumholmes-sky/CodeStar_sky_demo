#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/add/<float:x>/<float:y>')
def add(x,y):
    return Response(json.dumps({'Output': x+y}), mimetype='application/json', status=200)

@application.route('/callum/')
def callum():
    return Response(json.dumps({'Output': 'Hello Callum :)'}), mimetype='application/json', status=200)

@application.route('/will')
def will():
    return Response(json.dumps({'Output': 'hello will :'}), mimetype='application/json', status=200)

    
@application.route('/kev', methods=['GET'])
def kevFun():
    return Response(json.dumps({'kevin': 'I am the best'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
