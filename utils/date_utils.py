from datetime import datetime, timedelta


def get_default_start_date(days_back=7):
    """
    Return the default start date

    :param days_back: Number of days back, defaults to 7
    :return: Default start date
    """
    return datetime.today() - timedelta(days=days_back)


def get_default_end_date():
    """
    Return the default end date

    :return: Default end date
    """
    return datetime.today()
