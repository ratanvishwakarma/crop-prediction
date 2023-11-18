import streamlit as st
import pickle 
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import sklearn

model = pickle.load(open('model.pkl','rb'))

st.markdown("<h1 style='text-align: center;'>AMAA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>CROP PREDICTION SYSTEM🌱</h3>", unsafe_allow_html=True)

N = float(st.number_input('Nitrogen', 0,100))
P = float(st.number_input('Phosphorus', 0,100))
K = float(st.number_input('Potassium', 0,100))
temperature = float(st.number_input('Temperature', 0,100))
humidity = float(st.number_input('Humidity', 0,100))
ph = float(st.number_input('Ph', 0,100))

btn = st.button("Crop Prediction")

if btn:
    pred = model(np.array([N,P,K,temperature,humidity,ph]).reshape(1,-1))
    print(pred)
    print(np.array(pred))
    pred = np.array([*pred])
    print(pred)
    st.subheader(*pred)

