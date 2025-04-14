# app.py

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load('xgb_house_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        overallqual = float(request.form['OverallQual'])
        grlivarea = float(request.form['GrLivArea'])
        garagecars = float(request.form['GarageCars'])
        firstflrsf = float(request.form['1stFlrSF'])
        totrms = float(request.form['TotRmsAbvGrd'])

        features = np.array([[overallqual, grlivarea, garagecars, firstflrsf, totrms]])
        prediction = model.predict(features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f"Estimated House Price: ${output}")
    except Exception as e:
        print("Error:", e)
        return render_template('index.html', prediction_text="Error: Please check your input!")

if __name__ == '__main__':
    app.run(debug=True)
