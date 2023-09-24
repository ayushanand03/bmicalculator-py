import streamlit as st
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

    # Generate a range of heights and corresponding BMI values
    heights = np.arange(140, 220, 1)  # Heights range
    weights = np.arange(40, 140, 1)  # Weights range
    bmi_values = np.zeros((len(heights), len(weights)))

    for i, h in enumerate(heights):
        for j, w in enumerate(weights):
            height_meters = h / 100
            bmi_values[i, j] = w / (height_meters ** 2)

    # Create a heatmap plot
    fig, ax = plt.subplots()
    c = ax.pcolor(weights, heights, bmi_values, cmap='viridis')
    plt.colorbar(c, label='BMI')
    ax.set_xlabel('Weight (kg)')
    ax.set_ylabel('Height (cm)')
    ax.set_title('BMI Curve')

    # Show the plot in Streamlit
    st.pyplot(fig)
if __name__ == "__main__":
    run()
