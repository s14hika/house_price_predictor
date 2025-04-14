House Price Prediction Using XGBoost & Flask
This project leverages XGBoost to predict house prices based on various features such as overall quality, living area, garage capacity, and more. The trained model is deployed as a web application using Flask to allow users to enter property details and receive an estimated house price.

🚀 Features
Machine Learning: Predict house prices using features such as overall quality, garage size, living area, etc.

Flask Web App: Users can input property features through a form to get a price prediction.

XGBoost: An advanced regression model used for prediction with high accuracy (R² Score of 0.91).

🛠️ Tools & Technologies Used
Python

Flask (for web app deployment)

XGBoost (for training the machine learning model)

Pandas (for data preprocessing)

Scikit-learn (for model evaluation and splitting the dataset)

HTML/CSS (for user interface)

Joblib (to save the trained model)

🔄 Workflow
Data Collection: The data is sourced from the Ames Housing dataset, which includes various features like house quality, area, and number of rooms.

Model Training: The features are processed and used to train an XGBoost regression model.

Web App Deployment: The model is saved and deployed using Flask to create a user-friendly interface where users can input data and receive house price predictions.

📂 Project Structure
bash
Copy
Edit
├── app.py                # Main Flask application file
├── train_model.py        # Script to train the model
├── xgb_house_model.pkl   # Saved model (XGBoost)
├── templates
│   └── index.html        # HTML template for the Flask app
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation (this file)
💻 Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/s14hika/house_price_predictor.git
cd house_price_predictor
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Train the Model
Run the train_model.py script to train the XGBoost model and save it as xgb_house_model.pkl:

bash
Copy
Edit
python train_model.py
5. Start the Flask Application
Run the Flask app:

bash
Copy
Edit
python app.py
The application will be available at http://127.0.0.1:5000 in your browser.

6. Make Predictions
Open the app in your browser.

Enter property details such as Overall Quality, Living Area, Garage Cars, 1st Floor SF, and Total Rooms Above Ground.

Submit the form to get an estimated house price.

📝 Model Evaluation
The trained model uses XGBoost regression, and its performance is evaluated using the R² score, which is 0.91 on the test set, indicating a high level of prediction accuracy.

📋 Future Enhancements
Additional Features: Include more features like location, neighborhood, and house age for more accurate predictions.

Deployment: Deploy the Flask app on cloud platforms like Heroku or PythonAnywhere for public access.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Let me know if you need any modifications or further clarifications!