import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Home Energy Management System", layout="wide")

# Title and Description
st.title("🏠 Home Energy Management System")
st.markdown("""
    Energy consumption is a growing concern for homeowners due to rising energy costs and environmental sustainability. 
    Our system helps track real-time energy usage, offers actionable feedback, and provides tips for reducing energy consumption.
""", unsafe_allow_html=True)

# Example Data: Appliance energy usage (in kWh)
appliances = ["Air Conditioner", "Refrigerator", "Washing Machine", "TV", "Light Bulb"]
usage_data = np.random.uniform(0.5, 2.5, len(appliances))  # Random data for energy usage in kWh

# Display the energy usage data in a table
energy_data = pd.DataFrame({
    "Appliance": appliances,
    "Energy Consumption (kWh)": usage_data
})

# Display table in Streamlit
st.subheader("Current Energy Consumption")
st.write(energy_data)

# Plot using Matplotlib
fig, ax = plt.subplots()
ax.bar(energy_data['Appliance'], energy_data['Energy Consumption (kWh)'])
ax.set_title("Real-Time Energy Consumption")
ax.set_xlabel("Appliance")
ax.set_ylabel("Energy Consumption (kWh)")

# Show the plot
st.pyplot(fig)

# Feedback based on energy usage
st.subheader("Energy Saving Tips")
for appliance, usage in zip(appliances, usage_data):
    if usage > 2.0:
        st.warning(f"The {appliance} is using a lot of energy! Consider using it less frequently or replacing it with an energy-efficient model.")
    elif usage > 1.5:
        st.info(f"The {appliance} is consuming moderate energy. Try using it during off-peak hours for cost savings.")
    else:
        st.success(f"The {appliance} is using minimal energy. Keep it up!")

# Suggest Energy-Saving Actions
st.subheader("How to Reduce Energy Consumption")
st.markdown("""
- **Air Conditioner**: Keep doors and windows closed while operating the AC.
- **Refrigerator**: Set your refrigerator temperature to 37°F (3°C) and freezer to 0°F (-18°C).
- **Washing Machine**: Use cold water for washing clothes.
- **TV**: Turn off the TV when not in use.
- **Light Bulb**: Switch to energy-efficient LED bulbs.
""")

# Interactive Energy Usage Adjustments
st.subheader("Adjust Your Energy Usage")
appliance_select = st.selectbox("Choose an appliance to modify its energy usage:", appliances)
usage_input = st.slider(f"Set energy usage for {appliance_select} (kWh):", 0.0, 5.0, float(usage_data[appliances.index(appliance_select)]))

# Update energy data based on user input
energy_data.loc[energy_data['Appliance'] == appliance_select, 'Energy Consumption (kWh)'] = usage_input
st.write("Updated Energy Consumption Data:")
st.write(energy_data)

# Re-plot the updated graph
fig_updated, ax_updated = plt.subplots()
ax_updated.bar(energy_data['Appliance'], energy_data['Energy Consumption (kWh)'])
ax_updated.set_title("Updated Energy Consumption")
ax_updated.set_xlabel("Appliance")
ax_updated.set_ylabel("Energy Consumption (kWh)")

# Show the updated plot
st.pyplot(fig_updated)


