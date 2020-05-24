import uuid, json

from flask import Flask, jsonify, request
from flask_cors import CORS

TASKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Hackerearth problem',
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Economics Maths'
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

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        TASKS.append({
            'id': uuid.uuid4().hex,
            'title': data.get('task')
        })
    return { "tasks": TASKS}

if __name__ == '__main__':
    app.run()