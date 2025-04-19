# PCOS Prediction (Machine Learning/AI - ML)

## Overview
This project focuses on predicting Polycystic Ovary Syndrome (PCOS) using machine learning techniques. The notebook `PCOS_19.ipynb` contains the implementation of preprocessing, feature engineering, model training, evaluation, and saving the best model. A web application is also created using Flask to interact with the trained model via a simple HTML interface.

## Features
- PCOS prediction based on medical data
- Data visualization and preprocessing
- Multiple machine learning models tested
- Evaluation with accuracy, precision, recall
- Flask-based web application for user input
- HTML frontend to display predictions

## Requirements
Install the required dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask


Dataset
The model uses a dataset containing various health-related features to predict the presence of PCOS. The dataset includes features such as age, weight, BMI, hormonal levels, and symptoms like irregular periods, skin darkening, etc.

Ensure the dataset is properly preprocessed before training:

Handle missing values

Encode categorical variables

Normalize or standardize numerical features

How to Use
Open PCOS_19.ipynb to explore and preprocess the data.

Train machine learning models (e.g., Random Forest, SVM, Logistic Regression).

Save the best-performing model (e.g., model.pkl).

Use app.py to launch the Flask server.

Open index.html from the templates folder in the browser to enter data.

Get prediction results on a new page (result.html).

Model Architecture
The models used include traditional ML algorithms:

Logistic Regression

Support Vector Machine

K-Nearest Neighbors

Random Forest

The models are evaluated using:

Accuracy

Confusion Matrix

Classification Report

Web Application
Backend: Flask app (app.py) loads the model and handles prediction logic

Frontend: HTML templates for user-friendly input and result display

Supports form submission and result rendering

Results
The best model achieved high accuracy on the test set. Results are displayed clearly in the notebook with metrics and plots showing training/validation performance.

Future Improvements
Deploy the app online using Heroku or Render

Add error handling and input validation

Use advanced models or deep learning techniques

Collect more diverse and real-time data for better generalization

License
This project is open-source and free to use. Please give credit if used in research or production.

Author
Developed by Arnab Chakrabort
