import pandas as pd
import numpy as np


def generate_sample_data(num_records=1000):
    """Generate sample sales data for demonstration"""
    np.random.seed(42)

    # Date range for the past year
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', periods=num_records)

    # Regions and products
    regions = ['North', 'South', 'East', 'West']
    products = ['Product A', 'Product B', 'Product C', 'Product D']

    # Generate random data
    data = {
        'date': dates,
        'region': np.random.choice(regions, num_records),
        'product': np.random.choice(products, num_records),
        'units_sold': np.random.randint(10, 100, num_records),
        'revenue': np.random.uniform(1000, 10000, num_records),
        'costs': np.random.uniform(500, 5000, num_records)
    }

    return pd.DataFrame(data)


def format_currency(value):
    """Format number as currency"""
    return f"${value:,.2f}"


def format_percentage(value):
    """Format number as percentage"""
    return f"{value:.1f}%"