import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Customer Analytics")

df = pd.read_excel("../OnlineRetail.xlsx")

df['StockCode'] = df['StockCode'].astype(str)

df['Revenue'] = df['Quantity'] * df['Price']

top_customers = df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False).head(10)

st.subheader("Top 10 Customers")

fig, ax = plt.subplots()

top_customers.plot(kind='bar', ax=ax)

ax.set_xlabel("Customer ID")

ax.set_ylabel("Revenue")

st.pyplot(fig)

st.subheader("Customer Revenue Data")

st.write(top_customers)