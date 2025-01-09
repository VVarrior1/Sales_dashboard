import pytest
import pandas as pd
from src.data_processor import DataProcessor
from src.visualizations import DashboardVisualizer

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
def visualizer(sample_df):
    processor = DataProcessor(sample_df)
    return DashboardVisualizer(processor)

def test_create_revenue_trend(visualizer):
    """Test if revenue trend visualization is created"""
    fig = visualizer.create_revenue_trend()
    assert fig is not None
    assert 'data' in fig
    assert len(fig.data) > 0

def test_create_regional_performance(visualizer):
    """Test if regional performance visualization is created"""
    fig = visualizer.create_regional_performance()
    assert fig is not None
    assert 'data' in fig
    assert len(fig.data) > 0

def test_create_product_performance(visualizer):
    """Test if product performance visualization is created"""
    fig = visualizer.create_product_performance()
    assert fig is not None
    assert 'data' in fig
    assert len(fig.data) > 0