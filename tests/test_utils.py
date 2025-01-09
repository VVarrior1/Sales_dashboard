import pytest
import pandas as pd
from src.utils import generate_sample_data, format_currency, format_percentage

def test_generate_sample_data():
    """Test if sample data generation works correctly"""
    df = generate_sample_data(num_records=100)
    assert len(df) == 100
    assert all(col in df.columns for col in ['date', 'region', 'product', 'units_sold', 'revenue', 'costs'])
    assert isinstance(df['date'].iloc[0], pd.Timestamp)

def test_format_currency():
    """Test currency formatting"""
    assert format_currency(1000) == "$1,000.00"
    assert format_currency(1000.50) == "$1,000.50"
    assert format_currency(0) == "$0.00"

def test_format_percentage():
    """Test percentage formatting"""
    assert format_percentage(50) == "50.0%"
    assert format_percentage(33.333) == "33.3%"
    assert format_percentage(0) == "0.0%"