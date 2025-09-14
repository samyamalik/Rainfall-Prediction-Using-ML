from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open('rainfall_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ""
    if request.method == 'POST':
        # Get form data
        pressure = float(request.form['pressure'])
        dewpoint = float(request.form['dewpoint'])
        humidity = int(request.form['humidity'])
        cloud = int(request.form['cloud'])
        sunshine = float(request.form['sunshine'])
        winddirection = float(request.form['winddirection'])
        windspeed = float(request.form['windspeed'])

        # Prepare the input
        input_features = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])
        
        # Make prediction
        prediction = model.predict(input_features)[0]
        
        if prediction == 1:
            prediction_text = "🌧️ It will rain!"
        else:
            prediction_text = "☀️ It will not rain!"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
