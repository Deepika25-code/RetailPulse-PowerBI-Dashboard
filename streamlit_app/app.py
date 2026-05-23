import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_excel("../OnlineRetail.xlsx")

# FIX DATATYPES
df['StockCode'] = df['StockCode'].astype(str)

# CREATE REVENUE COLUMN
df['Revenue'] = df['Quantity'] * df['Price']

# DATE CONVERSION
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# PAGE TITLE
st.title("RetailPulse Analytics Dashboard")

# SIDEBAR FILTER
st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    df['Country'].unique()
)

# FILTER DATA
filtered_df = df[df['Country'] == country]

# KPI SECTION
st.subheader("Business KPIs")

total_revenue = filtered_df['Revenue'].sum()

total_orders = filtered_df['Invoice'].nunique()

total_customers = filtered_df['Customer ID'].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")

col2.metric("Total Orders", total_orders)

col3.metric("Total Customers", total_customers)

# DATASET PREVIEW
st.subheader("Dataset Preview")

st.write(filtered_df.head())

# TOP 10 COUNTRIES
st.subheader("Top 10 Countries by Revenue")

top_countries = (
    df.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,5))

top_countries.plot(kind='bar', ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

# MONTHLY REVENUE TREND
st.subheader("Monthly Revenue Trend")

monthly_sales = (
    filtered_df.groupby(filtered_df['InvoiceDate'].dt.month)['Revenue']
    .sum()
)

fig2, ax2 = plt.subplots(figsize=(10,5))

monthly_sales.plot(kind='line', marker='o', ax=ax2)

plt.xlabel("Month")

plt.ylabel("Revenue")

st.pyplot(fig2)

# TOP PRODUCTS
st.subheader("Top 10 Products")

top_products = (
    filtered_df.groupby('Description')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots(figsize=(10,5))

top_products.plot(kind='bar', ax=ax3)

plt.xticks(rotation=90)

st.pyplot(fig3)

# PIE CHART
st.subheader("Revenue Share by Top Countries")

country_revenue = (
    df.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig4, ax4 = plt.subplots(figsize=(8,8))

ax4.pie(
    country_revenue,
    labels=country_revenue.index,
    autopct='%1.1f%%'
)

st.pyplot(fig4)

# CUSTOMER ANALYSIS
st.subheader("Top 10 Customers by Revenue")

top_customers = (
    filtered_df.groupby('Customer ID')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig5, ax5 = plt.subplots(figsize=(10,5))

top_customers.plot(kind='bar', ax=ax5)

plt.xticks(rotation=45)

st.pyplot(fig5)

# FORECASTING
st.subheader("Next 3 Months Revenue Forecast")

forecast_data = monthly_sales.reset_index()

forecast_data.columns = ['Month', 'Revenue']

forecast_data['Forecast'] = forecast_data['Revenue'].rolling(2).mean()

fig6, ax6 = plt.subplots(figsize=(10,5))

ax6.plot(
    forecast_data['Month'],
    forecast_data['Revenue'],
    marker='o',
    label='Actual Revenue'
)

ax6.plot(
    forecast_data['Month'],
    forecast_data['Forecast'],
    marker='o',
    linestyle='dashed',
    label='Forecast Revenue'
)

ax6.legend()

plt.xlabel("Month")

plt.ylabel("Revenue")

st.pyplot(fig6)

# DOWNLOAD BUTTON
st.subheader("Download Report")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Filtered Data CSV",
    data=csv,
    file_name='RetailPulse_Report.csv',
    mime='text/csv'
)

st.success("Click above button to download report")

# CUSTOM STYLE
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3 {
        color: #00FFAA;
    }
    </style>
""", unsafe_allow_html=True)

# REAL TIME ALERTS

st.subheader("Business Alerts")

if total_revenue > 500000:
    st.success("Revenue target achieved!")

if total_orders > 1000:
    st.info("High number of orders detected!")

if total_customers > 500:
    st.warning("Customer activity is very high!")

# INVENTORY RECOMMENDATIONS

st.subheader("Inventory Recommendations")

low_stock_products = (
    filtered_df.groupby('Description')['Quantity']
    .sum()
    .sort_values()
    .head(10)
)

st.write("Products needing restock:")

st.write(low_stock_products)

# CHURN RISK DASHBOARD

st.subheader("Customer Churn Risk")

customer_orders = (
    filtered_df.groupby('Customer ID')['Invoice']
    .nunique()
)

low_activity_customers = customer_orders[customer_orders < 2]

st.write(
    "Customers with low activity (possible churn risk):"
)

st.write(low_activity_customers.head(10))

# WHAT-IF ANALYSIS

st.subheader("What-If Revenue Analysis")

increase_percent = st.slider(
    "Increase Revenue by %",
    0,
    100,
    10
)

new_revenue = total_revenue * (1 + increase_percent / 100)

st.write(
    f"Projected Revenue after {increase_percent}% increase:"
)

st.success(f"${new_revenue:,.2f}")