import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd


url = 'ayushbmi.csv'
df = pd.read_csv(url)

# Title
st.title('BMI Calculator')

df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)

# Title
st.title('BMI Calculator')

# Create a heatmap using Plotly Express
heatmap_fig = px.imshow(
    df.pivot_table(index='Height', columns='Weight', values='BMI'),
    x=df['Weight'].unique(),
    y=df['Height'].unique(),
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

print("\nMissing Values:")
print(df.isnull().sum())




# BMI Calculator
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
