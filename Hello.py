import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd
import seaborn as sns

url = 'ayushbmi.csv'
df = pd.read_csv(url)

# Title
st.title('BMI Calculator')

# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Define a range of heights and weights
heights_m = np.arange(1.5, 2.1, 0.05)
weights_kg = np.arange(50, 151, 5)

# Calculate BMI values for all combinations of height and weight
bmi_values = np.empty((len(heights_m), len(weights_kg)))
for i, height in enumerate(heights_m):
    for j, weight in enumerate(weights_kg):
        bmi = calculate_bmi(weight, height)
        bmi_values[i, j] = bmi
        
# Display basic information about the dataset
st.subheader("Dataset Info:")
st.write(df.info())

# Display summary statistics
st.subheader("Summary Statistics:")
st.write(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Calculate the average BMI
average_bmi = df['bmi'].mean()
print("\nAverage BMI:", average_bmi)


# Create a heatmap using Plotly
heatmap_fig = px.imshow(
    bmi_values,
    x=weights_kg,
    y=heights_m,
    labels=dict(x="Weight (kg)", y="Height (m)", color="BMI"),
    color_continuous_scale="YlGnBu",
    title="BMI Chart"
)

# Display the heatmap
st.subheader("BMI Chart:")
st.plotly_chart(heatmap_fig)

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
