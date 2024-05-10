from flask import Flask
from flask_cors import CORS
from train import model, X_valid, y_valid
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load('trained_model.pkl')
testInput = X_valid[0]
testInput = np.array(testInput).reshape(1, -1)
result = model.predict(testInput)

@app.route('/')
def process_input():
    return str(result[0] + 1)

if __name__ == '__main__':
    app.run(debug=True)
