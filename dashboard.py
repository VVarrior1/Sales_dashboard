import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("data/sales_data.csv")
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region", data['Region'].unique())
selected_product = st.sidebar.multiselect("Select Product", data['Product'].unique())

# Filter data
filtered_data = data  # Start with the full dataset
if selected_region:
    filtered_data = filtered_data[filtered_data['Region'].isin(selected_region)]
if selected_product:
    filtered_data = filtered_data[filtered_data['Product'].isin(selected_product)]

# Dashboard Title
st.title("Sales Performance Dashboard")

# Monthly Sales Trends
st.subheader("Monthly Sales Trends")

# Ensure proper date formatting for the x-axis
filtered_data['Year-Month'] = filtered_data['Date'].dt.to_period('M').astype(str)

# Group data by 'Year-Month'
monthly_sales = filtered_data.groupby('Year-Month', as_index=False)['Sales'].sum()

# Ensure data is sorted by date
monthly_sales['Year-Month'] = pd.to_datetime(monthly_sales['Year-Month'])
monthly_sales = monthly_sales.sort_values('Year-Month')

# Check for empty data
if monthly_sales.empty:
    st.write("No data available for the selected filters.")
else:
    # Create line chart
    fig = px.line(
        monthly_sales,
        x='Year-Month',
        y='Sales',
        title="Monthly Sales Trends",
        labels={'Year-Month': 'Date', 'Sales': 'Sales Amount'}
    )
    fig.update_xaxes(
        dtick="M1",  # Set ticks to monthly intervals
        tickformat="%b %Y"  # Format ticks as 'Month Year'
    )
    st.plotly_chart(fig)


# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_data.groupby('Region')['Sales'].sum().reset_index()
fig = px.pie(region_sales, values='Sales', names='Region', title="Sales by Region")
st.plotly_chart(fig)
