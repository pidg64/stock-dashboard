import numpy as np
from scipy.stats.mstats import gmean


def calculate_geometric_mean_daily_return(data):
    """
    Calculate the geometric mean daily return of the stock.

    :param data: Pandas DataFrame
    :return: Geometric mean daily return
    """
    data['Daily return'] = data['Adj Close'].pct_change()
    data.dropna(inplace=True)
    geometric_mean_daily_return = gmean(1 + data["Daily return"]) - 1
    return geometric_mean_daily_return


def calculate_annualized_return(geometric_mean_daily_return):
    """
    Calculate the annualized return of the stock.

    :param geometric_mean_daily_return: Geometric mean daily return
    :return: Annualized return
    """
    trading_days_per_year = 252
    annualized_return = (
        1 + geometric_mean_daily_return
    ) ** trading_days_per_year - 1
    return annualized_return


def calculate_annualized_std_dev(data):
    """
    Calculate the annualized standard deviation of the stock.

    :param data: Pandas DataFrame
    :return: Annualized standard deviation
    """
    std_dev = data['Daily return'].std()
    trading_days_per_year = 252
    annualized_std_dev = std_dev * np.sqrt(trading_days_per_year)
    return annualized_std_dev
