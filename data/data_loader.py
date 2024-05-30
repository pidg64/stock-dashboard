import yfinance as yf


def load_pricing_data(ticker, start_date, end_date):
    """
    Load the stock price data.

    :param ticker: Ticker
    :param start_date: Start date
    :param end_date: End date
    :return: Stock price data
    """
    return yf.download(ticker, start=start_date, end=end_date)
