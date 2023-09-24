import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
       
# Generate some random data for demonstration
np.random.seed(0)
n_samples = 100
heights = np.random.uniform(150, 190, n_samples)
weights = np.random.uniform(50, 100, n_samples)
bmi = weights / ((heights / 100) ** 2)

# Create a DataFrame to hold the data
data = pd.DataFrame({'Height': heights, 'Weight': weights, 'BMI': bmi})

# Define the range for height, weight, and BMI
height_range = (160, 180)
weight_range = (60, 80)
bmi_range = (18, 25)

# Filter the data within the specified ranges
filtered_data = data[
    (data['Height'] >= height_range[0]) & (data['Height'] <= height_range[1]) &
    (data['Weight'] >= weight_range[0]) & (data['Weight'] <= weight_range[1]) &
    (data['BMI'] >= bmi_range[0]) & (data['BMI'] <= bmi_range[1])
]

# Create a pivot table for the heatmap
pivot_table = pd.pivot_table(filtered_data, values='BMI', index='Height', columns='Weight')

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of BMI by Height and Weight Range')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.show()
 

   
