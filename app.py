import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Example: Random energy data for demonstration
energy_data = {
    'Appliance': ['AC', 'Heater', 'Fridge', 'Washing Machine', 'TV'],
    'Energy Consumption (kWh)': [5.2, 3.1, 1.8, 2.5, 1.2]
}
df = pd.DataFrame(energy_data)

# Title and Introduction
st.title("Home Energy Management System")
st.write("""
    Energy consumption is a growing concern for homeowners. Managing and monitoring energy usage in homes is often challenging. This app provides a way to track the energy consumption of household appliances in real-time.
""")

# Bar Chart Visualization using Plotly
fig = px.bar(df, x='Appliance', y='Energy Consumption (kWh)', 
             title='Energy Consumption of Household Appliances',
             labels={'Energy Consumption (kWh)': 'Energy Consumption (kWh)', 'Appliance': 'Appliance'},
             color='Energy Consumption (kWh)',
             color_continuous_scale='Viridis')

st.plotly_chart(fig)

# Display Data Table
st.write("Energy Consumption Data:")
st.dataframe(df)

# Feedback Section
st.write("### Energy Usage Feedback:")
for appliance, consumption in zip(df['Appliance'], df['Energy Consumption (kWh)']):
    if consumption > 3:
        st.write(f"**{appliance}** is using a high amount of energy. Consider reducing usage.")
    else:
        st.write(f"**{appliance}** is energy-efficient. Keep up the good work!")

# Suggestions for Saving Energy
st.write("""
    ### Suggestions for Saving Energy:
    - Unplug appliances when not in use.
    - Use energy-efficient appliances.
    - Opt for smart thermostats to better manage heating and cooling.
""")



