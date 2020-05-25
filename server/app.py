import uuid, json

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from utils import *

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

@app.route('/tasks/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    index = findIndexById(task_id, TASKS)
    if index >= 0:
        TASKS.pop(index)
        return {"tasks": TASKS}
    else:
        abort(404)

@app.route('/tasks/update', methods=['PUT'])
def update_task():
    data = request.get_json()
    index = findIndexById(data.get('id'), TASKS)
    TASKS[index] = {
        'id' : data.get('id'),
        'title' : data.get('title')
    }
    return { "tasks": TASKS }

if __name__ == '__main__':
    app.run()