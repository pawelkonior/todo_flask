from flask import Flask, jsonify, request

app = Flask(__name__)

db = [
    {
        "id": 1,
        "name": "learn python",
        "status": False
    },
    {
        "id": 2,
        "name": "learn sql",
        "status": False
    },
    {
        "id": 4,
        "name": "learn django",
        "status": False
    }
]


@app.route('/todos')
def get_todos():
    return jsonify(db), 200


@app.route('/todos/<int:idx>', methods=['GET'])
def get_todo(idx):
    for todo in db:
        if todo["id"] == idx:
            return jsonify(todo), 200

    return jsonify({"message": "Todo not found", "code": 404}), 404


@app.route('/todos', methods=['POST'])
def add_todo():
    db.append(request.json)
    return request.json, 201


@app.route('/')
def home():
    return 'Welcome home'
