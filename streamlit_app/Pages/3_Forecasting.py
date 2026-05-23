import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Forecasting Dashboard")

df = pd.read_excel("../OnlineRetail.xlsx")

df['StockCode'] = df['StockCode'].astype(str)

df['Revenue'] = df['Quantity'] * df['Price']

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


monthly_sales = df.groupby(df['InvoiceDate'].dt.month)['Revenue'].sum()

st.subheader("Monthly Revenue Forecast")

growth = st.slider(
    "Increase Forecast Percentage",
    0,
    100,
    10
)

forecast_sales = monthly_sales * (1 + growth / 100)

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    label='Original Sales'
)

ax.plot(
    forecast_sales.index,
    forecast_sales.values,
    marker='o',
    linestyle='--',
    label='Forecast Sales'
)

ax.set_xlabel("Month")

ax.set_ylabel("Revenue")

ax.legend()

st.pyplot(fig)

st.write("Forecast Increase:", growth, "%")