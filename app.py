import streamlit as st
import pandas as pd
import numpy as np

# Title and Introduction
st.set_page_config(page_title="Home Energy Management System (HEMS)", layout="wide")
st.title("🏠 Home Energy Management System")
st.subheader("Monitor and manage your home's energy usage efficiently")

st.write("""
Welcome to the Home Energy Management System! Track your energy consumption, view insights, and find suggestions 
to reduce your energy usage and lower your costs. Let's take control of your home's energy!
""")

# Sidebar for Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Overview", "Energy Usage", "Cost Analysis", "Savings Tips"])

# Sample data for demonstration
np.random.seed(42)
date_range = pd.date_range(start="2024-01-01", end="2024-11-10", freq="D")
data = {
    "Date": date_range,
    "Appliance 1 (kWh)": np.random.uniform(0.5, 3.5, len(date_range)),
    "Appliance 2 (kWh)": np.random.uniform(1.0, 5.0, len(date_range)),
    "Appliance 3 (kWh)": np.random.uniform(0.3, 2.5, len(date_range))
}
energy_data = pd.DataFrame(data)

# Overview Section
if section == "Overview":
    st.header("📊 Overview")
    st.write("Get a summary of your recent energy usage.")

    total_usage = energy_data.iloc[:, 1:].sum().sum()
    avg_daily_usage = energy_data.iloc[:, 1:].sum(axis=1).mean()
    st.metric("Total Energy Usage (kWh)", f"{total_usage:.2f}")
    st.metric("Average Daily Usage (kWh)", f"{avg_daily_usage:.2f}")

    st.write("Here's a quick overview of energy usage by appliance:")
    st.bar_chart(energy_data.iloc[:, 1:].sum())

# Energy Usage Section
elif section == "Energy Usage":
    st.header("📉 Energy Usage Analysis")
    st.write("Check your daily and monthly energy usage trends.")

    st.line_chart(energy_data.set_index("Date")[["Appliance 1 (kWh)", "Appliance 2 (kWh)", "Appliance 3 (kWh)"]])

    st.write("Choose a date range to see specific usage details.")
    start_date = st.date_input("Start Date", value=date_range[0])
    end_date = st.date_input("End Date", value=date_range[-1])
    filtered_data = energy_data[(energy_data["Date"] >= pd.to_datetime(start_date)) & (energy_data["Date"] <= pd.to_datetime(end_date))]
    st.line_chart(filtered_data.set_index("Date")[["Appliance 1 (kWh)", "Appliance 2 (kWh)", "Appliance 3 (kWh)"]])

# Cost Analysis Section
elif section == "Cost Analysis":
    st.header("💰 Cost Analysis")
    st.write("Analyze your energy costs based on usage.")

    rate_per_kwh = st.slider("Energy Rate ($/kWh)", min_value=0.1, max_value=1.0, value=0.3)
    energy_data["Total Cost ($)"] = energy_data.iloc[:, 1:].sum(axis=1) * rate_per_kwh
    total_cost = energy_data["Total Cost ($)"].sum()

    st.metric("Total Energy Cost ($)", f"{total_cost:.2f}")
    st.area_chart(energy_data.set_index("Date")["Total Cost ($)"])

# Savings Tips Section
elif section == "Savings Tips":
    st.header("💡 Energy-Saving Tips")
    st.write("Simple ways to reduce your energy consumption and save money!")

    tips = [
        "Turn off lights when not in use.",
        "Use energy-efficient LED bulbs.",
        "Unplug appliances when not in use to prevent phantom loads.",
        "Use a programmable thermostat to manage heating and cooling.",
        "Limit usage of energy-intensive appliances during peak hours."
    ]
    for tip in tips:
        st.write(f"- {tip}")

# Footer
st.sidebar.markdown("----")
st.sidebar.write("**Developed by Bevan Mauya Bosire**")
st.sidebar.write("GitHub: [mauyaa](https://github.com/mauyaa)")

st.write("💡 Tip: To see a breakdown of appliance-specific energy costs, go to the 'Energy Usage' section.")

