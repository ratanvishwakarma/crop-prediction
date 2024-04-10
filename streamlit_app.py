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

# Define language options
language_options = ["English", "Hindi"]

# Display language options side by side
col1, col2 = st.sidebar.columns(2)
selected_language = col1.radio("Select Language", language_options)

# Define page options
page_options = ["Crop Prediction", "Crop Details"]
selected_page = st.sidebar.radio("Select Page", page_options)

# Define function to convert English crop names to Hindi
def english_to_hindi(english_crop):
    crop_mapping = {
        "Apple": "सेब",
        "Banana": "केला",
        "Blackgram": "काली उरद",
        "Chickpea": "चना",
        "Coconut": "नारियल",
        "Coffee": "कॉफ़ी",
        "Cotton": "कपास",
        "Grapes": "अंगूर",
        "Jute": "जूट",
        "Kidneybeans": "राजमा",
        "lentil": "मसूर",
        "Maize": "मक्का",
        "Mango": "आम",
        "Mothbeans": "मोथ",
        "Mungbeans": "मूंग",
        "Muskmelon": "खरबूजा",
        "Orange": "संतरा",
        "Papaya": "पपीता",
        "Pigeonpeas": "अरहर",
        "Pomegranate": "अनार",
        "Rice": "चावल",
        "Watermelon": "तरबूज"
    }
    return crop_mapping.get(english_crop, "Unknown")

# Define functions for each page
def crop_prediction():
    # Input fields for user to provide data
    N = float(st.number_input('Nitrogen', 0))
    P = float(st.number_input('Phosphorus', 0))
    K = float(st.number_input('Potassium', 0))
    temperature = float(st.number_input('Temperature', 0, 100))
    humidity = float(st.number_input('Humidity', 0, 100))
    ph = float(st.number_input('Ph', 0, 14))

    # Button to trigger crop prediction
    btn = st.button("Predict Crop")
    
  # Perform prediction when the button is clicked
    if btn:
        if N == 0 and P == 0 and K == 0 and temperature == 0 and humidity == 0 and ph == 0:
            st.error("Cannot grow crops with all input values set to zero.")
        else:
            pred = model.predict(np.array([N,P,K,temperature,humidity,ph]).reshape(1,-1))
            print(pred)
            print(np.array(pred))
            pred = np.array([*pred])
            print(pred)
            st.subheader(*pred)
            if selected_language == "Hindi":
                pred = english_to_hindi(*pred)
            st.subheader(pred)


def crop_details():
    # Table section
    st.subheader("Crop Details:")
    # Define your crop details here as a dictionary
    crop_details = {
        'Crop': ['Apple', 'Banana', 'Blackgram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton', 'Grapes', 'Jute', 'Kidneybeans', 'lentil', 'Maize', 'Mango', 'Mothbeans', 'Mungbeans', 'Muskmelon', 'Orange', 'Papaya', 'Pigeonpeas', 'Pomegranate', 'Rice', 'Watermelon'],
        'Nitrogen': ['0 - 40', '80 - 120', '20 - 60', '20 - 60', '0 - 40', '80 - 120', '100 - 140', '0 - 40', '60 - 100', '0 - 40', '0 - 40', '60 - 100', '0 - 40', '0 - 40', '0 - 40', '80 - 120', '0 - 40', '31 - 70', '0 - 40', '0 - 40', '0 - 40', '80 - 120'],  
        'Phosphorus': ['120 - 145', '70 - 95', '55 - 80', '55 - 80', '5 - 30', '15 - 40', '35 - 60', '120 - 145', '35 - 60', '55 - 80', '38 - 80', '35 - 60', '15 - 40', '35 - 60', '35 - 60', '5 - 30', '5 - 30', '46 - 70', '55 - 80', '5 - 30', '35 - 60', '5 - 30'],  
        'Potassium': ['195 - 205', '45 - 55', '15 - 25', '75 - 85', '25 - 35', '25 - 35', '15 - 25', '195 - 205', '35 - 45', '15 - 25', '15 - 34', '15 - 25', '25 - 35', '15 - 25', '15 - 25', '45 - 55', '5 - 15', '45 - 55', '15 - 25', '35 - 45', '15 - 25', '45 - 55'],
        'Temperature': ['21 - 24', '25 - 30', '25 - 35', '17 - 21', '25 - 30', '23 - 28', '22 - 26', '8.8 - 42', '23 - 27', '15 - 25', '18 - 30', '18 - 26.5', '27 - 36', '24 - 32', '27 - 30', '27 - 30', '10 - 38', '23 - 44', '18 - 37', '18 - 25', '24 - 32', '24 - 27'],
        'Humidity': ['90 - 95', '75 - 85', '60 - 70', '14 - 20', '90 - 100', '50 - 70', '75 - 85', '80 - 84', '70 - 90', '18 - 25', '40 - 80', '55 - 75', '45 - 55', '40 - 65', '80 - 90', '90 - 95', '90 - 95', '90 - 95', '30 - 70', '80 - 95', '40 - 65', '80 - 90'],
        'Ph': ['5 - 6.5', '5 - 6.5', '6 - 8', '5 - 9', '5 - 6.5', '6 - 7.5', '5.8 - 8', '5.5 - 6.5', '6 - 7.5', '5.5 - 6', '5 - 6', '5.5 - 7', '4.5 - 7', '3 - 10', '6 - 7', '6 - 7', '6 - 8', '6.5 - 7', '4.5 - 7.5', '5.5 - 7.2', '3 - 10', '6 - 7'],
    }
    crop_details_df = pd.DataFrame(crop_details)
    # Display the crop details in a table
    st.table(crop_details_df)

# Page navigation
if selected_page == "Crop Prediction":
    crop_prediction()
elif selected_page == "Crop Details":
    crop_details()
