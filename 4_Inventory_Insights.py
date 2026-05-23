import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Inventory Insights")

df = pd.read_excel("../OnlineRetail.xlsx")

df['StockCode'] = df['StockCode'].astype(str)

df['Revenue'] = df['Quantity'] * df['Price']

inventory_data = df.groupby('Description')['Quantity'].sum().sort_values().head(10)

st.subheader("Low Stock Products")

fig, ax = plt.subplots(figsize=(10,5))

inventory_data.plot(kind='bar', color='red', ax=ax)

ax.set_xlabel("Products")

ax.set_ylabel("Quantity")

st.pyplot(fig)

st.subheader("Inventory Recommendations")

for product in inventory_data.index:
    st.write(product, "→ Restock Recommended")