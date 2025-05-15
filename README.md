Parkinson's disease is a chronic and progressive neurological disorder that affects the central nervous system. It primarily impairs motor functions due to the loss of dopamine-producing brain cells. Common symptoms include tremors, rigidity, slowness of movement (bradykinesia), postural instability, and speech difficulties. Early and accurate detection of Parkinson's disease is crucial for timely treatment and management of symptoms.

Project Description:
This project aims to develop a Machine Learning-based system to detect Parkinson's Disease using handwriting and voice data. The system leverages both static images of handwriting patterns (spiral and wave drawings) and voice recordings to analyze motor and speech impairments associated with Parkinson's disease.

Features:
Handwriting Data Analysis:
Users upload spiral and wave drawing images.
The system uses image processing techniques and trained ML models to detect abnormalities in the drawing patterns, such as tremors, irregularities, or distortions.
Based on the analysis, it predicts whether the handwriting pattern indicates Parkinson's or healthy control.

Voice Data Analysis:
Gives the voice accuracy
The system extracts voice features such as jitter, shimmer, and harmonic-to-noise ratio.
The voice features are analyzed using trained ML models to detect speech impairments typical of Parkinson's disease.

Output:
The system combines the results from handwriting and voice analysis.
Provides a simple diagnostic result:
"Healthy"

"Parkinson's Disease"

Technologies Used:
Machine Learning (classification models)
Image Processing (for handwriting image features)
Python , Streamlit , TensorFlow / Keras , Scikit-learn , OpenCV , Librosa , Pickle , NumPy 


Algorithms used:
Convolutional Neural Network (CNN) --	Used for classifying spiral handwriting images (handwriting model).
Support Vector Machine (SVM)	--Used for classifying voice data based on extracted features (voice model).
Feature Extraction (MFCC, etc.)	--Used to extract important features from voice data for classification.
Feature Scaling (StandardScaler)	--Used to normalize the voice feature data before classification.
Fusion Model (Rule-based fusion)	--Combines predictions from handwriting and voice models for final decision.

