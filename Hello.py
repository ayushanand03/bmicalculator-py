 # Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
   

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
