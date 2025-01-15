import pickle
import streamlit as st
import numpy as np

# Load the model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the application
st.title('Heart Disease Prediction Model')

# Input fields for the features
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", options=[0, 1])
cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=60, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)", options=[0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results (0-2)", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", options=[0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", options=[0, 1, 2])
ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, value=0)
thal = st.selectbox("Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)", options=[0, 1, 2])

# Predict button
if st.button('Predict Heart Disease'):
    # Prepare the input array
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Output the result
    if prediction[0] == 1:
        st.error('Heart Disease Present.')
    else:
        st.success('Heart Disease Not Present.')
