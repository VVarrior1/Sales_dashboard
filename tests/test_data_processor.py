import pytest
import pandas as pd
from src.data_processor import DataProcessor

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', end='2023-01-10'),
        'region': ['North'] * 5 + ['South'] * 5,
        'product': ['Product A'] * 5 + ['Product B'] * 5,
        'units_sold': [10] * 10,
        'revenue': [1000] * 10,
        'costs': [500] * 10
    })

@pytest.fixture
def processor(sample_df):
    return DataProcessor(sample_df)

def test_preprocess_data(processor):
    """Test if preprocessing adds required columns"""
    df = processor.df
    assert 'profit' in df.columns
    assert 'profit_margin' in df.columns
    assert 'month' in df.columns
    assert 'year' in df.columns
    assert 'quarter' in df.columns

def test_get_overall_metrics(processor):
    """Test if overall metrics are calculated correctly"""
    metrics = processor.get_overall_metrics()
    assert metrics['total_revenue'] == 10000  # 1000 * 10
    assert metrics['total_profit'] == 5000    # (1000 - 500) * 10
    assert metrics['total_sales'] == 100      # 10 * 10

def test_get_regional_performance(processor):
    """Test if regional performance is calculated correctly"""
    regional_perf = processor.get_regional_performance()
    assert len(regional_perf) == 2  # North and South
    assert 'North' in regional_perf['region'].values
    assert 'South' in regional_perf['region'].values