# Rainfall Prediction Using Machine Learning

## Project Overview
This project predicts rainfall based on key weather parameters such as pressure, humidity, dew point, and cloud cover using machine learning. It integrates a Flask backend with a simple web interface to provide real-time rainfall predictions based on user input. The system helps farmers, planners, and authorities make informed decisions.

---

## Features
- Predict rainfall using historical weather data.
- User-friendly web interface for inputting weather parameters.
- Real-time predictions via Flask backend.
- Model saved using Pickle for easy deployment.

---

## Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, scikit-learn, Flask, Matplotlib/Seaborn
- **Frontend:** HTML, CSS, JavaScript
- **Model Serialization:** Pickle
- **Development Environment:** Jupyter Notebook / VS Code

---

## Methodology
1. Collect historical weather data (pressure, humidity, dew point, cloud cover, rainfall).
2. Preprocess the data (handle missing values, normalize, feature selection).
3. Split data into training and testing sets.
4. Train machine learning models (Linear Regression, Random Forest, etc.).
5. Evaluate models using RMSE, MAE, and R² metrics.
6. Deploy the trained model with Flask backend.
7. Build a frontend interface to input weather parameters and display predictions.

---

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
