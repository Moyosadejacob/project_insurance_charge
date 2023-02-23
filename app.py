## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
import numpy as np

st.title('Insurance Premium Charge Prediction')

age = st.slider('How old are you?', 0, 100, 25)
sex = st.selectbox("Sex", options=["Male", "Female"])
bmi = st.slider('BMI', 0, 100, 25)
children = st.number_input('Insert a number')
smoker = st.selectbox('Smoker', options=['Yes', 'No'])
region = st.selectbox('Region', options=['northeast', 'northwest', 'southwest','southeast'])