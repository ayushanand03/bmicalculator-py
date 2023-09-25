import streamlit as st
import numpy as np
import pandas as pd

import numpy as np

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


# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Define a range of heights and weights
heights_m = np.arange(1.5, 2.1, 0.05)  # Heights from 1.5m to 2.0m in 5cm increments
weights_kg = np.arange(50, 151, 5)  # Weights from 50kg to 150kg in 5kg increments

# Calculate BMI values for all combinations of height and weight
bmi_values = np.empty((len(heights_m), len(weights_kg)))
for i, height in enumerate(heights_m):
    for j, weight in enumerate(weights_kg):
        bmi = calculate_bmi(weight, height)
        bmi_values[i, j] = bmi

# Create a heatmap to visualize BMI values
plt.figure(figsize=(12, 8))
plt.imshow(bmi_values, cmap='YlGnBu', extent=[50, 150, 1.5, 2.0])
plt.colorbar(label='BMI')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (m)')
plt.title('BMI Chart')
plt.xticks(np.arange(50, 151, 10))
plt.yticks(np.arange(1.5, 2.1, 0.1))
plt.grid(False)
plt.show()

        

 

   
