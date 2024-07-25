from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = "todos list"
        response_body['results'] = "todos"
        return response_body, 200
    if request.method == 'POST':
        data = request.json
        todos.append(data)
        response_body['message'] = 'task added'
        response_body['results'] = 'todos'
        return response_body, 201

# @app.route('/todos', methods=['POST'])
# def add_new_todo():


@app.route('/todos/<int:position>', methods=[ 'GET', 'PUT', 'DELETE'])
def hadle_todo(position):
    response_body = {}
    if position >= len(todos):
        response_body['message'] = 'task not created'
        response_body['results'] = {}
        return response_body, 404
    if request.method == 'GET':
        response_body['message'] = f'Task data {position}'
        response_body['results'] = todos[position]        
        return response_body, 200
    if request.method == 'PUT':
        todos[position] = request.json
        response_body['message'] = f'Task {position} modified'
        response_body['results'] = todos[position]        
        return response_body, 200
    if request.method == 'DELETE':
        return response_body, 404
        del todos[position]
        response_body['message'] = 'Deleted'
        response_body['results'] = todos

some_data = {"name": "Bobby", "lastname": "Rixer"}
todos = [{"label": "My first task", "done": False}]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
