import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Analytics")

df = pd.read_excel("../OnlineRetail.xlsx")

df['StockCode'] = df['StockCode'].astype(str)

df['Revenue'] = df['Quantity'] * df['Price']

top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

st.subheader("Top 10 Products")

fig, ax = plt.subplots(figsize=(10,5))

top_products.plot(kind='bar', ax=ax)

ax.set_xlabel("Products")

ax.set_ylabel("Revenue")

st.pyplot(fig)

st.subheader("Product Revenue Data")

st.write(top_products)