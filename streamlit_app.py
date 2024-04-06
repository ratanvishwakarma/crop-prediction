import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import sklearn

model = pickle.load(open('model.pkl','rb'))

st.markdown("<h1 style='text-align: center;'>AMAA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>CROP PREDICTION SYSTEM🌱</h3>", unsafe_allow_html=True)

N = float(st.number_input('Nitrogen', 0,1000))
P = float(st.number_input('Phosphorus', 0,1000))
K = float(st.number_input('Potassium', 0,1000))
temperature = float(st.number_input('Temperature', 0,100))
humidity = float(st.number_input('Humidity', 0,100))
ph = float(st.number_input('Ph', 0,14))

btn = st.button("Crop Prediction")

if btn:
    pred = model.predict(np.array([N,P,K,temperature,humidity,ph]).reshape(1,-1))
    print(pred)
    print(np.array(pred))
    pred = np.array([*pred])
    print(pred)
    st.subheader(*pred)

 <table>
        <tr>
          <th>Label</th>
          <th>N</th>
          <th>P</th>
          <th>K</th>
          <th>Temperature</th>
          <th>Humidity</th>
          <th>pH</th>
        </tr>
        <tr>
          <td>Apple</td>
          <td>0 - 40</td>
          <td>120 - 145</td>
          <td>195 - 205</td>
          <td>21 - 24</td>
          <td>90 - 95</td>
          <td>5 - 6.5</td>
        </tr>
         <tr>
          <td>Banana</td>
          <td>80 - 120</td>
          <td>70 - 95</td>
          <td>45 - 55</td>
          <td>25 - 30</td>
          <td>75 - 85</td>
          <td>5 - 6.5</td>
        </tr>
      </table>
