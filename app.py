from flask import Flask, Response, request, jsonify
from bson import Binary, Code
from bson.json_util import dumps
import re

app = Flask(__name__)

client = MongoClient()
db = client.tasks

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
app.after_request(add_cors_headers)


@app.route('/programs/<program_name>', methods=['GET'])
def run_program():
    code = tasks.run_process(program_name)
    data = {"status":str(code)}
    return Response(dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.after_request(add_cors_headers)
    app.run(threaded=True, host='0.0.0.0', port=7001, debug=True)
