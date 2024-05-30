import streamlit as st
import plotly.express as px

from config import alpha_vantage_api_key
from data.news_data import get_news
from data.data_loader import load_pricing_data
from utils.date_utils import get_default_end_date, get_default_start_date
from utils.numbers_utils import cardinal_to_ordinal
from utils.pricing_utils import (
    calculate_annualized_return,
    calculate_annualized_std_dev,
    calculate_geometric_mean_daily_return,
)
from data.fundamental_data import get_fundamental_data


class StockDashboard:
    """
    Initialize a StockDashboard object.
    """

    def __init__(self):
        st.title('Stock Dashboard')
        self.ticker = st.sidebar.text_input('Ticker', 'NVDA')
        self.start_date = st.sidebar.date_input(
            'Start date', get_default_start_date()
        )
        self.end_date = st.sidebar.date_input(
            'End date', get_default_end_date()
        )
        self.data = load_pricing_data(
            self.ticker, self.start_date, self.end_date
        )
        self.plot_pricing_data()
        self.add_tabs()
        self.add_pricing_data_tab()
        self.add_fundamental_data_tab()
        self.add_news_tab()

    def plot_pricing_data(self):
        """
        Plot the stock price data.
        """
        fig = px.line(
            self.data,
            x=self.data.index,
            y=self.data['Adj Close'],
            title=self.ticker,
        )
        st.plotly_chart(fig)

    def add_tabs(self):
        """
        Add tabs to the dashboard.
        """
        self.pricing_data, self.fundamental_data, self.news = st.tabs(
            ['Pricing Data', 'Fundamental Data', 'Top 10 News']
        )

    def add_pricing_data_tab(self):
        """
        Add pricing data tab to the dashboard.
        """
        with self.pricing_data:
            st.header('Price Movements')
            data_aux = self.data.copy()
            geometric_mean_daily_return = (
                calculate_geometric_mean_daily_return(data_aux)
            )
            annualized_return = calculate_annualized_return(
                geometric_mean_daily_return
            )
            st.write(data_aux)
            st.write(
                'Estimated annualized return for the period:',
                annualized_return * 100,
                '%',
            )
            annualized_std_dev = calculate_annualized_std_dev(data_aux)
            st.write(
                'Estimated annualized standard deviation for the period:',
                annualized_std_dev * 100,
                '%',
            )
            st.write(
                'Estimated annualized risk-adjusted return for the period:',
                annualized_return / annualized_std_dev,
            )

    def add_fundamental_data_tab(self):
        """
        Add fundamental data tab to the dashboard.
        """
        with self.fundamental_data:
            st.write('Fundamental')
            st.subheader('Balance Sheet')
            balance_sheet = get_fundamental_data(
                self.ticker, alpha_vantage_api_key
            )
            st.write(balance_sheet)

    def add_news_tab(self):
        """
        Add news tab to the dashboard.
        """
        with self.news:
            st.header(f'News of {self.ticker}')
            news_df = get_news(self.ticker)
            for i in range(10):
                st.subheader(f'{cardinal_to_ordinal(i+1)} News')
                st.write(news_df['published'][i])
                st.write(news_df['title'][i])
                st.write(news_df['summary'][i])
                st.write(
                    f'Sentiment analysis result on title: {news_df["sentiment_title"][i]}'
                )
                st.write(
                    f'Sentiment analysis result on news: {news_df["sentiment_summary"][i]}'
                )


if __name__ == '__main__':
    StockDashboard()
