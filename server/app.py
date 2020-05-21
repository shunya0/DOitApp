import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

LIST = [
    {
        'id': uuid.uuid4().hex,
        'task': 'Hackerearth problem',
    },
    {
        'id': uuid.uuid4().hex,
        'task': 'Economics Maths'
    }
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()