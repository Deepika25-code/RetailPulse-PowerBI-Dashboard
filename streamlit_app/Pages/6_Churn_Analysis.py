import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Customer Churn Analysis")

# Load Data
df = pd.read_excel("../OnlineRetail.xlsx")

# Create Revenue
df['Revenue'] = df['Quantity'] * df['Price']

# Customer Revenue
customer_revenue = (
    df.groupby('Customer ID')['Revenue']
    .sum()
)

# Dummy Churn Logic
churn_customers = customer_revenue[
    customer_revenue < 500
]

active_customers = customer_revenue[
    customer_revenue >= 500
]

# Metrics
st.metric("Churn Customers", len(churn_customers))

st.metric("Active Customers", len(active_customers))

# Pie Chart
labels = ['Active', 'Churn']

sizes = [
    len(active_customers),
    len(churn_customers)
]

fig, ax = plt.subplots()

ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%'
)

st.pyplot(fig)