# House Price Predictor - Quick Start Guide

## 🚀 Get Started in 5 Minutes!

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/s14hika/house_price_predictor.git
cd house_price_predictor
```

### Step 2: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:
```bash
pip install flask numpy joblib scikit-learn
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

```
http://localhost:5000
```

That's it! You should see the House Price Prediction application with:
- Beautiful purple gradient UI
- Form to enter property details
- Real-time validation
- Instant price predictions

---

## 📋 Required Files

Make sure these files are in your project directory:

```
house_price_predictor/
├── app.py                      # Flask application (enhanced backend)
├── xgb_house_model.pkl        # Pre-trained XGBoost model
├── train_model.py             # Training script
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html            # Modern UI with Bootstrap
├── train (1).csv             # Training dataset
└── readme.md                 # Project documentation
```

---

## 🎯 Using the Application

### Option 1: Web Form Interface

1. **Open http://localhost:5000** in your browser
2. **Fill in the property details:**
   - **Overall Quality**: 1-10 rating
   - **Living Area**: Square footage
   - **Garage Capacity**: Number of cars
   - **1st Floor Area**: Square footage
   - **Total Rooms**: Above ground
3. **Click "Predict Price"** button
4. **View the estimated price** in the result box

### Option 2: API Endpoint

**Using curl:**
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "OverallQual": 8,
    "GrLivArea": 2500,
    "GarageCars": 2,
    "1stFlrSF": 1200,
    "TotRmsAbvGrd": 9
  }'
```

**Using Python:**
```python
import requests

url = 'http://localhost:5000/api/predict'
data = {
    'OverallQual': 8,
    'GrLivArea': 2500,
    'GarageCars': 2,
    '1stFlrSF': 1200,
    'TotRmsAbvGrd': 9
}

response = requests.post(url, json=data)
print(response.json())
```

**Using JavaScript (fetch):**
```javascript
const data = {
  OverallQual: 8,
  GrLivArea: 2500,
  GarageCars: 2,
  '1stFlrSF': 1200,
  TotRmsAbvGrd: 9
};

fetch('http://localhost:5000/api/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data)
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## 📡 API Endpoints

### Home Page
```
GET http://localhost:5000/
```
Returns the web interface

### Model Information
```
GET http://localhost:5000/api/model-info
```

Response:
```json
{
  "model_type": "XGBoost Regressor",
  "r2_score": 0.91,
  "features": ["OverallQual", "GrLivArea", "GarageCars", "1stFlrSF", "TotRmsAbvGrd"],
  "accuracy_info": "R² = 0.91 on test dataset, RMSE ≈ $25,000"
}
```

### Make Prediction (JSON API)
```
POST http://localhost:5000/api/predict
Content-Type: application/json
```

Response:
```json
{
  "success": true,
  "predicted_price": 285000.50,
  "currency": "USD",
  "model_r2_score": 0.91,
  "confidence": "High",
  "timestamp": "2024-12-28T15:30:45.123456"
}
```

### Health Check
```
GET http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-12-28T15:30:45.123456"
}
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask numpy joblib
```

### Issue: "FileNotFoundError: xgb_house_model.pkl"
**Solution:**
- Ensure `xgb_house_model.pkl` is in the project root directory
- Run `python train_model.py` to train the model if missing

### Issue: "Port 5000 is already in use"
**Solution:**
```bash
# Use a different port
PORT=8000 python app.py
# Then access http://localhost:8000
```

### Issue: Virtual environment not activating
**Windows:** Make sure you're in the project directory and run:
```bash
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

## 🧪 Testing the Application

### Test with Sample Data

```bash
# Open terminal and run these curl commands:

# High-end property
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"OverallQual": 9, "GrLivArea": 4000, "GarageCars": 3, "1stFlrSF": 2000, "TotRmsAbvGrd": 12}'

# Average property
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"OverallQual": 6, "GrLivArea": 1800, "GarageCars": 2, "1stFlrSF": 900, "TotRmsAbvGrd": 8}'

# Budget property
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"OverallQual": 3, "GrLivArea": 800, "GarageCars": 1, "1stFlrSF": 400, "TotRmsAbvGrd": 4}'
```

---

## 📚 Features Overview

✅ **Frontend Features:**
- Modern Bootstrap 5.3 UI
- Responsive design (desktop, tablet, mobile)
- Real-time input validation
- Beautiful gradient background
- Animated transitions
- Professional result display

✅ **Backend Features:**
- Flask REST API
- Input validation with decorators
- Comprehensive logging
- Error handling
- Health check endpoint
- Model information API
- JSON response formatting

---

## 🚀 Next Steps

1. **Explore the Code:**
   - `app.py` - Backend application logic
   - `templates/index.html` - Frontend UI
   - `IMPROVEMENTS.md` - Detailed enhancement documentation

2. **Run Tests:**
   - Test the web interface
   - Test API endpoints with curl
   - Check logs in terminal

3. **Deploy (Optional):**
   - Deploy to Heroku: `heroku create && git push heroku main`
   - Deploy to AWS: Use Elastic Beanstalk
   - Deploy to Google Cloud: Use Cloud Run

---

## 💡 Tips & Tricks

- **Debug Mode:** Set `FLASK_DEBUG=1` to enable auto-reload on code changes
- **Custom Port:** Use `PORT=8080 python app.py`
- **Check Logs:** Terminal will show all requests and predictions
- **API Testing:** Use Postman, Insomnia, or curl for API endpoints

---

## 📞 Support

If you encounter issues:
1. Check the terminal for error messages
2. Verify all files are in the correct location
3. Ensure Python 3.8+ is installed
4. Check requirements in IMPROVEMENTS.md

---

**Happy Predicting!** 🏠💰

*Last Updated: December 28, 2024*
