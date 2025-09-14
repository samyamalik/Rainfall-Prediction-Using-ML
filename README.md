# Rainfall-Prediction-Using-ML

# Project Overview

This project predicts rainfall based on key weather parameters such as pressure, humidity, dew point, and cloud cover using machine learning. It integrates a Flask backend with a simple web interface to provide real-time rainfall predictions based on user input. The system can assist farmers, planners, and authorities in decision-making and resource management.
# Features

Predict rainfall using historical weather data.
User-friendly web interface for inputting weather parameters.
Real-time predictions via Flask backend.
Model saved using Pickle for easy deployment.


# Tools & Technologies
Programming Language: Python
Libraries: Pandas, NumPy, scikit-learn, Flask, Matplotlib/Seaborn
Frontend: HTML, CSS, JavaScript
Model Serialization: Pickle
Development Environment: Jupyter Notebook / VS Code


# Methodology
Collect historical weather data (pressure, humidity, dew point, cloud cover, rainfall).
Preprocess the data (handle missing values, normalize, feature selection).
Split data into training and testing sets.
Train machine learning models (Linear Regression, Random Forest, etc.).
Evaluate models using RMSE, MAE, and R² metrics.
Deploy the trained model with Flask backend.
Build a frontend interface to input weather parameters and display predictions.
