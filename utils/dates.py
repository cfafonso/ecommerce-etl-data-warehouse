

def get_trimester(date):
    """
    Determines which trimester a given date falls into.
    
    Args:
        date (pd.Timestamp): a Pandas Timestamp representing a single date.

    Returns:
        str: the trimester label ("Q1", "Q2", "Q3", or "Q4").
    """

    if date.month <= 3: 
        return "Q1"
    
    elif date.month <= 6: 
        return "Q2"
    
    elif date.month <= 9: 
        return "Q3"
    
    return "Q4"


def get_week_day(date):
    """
    
    Args:
        date (pd.Timestamp): a Pandas Timestamp representing a single date.

    Returns:
        str: the week name ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
             of the day associated with date.
    """

    weekday_mappings = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
                        4: "Friday", 5: "Saturday", 6: "Sunday"}
    
    return weekday_mappings[date.weekday()]


def get_day_type(date):
    """
    Determines whether a given date is a weekday or a weekend.
    
    Args:
        date (pd.Timestamp): a Pandas Timestamp representing a single date.

    Returns:
        str: either "Weekday" or "Weekend" indicating whether the date is a weekday or a weekend.
    """

    if date.weekday() >= 5: 
        return "Weekend"
    
    return "Weekday"


def get_national_holiday_indicator(date):
    """
    Determines which trimester a given date falls into.
    
    Args:
        date (pd.Timestamp): a Pandas Timestamp representing a single date.

    Returns:
        str: either "Holiday" or "Not Holiday" indicating whether the date is a Brazilian national
             holiday or not.
    """

    if date.day == 1 and date.month == 1 or date.day == 21 and date.month == 4 \
        or date.day == 1 and date.month == 5 or date.day == 7 and date.month == 9 \
            or date.day == 12 and date.month == 10 or date.day == 2 and date.month == 11 \
                or date.day == 15 and date.month == 11 or date.day == 25 and date.month == 12:
        return "Holiday"
    
    return "Non-Holiday"