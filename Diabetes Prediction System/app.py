from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('xgb_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract features from form
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bloodpressure = int(request.form['blood_pressure'])
        skinthickness = int(request.form['skin_thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetespedigreefunction = float(request.form['diabetes_pedigree_function'])
        age = int(request.form['age'])

        # Create a numpy array from the input features
        features = np.array([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])

        # Scale the features
        scaled_features = scaler.transform(features)

        # Make prediction
        prediction = model.predict(scaled_features)[0]

        if prediction == 1:
            result = 'Diabetic'
            prediction_class = 'negative'
        else:
            result = 'Not Diabetic'
            prediction_class = 'positive'

        return render_template('result.html', prediction_text=result, prediction_class=prediction_class)

if __name__ == '__main__':
    app.run(debug=True)