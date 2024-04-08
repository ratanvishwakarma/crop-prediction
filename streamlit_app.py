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
    pred = model.predict(np.array([N,P,K,temperature,humidity,ph]).reshape(1,-1))
    print(pred)
    print(np.array(pred))
    pred = np.array([*pred])
    print(pred)
    st.subheader(*pred)

# Table section
st.subheader("Crop Details:")
# Define your crop details here as a dictionary
crop_details = {
    'Crop': ['Apple', 'Banana', 'Blackgram'],  # Example crop names
    'Nitrogen': ['0 - 40', '80 - 120', '20 - 60'],  # Example details
    'Phosphorus': ['120 - 145', '70 - 95', '55 - 80'],  # Example details
    'Potassium': ['195 - 205', '45 - 55', '15 - 25'],
    'Temperature': ['21 - 24', '25 - 30', '25 - 35'],
    'Humidity': ['90 - 95', '75 - 85', '60 - 70'],
    'Ph': ['5 - 6.5', '5 - 6.5', '6 - 8'],
}
crop_details_df = pd.DataFrame(crop_details)
# Display the crop details in a table
st.table(crop_details_df)
