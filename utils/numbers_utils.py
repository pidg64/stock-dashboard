def cardinal_to_ordinal(number):
    """
    Convert a cardinal number to an ordinal number

    :param number: Cardinal number
    :return: Ordinal number
    """
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = suffixes.get(number % 10, 'th')
    return str(number) + suffix
