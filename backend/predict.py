from flask import Flask, request, jsonify
from flask_cors import CORS
from train import model, X_valid, y_valid
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load('trained_model.pkl')

# Example input for testing
testInput = X_valid[0]
testInput = np.array(testInput).reshape(1, -1)
result = model.predict(testInput)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Handle data sent from the frontend
        data = request.json
        input_value = data.get('inputValue')
        if input_value:
            # Process the input_value as needed
            return jsonify({"message": "Input received successfully"}), 200
        else:
            return jsonify({"message": "Invalid input"}), 400
    elif request.method == 'GET':
        # Handle data retrieval for the frontend
        return jsonify({"message": "Here is the data from the backend"}), 200

if __name__ == '__main__':
    app.run(debug=True)
