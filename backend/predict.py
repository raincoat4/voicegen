from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from pydub import AudioSegment
import numpy as np
import python_speech_features as psf
import io
import joblib
import logging

# just put this here
logging.basicConfig(level=logging.DEBUG)

model = joblib.load('trained_model.pkl')

def get_mfcc(file_path):
    try:
        logging.debug(f"Processing file: {file_path}")
        audio = AudioSegment.from_file(file_path)
        audio = audio.set_channels(1)
        wav_io = io.BytesIO()
        audio.export(wav_io, format='wav')
        wav_io.seek(0)

        sample_rate = audio.frame_rate
        signal = np.frombuffer(wav_io.read(), dtype=np.int16)

        frame_length = 0.025  # 25ms frame length in seconds
        nfft = int(frame_length * sample_rate)
        mfccs = psf.mfcc(signal, samplerate=sample_rate, numcep=13, nfft=nfft)
        logging.debug(f"MFCCs shape: {mfccs.shape}")
        return ','.join(map(str, mfccs.flatten()))
    except Exception as e:
        logging.error(f"Error processing audio file: {e}")
        raise RuntimeError(f"Error processing audio file: {e}")

def len_mfcc(mfcc, max_length=6):
    mfcc = mfcc.split(",")
    mfcc_len = len(mfcc)
    mfcc = [int(digit) for digit in str(mfcc_len)]
    if len(mfcc) < max_length:
        mfcc = [0] * (max_length - len(mfcc)) + mfcc
    elif len(mfcc) > max_length:
        mfcc = mfcc[:max_length]
    return mfcc

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        logging.error("No file selected for uploading")
        return jsonify({'error': 'No file selected for uploading'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    try:
        file.save(filepath)
        logging.debug(f"File saved to: {filepath}")
        
        mfcc = get_mfcc(filepath)
        mfcc2 = len_mfcc(mfcc)
        
        # convert to numpy array and reshape for model input
        mfcc2 = np.array(mfcc2).reshape(1, -1)
        logging.debug(f"Input for model: {mfcc2}")

        result = model.predict(mfcc2)
        logging.debug(f"Model prediction: {result}")

        return jsonify({'mfcc2': mfcc2.tolist(), 'result': result.tolist()}), 200
    except Exception as e:
        logging.error(f"Processing error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
            logging.debug(f"File removed: {filepath}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
