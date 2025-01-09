"""
Sales Dashboard package for analyzing and visualizing sales performance data.
"""

from .data_processor import DataProcessor
from .visualizations import DashboardVisualizer
from .utils import generate_sample_data, format_currency, format_percentage

__version__ = '1.0.0'
__author__ = 'Abdelrahman Mohamed'

# Export main classes and functions
__all__ = [
    'DataProcessor',
    'DashboardVisualizer',
    'generate_sample_data',
    'format_currency',
    'format_percentage'
]