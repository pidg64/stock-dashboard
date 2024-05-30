# Stock Dashboard

This dashboard provides:

- Pricing data analysis
- Fundamental data
- Top 10 news

Overview
--------

The Stock Dashboard is a Streamlit application that enables users to visualize stock price data, review fundamental financial data, and stay updated with the latest news on a given stock ticker.

Features
--------

- **Pricing Data Analysis**

  - Visualize historical stock price data.
  - Calculate and display key financial metrics such as annualized return and standard deviation.
  - Assess risk-adjusted return.

- **Fundamental Data**

  - Display key financial statements like the balance sheet for the selected stock.

- **Top 10 News**

  - Fetch and display the latest top 10 news articles related to the selected stock.
  - Sentiment analysis on news titles and summaries.

Installation
------------

- **Prerequisites**

  - Python 3.7 or higher
  - Streamlit
  - Plotly
  - yfinance
  - alpha_vantage
  - stocknews
  - dotenv

- **Setup**
1. Clone the repository.
    ```bash
    git clone https://github.com/yourusername/stock-dashboard.git
    cd stock-dashboard
    ```

2. Install Poetry if you haven't already:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install the dependencies:
```bash
poetry install
```

4. Set up your environment variables:
    Create a .env file in the root directory of the project and add your Alpha Vantage API key:

```python
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

Running the Application
------------------------

To start the application, run:

```bash
poetry run streamlit run dashboard.py
```

The application will open in your default web browser.

File structure
---------------

```bash
.
├── README.md
├── pyproject.toml
├── dashboard.py
├── config.py
├── data
│   ├── data_loader.py
│   ├── fundamental_data.py
│   ├── news_data.py
├── utils
│   ├── date_utils.py
│   ├── numbers_utils.py
│   ├── pricing_utils.py
```
- config.py: Contains configuration variables such as API keys.
- data_loader.py: Functions for loading pricing data from various sources.
- fundamental_data.py: Functions for retrieving fundamental financial data.
- news_data.py: Functions for fetching the latest news related to a stock.
- date_utils.py: Utility functions for handling dates.
- numbers_utils.py: Utility functions for numerical operations like converting cardinal to ordinal numbers.
- pricing_utils.py: Functions for calculating financial metrics.

Usage
-----
**Input Ticker**
   1. Use the sidebar to input the stock ticker symbol (e.g., NVDA for NVIDIA).
   2. Select the start and end dates for the analysis.

**Tabs**
1. **Pricing Data Tab**
    - Displays historical stock price data and calculated financial metrics.
2. **Fundamental Data Tab**
    - Displays fundamental financial data such as the balance sheet.
3. **News Tab**
    - Displays the latest top 10 news articles and sentiment analysis for the news.
