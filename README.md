# Diabetes Prediction System

## Description
This project implements a Diabetes Prediction System using a machine learning model (XGBoost) deployed with a Flask web application. Users can input various health parameters, and the system will predict whether they are diabetic or not.

## Features
- Web-based interface for inputting patient data.
- Real-time prediction using a pre-trained XGBoost model.
- Clear display of prediction results (Diabetic/Not Diabetic) with visual cues.
- Scaler for feature scaling to ensure accurate predictions.

## Technologies Used
- **Flask**: Web framework for building the application.
- **Scikit-learn**: For data preprocessing (StandardScaler).
- **XGBoost**: Machine learning model for classification.
- **Pandas**: For data manipulation.
- **Numpy**: For numerical operations.
- **HTML/CSS**: For the frontend user interface.

## Setup and Installation
To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/technical-beast-7/Diabetes-Prediction-System.git
    cd Diabetes-Prediction-System
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Generate `scaler.pkl` and `xgb_model.pkl`:**
    Open the `Diabetes_Prediction_final (2).ipynb` Jupyter notebook. Ensure that the `pickle.dump` paths are set to save the files in the current directory (e.g., `scaler.pkl` and `xgb_model.pkl`). Run all cells in the notebook to generate these model files.

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```

6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage
1.  Navigate to the application in your web browser.
2.  Enter the required health parameters in the form.
3.  Click the "Predict" button to get the diabetes prediction.
4.  The result will be displayed, indicating whether the person is "Diabetic" (in red) or "Not Diabetic" (in green).

## Model Training (Optional)
The `Diabetes_Prediction_final (2).ipynb` Jupyter notebook contains the code used to train the XGBoost model and generate the `scaler.pkl` and `xgb_model.pkl` files. You can review and re-run this notebook to understand the model training process or retrain the model with new data.