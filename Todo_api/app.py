from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/todo', methods=['GET'])
def get_todo():
    todo_list = [
       { "id": 1, "description": "Clean room" },
        { "id": 2, "description": "Tea party with Karter" },
        { "id": 3, "description": "Worship wife"}
    ]
    return jsonify(todo_list)