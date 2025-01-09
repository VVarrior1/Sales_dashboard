# Sales Performance Dashboard

An interactive dashboard built with Streamlit and Plotly to analyze sales performance across regions, products, and time periods.

## Features

- Real-time sales performance metrics
- Interactive visualizations
- Regional performance analysis
- Product performance tracking
- Anomaly detection
- Filtering capabilities by date, region, and product

## Technologies Used

- Python 3.9+
- Streamlit
- Pandas
- Plotly
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sales-dashboard.git
cd sales-dashboard
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Project Structure

```
sales_dashboard/
├── data/
│   └── sample_sales_data.csv
├── src/
│   ├── __init__.py
│   ├── data_processor.py
│   ├── visualizations.py
│   └── utils.py
├── requirements.txt
├── README.md
└── app.py
```

## Features Explanation

1. **Data Processing**
   - Automated data cleaning and preprocessing
   - Calculation of key metrics and KPIs
   - Anomaly detection using statistical methods

2. **Visualizations**
   - Revenue trend analysis
   - Regional performance comparison
   - Product performance scatter plot
   - Anomaly detection visualization

3. **Interactive Filters**
   - Date range selection
   - Region filtering
   - Product filtering

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request