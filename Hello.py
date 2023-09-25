import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd


url = 'ayushbmi.csv'
df = pd.read_csv(url)

# Calculate BMI for all entries
df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)

# Title
st.title('BMI Calculator')

st.subheader('BMI Index Categories:')
st.write('0 - Extremely Weak')
st.write('1 - Weak')
st.write('2 - Normal')
st.write('3 - Overweight')
st.write('4 - Obesity')
st.write('5 - Extreme Obesity')

#data represent
st.subheader('BMI sample Data')
st.write(df) 

# Create a heatmap using Plotly Express
heatmap_fig = px.scatter(
    df,
    x='Weight',
    y='Height',
    color='BMI',
    labels=dict(x="Weight (kg)", y="Height (cm)", color="BMI"),
    color_continuous_scale="YlGnBu",
    title="BMI Chart"
)

# Display the heatmap
st.subheader("BMI Chart:")
st.plotly_chart(heatmap_fig)

# Display summary statistics
st.subheader("Summary Statistics:")
st.write(df.describe())



# Sidebar for BMI calculation
st.sidebar.header('BMI Calculator')

# Sidebar input for weight and height
weight = st.sidebar.number_input('Enter your weight (kg):', min_value=0.0, step=0.1)
height_cm = st.sidebar.number_input('Enter your height (cm):', min_value=0.0, step=0.1)

# Calculate BMI
if st.sidebar.button('Calculate BMI'):
    # Convert height from cm to meters
    height_m = height_cm / 100

    # Calculate BMI
    bmi = weight / (height_m ** 2)

    # Display BMI
    st.sidebar.subheader('Your BMI is:')
    st.sidebar.write(f'{bmi:.2f}')

    # Interpret BMI
    if bmi < 18.5:
        st.sidebar.write('You are underweight.')
    elif 18.5 <= bmi < 24.9:
        st.sidebar.write('You have a normal weight.')
    elif 25 <= bmi < 29.9:
        st.sidebar.write('You are overweight.')
    else:
        st.sidebar.write('You are obese')


