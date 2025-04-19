from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging
import numpy as np

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
model = None
scaler = None
expected_features = None

# Load model and scaler
def load_artifacts():
    global model, scaler, expected_features
    try:
        # Load model
        with open('pcos_best_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        # Load scaler
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
            
        # Get expected features
        if hasattr(model, 'feature_names_in_'):
            expected_features = model.feature_names_in_
        else:
            expected_features = ['Follicle No.(R)', 'Follicle No.(L)', 
                                 'Skin darkening(Y/N)', 'hair growth(Y/N)',
                                 'Weight gain(Y/N)', 'Cycle(R/I)']
            
        logger.info("Model and scaler loaded successfully")
    except Exception as e:
        logger.error(f"Error loading artifacts: {str(e)}")
        raise e

# Load artifacts on startup
load_artifacts()

# Home route for browser access
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "👋 PCOS Prediction API is running!",
        "usage": "Send a POST request to /predict with input JSON data."
    })

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.json

        # Validate required fields
        required_fields = ['Follicle No.(R)', 'Follicle No.(L)', 
                           'Skin darkening(Y/N)', 'hair growth(Y/N)',
                           'Weight gain(Y/N)', 'Cycle(R/I)']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Prepare input data
        input_data = {}
        for feature in expected_features:
            if feature in data:
                input_data[feature] = float(data[feature])
            else:
                input_data[feature] = 0.0  # Default for missing optional features

        # Convert to DataFrame in correct order
        features = pd.DataFrame([input_data], columns=expected_features)

        # Scale features
        scaled_features = scaler.transform(features)

        # Make prediction
        prediction = model.predict(scaled_features)[0]
        probability = model.predict_proba(scaled_features)[0][1]

        return jsonify({
            'prediction': int(prediction),
            'probability': round(float(probability), 4),
            'interpretation': '✅ PCOS likely' if prediction == 1 else '❌ PCOS unlikely'
        })
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
