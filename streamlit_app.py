import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import sklearn

# Load your machine learning model
model = pickle.load(open('model.pkl','rb'))

# Define the title and description of your app
st.markdown("<h1 style='text-align: center;'>AMAA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>CROP PREDICTION SYSTEM🌱</h3>", unsafe_allow_html=True)

# Input fields for user to provide data
N = float(st.number_input('Nitrogen', 0, 1000))
P = float(st.number_input('Phosphorus', 0, 1000))
K = float(st.number_input('Potassium', 0, 1000))
temperature = float(st.number_input('Temperature', 0, 100))
humidity = float(st.number_input('Humidity', 0, 100))
ph = float(st.number_input('Ph', 0, 14))

# Button to trigger crop prediction
btn = st.button("Crop Prediction")

# Perform prediction when the button is clicked
if btn:
    # Make prediction using the loaded model
    pred = model.predict(np.array([N, P, K, temperature, humidity, ph]).reshape(1,-1))
    
    # Assuming pred is an array with probabilities for each crop, and crop_names contains the names of the crops
    crop_names = ['Crop A', 'Crop B', 'Crop C']  # Example crop names
    pred = pred[0]  # Assuming pred is an array with probabilities for each crop
    pred_dict = {'Crop': crop_names, 'Probability': pred}
    pred_df = pd.DataFrame(pred_dict)
    
    # Display the predicted crop probabilities in a table
    st.subheader("Predicted Crop Probabilities:")
    st.table(pred_df)

# Table section
st.subheader("Crop Details:")
# Define your crop details here as a dictionary
crop_details = {
    'Crop': ['Crop A', 'Crop B', 'Crop C'],  # Example crop names
    'Detail 1': ['Detail A1', 'Detail B1', 'Detail C1'],  # Example details
    'Detail 2': ['Detail A2', 'Detail B2', 'Detail C2'],  # Example details
    # Add more details columns as needed
}
crop_details_df = pd.DataFrame(crop_details)
# Display the crop details in a table
st.table(crop_details_df)
