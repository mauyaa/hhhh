import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Home Energy Management System", layout="wide")
st.title("🏠 Home Energy Management System")
st.markdown("""
    <style>
        .main { background-color: #f4f7fc; }
        .sidebar .sidebar-content { background-color: #f7f7f7; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 16px; padding: 12px 24px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Introduction Section
st.markdown("""
    <div style="text-align: center;">
        <h2>Welcome to the Home Energy Management System (HEMS)</h2>
        <p>Track your energy usage and discover savings tips to help you reduce your carbon footprint and costs.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Overview", "Energy Usage", "Cost Analysis", "Savings Tips"])

# Sample Data for Demo
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
    st.write("Here’s a quick overview of your home’s energy usage.")

    total_usage = energy_data.iloc[:, 1:].sum().sum()
    avg_daily_usage = energy_data.iloc[:, 1:].sum(axis=1).mean()
    st.metric("Total Energy Usage (kWh)", f"{total_usage:.2f}")
    st.metric("Average Daily Usage (kWh)", f"{avg_daily_usage:.2f}")

    st.write("Energy Usage by Appliance:")
    st.bar_chart(energy_data.iloc[:, 1:].sum())

# Energy Usage Section
elif section == "Energy Usage":
    st.header("📉 Energy Usage Analysis")
    st.write("Track your energy usage over time and understand the patterns.")

    st.line_chart(energy_data.set_index("Date")[["Appliance 1 (kWh)", "Appliance 2 (kWh)", "Appliance 3 (kWh)"]])

    st.write("Select a date range to narrow down your energy usage.")
    start_date = st.date_input("Start Date", value=date_range[0])
    end_date = st.date_input("End Date", value=date_range[-1])
    filtered_data = energy_data[(energy_data["Date"] >= pd.to_datetime(start_date)) & (energy_data["Date"] <= pd.to_datetime(end_date))]
    st.line_chart(filtered_data.set_index("Date")[["Appliance 1 (kWh)", "Appliance 2 (kWh)", "Appliance 3 (kWh)"]])

# Cost Analysis Section
elif section == "Cost Analysis":
    st.header("💰 Cost Analysis")
    st.write("Estimate the cost of your energy consumption based on real-time data.")

    rate_per_kwh = st.slider("Energy Rate ($/kWh)", min_value=0.1, max_value=1.0, value=0.3)
    energy_data["Total Cost ($)"] = energy_data.iloc[:, 1:].sum(axis=1) * rate_per_kwh
    total_cost = energy_data["Total Cost ($)"].sum()

    st.metric("Total Energy Cost ($)", f"{total_cost:.2f}")
    st.area_chart(energy_data.set_index("Date")["Total Cost ($)"])

# Savings Tips Section
elif section == "Savings Tips":
    st.header("💡 Energy-Saving Tips")
    st.write("Here are some practical tips to help you reduce energy consumption and save money.")

    tips = [
        "Turn off lights and appliances when not in use.",
        "Switch to energy-efficient LED bulbs.",
        "Unplug appliances to avoid phantom energy usage.",
        "Use a programmable thermostat for heating and cooling.",
        "Limit the use of high-energy appliances during peak hours."
    ]
    for tip in tips:
        st.write(f"- {tip}")

# Footer
st.sidebar.markdown("----")
st.sidebar.write("**Developed by Bevan Mauya Bosire**")
st.sidebar.write("GitHub: [mauyaa](https://github.com/mauyaa)")

# Footer for the Main Area
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <p>💡 Take control of your energy today! Track, analyze, and save.</p>
    </div>
""", unsafe_allow_html=True)


