# app.py - House Price Prediction Flask Application

from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import logging
from datetime import datetime
import os
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Load trained model
try:
    model = joblib.load('xgb_house_model.pkl')
    logger.info("Model loaded successfully")
except FileNotFoundError:
    logger.error("Model file not found")
    model = None

# Constants
FEATURE_NAMES = ['OverallQual', 'GrLivArea', 'GarageCars', '1stFlrSF', 'TotRmsAbvGrd']
MODEL_R2_SCORE = 0.91
MIN_VALUES = {'OverallQual': 1, 'GrLivArea': 400, 'GarageCars': 0, '1stFlrSF': 0, 'TotRmsAbvGrd': 2}
MAX_VALUES = {'OverallQual': 10, 'GrLivArea': 6000, 'GarageCars': 5, '1stFlrSF': 5000, 'TotRmsAbvGrd': 15}


def validate_input(f):
    """Decorator to validate prediction input"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            data = request.form if request.method == 'POST' else request.args
            
            # Extract and validate features
            features = {}
            for feature in FEATURE_NAMES:
                try:
                    value = float(data.get(feature, 0))
                    
                    # Validate range
                    if value < MIN_VALUES.get(feature, float('-inf')) or value > MAX_VALUES.get(feature, float('inf')):
                        raise ValueError(f"{feature} must be between {MIN_VALUES.get(feature)} and {MAX_VALUES.get(feature)}")
                    
                    features[feature] = value
                except ValueError as e:
                    raise ValueError(f"Invalid value for {feature}: {str(e)}")
            
            return f(features, *args, **kwargs)
        except Exception as e:
            logger.error(f"Input validation error: {str(e)}")
            return None
    
    return decorated_function


@app.route('/')
def home():
    """Home page route"""
    try:
        logger.info("Home page accessed")
        return render_template('index.html', model_r2=MODEL_R2_SCORE)
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        return render_template('index.html', error="Error loading page")


@app.route('/api/model-info')
def model_info():
    """API endpoint to get model information"""
    try:
        model_details = {
            'model_type': 'XGBoost Regressor',
            'r2_score': MODEL_R2_SCORE,
            'features': FEATURE_NAMES,
            'min_values': MIN_VALUES,
            'max_values': MAX_VALUES,
            'last_updated': '2024-12-28',
            'accuracy_info': 'R² = 0.91 on test dataset, RMSE ≈ $25,000'
        }
        logger.info("Model info requested")
        return jsonify(model_details), 200
    except Exception as e:
        logger.error(f"Error fetching model info: {str(e)}")
        return jsonify({'error': 'Failed to fetch model information'}), 500


@app.route('/api/predict', methods=['POST'])
@validate_input
def api_predict(features):
    """API endpoint for price prediction (JSON)"""
    try:
        if model is None:
            logger.error("Model not loaded")
            return jsonify({'error': 'Model not available'}), 503
        
        # Prepare feature array
        feature_array = np.array([[features.get(f, 0) for f in FEATURE_NAMES]])
        
        # Make prediction
        prediction = model.predict(feature_array)[0]
        predicted_price = round(float(prediction), 2)
        
        # Log prediction
        logger.info(f"Prediction made: {features} -> ${predicted_price}")
        
        # Return structured response
        response = {
            'success': True,
            'predicted_price': predicted_price,
            'currency': 'USD',
            'model_r2_score': MODEL_R2_SCORE,
            'confidence': 'High' if MODEL_R2_SCORE > 0.85 else 'Medium',
            'input_features': features,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 400


@app.route('/predict', methods=['POST'])
def predict():
    """Traditional form-based prediction endpoint"""
    try:
        if model is None:
            logger.error("Model not loaded")
            return render_template('index.html', error="Model is not available")
        
        # Extract form data
        try:
            overallqual = float(request.form['OverallQual'])
            grlivarea = float(request.form['GrLivArea'])
            garagecars = float(request.form['GarageCars'])
            firstflrsf = float(request.form['1stFlrSF'])
            totrms = float(request.form['TotRmsAbvGrd'])
            
            # Validate inputs
            if not (1 <= overallqual <= 10):
                raise ValueError("Overall Quality must be between 1 and 10")
            if grlivarea < 400 or grlivarea > 6000:
                raise ValueError("Living Area must be between 400 and 6000 sq ft")
            if garagecars < 0 or garagecars > 5:
                raise ValueError("Garage Cars must be between 0 and 5")
            if firstflrsf < 0 or firstflrsf > 5000:
                raise ValueError("1st Floor SF must be between 0 and 5000")
            if totrms < 2 or totrms > 15:
                raise ValueError("Total Rooms must be between 2 and 15")
            
            # Create feature array
            features = np.array([[overallqual, grlivarea, garagecars, firstflrsf, totrms]])
            
            # Make prediction
            prediction = model.predict(features)
            predicted_price = round(float(prediction[0]), 2)
            
            # Format prediction message
            prediction_message = f"Estimated House Price: ${predicted_price:,.2f}"
            
            logger.info(f"Prediction: Input={features[0]} -> Output=${predicted_price}")
            
            return render_template('index.html', 
                                   prediction_text=prediction_message,
                                   show_result=True)
        
        except ValueError as ve:
            logger.warning(f"Input validation error: {str(ve)}")
            return render_template('index.html', 
                                   error=f"Validation Error: {str(ve)}",
                                   prediction_text="")
        
        except KeyError as ke:
            logger.warning(f"Missing required field: {str(ke)}")
            return render_template('index.html', 
                                   error="Missing required input fields",
                                   prediction_text="")
    
    except Exception as e:
        logger.error(f"Unexpected error in prediction: {str(e)}")
        return render_template('index.html', 
                               error=f"Error: {str(e)}",
                               prediction_text="")


@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    }), 200


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    logger.warning(f"404 error: {request.path}")
    return render_template('index.html', error="Page not found"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    logger.error(f"500 error: {str(e)}")
    return render_template('index.html', error="Internal server error"), 500


if __name__ == '__main__':
    # Development mode
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', True)
    
    logger.info(f"Starting Flask app on port {port} (debug={debug_mode})")
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
