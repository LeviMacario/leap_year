def leap_year(year):
    """Returns if the year is leap.

    >>> leap_year(2010)
    False
    >>> leap_year(2014)
    False
    >>> leap_year(2016)
    True
    >>> leap_year(2019)
    False
    >>> leap_year(2020)
    True
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False