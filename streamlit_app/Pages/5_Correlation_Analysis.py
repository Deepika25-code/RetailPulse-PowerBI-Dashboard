import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Correlation Analysis")

# Load Dataset
df = pd.read_excel("../OnlineRetail.xlsx")

# Create Revenue
df['Revenue'] = df['Quantity'] * df['Price']

# Select Numeric Columns
numeric_df = df[['Quantity', 'Price', 'Revenue']]

# Correlation
correlation = numeric_df.corr()

st.subheader("Correlation Matrix")

st.write(correlation)

# Heatmap
fig, ax = plt.subplots(figsize=(6,4))

cax = ax.matshow(correlation)

plt.xticks(range(len(correlation.columns)), correlation.columns)

plt.yticks(range(len(correlation.columns)), correlation.columns)

fig.colorbar(cax)

st.pyplot(fig)