from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
create_table_query = '''CREATE TABLE IF NOT EXISTS todo (
        id INTEGER,
        description TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    )'''
cursor.execute(create_table_query)
# Commit changes and close the cursor
conn.commit()
cursor.close()

@app.route('/api/todo', methods=['GET'])
def get_todo():
    select_query = "SELECT * FROM todo"
    todo_list = open_database_conn(select_query, True)
    data = [{'id': item[0], 'description': item[1]} for item in todo_list]
    return jsonify(data)

@app.route('/api/todo', methods=['POST'])
def post_todo():
    data = request.json
    desc = data['description']
    sqlStatement = 'INSERT INTO todo (description) VALUES (\'%s\')'% (desc)
    open_database_conn(sqlStatement)
    return
    


def open_database_conn(sqlStatement, isSelect = False):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(sqlStatement)
    if(isSelect):
       data = cursor.fetchall()
       cursor.close()
       conn.close()
       return data
    conn.commit()
    cursor.close()
    conn.close()

