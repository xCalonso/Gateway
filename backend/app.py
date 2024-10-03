from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api')
def api_message():
    return jsonify({"message": "Hola desde Flask"})

if __name__ == "__main__":
    app.run(debug=True)