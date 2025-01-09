import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class DashboardVisualizer:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def create_revenue_trend(self):
        """Create revenue trend line chart"""
        trends = self.data_processor.get_trends_by_period()
        fig = px.line(
            trends,
            x='month',
            y='revenue',
            title='Monthly Revenue Trend',
            labels={'month': 'Month', 'revenue': 'Revenue ($)'}
        )
        return fig

    def create_regional_performance(self):
        """Create regional performance bar chart"""
        regional_data = self.data_processor.get_regional_performance()
        fig = px.bar(
            regional_data,
            x='region',
            y=['revenue', 'profit'],
            title='Performance by Region',
            barmode='group',
            labels={
                'region': 'Region',
                'revenue': 'Revenue ($)',
                'profit': 'Profit ($)',
                'variable': 'Metric'
            }
        )
        return fig

    def create_product_performance(self):
        """Create product performance scatter plot"""
        product_data = self.data_processor.get_product_performance()
        fig = px.scatter(
            product_data,
            x='revenue',
            y='profit_margin',
            size='units_sold',
            color='product',
            title='Product Performance Analysis',
            labels={
                'revenue': 'Revenue ($)',
                'profit_margin': 'Profit Margin (%)',
                'units_sold': 'Units Sold'
            }
        )
        return fig

    def create_anomalies_chart(self):
        """Create anomalies visualization"""
        df = self.data_processor.df
        anomalies = self.data_processor.get_anomalies()

        fig = go.Figure()

        # Add regular points
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['revenue'],
            mode='lines+markers',
            name='Normal Revenue'
        ))

        # Add anomalies
        fig.add_trace(go.Scatter(
            x=anomalies['date'],
            y=anomalies['revenue'],
            mode='markers',
            marker=dict(
                size=12,
                symbol='x',
                color='red'
            ),
            name='Anomalies'
        ))

        fig.update_layout(
            title='Revenue Anomalies Detection',
            xaxis_title='Date',
            yaxis_title='Revenue ($)'
        )
        return fig