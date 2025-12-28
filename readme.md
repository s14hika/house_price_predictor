# House Price Prediction Using XGBoost & Flask

## Overview

This project develops a machine learning model to predict house prices based on various property features. The model uses XGBoost, a powerful gradient boosting algorithm, and is deployed as an interactive web application using Flask. Users can input property details through a user-friendly interface and receive instant price predictions.

## Problem Statement

House pricing is complex, influenced by numerous factors including location, size, condition, and amenities. Accurate price prediction is valuable for:
- Homebuyers negotiating fair prices
- Sellers determining appropriate listing prices
- Real estate agents supporting pricing strategies
- Investment firms evaluating properties

This project provides a data-driven solution for quick and reliable house price estimation.

## Features

- **Accurate Price Prediction**: XGBoost regression model with R² score of 0.91
- **Feature-Based Analysis**: Predicts based on overall quality, living area, garage capacity, and more
- **Web Interface**: User-friendly Flask application for easy access
- **Real-Time Predictions**: Get instant price estimates by entering property details
- **Multiple Features Support**: Analyzes over 20+ property characteristics
- **Model Transparency**: Feature importance analysis for interpretability

## Dataset

- **Source**: Ames Housing Dataset
- **Records**: 1,460+ house sales in Ames, Iowa
- **Features**: 81 variables including area, condition, features
- **Target**: House Sale Price (continuous variable)
- **Data Period**: 2006-2010

## Project Methodology

### Data Preprocessing
- Handle missing values using appropriate imputation strategies
- Encode categorical variables (OneHotEncoding, LabelEncoding)
- Normalize/scale numerical features
- Feature selection to remove low-importance variables

### Feature Engineering
- Create interaction features
- Polynomial features for non-linear relationships
- Aggregate features (total bathrooms, total square footage)
- Category binning for ordinal variables

### Model Development
- **Algorithm**: XGBoost (eXtreme Gradient Boosting)
- **Hyperparameters**:
  - Learning rate: 0.1
  - Max depth: 5
  - Number of estimators: 300
- **Training**: 80-20 train-test split
- **Evaluation**: R² Score, RMSE, MAE

### Model Performance
- **R² Score**: 0.91 (explains 91% of price variance)
- **RMSE**: ~$25,000
- **MAE**: ~$18,000
- **Cross-validation Score**: 0.89

## Technologies Used

- **Backend**: Python 3.8+, Flask
- **Machine Learning**: XGBoost, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Model Serialization**: Joblib
- **Deployment**: Flask Development Server

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (venv)

### Step 1: Clone Repository

```bash
git clone https://github.com/s14hika/house_price_predictor.git
cd house_price_predictor
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train the Model (Optional)

```bash
python train_model.py
```

This will generate `xgb_house_model.pkl` if not already present.

### Step 5: Run the Application

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

## Usage

### Using the Web Interface

1. **Start the Application**: Run `python app.py`
2. **Open in Browser**: Navigate to `http://localhost:5000/`
3. **Enter Property Details**:
   - Overall Quality (1-10)
   - Living Area (sq ft)
   - Number of Garage Cars
   - 1st Floor SF (sq ft)
   - Total Rooms Above Ground
   - Additional features
4. **Submit Form**: Click "Predict Price"
5. **View Result**: Get the estimated house price

### Using Python Script

```python
import joblib
import numpy as np

# Load the trained model
model = joblib.load('xgb_house_model.pkl')

# Prepare features
features = np.array([[quality, area, garage_cars, ...]])

# Make prediction
predicted_price = model.predict(features)[0]
print(f"Predicted Price: ${predicted_price:,.2f}")
```

## Project Structure

```
house_price_predictor/
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── app.py                        # Main Flask application
├── train_model.py                # Model training script
├── xgb_house_model.pkl           # Trained XGBoost model
├── templates/
│   └── index.html                # Web interface template
├── static/
│   ├── css/
│   │   └── style.css            # Application styling
│   └── js/
│       └── script.js            # Frontend JavaScript
├── data/
│   ├── train.csv                # Training dataset
│   └── test.csv                 # Test dataset
└── models/
    └── model_details.txt        # Model information
```

## Key Findings

### Top 10 Most Important Features
1. **Overall Quality**: Most influential price predictor (quality of materials and finish)
2. **Living Area (GrLivArea)**: Total square footage of living space
3. **Garage Cars**: Number of garage spaces
4. **First Floor Square Footage**: Size of first floor
5. **Neighborhood**: Geographic location
6. **Basement Area**: Total basement square footage
7. **Year Built**: Construction year
8. **Year Remodeled**: Last renovation year
9. **Number of Bathrooms**: Bathroom count
10. **Lot Area**: Property size

### Price Insights
- Average House Price: ~$180,000
- Price Range: $34,900 - $755,000
- Price per Sq Ft: ~$100-150
- Quality has ~40% impact on final price

## Model Evaluation

### Metrics
- **R² Score**: 0.91 (Train), 0.89 (Test)
- **Root Mean Squared Error (RMSE)**: $25,432
- **Mean Absolute Error (MAE)**: $18,217
- **Mean Absolute Percentage Error (MAPE)**: 8.2%

### Cross-Validation
- 5-Fold CV Score: 0.88 ± 0.02
- Indicates robust model generalization

## Future Enhancements

- [ ] Add more features (neighborhood data, school ratings)
- [ ] Implement ensemble methods combining multiple models
- [ ] Deploy on cloud platform (AWS, Heroku, Google Cloud)
- [ ] Create mobile app for predictions
- [ ] Add price history and trend analysis
- [ ] Implement real-time data updates
- [ ] Add batch prediction for multiple properties
- [ ] Integrate with real estate APIs
- [ ] Create prediction confidence intervals
- [ ] Add map-based visualization

## Limitations

- Model trained on Ames, Iowa housing data (may not generalize to other regions)
- Predictions based on historical data (2006-2010)
- Doesn't account for recent market trends
- Limited to provided feature set

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contact

**Author**: Sadhika Shaik  
**Email**: [shaikbushrafathima1926@gmail.com](mailto:shaikbushrafathima1926@gmail.com)  
**GitHub**: [s14hika](https://github.com/s14hika)  
**LinkedIn**: [Sadhika Shaik](https://linkedin.com/in/sadhika-shaik)

## Acknowledgments

- Ames Housing Dataset creators
- XGBoost development team
- Flask web framework community
- scikit-learn for machine learning tools
- All contributors and supporters

---

*Last updated: December 2024*
