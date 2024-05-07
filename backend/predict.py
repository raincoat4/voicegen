from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000

@app.route('/')
def process_input():
    return "600"

if __name__ == '__main__':
    app.run(debug=True)
