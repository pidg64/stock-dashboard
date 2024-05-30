from alpha_vantage.fundamentaldata import FundamentalData


def get_fundamental_data(ticker, api_key):
    """
    Get the fundamental data from the stock.

    :param ticker: Ticker
    :param api_key: API key
    :return: Fundamental data
    """
    fd = FundamentalData(key=api_key, output_format='pandas')
    try:
        balance_sheet_raw = fd.get_balance_sheet_annual(ticker)[0]
        balance_sheet = balance_sheet_raw.transpose()[2:]
        balance_sheet.columns = list(balance_sheet_raw.transpose().iloc[0])
        return balance_sheet
    except Exception as e:
        return str(e) + f' Instrument: {ticker}'
