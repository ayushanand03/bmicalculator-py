import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('BMI Calculator')


weight = st.number_input('Enter your weight (kg):')
height = st.number_input('Enter your height (cm):')

# Calculate BMI
if st.button('Calculate BMI'):
    # Convert height to meters
    height_meters = height / 100

    bmi = weight / (height_meters ** 2)

    # Display BMI
    st.write(f'Your BMI is {bmi:.2f}')

    # Interpret BMI
    if bmi < 18.5:
        st.write('You are underweight.')
    elif 18.5 <= bmi < 24.9:
        st.write('You have a normal weight.')
    elif 25 <= bmi < 29.9:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')
        

 

   
