import streamlit as st
import pandas as pd
from src.data_processor import DataProcessor
from src.visualizations import DashboardVisualizer
from src.utils import generate_sample_data, format_currency, format_percentage


def main():
    st.set_page_config(
        page_title="Sales Performance Dashboard",
        page_icon="📊",
        layout="wide"
    )

    # Header
    st.title("📊 Sales Performance Dashboard")
    st.markdown("### Real-time sales performance analytics and insights")

    # Load data
    # In a real application, you would load your actual data here
    df = generate_sample_data()

    # Initialize processors
    data_processor = DataProcessor(df)
    visualizer = DashboardVisualizer(data_processor)

    # Get metrics
    metrics = data_processor.get_overall_metrics()

    # Display key metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Revenue", format_currency(metrics['total_revenue']))
    with col2:
        st.metric("Total Profit", format_currency(metrics['total_profit']))
    with col3:
        st.metric("Average Margin", format_percentage(metrics['average_margin']))
    with col4:
        st.metric("Total Sales", f"{metrics['total_sales']:,} units")

    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs([
        "Revenue Trends",
        "Regional Performance",
        "Product Analysis",
        "Anomaly Detection"
    ])

    with tab1:
        st.plotly_chart(visualizer.create_revenue_trend(), use_container_width=True)

    with tab2:
        st.plotly_chart(visualizer.create_regional_performance(), use_container_width=True)

    with tab3:
        st.plotly_chart(visualizer.create_product_performance(), use_container_width=True)

    with tab4:
        st.plotly_chart(visualizer.create_anomalies_chart(), use_container_width=True)

    # Add filters in sidebar
    st.sidebar.header("Filters")

    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['date'].min(), df['date'].max())
    )

    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['region'].unique(),
        default=df['region'].unique()
    )

    # Product filter
    selected_products = st.sidebar.multiselect(
        "Select Products",
        options=df['product'].unique(),
        default=df['product'].unique()
    )


if __name__ == "__main__":
    main()