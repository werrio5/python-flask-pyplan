import http
import json

from flask import Flask, Response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def helloworld():
    return Response(
      response=json.dumps({ 'message' : 'hello world!'}),
      status=http.HTTPStatus.OK,
      mimetype='application/json'
   )
