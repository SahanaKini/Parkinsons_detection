from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load your trained model
model = joblib.load('parkinsons_model.pkl')

# Function to preprocess image
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100))
    img = img.flatten().reshape(1, -1)
    return img

# Route to show the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    # Save the file to a temporary location
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Preprocess and predict
    img = preprocess_image(file_path)
    prediction = model.predict(img)[0]

    # Clean up the uploaded file
    os.remove(file_path)

    # Return result
    result = "Parkinson's Detected" if prediction == 1 else "Healthy"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
