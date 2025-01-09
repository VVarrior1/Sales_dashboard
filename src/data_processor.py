import pandas as pd
import numpy as np
from datetime import datetime


class DataProcessor:
    def __init__(self, df):
        self.df = df
        self._preprocess_data()

    def _preprocess_data(self):
        """Preprocess the sales data"""
        # Convert date column to datetime
        self.df['date'] = pd.to_datetime(self.df['date'])

        # Add derived columns
        self.df['month'] = self.df['date'].dt.month
        self.df['year'] = self.df['date'].dt.year
        self.df['quarter'] = self.df['date'].dt.quarter

        # Calculate profit
        self.df['profit'] = self.df['revenue'] - self.df['costs']

        # Calculate profit margin
        self.df['profit_margin'] = (self.df['profit'] / self.df['revenue']) * 100

    def get_overall_metrics(self):
        """Calculate overall performance metrics"""
        return {
            'total_revenue': self.df['revenue'].sum(),
            'total_profit': self.df['profit'].sum(),
            'average_margin': self.df['profit_margin'].mean(),
            'total_sales': self.df['units_sold'].sum()
        }

    def get_trends_by_period(self, period='month'):
        """Get sales trends by specified period"""
        grouped = self.df.groupby(period).agg({
            'revenue': 'sum',
            'profit': 'sum',
            'units_sold': 'sum',
            'profit_margin': 'mean'
        }).reset_index()
        return grouped

    def get_regional_performance(self):
        """Analyze performance by region"""
        return self.df.groupby('region').agg({
            'revenue': 'sum',
            'profit': 'sum',
            'units_sold': 'sum',
            'profit_margin': 'mean'
        }).reset_index()

    def get_product_performance(self):
        """Analyze performance by product"""
        return self.df.groupby('product').agg({
            'revenue': 'sum',
            'profit': 'sum',
            'units_sold': 'sum',
            'profit_margin': 'mean'
        }).reset_index()

    def get_anomalies(self, column='revenue', threshold=2):
        """Detect anomalies using z-score method"""
        z_scores = np.abs((self.df[column] - self.df[column].mean()) / self.df[column].std())
        return self.df[z_scores > threshold]