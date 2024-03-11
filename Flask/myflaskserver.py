import sqlite3
import json
from flask import Flask, request, app

app = Flask(__name__)



@app.route('/')
def start():
    return ("<h1> Welcome to my page </h1>")


@app.route('/post_json', methods=['POST'])
def handle_json():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    data = request.form.to_dict(flat=True)
    for key, value in data.items():
        print(f"UPTDATE stats set count = {value} where id = '{key}'")
        cursor.execute(f"UPDATE stats set count = {value} where id = '{key}'")
    connection.commit()
    connection.close()
    return "yeet"


if __name__ == '__main__':
    app.run(debug=True)
