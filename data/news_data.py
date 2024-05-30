from stocknews import StockNews


def get_news(ticker):
    """
    Get the news data from the stock.

    :param ticker: Ticker
    :return: News data
    """
    sn = StockNews(ticker, save_news=False)
    news_df = sn.read_rss()
    return news_df
